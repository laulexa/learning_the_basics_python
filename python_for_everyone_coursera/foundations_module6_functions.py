def computepay(h, r):
    if h <= 40:
        rph = h * r
        return rph
    else:
        extra_hours = h - 40
        cost_extra_hours = (extra_hours * r) * 1.5
        print(cost_extra_hours)
        rph = (40 * r) + cost_extra_hours
        return  rph

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

p = computepay(h, r)
print("Pay", p)

