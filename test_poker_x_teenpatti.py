import pytest
import random
import string
import poker_x_teenpatti as pxt
import os
import inspect
import re
import math
from decimal import Decimal, getcontext

value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
README_CONTENT_CHECK_FOR = [
    'keyword',
    'positional',
    'tuple',
    'time_it',
    'myprint',
    'squared_power_list',
    'create_list',
    'polygon_area',
    'temp_converter',
    'speed_converter',
    'absolute zero',
    'negative',
    'positive'
]

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(pxt, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 40, 'You are not writing proper heading'

def test_generate_deck_using_list_comprehension():
    assert pxt.generate_deck_using_list_comprehension(suits,value) == ['2 spades', '2 clubs', '2 hearts', '2 diamonds', '3 spades', '3 clubs', '3 hearts', '3 diamonds', '4 spades', '4 clubs', '4 hearts', '4 diamonds', '5 spades', '5 clubs', '5 hearts', '5 diamonds', '6 spades', '6 clubs', '6 hearts', '6 diamonds', '7 spades', '7 clubs', '7 hearts', '7 diamonds', '8 spades', '8 clubs', '8 hearts', '8 diamonds', '9 spades', '9 clubs', '9 hearts', '9 diamonds', '10 spades', '10 clubs', '10 hearts', '10 diamonds', 'jack spades', 'jack clubs', 'jack hearts', 'jack diamonds', 'queen spades', 'queen clubs', 'queen hearts', 'queen diamonds', 'king spades', 'king clubs', 'king hearts', 'king diamonds', 'ace spades', 'ace clubs', 'ace hearts', 'ace diamonds'],'deck is not generated properly'

def test_generate_deck():
    assert pxt.generate_deck(suits,value) == ['2 spades', '2 clubs', '2 hearts', '2 diamonds', '3 spades', '3 clubs', '3 hearts', '3 diamonds', '4 spades', '4 clubs', '4 hearts', '4 diamonds', '5 spades', '5 clubs', '5 hearts', '5 diamonds', '6 spades', '6 clubs', '6 hearts', '6 diamonds', '7 spades', '7 clubs', '7 hearts', '7 diamonds', '8 spades', '8 clubs', '8 hearts', '8 diamonds', '9 spades', '9 clubs', '9 hearts', '9 diamonds', '10 spades', '10 clubs', '10 hearts', '10 diamonds', 'jack spades', 'jack clubs', 'jack hearts', 'jack diamonds', 'queen spades', 'queen clubs', 'queen hearts', 'queen diamonds', 'king spades', 'king clubs', 'king hearts', 'king diamonds', 'ace spades', 'ace clubs', 'ace hearts', 'ace diamonds'], 'Deck is not generated properly'

def test_check_for_number_sequence_for_no_sequence():
    my_list = [1,3,2,4,8]
    assert pxt.check_for_number_sequence(my_list) == False, 'This shouldnt be a sequence'

def test_check_for_number_sequence_for_sequence():
    my_list = [1,3,2,4,6,5]
    assert pxt.check_for_number_sequence(my_list) == True, 'This shouldnt be a sequence'

def test_check_for_color_for_same_color():
    my_list = ['diamonds','diamonds','diamonds','diamonds']
    assert pxt.check_for_color(my_list) == True,'The output should say they are all same'

def test_check_for_color_for_different_color():
    my_list = ['diamonds','diamonds','diamonds','hearts']
    assert pxt.check_for_color(my_list) == False,'It is okay to be different, but you are not cathcing that..'

def test_transform_value_list_for_single_occurance_jack():
    my_list = ['1','2','jack']
    assert pxt.transform_value_list(my_list) == [1,2,11],'jack Conversion not working'

def test_transform_value_list_for_single_occurance_queen():
    my_list = ['1','2','queen']
    assert pxt.transform_value_list(my_list) == [1,2,12],'Queen Conversion not working'

def test_transform_value_list_for_single_occurance_king():
    my_list = ['1','2','king']
    assert pxt.transform_value_list(my_list) == [1,2,13],'King Conversion not working'

def test_transform_value_list_for_single_occurance_ace():
    my_list = ['1','2','ace']
    assert pxt.transform_value_list(my_list) == [1,2,14],'Ace Conversion not working'

def test_transform_value_list_for_multiple_occurance_jack_and_queen():
    my_list = ['1','queen','jack']
    assert pxt.transform_value_list(my_list) == [1,12,11],'Multiple Combinations replace not working'

def test_transform_value_list_for_multiple_occurance_jack_and_king():
    my_list = ['1','king','jack']
    assert pxt.transform_value_list(my_list) == [1,13,11],'Multiple Combinations replace not working'

def test_transform_value_list_for_multiple_occurance_jack_and_jack():
    my_list = ['1','jack','jack']
    assert pxt.transform_value_list(my_list) == [1,11,11],'Multiple Combinations replace not working'

def test_transform_value_list_for_multiple_occurance_jack_and_ace():
    my_list = ['1','ace','jack']
    assert pxt.transform_value_list(my_list) == [1,14,11],'Multiple Combinations replace not working'

def test_transform_value_list_for_multiple_occurance_queen_and_queen():
    my_list = ['1','queen','queen']
    assert pxt.transform_value_list(my_list) == [1,12,12],'Multiple Combinations replace not working'

def test_transform_value_list_for_multiple_occurance_king_and_queen():
    my_list = ['1','king','queen']
    assert pxt.transform_value_list(my_list) == [1,13,12],'Multiple Combinations replace not working'

def test_transform_value_list_for_multiple_occurance_ace_and_queen():
    my_list = ['1','ace','queen']
    assert pxt.transform_value_list(my_list) == [1,14,12],'Multiple Combinations replace not working'

def test_transform_value_list_for_multiple_occurance_king_and_king():
    my_list = ['1','king','king']
    assert pxt.transform_value_list(my_list) == [1,13,13],'Multiple Combinations replace not working'

def test_transform_value_list_for_multiple_occurance_king_and_ace():
    my_list = ['1','ace','king']
    assert pxt.transform_value_list(my_list) == [1,14,13],'Multiple Combinations replace not working'

def test_transform_value_list_for_multiple_occurance_ace_and_ace():
    my_list = ['1','ace','ace']
    assert pxt.transform_value_list(my_list) == [1,14,14],'Multiple Combinations replace not working'

def test_show_for_5_for_1_v_1():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    set2 = ['ace spades', 'king spades', 'queen spades','jack spades','10 spades']
    assert pxt.show(set1,set2) == '0',"Royal Flush vs Royal Flush should be a draw"

def test_show_for_4_for_1_v_1():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    set2 = ['ace spades', 'king spades', 'queen spades','jack spades']
    assert pxt.show(set1,set2) == '0',"Royal Flush vs Royal Flush should be a draw"

def test_show_for_3_for_1_v_1():
    set1 = ['ace hearts', 'king hearts', 'queen hearts']
    set2 = ['ace spades', 'king spades', 'queen spades']
    assert pxt.show(set1,set2) == '0',"Royal Flush vs Royal Flush should be a draw"

def test_show_for_5_for_1_v_2():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    set2 = ['9 spades', 'king spades', 'queen spades','jack spades','10 spades']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs straight Flush, royal flush should win"

def test_show_for_4_for_1_v_2():
    set1 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    set2 = ['10 spades', 'king spades', 'queen spades','jack spades']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs straight Flush, royal flush should win"

def test_show_for_3_for_1_v_2():
    set1 = ['ace hearts', 'king hearts', 'queen hearts']
    set2 = ['jack spades', 'king spades', 'queen spades']
    assert pxt.show(set1,set2) == '1',"Royal Flush vs straight Flush, royal flush should win"

def test_show_for_5_for_2_v_1():
    set1 = ['9 spades', 'king spades', 'queen spades','jack spades','10 spades']
    set2 = ['ace hearts', 'king hearts', 'queen hearts','10 hearts','jack hearts']
    assert pxt.show(set1,set2) == '2',"straight Flush vs Royal Flush , royal flush should win"

def test_show_for_4_for_2_v_1():
    set1 = ['10 spades', 'king spades', 'queen spades','jack spades']
    set2 = ['ace hearts', 'king hearts', 'queen hearts','jack hearts']
    assert pxt.show(set1,set2) == '2',"straight Flush vs Royal Flush, royal flush should win"

def test_show_for_3_for_2_v_1():
    set1 = ['jack spades', 'king spades', 'queen spades']
    set2 = ['ace hearts', 'king hearts', 'queen hearts']
    assert pxt.show(set1,set2) == '2',"straight Flush vs Royal Flush, royal flush should win"