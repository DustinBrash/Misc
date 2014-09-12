_name_ = "fac"
def check(old):
    def new(arg):
        if arg < 0:
            return "Bad Sign"
        else:
            return old(arg)
    return new


@check
def fac(x):
    if x == 0:
        return 1
    return (fac(x - 1) * x)

