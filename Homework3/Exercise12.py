def main():
    print("With this program, you can perform basic mathematical calculations.")
    print("Use + to add nunbers, - to subtract them, * to multiply them.")
    print("To divide numbers, use / and to expone them, use **.")
    for i in range(100):
      calc = eval(input("Enter the expression you want to be performed: "))
      print("=",calc)
      input("Press the <Enter> key to quit.")

main ()
