#include<syslog.h>

int main(int argc, char **argv){
    openlog("my/j/logger", LOG_PID || LOG_PERROR, LOG_USER);

    syslog(LOG_INFO, "test message");

    closelog();
    return 0;
}
