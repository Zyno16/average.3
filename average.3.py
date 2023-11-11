num =list()
while True:
    inp = input("enter the number")
    if inp == "done" : break
    value = float(inp)
    num.append(value)
average = sum(num) / len(num)

print("the average  " ,average)