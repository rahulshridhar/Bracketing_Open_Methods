import math
import _plot, _roots1

def f(x): return -25 + 82 * x - 90 * x**2 + 44 * x**3 - 8 * x**4 + 0.7 * x**5

_plot.graph(f, xl=0.5, xu=1.0)
#visual inspection reveals root between 0.5 and 0.6

_plot.graph(f, xl=0.5, xu=0.6)

print('bisection:')
xr = _roots1.bisect(f, xl=0.5, xu=1.0, debug=True, tab=10)

print('false position:')
xr = _roots1.falsepos(f, xl=0.5, xu=1.0, debug=True, tab=10)
