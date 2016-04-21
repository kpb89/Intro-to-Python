#! /usr/bin/env python
# function.py


def typing_speed(words,seconds):
    """Returns the typing speed using words/seconds"""
    return ((words/seconds) * 60)

def remove_rightmost_digit(num):
    """ Removes the last digit"""
    return int(num / 10)

def get_rightmost_digit(num):
    """Retrieves the last digit"""
    # Convert to string, get last character
    rmv = str(num)[-1]
    # Return the integer
    return int(rmv)

    #Can also do
    num % 10
        
def month(code):
    """Returns the month"""
    return int(code[2:4])

def main():
    # testing typing_speed
    print(format(typing_speed(3,70),".2f"), "should be 2.57")
    print(format(typing_speed(200,175),".2f"), "should be 68.57")
    print(format(typing_speed(4,166),".2f"), "should be 1.44")
    print(format(typing_speed(1,189),".2f"), "should be 0.00")

    # testing remove_rightmost_digit
    print(remove_rightmost_digit(1234), "should be 123")
    print(remove_rightmost_digit(46352), "should be 4635")
    print(remove_rightmost_digit(2), "should be 0")
    print(remove_rightmost_digit(344), "should be 34")

    #testing get_rightmost_digit
    print(get_rightmost_digit(32737), "should be 7")
    print(get_rightmost_digit(48371), "should be 1")
    print(get_rightmost_digit(12), "should be 2")
    print(get_rightmost_digit(239), "should be 9")
     
    #testing month
    print(format (month('150724'), "02d"), "should be 07")
    print(format (month('141122'), "02d"), "should be 11")
    print(format (month('121030'), "02d"), "should be 10")
    print(format (month('110916'), "02d"), "should be 09")
if __name__ == "__main__":
    main()
