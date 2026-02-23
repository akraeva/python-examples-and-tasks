import pytest
from src.module_1 import (
    m_1_4_1,
    m_1_4_2,
    m_1_4_3,
)


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
        # Ошибки
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
