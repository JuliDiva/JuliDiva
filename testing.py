def double(x):
    return x*2

seq = [1,3,4,6,7]
d = [double(x)for x in seq]
# or
dob = map(double, seq)
print(d)
print(dob)

def named (**kwargs):
    print(kwargs)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="bob", age=2)

