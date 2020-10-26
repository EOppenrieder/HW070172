# convert.py
# A program to convert Celsius temps to Fahrenheit

print("This program allows you to convert temperature")
print("entered in Celsius to Fahrenheit")

def main():

    for celsius in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        fahrenheit = 9 / 5 * celsius + 32
        print(celsius,fahrenheit)
    
main ()