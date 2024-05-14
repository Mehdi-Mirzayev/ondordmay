import random
import math

def process_numbers():
    
    numbers = [random.randint(20, 50) for _ in range(5)]
    print("Istifade olunan random reqemler:", numbers)

    
    squared_even_numbers = [math.pow(num, 2) for num in numbers if num % 2 == 0]
    
    print("Kvadrata Yukseldilmis cüt rəqəmlər:", squared_even_numbers)


process_numbers()
