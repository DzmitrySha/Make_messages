"""Parser module - parsing args from user command line"""

import argparse


def parsing_args():
    """Parsing args from user command line"""
    parser = argparse.ArgumentParser(
        prog='make_messages',
        description="Make messages from special .xlsx file")
    parser.add_argument('xlsx_filepath', type=str)
    args = parser.parse_args()
    return args.xlsx_filepath
