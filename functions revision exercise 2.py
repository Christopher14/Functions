#christopher pullen
#28.11.2014
# revision exercise 2 functions

def details () :
    number = int(input( "please input an odd number"))
    number_check = number % 2
    if number_check == 1 :
       for count in range (number,0,-2):
        stars= count * "*"
        print ("{0:^{1}}".format(stars,number))
        

details()


