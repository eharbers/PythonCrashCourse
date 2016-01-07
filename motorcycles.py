motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles[0] = 'honda'

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(2,'gazelle')
print(motorcycles)

del motorcycles[2]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
