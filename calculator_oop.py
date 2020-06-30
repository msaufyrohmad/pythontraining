#!/usr/bin/env python

class Calculator:
    def __init__(self,num1=0,num2=0):
        self.num1=num1
        self.num2=num2

    def add(self):
        return self.num1+self.num2
    
    def minus(self):
        return self.num1-self.num2

    def mult(self):
        return self.num1*self.num2

    def div(self):
        return self.num1/self.num2

    def take_number(self,msg):
        num=input(msg)
        while not num.isnumeric():
            print('The value need to be a number')
            num=input(msg)
        return int(num)


run=1
print('Worlds First OOP Calculator ;)')
while run==1:
    p1=Calculator()
    num1=p1.take_number('Enter first number:')
    num2=p1.take_number('Enter second number:')
    p1=Calculator(num1,num2)
    answer=0
    select=int(input('Select operation. 1. add 2.minus 3.multiply 4.divide:'))
    if select==1:
        answer=p1.add()
    elif select==2:
        answer=p1.minus()
    elif select==3:
        answer=p1.mult()
    elif select==4:
        answer=p1.div()
    else:
        print('Invalid Operation')
    print('The answer is:',answer)




    



    



    



    
