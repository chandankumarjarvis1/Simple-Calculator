print("=== TERMUX ===")
print("++++ Caclulator ++++")
print("1. Add")
print("2. Sub")
print("3. Multiplication")
print("4. Divide")
print("5. Square")
print("6. Cube")
choose=input("Please enter your choice :")
if choose=="1" and "Add" and "add" and "addition":
   lst = []
   num = int(input('How many numbers: '))
   for n in range(num):
      numbers = int(input('Enter number '))
      lst.append(numbers)
   print("Result :", sum(lst))
if choose=="2" and "sub" and "Sub" and "Subtraction":
   num1=float(input("Enter number :"))
   num2=float(input("Enter number :"))
   sub=(num1-num2)
   print("Result :",sub)
if choose=="3" and "Multi" and "multi" and  "Multiplicaton":
   num4 = float(input("Enter number :"))
   num5 = float(input("Enter number :"))
   mul=(num4*num5)
   print("Result :",mul)
if choose =="4" and "Divide" and "Div" and "div":
   ls=float(input("Enter number :"))
   ls1=float(input("Enter number :"))
   div=(ls/ls1)
   print("Result :",div)
if choose == "5" and "square" and "Square":
   ps=int(input("Enter number :"))
   sq=(ps*ps)
   print("Square Result :",sq)
if choose == "6" and "cube" and "Cube":
   l=int(input("Enter number :"))
   cub=(l*l*l)
   print("Cube Result :", cub)
