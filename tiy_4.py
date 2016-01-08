#4-3
print("---[4-3]")
for count in range(1,21):
   print(count)

#4-4 iets minder getalletjes
print("---[4-4]")
numbers =[]
numbers = [number for number in range(1,101)]
print(numbers)

#4-5
print("---[4-5]")
print("min: " + str(min(numbers)))
print("max: " + str(max(numbers)))
print("sum: " + str(sum(numbers)))

#4-6
print("---[4-6]")
odd_list=[]
for odd in range(1,20,2):
   odd_list.append(odd)
print(odd_list)

#4-7
print("---[4-7]")
three_list=[]
for three in range(3,31,3):
   three_list.append(three)
print(three_list)

#4-8
print("---[4-8")
cube_list=[]
for cube in range(1,11):
   cube_list.append(cube**3)
print(cube_list)

#4-9
print("---[4-9]")
cube_list_two=[]
cube_list_two = [cube**3 for cube in range(1,11)]
print(cube_list_two)
