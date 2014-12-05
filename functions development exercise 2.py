#Christopher pullen
#05-12-2014
#Functions develpment exercise 2

def details ():
    number = int(input("please enter an odd number"))
    return number
def check (number):
    if number % 2 == 1:
        odd_number = number
        return odd_number
def diamond (odd_number):
    for count in range (1,odd_number,+2):
        stars = count * "*"
        print ("{0:^{1}}".format (stars,odd_number))
    for value in range (odd_number,0,-2):
        stars = value * "*"
        print ("{0:^{1}}".format (stars,odd_number))

number = details ()
odd_number = check (number)
diamond(odd_number)
