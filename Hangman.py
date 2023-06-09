#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def choose_word():
    word_list = ["men", "boy", "girl", "banana", "apple"]
    return random.choice(word_list)
        

 


# In[2]:



def display_word(word, guessed_letters):
    
    displayed = " "
    for letter in word:
        if letter in guessed_letters:
            displayed += letter + "_"
        
        else:
            display_word += "_"
    return displayed.strip() 
            


# In[3]:



def display_hangman(attempts):
    hangman =[
        "----",
        "|   |" ,
        "|    " +  ("O" if attempts < 6 else " "),
        "|    " + ("/|\\" if attempts < 5 else " "),
        "|    " +("/   \\" if attempts < 4 else ""),
       "_|_"
 ]
    for line in hangman:
        print(line)
        
        


# In[ ]:



def play_hangman():
   attempts = 6
   guessed_letters = []
   word = choose_word()
   word_count = len(word)
   #displayed = display_word(word, guessed_letters)
   
   while attempts > 0:
       print("You have", attempts, "attempts left")
       display_hangman(attempts)
       print("the word is a :", word_count, "letter word")
       
       guess = input("guess the word by entering a letter\n").lower()
       
       if len(guess) == 1 and guess.isalpha():
           
           
           
           if guess not in guessed_letters:
               guessed_letters.append(guess)

           else:
               print("Please the input should be a single letter and an alphabet")




           if guess in word:
               print("excellent!")

           else:
               print("Try again!")
               attempts -= 1

           if all(letter in guessed_letters for letter in word):
               print("You did it!")
               break
               
       else:
           print("letter already guessed")
           continue
           
   if attempts == 0:
       print("You've been hanged, you can play again. The word is", word)
           
           
           
play_hangman()
       
       
       
       
       
   
   


# In[ ]:





# In[ ]:




