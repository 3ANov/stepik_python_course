def closest_mod_5(x):
    m = x % 5
    if m == 0:
        return x
    else:
        return x+5-m


print(closest_mod_5(18))
