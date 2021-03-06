from rootpy.plotting import Hist, Hist2D, Hist3D

# create a 1D histogram
h = Hist(10, 0, 1)

# 2D and 3D histograms are handled in the same way
# the constructor arguments are repetitions of #bins, left bound, right bound.
h2d = Hist2D(10, 0, 1, 50, -40, 10, name='2d hist')
h3d = Hist3D(3, -1, 4, 10, -1000, -200, 2, 0, 1, name='3d hist')

# variable-width bins may be created by passing the bin edges directly:
h1d_variable = Hist([1, 4, 10, 100])
h2d_variable = Hist2D([2, 4, 7, 100, 200], [-100, -50, 0, 10, 20])
h3d_variable = Hist3D([1, 3, 10], [20, 50, 100], [-10, -5, 10, 20])

# variable-width and constant-width bins can be mixed:
h2d_mixed = Hist2D([2, 10, 30], 10, 1, 5)

# easily set visual attributes
h.linecolor = 'blue'
h.fillcolor = 'green'
h.fillstyle = '/'
