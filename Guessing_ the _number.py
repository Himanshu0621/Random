#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
name  = input('Whats your name?')
number = random.randint(1,20)
print('Welcome, {}! I am thinking of an integer between 1 to 20. '.format(number))

number_of_guesses = 0
while number_of_guesses<10:
    guess = int(input('Guess a number'))
    number_of_guesses += 1
    
    if guess< number:
        print('Number is too low.')
    if guess > number:
        print('Number is too high.')
    if guess == number:
        break
        
if guess == number:
    print('Well done {}!, you guessd the number in {}attempts.'.format(name, number_of_guesses))
else:
    print('Sorry. you lose! The number that I was thinking was {}'.format(number))


# In[ ]:




