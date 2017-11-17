def Factorial(number):

    if(number > 1):
        return number * Factorial(number - 1)
    else:
        return 1

def main():
    number=int(input("Please enter the number :"))
    print("The factorial of the number {} is = ".format(number),Factorial(number))
if __name__ == '__main__':
        main()



