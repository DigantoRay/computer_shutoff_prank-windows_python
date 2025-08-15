#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 19:39:27 2025.

@author: Gumbit
"""

import time as t
import os
import sys
import platform

name = 'Friend'


def greeting():
    """Greet the player."""
    print('Hello, ', end='')
    t.sleep(3)
    print(f'{name}.  ', end='')
    t.sleep(2)
    print(f'Let\'s play a game together, {name}.')


def ask_again():
    """Play if a non-integer is entered."""
    t.sleep(1)
    print(f'{name}.')
    t.sleep(2)
    print(f'Guess a number, {name}.')


def too_low():
    """Plays if answer is too low."""
    t.sleep(1)
    print('That is too low.')
    t.sleep(2)
    print('Guess again.')


def too_high():
    """Plays if answer is too high."""
    t.sleep(1)
    print('That is too high.')
    t.sleep(2)
    print('Guess again.')


def win():
    """Plays if right answer is picked."""
    t.sleep(3)
    print('You win.')
    t.sleep(2)
    print(f'Good job, {name}.')
    print('Bye bye.')
    t.sleep(2)
    sys.exit()


def teardown():
    """Initiate trolling."""
    t.sleep(3)
    print('Actually, no.  You took too long.')
    t.sleep(1)
    print('You only got three tries.')
    t.sleep(1)
    print('Maybe I can have fun now.')
    t.sleep(3)
    os.system('cls')
    t.sleep(2)
    print('Injection in progress; please wait.')
    t.sleep(2)
    os.system('cls')
    t.sleep(2)
    print('Architecture:', platform.architecture())
    print('Machine:', platform.machine())
    print('Network Id:', platform.node())
    print('Loading...')
    t.sleep(2)
    print('Version:', platform.version())
    print('CPU:', platform.processor())
    print('Release:', platform.release())
    print('Please wait...')
    t.sleep(2)
    print('Installing: [bit.elson//package1] [bit.elson//package2]')
    t.sleep(1)
    print('Installing: [rex.send_home//extract] [rex.send_home//comp.send]')
    t.sleep(1)
    print('Packaging fun_plugin...')
    t.sleep(3)
    for i in range(43):
        t.sleep(0.1)
        print(f'sent_id = rex.package{i}')
    t.sleep(3)
