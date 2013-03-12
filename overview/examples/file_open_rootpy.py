"""
rootpy routes ROOT messages through Python`s logging system and raises error
messages as Python exceptions at the point of failure:
"""
from rootpy.io import root_open

myfile = root_open("file_does_not_exist.root")
print myfile
myfile.Get("something")