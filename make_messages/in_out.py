"""Working with file system module
модуль для работы с файловой системой
"""

import os


def create_dir(dir_path: str):
    """Create directory if it not exists"""
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
#
#
# def write_to_file(file_path, file_content):
#     """Write source content to file"""
#     flag = 'wb' if isinstance(file_content, bytes) else 'w'
#     with open(file_path, flag) as file:
#         file.write(file_content)
