# Ajay Chandrasekaran (HPD2DZ)

# x = age
# y = current heart rate (hr)


def gellish2(x):
    hr_max = 191.5 - (0.007 * (x ** 2))
    return float(hr_max)


def in_target_range(y, x):
    hr_max = gellish2(x)
    return (hr_max * 0.65) <= y <= (hr_max * 0.85)