import pytest
from lib.estimate_reading_time import *

## Given 200 words
## It returns a reading time of 1.0

def test_with_two_hundred_words():
    text = " ".join(["one" for i in range(0, 200)])
    result = estimate_reading_time(text)
    assert result == 1.0

## Given 400 words
## It returns a reading time of 2.0

def test_with_four_hundred_words():
    text = " ".join(["one" for i in range(0, 400)])
    result = estimate_reading_time(text)
    assert result == 2.0

## Given 300 words
## It returns a reading time of 1.5

def test_with_three_hundred_words():
    text = " ".join(["one" for i in range(0, 300)])
    result = estimate_reading_time(text)
    assert result == 1.5

## Given 500 words
## It returns a reading time of 2.5

def test_with_five_hundred_words():
    text = " ".join(["one" for i in range(0, 500)])
    result = estimate_reading_time(text)
    assert result == 2.5

## Given an empty string
## It raises an error because there is nothing to calculate

def test_with_empty_string():
    with pytest.raises(Exception) as e:
        estimate_reading_time("")
    error_message = str(e.value)
    assert error_message == "Text needs to be added in order to calculate a reading time"