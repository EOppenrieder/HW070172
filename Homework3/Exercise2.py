#convert.py
# A program to convert Celsius temps to Fahrenheit

print("This program allows you to convert temperature")
print("entered in Celsius to Fahrenheit")

def main():
    celsius = eval(input("What is the Celsius temperature?: "))
    fahrenheit = 9 / 5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")
main ()

input("Press the <Enter> key to quit.")
