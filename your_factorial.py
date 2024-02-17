# a simple factorial function that uses recersion

def your_factorial(n):
    if n < 0:
        print("Input must be an interger greater than zero.")
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * your_factorial(n-1)

if (__name__ == "__main__"):    
    print("e.g. your_factorial(5) = ", str(your_factorial(5)))

