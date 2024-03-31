def add(a,b):
    return a+b
def sub (a,b):
    return a-b
def mul(a,b):
    return a*b
def div (a,b):
    return a/b
def fruits():
    fruit=["Apple","banana","mango","guava","kiwi","orange","coconut","grapes","lichi","black berry", "dragon fruit","sex"]
    return fruit
a = int(input("enter first no"))
b = int(input("enter second no"))
op=("press + for add \npress - for sub \npress * for multiplication \npress / for divide")
print(op)
symbol = input("enter symbol ")
if symbol == "+":
  print(add(a,b))
elif symbol == "-":
    print(sub(a,b))
elif symbol == "*":
    print(mul(a,b))
elif symbol == "/":
    print(div(a,b))
else:
    print("invalid input")