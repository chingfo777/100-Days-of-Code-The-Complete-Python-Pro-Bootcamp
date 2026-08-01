def add(*args):
    print(args[0])
    for i in args:
        print(i)

def calculate(**kwargs):
    print(kwargs)
calculate(add=3,multiply=5)
