def add(x,y):
    sum = x + y
    print("Sum of numbers:", sum)
    

add(5, 4)

# list : contain different types, o based indexing
a = []
b = ["python", 2, 5.6, True]

print(b)
print(b[0])
print(b[1:3])

# concatenating two lists
a = ["apple", "orange", "grapes"]
b = [2, 5,"cabbage", "carrot"]
a = a + b
print(a)

#adding an element at the end of the list
b.append("pears")
print(b)


# for loop
numbers = [1,2,3,4,5]
total = 0
for number in numbers:
    total += number
print(total)

for number in numbers:
    if number % 2 == 0:
        print("Even number: ", number)
    else:
        print("Odd number: ", number)

# range function
# range(start, stop)
# range(start, stop, step)
for i in range(2, 10, 1):
    print(i)

























