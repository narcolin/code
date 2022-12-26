#-------------------------------------------------------------------------------
# Name: Nicole      module1
# Purpose:
#
# Author:      Hisham
#
# Created:     15/01/2015
# Copyright:   (c) Hisham 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math

def cat_twice(part1, part2):
    cat = part1 + part2
    cat += cat
    print(cat)

def sqr(x):
    return x*x

def sqrtsqr(x):
    a = sqr(x)
    b = math.sqrt(a)
    print "a:", a, " b:", b

def main():
##    cat_twice("One ", "two ")
##    sqrtsqr(3)
    print math.sqrt(sqr(7))

if __name__ == '__main__':
    main()
