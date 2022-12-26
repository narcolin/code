# 202 Project 1
# Nicole Arcolino

def bears(n):
    if n == 42:   # base case
        return True
    elif n % 5 == 0:
        return bears(42)
    elif n % 3 == 0 or n % 4 == 0:
        first = int(str(n)[len(str(n))-2])
        second = int(str(n)[len(str(n))-2])
        return bears(first * second)
    elif n % 2 == 0:
        return bears(n//2)
    else:
        return False

