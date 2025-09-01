import math
print('''   ✨✨ WELCOME TO THE 
              SIMPLE CALCULATOR 🧮''')
print('''   HERE YOU CAN USE ONLY TWO NUMBER AND
SOME FEATURES LIKE 
        1)ADDITION (+), 
        2)SUBRATION (-),
        3)DIVISION (/),
        4)MULTIPLICATION (*),
        5)POWER (^),
        6)REMAINDER (%),
        7)SQUARE ROOT (√) AND 
        8)IF YOU WANTS TO EXIT ,
        9)ENTER "EXIT" ''')
print("OPERATOR: + , - , / , * , ^ , %  , √  or exit")
while True:
    print("ENTER THE OPERATOR : ")
    operator=input()
    if operator.lower() == "exit":
        print("👋 Goodbye! Thanks for using the calculator.")
        break
    print("ENTER THE 1ST NUMBER: ")
    number1=float(input())
    print("ENTER THE 2ND NUMBER: ")
    number2=float(input())
   
    print("YOUR OUTPUT 👇:")
    if operator=="+":
        print(number1+number2)
    elif operator=="-":
        print(number1-number2)
    elif operator=="*":
        print(number1*number2)
    elif operator=="^":
        print(number1**number2)
    elif operator=="/":
        if number2==0:
            print("❌ ENTER THE VALID NUMBER")  
        else:
            print(number1/number2) 
    elif operator=="%":
        print(number1%number2)        
    elif operator=="√":
        print("ENTER THE NUMBER TO BE SQUARED (1st or 2nd ) :  ")
        num_sqt=float(input())
        if num_sqt==1:
            print(math.sqrt(number1)) # without function for sq root ---> (num ** 0.5) 
        elif num_sqt==2:
            print(math.sqrt(number2))
        else:
            print("❌ ENTER THE VALID NUMBER")    

    else:
        print("MAKE THE RIGHT CHOICE ✅!")
    print("DO YOU WANT TO CONTINUE ? ")
    print("(YES OR NO )")
    again_run= input().lower()

    if again_run!="yes":
        print("👋 Goodbye! Thanks for using the calculator.")
        break         
