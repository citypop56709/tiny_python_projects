#!/usr/bin/env python3
"""
Author : Ayun Daywhea <daywhea@gmail.com>
Date   : 2022-05-25
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Parses the text to Jump the five for the numbers in it."""
    args = get_args()
    table = {
        '0': '5',
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1'
    }
    print(args.text.translate(str.maketrans(table)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
