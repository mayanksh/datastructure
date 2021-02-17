max = int(input("enter the number: "))
#max= 20
odd_numbers = []
for i in range(max):
    if i%2==1:
        odd_numbers.append(i)
print(odd_numbers)