from unittest import mock

import main
from main import *


@mock.patch("main.DOB")


def test_day(mock_findaday):

    mock_findaday.return_value
    assert mock_findaday()

