#Christopher pullen
#28.11.2014
#fucntions

#in this functions the parameter is (number) 
def parameters (number):
    number=number+4
    #return is outputing number so that it can be called by the rest of the program
    return number

#main program
#argument value (4) is being assiged to parameter(number)
number = parameter(4)
#then number is printed
print (number)
# global is assigning the value 4 to the variable in the whole program including outside that fuction
global number_2
print (number_2 + number)
