

def load_cars():
  f = open("cars.db", "r")
  cars = []
  for car in f.readlines():
    cars.append(car[:-1])

  f.close()

  return cars

def write_cars(cars):
  f = open("cars.db", "w")
  for car in cars:
    f.write(car + '\n')

  f.close()

