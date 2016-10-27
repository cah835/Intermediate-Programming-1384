from Roman import *

def main():
    user_info= input('Enter a roman Numeral: ')
    roman1 = Roman(user_info)
    roman2 = Roman(input('Enter another Roman Numeral: '))

    print(roman1.get_roman(), '=' , roman1.number)
    print(roman2.get_roman(), '=' , roman2.number)

 

    roman3= roman1 + (roman2)
    print(roman3.get_roman(), '=', roman3.number)
    

    return

main()
