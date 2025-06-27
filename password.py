#generate program to create Password
import random
import string
def main():
    print("Welcome to our random password generator")
    Strength=int(input("Enter the Length of password you Want: "))

    lowerA=string.ascii_lowercase
    upperB=string.ascii_uppercase
    digitC=string.digits
    symbolsD=string.punctuation
    ## print(symbolsD)

    combine=lowerA+upperB+digitC+symbolsD
    x= random.sample(combine, Strength)

    password="".join(x)
    print(password)
    main()
main()







