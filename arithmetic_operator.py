def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def mul(a,b):
    return (a*b)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    add = add(a,b)
    print(add)
    sub = sub(a,b)
    print(sub)
    mul = mul(a,b)
    print(mul)

