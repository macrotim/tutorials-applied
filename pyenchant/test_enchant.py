from enchant.checker import SpellChecker
import enchant
import pytest

@pytest.fixture
def enchant_dict():
    return enchant.Dict("en_US")

def test_check(enchant_dict):
    assert enchant_dict.check("Hello") is True
    assert enchant_dict.check("Helo") is False
    assert len(enchant_dict.suggest("Helo")) > 0

def test_spellchecker():
    chkr = SpellChecker("en_US")
    chkr.set_text("This is sme sample txt with erors.")
    assert [err.word for err in chkr] == ['sme', 'txt', 'erors']
