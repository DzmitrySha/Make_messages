"""Test Make messages"""

import os
import pytest
import tempfile
from make_messages.messages import make_messages_


FIXTURES_FOLDER = "fixtures"
XLSX_FILENAME = "mmtest.xlsx"
TXT_FILENAME = "messages.txt"


@pytest.fixture()
def xlsx_path():
    xlsx_path = os.path.join(os.getcwd(), FIXTURES_FOLDER, XLSX_FILENAME)
    return xlsx_path


@pytest.fixture()
def output_txt_filepath():
    output_txt_filepath = os.path.join(os.getcwd(),
                                       FIXTURES_FOLDER, TXT_FILENAME)
    return output_txt_filepath


def test_make_messages(xlsx_path, output_txt_filepath):
    with tempfile.TemporaryDirectory() as tmpdirname:
        output_filepath = make_messages_(xlsx_path, tmpdirname)
        with open(output_filepath) as f1:
            with open(output_txt_filepath) as f2:
                assert f1.read() == f2.read()
