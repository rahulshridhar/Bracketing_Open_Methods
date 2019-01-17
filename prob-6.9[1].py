import math
import _plot, _roots2

def f(x): return x**3 - 6 * x**2 + 11 * x - 6.1

_plot.graph(f, xl=0, xu=5)
#visual inspection reveals root between x = 1 and x = 4

_plot.graph(f, xl=1, xu=4)
_plot.graph(f, xl=3, xu=3.5)

print('newton method:')
def df(x): return 3 * x**2 - 12 * x + 11
_roots2.newton(f, df, x0=3.5, debug=True)

print('\nsecant method:')
_roots2.secant(f, xi1=2.5, xi2=3.5, debug=True)

print('\nmodified secant method:')
_roots2.modified_secant(f, x0=3.5, p_f=0.01, debug=True)
