import pytest
from lib.verify_text import *

## Given a empty string
## It raises an error 

def test_with_an_empty_string():
    with pytest.raises(Exception) as e:
        verify_text("")
    error_message = str(e.value)
    assert error_message == "No text"

## Given a string with first letter Cap and no punctuation
## It raises an error "The sentence starts with a capital letter, 
## but does not end in suitable punctuation"

def test_with_first_letter_caps_and_no_punctuation_on_end():
    with pytest.raises(Exception) as e:
        verify_text("Today is a good day")
    error_message = str(e.value)
    assert error_message == "No punctuation finishing the sentence"


## Given a string with no first letter Cap and punctuation
## It raises an error

def test_with_no_first_letter_caps_and_punct_on_end():
    result = verify_text("tomorrow will a good day!")
    assert result == "No capital letter at the start of the sentence"    

## Given a string with no first letter cap and no punctuation
## It raises an error

def test_with_no_cap_and_no_punct():
    result = verify_text("today is a good day") 
    assert result == "No capital letter at start or punctuation at the end"

## Given a string with first letter Cap and punctuation
## It returns True

def test_with_capital_letter_and_punctuation():
    result = verify_text("Today is the greatest day ever.") 
    assert result == "This text is CORRECT!"