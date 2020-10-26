
def main(): 
    print("This program converts Fahrenheit temperatures to Celsius.")
    fahrenheit = eval(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * (5 / 9)

    print("The temperature is",celsius,"degrees Celsius.")

main ()