#!/usr/bin/env python2

"""TestFS --- Hell World Filesystem

usage: ./main.py <mountpoint> [<opts>]
"""

import stat
import os
import errno
from time import time

import fuse
fuse.fuse_python_api = (0, 2)

class TestStat(fuse.Stat):
    def __init__(self):
        # http://docs.python.org/2.7/library/os.html#os.stat

        # protection bit
        self.st_mode = stat.S_IFREG | 0644

        # inode number
        self.st_ino = 0
        # device
        self.st_dev = 0
        # st_ino and st_dev can be ignored: FUSE will handle these

        # number of hard links: directories have at reast two
        # 1 for usual files
        self.st_nlink = 1

        # uid and gid of owner
        self.st_uid = os.getuid()
        self.st_gid = os.getgid()

        # size in bytes
        self.st_size = 0

        # access, modify, and create time
        self.st_atime = 0
        self.st_mtime = 0
        self.st_ctime = 0

class TestFS(fuse.Fuse):
    hw = "Hell, World!\n"

    # available attrs are (from fuse.py):
    _attrs = ['getattr', 'readlink', 'readdir', 'mknod', 'mkdir',
              'unlink', 'rmdir', 'symlink', 'rename', 'link', 'chmod',
              'chown', 'truncate', 'utime', 'open', 'read', 'write', 'release',
              'statfs', 'fsync', 'create', 'opendir', 'releasedir', 'fsyncdir',
              'flush', 'fgetattr', 'ftruncate', 'getxattr', 'listxattr',
              'setxattr', 'removexattr', 'access', 'lock', 'utimens', 'bmap',
              'fsinit', 'fsdestroy']

    def __init__(self, *args, **kargs):
        fuse.Fuse.__init__(self, *args, **kargs)
        return

    def getattr(self, path):
        """Return stat object for file specified by PATH."""
        if len(path.split("/")) > 2:
            # includes subdirectories like "/abc/def"
            # emit "no such file or directory" error
            return -errno.ENOENT

        st = TestStat()
        st.st_atime = int(time())
        st.st_mtime = st.st_atime
        st.st_ctime = st.st_atime

        if path == "/":
            # root directory
            st.st_mode = stat.S_IFDIR | 0755
            st.st_nlink = 2
            st.st_size = 4096
        else:
            st.st_size = len(self.hw)

        return st

    # filesystem implementations
    # For minimum read-only system, readdir, open and read are required

    def readdir(self, path, offset):
        """Return iterable of files in directory PATH."""
        # what is OFFSET?
        return (fuse.Direntry(r) for r in (".", "..", "a.txt"))

    def mknod(self, path, mode, dev):
        """Make node. MODE and DEV are used for stat object."""
        # silently ignore
        return 0

    def unlink(self, path):
        """Remove node."""
        return 0

    def write(self, path, buf, offset):
        """Write to file. Return length of data that was written."""
        return len(buf)

    def read(self, path, size, offset):
        return self.hw[offset:offset+size]

    def release(self, path, flags):
        """close(2) file."""
        return 0

    def open(self, path, flags):
        return 0

    def truncate(self, path, size):
        return 0

    def utime(self, path, times):
        return 0

    def mkdir(self, path, mode):
        return 0

    def rmdir(self, path):
        return 0

    def rename(self, pathfrom, pathto):
        return 0

    def fsync(self, path, isfsyncfile):
        return 0


def main():
    # usage="""
    # TestFS: Helloworld filesystem
    # """ + fuse.Fuse.fusage

    server = TestFS(version="%prog " + fuse.__version__,
                    dash_s_do='setsingle')
    server.parse(errex=1)
    server.main()

if __name__ == '__main__':
    main()
