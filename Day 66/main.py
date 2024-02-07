#Pow(x,n)
def myPow(self, x: float, n: int) -> float:
    b = n
    if x == 0:
        return 0
    elif b == 0:
        return 1
    elif b < 0:
        b = -b
        x = 1 / x
    
    a = 1
    while b > 0:
        if b % 2 == 0:
            x = x * x
            b = b // 2
        else:
            b = b - 1
            a = a * x
            
    return a