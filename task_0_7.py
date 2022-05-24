def to_fahrenheit(celcius):
    fahrenheit = (celcius * 1.8) + 32
    return fahrenheit

def to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * (5 / 9)
    return celcius