answer="yes"
while answer !="no":
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    total=num1*num2
    print("{0} and {1} multiplied make {2}".format(num1,num2,total))
    answer=input("again? ")
