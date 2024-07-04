def geeting(name):
    return "Hello " + name

print(geeting("John"))

# lambda arguments : expression
greet = lambda name: "From inside Lambda, Hello " + name
print(greet("Jhon"))
