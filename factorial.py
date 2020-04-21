# factorial by recursive
def factorial(num):
    if num == 1:
        return 1
    else:
        result = 1
        if num>=2:
            print(num)
            result = num * factorial(num-1)
        return result


n = 5
print(factorial(n))
