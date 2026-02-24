import pytest
from src.module_1 import (
    m_1_4_1,
    m_1_4_2,
    m_1_4_3,
    m_1_4_4,
    m_1_4_5,
    m_1_4_6,
)


# m_1_4_1
@pytest.mark.parametrize(
    "input_val, expected",
    [
        # Sample Input
        ("12.0", "2\n"),
        ("21.4", "3\n"),
        ("9.6", "1\n"),
        # Граничные значения
        ("7.8", "0\n"),  # ≤7.8 → Земля
        ("11.2", "2\n"),  # ≥11.2 → Солнце
        ("16.4", "2\n"),  # ≤16.4 → Солнце
        ("0.0", "error\n"),  # ≤0 → error
        ("-1.5", "error\n"),  # Отрицательное
        ("17.0", "3\n"),  # >16.4 → улетит
    ],
)
def test_1_4_1(input_val, expected, mocker, capsys):
    """
    Тесты для орбит ракеты по скорости.
    """
    mocker.patch("builtins.input", return_value=input_val)
    m_1_4_1()
    captured = capsys.readouterr()
    assert captured.out == expected


# m_1_4_2
@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["3.6", "5"], "9.353 33.189\n"),  # Sample Input 1
        (["11.2", "11.8"], "213.647 259.864\n"),  # Sample Input 2
        (["1", "1"], "0.144 1.994\n"),  # Маленькая пирамида
        (["10", "1"], "14.434 89.127\n"),  # Низкая пирамида
        (["0", "5"], "error\n"),
        (["3.6", "0"], "error\n"),
        (["-1", "5"], "error\n"),
        (["3.6", "-1"], "error\n"),
    ],
)
def test_1_4_2(inputs, expected, mocker, capsys):
    """
    Тесты для объема и площади треугольной пирамиды.
    Валидация: a>0, h>0.
    """
    mocker.patch("builtins.input", side_effect=inputs)
    m_1_4_2()
    captured = capsys.readouterr()
    assert captured.out == expected


# m_1_4_3
@pytest.mark.parametrize(
    "input_year, expected",
    [
        # Sample Input
        ("2020", "366\n"),  # 2020÷4=505 ✓
        ("2025", "365\n"),  # 2025÷4=506.25 ✗
        # Ключевые случаи високосных годов
        ("2000", "366\n"),  # ÷400 ✓
        ("1900", "365\n"),  # ÷100 но не ÷400 ✗
        ("1600", "366\n"),  # ÷400 ✓
        ("1700", "365\n"),  # ÷100 но не ÷400 ✗
        ("2024", "366\n"),  # ÷4 ✓
        ("1582", "error\n"),  # ≤1582
        ("1500", "error\n"),  # До григорианского
    ],
)
def test_1_4_3(input_year, expected, mocker, capsys):
    """
    Тесты високосного года (григорианский календарь).
    """
    mocker.patch("builtins.input", return_value=input_year)
    m_1_4_3()
    captured = capsys.readouterr()
    assert captured.out == expected


# m_1_4_4
@pytest.mark.parametrize(
    "input_val, expected",
    [
        ("2", "2 рубля\n"),
        ("25", "25 рублей\n"),
        ("41", "41 рубль\n"),
        ("1", "1 рубль\n"),
        ("11", "11 рублей\n"),
        ("0", "ошибка\n"),
        ("-2", "ошибка\n"),
        ("100", "ошибка\n"),
    ],
)
def test_1_4_4(input_val, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_val)
    m_1_4_4()
    assert capsys.readouterr().out == expected


# m_1_4_5
@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["6", "150", "3"], "9\n"),
        (["6.5", "150.6", "4"], "8\n"),
        # Граничные
        (["1", "1000", "1"], "5\n"),
        # Ошибки
        (["0", "150", "3"], "error\n"),
        (["6", "0", "3"], "error\n"),
        (["6", "150", "0"], "error\n"),
        (["-1", "150", "3"], "error\n"),
    ],
)
def test_1_4_5(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs)
    m_1_4_5()
    assert capsys.readouterr().out == expected


# m_1_4_6
@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["12", "1", "1"], "error\n"),  # h=12 >11
        (["6", "47", "19"], "203.66\n"),
        # Граничные
        (["0", "0", "0"], "0.0\n"),
        (["11", "59", "59"], "359.99\n"),
        # Ошибки
        (["13", "0", "0"], "error\n"),
        (["6", "60", "0"], "error\n"),
        (["6", "0", "60"], "error\n"),
    ],
)
def test_1_4_6(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs)
    m_1_4_6()
    assert capsys.readouterr().out == expected
