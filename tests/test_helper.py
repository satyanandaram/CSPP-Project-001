
import os, sys
sys.path.append(os.getcwd())

from helper import *

import pytest

@pytest.mark.parametrize('text, result', [
    (), (), ()
])
def test_head(text, result):
    assert head(text) == result


@pytest.mark.parametrize('text, result', [
    (), (), ()
])
def test_head(text, result):
    assert tail(text) == result
