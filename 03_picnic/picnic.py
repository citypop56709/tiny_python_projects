#!/usr/bin/env python3
"""
Author : Ayun Daywhea <daywhea@gmail.com>
Date   : 2022-05-21
Purpose: Going on a picnic.
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Going on a picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Items we are bringing to the picnic')

    parser.add_argument('-s',
                        '--sorted',
                        help='Whether to sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Process the text based on the user's arguments."""

    args = get_args()
    if (args.sorted):
        args.items.sort()
    bringing_text = ''
    if (len(args.items) == 1):
        bringing_text = f'{args.items[0]}.'
    elif (len(args.items) == 2):
        bringing_text = f'{args.items[0]} and {args.items[1]}.'
    else:
        last_item = args.items.pop()
        items_string = ', '.join(args.items)
        bringing_text = f'{items_string}, and {last_item}.'
    print(f'You are bringing {bringing_text}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
