answer="yes"
while answer !="no":
    num1 = int(input("What is the first number? "))
    while num1 != 1 or num1 != 2 or num1 != 3 or num1 != 4 or num1 != 5 or num1 != 6 or num1 != 7 or num1 != 8 or num1 != 9 or num1 != 10 or num1 != 11 or num1 != 12:
        num1= int(input("Not Applicable. Choose again. "))
    num2 = int(input("What is the second number? "))
    while num2 != 1 or num2 != 2 or num2 != 3 or num2 != 4 or num2 != 5 or num2 != 6 or num2 != 7 or num2 != 8 or num2 != 9 or num2 != 10 or num2 != 11 or num2 != 12:
        num2= int(input("Not Applicable. Choose again. "))
    total=num1*num2
    print("{0} and {1} multiplied make {2}".format(num1,num2,total))
    answer=input("again? ")
