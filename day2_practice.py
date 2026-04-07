# Day_2
numbers=[]
for i in range(5):
    num=int(input("Enter the number:"))
    numbers.append(num)

print("Numbers:",numbers)

total=sum(numbers)
print("The sum of the numbers is:",total)

avg=total/len(numbers)
print("The average is:",avg)

print("Max",max(numbers))
print("Min",min(numbers))

even_numbers=[n for n in numbers if n%2==0]
print("even_numbers:",even_numbers)