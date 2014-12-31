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