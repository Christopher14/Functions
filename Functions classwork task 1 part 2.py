#Christopher Pullen
#25-11-2014
#functions class exercise task1 part 2

def details ():
    first_name = input("please enter your first name")
    last_name = input ("please enter your last name")
    gender = input ("please enter your gender ")
    house_number = int(input("please enter your house number"))
    street_name = input("please enter your street name")
    town= input("please enter the town in which you live in")
    post_code = input("please enter your post code")
    return first_name, last_name, gender, 

def message (first_name,last_name,gender):
    name = msg.capitalize(first_name) + "" +  msg.capitalize(last_name)
    gender= msg.lower(gender)
    if gender == "male" :
        print(" Hello Mr. {0} " .format (name))
    else :
        print (" Hello Ms. {0} " .format (name))


#main program

a,b,c=details ()
message (a,b,c)


         
