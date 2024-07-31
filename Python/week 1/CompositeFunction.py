"""CompositeFunction"""
def func():
    """CompositeFunction"""
    def f(x):
        return 2*x
    def g(x):
        return x/2+1
    x=float(input())
    print(f"{f(g(x)):.2f}")
    print(f"{g(f(x)):.2f}")
func()
