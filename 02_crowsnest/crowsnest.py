#!/usr/bin/env python3
"""
Author : Ayun Daywhea <daywhea@gmail.com>
Date   : 2022-04-23
Purpose: Alert the crew!
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments for the crow's nest to shout-out."""

    parser = argparse.ArgumentParser(
        description='Give the sailor a thing to shout.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'thing',
        metavar='str',
        type=str,
        help='The creature that the sailor will call out to the crew.')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    vowels = ['a', 'e', 'i', 'o', 'u']
    args = get_args()
    article = 'a'
    if (args.thing[0].lower() in vowels):
        article = 'an'
    print(f'Ahoy, Captain, {article} {args.thing} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
