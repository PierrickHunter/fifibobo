def fibonacci(n):
    if (n == 0 or n == 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) + fibonacci(n - 3)





"""def fibonacci(n):

    if n == 0 or n == 1:
        return n
    else:
        l = [0, 1]
        if n == 0:
            return l[0]
        elif n == 1:
            return l[1]
        a = 0
        b = 1
        for i in range(0, n - 1):
            b = a + b
            a = b - a
            l.append(b)
            print (l)"""