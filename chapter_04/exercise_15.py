'''
Prompt user for input city
Prompt user for rainfall amount (integer)
If user enters NULL city name, exit loop and print report: {City Name}: {Accumulated Rainfall}
'''

def get_rainfall():
    CITIES = {}
    while True:
        input_city = input('City: ')
        if not input_city:
            break
        
        input_rainfall = int(input('Rainfall: '))

        if input_city not in CITIES:
            CITIES[input_city] = 0
            CITIES[input_city] = input_rainfall
        else:
            CITIES[input_city] += input_rainfall
    
    for city, rainfall in CITIES.items():
        print(f'{city}: {rainfall}')

if __name__ == "__main__":
    get_rainfall()