import pytest
from unittest.mock import  patch
from project import make_text, timer_control, validation

def test_make_text():
    assert make_text(1)[1]== 7
    assert make_text(2)[1]== 13
    assert make_text(3)[1] == 19

def test_timer_control():
    assert timer_control(60)[0]=='01'
    assert timer_control(60)[1] == '00'
    assert timer_control(61)[0] == '01'
    assert timer_control(61)[1] == '01'
    assert timer_control(123)[0] == '02'
    assert timer_control(123)[1] == '03'
    assert timer_control(93)[0] == '01'
    assert timer_control(93)[1] == '33'
    assert timer_control(666)[0] == '11'
    assert timer_control(66)[1] == '06'


def test_validation():
        assert validation('10') == 10
        assert validation('0') == 0
        assert validation('120') ==120
        assert validation(50) == 50
        assert validation(' ') == ValueError









