import os
print(os.getcwd())
os.chdir('/var/host/media/removable/K8 PEARL/codex/pypy')
print(os.getcwd())

## working with filenames and directory names

print(os.path.join('/var/host/media/removable/K8 PEARL/codex/pypy','humansize.py'))
print(os.path.expanduser('~')) #function will expand a pathname that uses ~ to represent the current user’s home directory

pathname = '/var/host/media/removable/K8 PEARL/codex/pypy/diveintopython3/humansize.py'
os.path.split(pathname)
(dirname, filename) = os.path.split(pathname)
dirname
filename
(shortname, extension) = os.path.splitext(filename)
shortname

os.chdir('/var/host/media/removable/K8 PEARL/codex/pypy/diveintopython3/')
import glob
glob.glob('*.py')
# glob module use shell-like wildcards

#### Getting file meta data

print (os.getcwd())
metadata = os.stat('feed.xml')
metadata.st_mtime
import time
time.localtime(metadata.st_mtime)
time.struct_time(tm_year=2009, tm_mon=7, tm_mday=13, tm_hour=17, tm_min=25, tm_sec=44, tm_wday=0, tm_yday=194, tm_isdst=1)