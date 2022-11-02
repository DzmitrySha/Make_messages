"""Parser module - parsing args from user command line"""

import os
import argparse


def parsing_args():
    """Parsing args from user command line"""
    parser = argparse.ArgumentParser(
        prog='make_messages',
        description="""
        Make messages from special .xlsx file with table of last names, 
        pairs of parent and child names and template message in a row. 
        Returns a list of unique messages with every pair 
        of parent and child names inside."""
    )
    parser.add_argument('xlsx_filepath', type=str)
    parser.add_argument('-o', '--output', default=os.getcwd())
    args = parser.parse_args()
    return args.xlsx_filepath
