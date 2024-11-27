cars = {'Honda' : 'Accord', 'Toyota' : 'Corolla', 'Nissan' : 'Altima', 'BMW' : 'x3'}
print(cars['Toyota'])
print(cars.get('Audi', 'Unknown'))
cars['AUdi']= 'q8'
print(cars.keys())
print(cars.values())
print(len(cars))
print('Maruti'in cars)
print('Maruti' not in cars)
del cars['Nissan']
print(cars)
cars['AUdi'] = 's3'
print(cars)

car_list = []

for i in cars:
    car_list.append(i)
print(car_list)