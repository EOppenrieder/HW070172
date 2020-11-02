# A program to encode and decode Caesar ciphers

def main():
    pltext = input("Enter the message which is to be encrypted: ")
    key = eval(input("Enter the key's value: "))
    ctext = ""
    for ch in pltext:
        ctext = ctext + (chr(ord(ch) + key))
        print("Your encoded message is {0}.".format(ctext))
    
main()