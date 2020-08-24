import pytest
import random
import string
from Poker_x_teenPatti import *
import os
import inspect
import re
import math
from decimal import Decimal, getcontext


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

def function_name_had_cap_letter(module_name):
    functions = inspect.getmembers(module_name, inspect.isfunction)
    for function in functions:
        t = re.findall('([A-Z])', function[0])
        if t:
            return True
    return False

def test_function_names():
    assert function_name_had_cap_letter(Poker_x_teenPatti) == False, "One of your function has a capitalized alphabet!"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 2500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"import pytest
import random
import string
from Poker_x_teenPatti import *
import os
import inspect
import re
import math
from decimal import Decimal, getcontext


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

def function_name_had_cap_letter(module_name):
    functions = inspect.getmembers(module_name, inspect.isfunction)
    for function in functions:
        t = re.findall('([A-Z])', function[0])
        if t:
            return True
    return False

def test_function_names():
    assert function_name_had_cap_letter(Poker_x_teenPatti) == False, "One of your function has a capitalized alphabet!"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 2500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"import pytest
import random
import string
from Poker_x_teenPatti import *
import os
import inspect
import re
import math
from decimal import Decimal, getcontext


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

def function_name_had_cap_letter(module_name):
    functions = inspect.getmembers(module_name, inspect.isfunction)
    for function in functions:
        t = re.findall('([A-Z])', function[0])
        if t:
            return True
    return False

def test_function_names():
    assert function_name_had_cap_letter(Poker_x_teenPatti) == False, "One of your function has a capitalized alphabet!"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 2500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"import pytest
import random
import string
from Poker_x_teenPatti import *
import os
import inspect
import re
import math
from decimal import Decimal, getcontext


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

def function_name_had_cap_letter(module_name):
    functions = inspect.getmembers(module_name, inspect.isfunction)
    for function in functions:
        t = re.findall('([A-Z])', function[0])
        if t:
            return True
    return False

def test_function_names():
    assert function_name_had_cap_letter(Poker_x_teenPatti) == False, "One of your function has a capitalized alphabet!"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 2500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"import pytest
import random
import string
from Poker_x_teenPatti import *
import os
import inspect
import re
import math
from decimal import Decimal, getcontext


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

def function_name_had_cap_letter(module_name):
    functions = inspect.getmembers(module_name, inspect.isfunction)
    for function in functions:
        t = re.findall('([A-Z])', function[0])
        if t:
            return True
    return False

def test_function_names():
    assert function_name_had_cap_letter(Poker_x_teenPatti) == False, "One of your function has a capitalized alphabet!"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 2500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"import pytest
import random
import string
from Poker_x_teenPatti import *
import os
import inspect
import re
import math
from decimal import Decimal, getcontext


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

def function_name_had_cap_letter(module_name):
    functions = inspect.getmembers(module_name, inspect.isfunction)
    for function in functions:
        t = re.findall('([A-Z])', function[0])
        if t:
            return True
    return False

def test_function_names():
    assert function_name_had_cap_letter(Poker_x_teenPatti) == False, "One of your function has a capitalized alphabet!"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 2500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"import pytest
import random
import string
from Poker_x_teenPatti import *
import os
import inspect
import re
import math
from decimal import Decimal, getcontext


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

def function_name_had_cap_letter(module_name):
    functions = inspect.getmembers(module_name, inspect.isfunction)
    for function in functions:
        t = re.findall('([A-Z])', function[0])
        if t:
            return True
    return False

def test_function_names():
    assert function_name_had_cap_letter(Poker_x_teenPatti) == False, "One of your function has a capitalized alphabet!"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 2500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"import pytest
import random
import string
from Poker_x_teenPatti import *
import os
import inspect
import re
import math
from decimal import Decimal, getcontext


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

def function_name_had_cap_letter(module_name):
    functions = inspect.getmembers(module_name, inspect.isfunction)
    for function in functions:
        t = re.findall('([A-Z])', function[0])
        if t:
            return True
    return False

def test_function_names():
    assert function_name_had_cap_letter(Poker_x_teenPatti) == False, "One of your function has a capitalized alphabet!"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 2500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"import pytest
import random
import string
from Poker_x_teenPatti import *
import os
import inspect
import re
import math
from decimal import Decimal, getcontext


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

def function_name_had_cap_letter(module_name):
    functions = inspect.getmembers(module_name, inspect.isfunction)
    for function in functions:
        t = re.findall('([A-Z])', function[0])
        if t:
            return True
    return False

def test_function_names():
    assert function_name_had_cap_letter(Poker_x_teenPatti) == False, "One of your function has a capitalized alphabet!"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 2500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"import pytest
import random
import string
from Poker_x_teenPatti import *
import os
import inspect
import re
import math
from decimal import Decimal, getcontext


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

def function_name_had_cap_letter(module_name):
    functions = inspect.getmembers(module_name, inspect.isfunction)
    for function in functions:
        t = re.findall('([A-Z])', function[0])
        if t:
            return True
    return False

def test_function_names():
    assert function_name_had_cap_letter(Poker_x_teenPatti) == False, "One of your function has a capitalized alphabet!"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 2500, "Make your README.md file interesting! Add atleast 500 words"

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

    ########################################################################################
    ########################################################################################
    ########################################################################################
    ########################################################################################
    ########################################################################################
    ################################################################################################################################################################################
    ########################################################################################
    ########################################################################################

    ################################################################################################################################################################################

    ########################################################################################
    ########################################################################################
    ########################################################################################
    ########################################################################################
    ########################################################################################
    ########################################################################################
    ########################################################################################