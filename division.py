def int_div(a,b):
    return (a//b)
def float_div(a,b):
    return (a/b)
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    div = int_div(a,b)
    print(div)
    div = float_div(a, b)
    print(div)

