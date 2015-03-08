/*
 * システムコール open(2) を横取りして「最近使ったファイル」
 * の履歴を取る実験 (Red Hat Linux 7.2 で動作確認)
 */
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <limits.h>
#include <sys/stat.h>
#include <sys/syscall.h>

static char *
date (void)
{
    static char datestr[BUFSIZ];
    time_t t;
    struct tm *tm;

    time(&t);
    tm = localtime(&t);
    strftime(datestr, BUFSIZ, "%Y-%m-%d %H:%M:%S", tm);
    return datestr;
}

static void
do_logging (const char *pathname)
{
    FILE *fp;
    char log_filename[PATH_MAX];
    char *user;

    user = getenv("USER");
    if (user) {
        sprintf(log_filename, "/tmp/%s-recentf", user);
        fp = fopen(log_filename, "a");
        if (fp) {
            fprintf(fp, "%s: %s\n", date(), pathname);
            fclose(fp);
            chmod(log_filename, 0600);
        }
    }
}

static int
under_home_p (const char *pathname)
{
    char *home, real_home[PATH_MAX];
    int homelen, pathlen;

    home = getenv("HOME");
    if (home) {
        realpath(home, real_home);
        homelen= strlen(real_home);
        pathlen = strlen(pathname);
        if (pathlen > homelen && strncmp(real_home, pathname, homelen) == 0) {
            return 1;
        } else {
            return 0;
        }
    } else {
        return 0;
    }
}

int
open (const char *pathname, int flags, mode_t mode)
{
    char real_pathname[PATH_MAX];

    realpath(pathname, real_pathname);
    if (under_home_p(real_pathname)) {
        do_logging(real_pathname);
    }
    return syscall(SYS_open, pathname, flags, mode);
}

int __open(const char *, int, mode_t)
    __attribute__((weak, alias("open")));
int __libc_open(const char *, int, mode_t)
    __attribute__((weak, alias("open")));
int open64(const char *, int, mode_t)
    __attribute__((weak, alias("open")));
int __libc_open64(const char *, int, mode_t)
    __attribute__((weak, alias("open")));
