# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 11:48:18 2021

@author: eu5492
"""
import math
import random

lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

number = random.randint(lower,upper)
chances = round(math.log(upper-lower+1,2))

print("You have only",chances,"chances to guess the number!\n")

while chances>0:
    guess = int(input("Guess a number:"))
    chances-=1
    if guess<number:
        print("Your guess is too low")
        print("You have",chances,"chances left")
    if guess>number:
        print("Your guess is too high")
        print("You have",chances,"chances left")
    if guess==number:
        print("You have guessed correct! Congratulations!")
        break
    
if chances==0:
    print("You used up all your chances. The number is %d",number)
    print("Better Luck Next Time!")
    