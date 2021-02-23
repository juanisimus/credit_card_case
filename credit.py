def typeofcard(num):
    #Check the type of card 
    
    numstr = ''.join([str(elem) for elem in num])
    
    if len(numstr) < 11:
        print(len(numstr))
        print("INVALID")
    amex = (
        numstr.startswith('37',0,3) or
        numstr.startswith('34',0,3)
        ) and len(numstr) == 15

    master_card = (
        numstr.startswith('51',0,3) or
        numstr.startswith('52',0,3) or
        numstr.startswith('53',0,3) or
        numstr.startswith('54',0,3) or
        numstr.startswith('55',0,3) 
        ) and len(numstr) == 16

    visa = (numstr.startswith('4')) and (len(numstr) == 13 or len(numstr) == 16)

    if amex:
        print("AMEX")
    elif master_card:
        print("MASTER CARD")
    elif visa:
        print("VISA")
    else:
        print("INVALID")
    


def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum


def validate(cc_num):
    # reverse the credit card number
    cc_num = cc_num[::-1]
    
    try:
        # convert to integer list
        cc_num = [int(x) for x in cc_num]
        # double every second digit
        doubled_second_digit_list = list()
        digits = list(enumerate(cc_num, start=1))
        for index, digit in digits:
            if index % 2 == 0:
                doubled_second_digit_list.append(digit * 2)
            else:
                doubled_second_digit_list.append(digit)

        # add the digits if any number is more than 9
        doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]
        # sum all digits
        sum_of_digits = sum(doubled_second_digit_list)
        # return True or False
        return sum_of_digits % 10 == 0
    except ValueError:
        pass


if __name__ == "__main__":
    while True:
        card = input("Enter the card number: ")
        if validate(card):
            typeofcard(card)
            break
        else:
            print("INVALID")
        
            
            
            
              
            