#christopher pullen
#05.12.14
#development exercise 3 functions

def details ():
    currency = input ("please enter your currency (euro, us dollar or british pound)")
    currency_wanted = input ("please enter the currency you wish to convert too(euro , us dollar or British pound)")
    money = int(input( "please enter the amount of money you wish to be converted"))
    return currency,currency_wanted,money

def conversion (currency,currency_wanted,money):
    if currency == "euro" :
        if currency_wanted == "us doller":
            converted_money = money * 1.302
        else :
            converted_money = money *0.814
    elif currency == "us doller":
        if currency_wanted == "euro":
            converted_money = money *0.768
        else :
            converted_money = money *0.625
    else :
        if currency_wanted == "euro":
            converted_money = money *1.229
        else:
            converted_money = money *1.601
    return converted_money

def output (money,converted_money):
    print ("{0}={1}".format (money, converted_money))
    
currency, currency_wanted , money = details()
converted_money = conversion (currency,currency_wanted,money)
output(money,converted_money)
