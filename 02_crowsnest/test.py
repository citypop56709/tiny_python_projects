#!/usr/bin/env python3
"""tests for crowsnest.py"""

import random
import string
import os
from sre_parse import SPECIAL_CHARS
from subprocess import getstatusoutput, getoutput
# flake8: noqa

prg = './crowsnest.py'
consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
template = 'Ahoy, Captain, {} {} off the larboard bow!'
errorTemplate = '{} is invalid. Input cannot contain numbers or special characters.'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('a', word)


# --------------------------------------------------
    """Function is changed so that it will check to make sure that the article is in uppercase as well. #noqa
    """


def test_consonant_upper():
    """brigantine -> a Brigatine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word.title()}')
        assert out.strip() == template.format('A', word.title())


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('an', word)


# --------------------------------------------------
    """Function is changed so that it will check to make sure that the article is in uppercase as well. #noqa
    """


def test_vowel_upper():
    """octopus -> an Octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word.upper()}')
        assert out.strip() == template.format('An', word.upper())


# --------------------------------------------------
    """The function will check to see if program will generate an error message if there is a number in the word. #noqa
    """


def test_number():
    """octopus -> 1Octopus"""

    for word in consonant_words:
        random_index = random.randint(0, len(word) - 1)
        word_random_letter = word[random_index]
        digit = random.choice(string.digits)
        word = word.replace(word_random_letter, digit, 1)
        out = getoutput(f'{prg} {word}')
        assert out.strip() == errorTemplate.format(word)


# --------------------------------------------------
    """The function will check to see if program will generate an error message if there is a special character in the word. #noqa
    """


def test_special_char():
    """octopus -> %Octopus"""

    for word in consonant_words:
        random_index = random.randint(0, len(word) - 1)
        word_random_letter = word[random_index]
        special_char = random.choice(string.punctuation)
        word = word.replace(word_random_letter, special_char, 1)
        out = getoutput(f'{prg} \'{word}\'')
        assert out.strip() == errorTemplate.format(word)
