try:
    k = 5//0
    print("The value of k is ",k)

except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    print('This is always executed')