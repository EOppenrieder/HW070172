# convert.py
# A program to convert Celsius temps to Fahrenheit

print("This program allows you to convert temperature")
print("entered in Celsius to Fahrenheit")

def main():
    
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature?: "))
        fahrenheit = 9 / 5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main ()