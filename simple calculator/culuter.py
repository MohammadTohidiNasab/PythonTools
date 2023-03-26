num1 = int (input("Enter numer 1 : "))
num2 = int (input("Enter numer 2 : "))
action = str (input(" choice action :   \n   add (+) :    \n   sub (-) :    \n   mult(*) :    \n   div (/) :  \n \t \t"))

print("resullt is =")
if action =="+":
    print((num1+num2))
elif action == "-":
    print(num1-num2)
elif action == "*":
    print((num1*num2))
else:
    print((num1 / num2))
