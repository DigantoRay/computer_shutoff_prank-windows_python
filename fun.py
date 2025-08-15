#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 19:29:52 2025.

@author: Gumbit
"""

import fun_aux
import time as t
import sys
import os
import random

fun_aux.greeting()
while True:  # Game start or exit
    choice = input('y/n: ')
    if choice == 'y':
        t.sleep(1)
        break
    elif choice == 'n':
        t.sleep(2)
        print(f'Goodbye, {fun_aux.name}.')
        t.sleep(2)
        sys.exit()

while True:  # Main loop
    target = random.randint(1, 20)
    print('I am thinking of a number between 1 and 20.  Guess the number.')
    for i in range(3):
        try:
            guess = int(input('> '))
        except (TypeError, ValueError):
            fun_aux.ask_again()
            continue
        if guess < target:
            fun_aux.too_low()
            continue
        elif guess > target:
            fun_aux.too_high()
            continue
        else:
            fun_aux.win()
    fun_aux.teardown()
    print(f'Thank you, {fun_aux.name}.  Goodbye.')
    t.sleep(3)
    os.system("shutdown /s /t 0")
    sys.exit()
