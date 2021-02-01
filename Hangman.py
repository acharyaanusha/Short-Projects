# -*- coding: utf-8 -*-
import random

name = input("Enter your name : ")

print("Hello",name,"! Welcome to the hangman game.")

movies = ["titanic","cinderella","godfather","hangover","bourne","jumanji","frozen","brave","pinocchio","scream","skyfall","divergent"]
movie = random.choice(movies)

print("Guess the name of the movie")
guesses=''
turns = 10

while turns>0:
    fail =0
    for char in movie:
        if char in guesses:
            print(char)
            
        else:
            print("_")
            fail+=1
            
    if fail ==0:
        print("You win")
        print("The movie is",movie)
        break
    
    guess = input("Guess a letter: ")
    guesses+=guess
    
    if guess not in movie:
        turns-=1
        print("Wrong")
        print("You have",turns,"more turns left")
        if turns == 0:
            print("You lose")

