# cuts
from ROOT import TCut

cut1 = TCut('a<10')
cut2 = TCut('b%2==0')

cut = TCut('(%s)&&(%s)' % (
    cut1.GetTitle(),
    cut2.GetTitle()))

print cut.GetTitle()
