#!/usr/bin/env python
"""Make messages start module."""

import os
from make_messages.cli import parse_args
from make_messages.messages import make_messages_


def main():
    print('Добро пожаловать в программу Make messages!')

    source_path, output = parse_args()
    output_path = os.path.join(os.getcwd(), output)

    print(f"Путь к исходному файлу: {source_path}")
    print(f"Папка для сохранения: {output_path}")

    output_filepath = make_messages_(source_path, output)

    print("Выполнено. Результат сохранен в файл: messages.txt")
    print(f"Путь к сохраненному файлу: {output_filepath}")


if __name__ == '__main__':
    main()
