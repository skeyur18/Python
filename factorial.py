#factorial code by skeyur18
def factorial(n): 
      
    # single line to find factorial 
    return 1 if (n==1 or n==0) else n * factorial(n - 1); 
num=int(input("enter the number"))
print("Factorial of",num,"is", 
factorial(num))
