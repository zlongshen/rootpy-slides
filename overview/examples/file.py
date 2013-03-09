from rootpy.testdata import get_file

# use the test file shipped with rootpy
with get_file() as f:
    myhist = f.dimensions.hist2d
    # recursively walk through the file
    for path, dirs, objects in f.walk():
        # do something
        print path, dirs, objects
