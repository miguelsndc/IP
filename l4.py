def max_val(a, b):
    return (a + b + (abs(a - b))) // 2


a = int(input(""))
l = int(input(""))
p = int(input(""))
h = int(input(""))

max = max_val(p, max_val(a, l))
print(max * h)
