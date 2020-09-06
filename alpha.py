def alpha(x):
    x = x.lower()
    x = list(x)
    if (x == sorted(x)):
        return True
    else:
        return False
