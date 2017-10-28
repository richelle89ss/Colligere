"""
Written by  : Shreyas Daniel - github.com/shreydan
Description : Uses Pythons eval() function
              as a way to implement calculator.
             
Functions available:
--------------------------------------------
                         + : addition
                         - : subtraction
                         * : multiplication
                         / : division
                         % : percentage
                         e : 2.718281...
                        pi : 3.141592... 
                      sine : sin(rad)
                    cosine : cos(rad)
                   tangent : tan(rad)
                 remainder : XmodY
               square root : sqrt(n)
  round to nearest integer : round(n)
convert degrees to radians : rad(deg)
"""

import math
import sys


def calc(k):
    
    k = k.replace(' ', '')
    k = k.replace('^', '**')
    k = k.replace('=', '')
    k = k.replace('?', '')
    k = k.replace('%', '/100')
    k = k.replace('rad', 'radians')
    k = k.replace('mod', '%')

    functions = ['sin', 'cos', 'tan', 'sqrt', 'pi', 'radians', 'e'] 

    for i in functions:
        if i in k.lower():
            withmath = 'math.' + i
            k = k.replace(i, withmath)

    try:
        k = eval(k)
    except ZeroDivisionError:
        print("Can't divide by 0")
        exit()
    except NameError:
        print('Invalid input')
        exit()
    except AttributeError:
        print('Check usage method')
        exit()
        
    return k


def result(k):
    print("\n" + str(calc(k)))


def main():
    
    print("\nScientific Calculator\nEg: sin(rad(90)) + 50% * (sqrt(16)) + round(1.42^2) - 12mod3\nEnter quit to exit")

    if sys.version_info.major >= 3:
        while True:
            k = input("\nWhat is ")
            if k == 'quit':
                break
            result(k)

    else:
        while True:
            k = raw_input("\nWhat is ")
            if k == 'quit':
                break
            result(k)


if __name__ == '__main__':
    main()
