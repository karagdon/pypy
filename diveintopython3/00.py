import glob
import os
print('here are my files:')
print([os.path.realpath(f) for f in glob.glob('diveintopython3/*.py')])
