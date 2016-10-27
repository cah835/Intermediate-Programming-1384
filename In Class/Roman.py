#Class that allows use of Roman numerals.  The constructor allows the user to
#send a string that can be "cast" as a Roman Numeral object.
class Roman:
    #Takes a Roman Numeral string passed to it and converts it to an integer.
    #The integer is the only instance data item for the class.
    def __init__(self, numeral = "I"):
        numeral = numeral.upper()
        switch = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        value = []

        #Convert string to integer list
        for each_letter in numeral:
            if not each_letter in switch:
                raise ValueError("Invalid Roman Numeral")
            value.append(switch[each_letter])

        #Accumulator
        self.number = 0
        count = 0

        #Convert integer list into integer value equal to roman numeral
        #Loop through and subtract if next value is greater
        while count < len(numeral) - 1:
            if value[count] < value[count + 1]:
                self.number -= value[count]
            else:
                self.number += value[count]
            count += 1
        #Add the last value
        self.number += value[len(numeral) - 1]

        return

    #Returns the string version ("Roman Numeral" version) of the instance
    #data item.
    def get_roman(self):

        roman_str = ""
        copy = self.number

        while copy >= 1000:
            roman_str += 'M'
            copy -= 1000
        if copy >= 900:
            roman_str += 'CM'
            copy -= 900
        if copy >= 500:
            roman_str += 'D'
            copy -= 500
        if copy >= 400:
            roman_str += 'CD'
            copy -= 400
        while copy >= 100:
            roman_str += 'C'
            copy -= 100
        if copy >= 90:
            roman_str += 'XC'
            copy -= 90
        if copy >= 50:
            roman_str += 'L'
            copy -= 50
        if copy >= 40:
            roman_str += 'XL'
            copy -= 40
        while copy >= 10:
            roman_str += 'X'
            copy -= 10
        if copy >= 9:
            roman_str += 'IX'
            copy -= 9
        if copy >= 5:
            roman_str += 'V'
            copy -= 5
        if copy >= 4:
            roman_str += 'IV'
            copy -= 4
        while copy >= 1:
            roman_str += 'I'
            copy -= 1
        return roman_str

    def __add__(self, other):
        answer = Roman()
        answer.number = self.number + other.number
        
        return answer

    
        
        
        
        
