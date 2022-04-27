#!/usr/bin/env python3
"""
Author : Ayun Daywhea <daywhea@gmail.com>
Date   : 2022-04-23
Purpose: Alert the crew!
"""

# flake8: noqa
import argparse
import string
from curses.ascii import isdigit


# --------------------------------------------------
def get_args():
    """Get command-line arguments for the crow's nest to shout-out."""

    parser = argparse.ArgumentParser(
        description='Give the sailor a thing to shout.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'word',
        metavar='word',
        type=str,
        help='The creature that the sailor will call out to the crew.')
    parser.add_argument(
        '--starboard',
        action='store_true',
        help='The point of the bow the creature is coming from')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    vowels = 'aeiou'
    args = get_args()
    for character in args.word:
        if (character in string.punctuation or isdigit(character)):
            print(
                f'{args.word} is invalid. Input cannot contain numbers or special characters.'  #noqa
            )
            return
    char = args.word[0]
    direction = 'larboard'
    article = 'an' if char.lower() in vowels else 'a'
    if (char.isupper()):
        article = article.capitalize()
    if (args.starboard):
        direction = 'starboard'
    print(f'Ahoy, Captain, {article} {args.word} off the {direction} bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
