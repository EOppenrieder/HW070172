# An advanced program to encode and decode Caesar ciphers

def main():
    ptext = input("Enter the message which is to be encrypted: ")
    key = eval(input("Enter the value of the key: "))
    ptext = ptext.lower()
    letter = "abcdefghijklmnopqrstuvwxyz"
    ctext = ""
    for ch in ptext:
        ctext = ctext + (letter[((ord(ch)) - 97) + key % 52])
        print("Your encoded message is {0}.".format(ctext))

main()