def compose(f, g):
    def h(x):
        return g(f(x))
    return h