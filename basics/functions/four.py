import math
def area_and_circumfrance(radius):
  area = math.floor(math.pi * radius **2)
  circumfrance =  math.floor(2 *math.pi*radius)
  return [area,circumfrance]


a,c = area_and_circumfrance(5)
print("area: ",a ,"circumfrance:",c)