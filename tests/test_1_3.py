import pytest
from src.module_1 import m_1_3_1, m_1_3_2


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["-2.3", "8.72"], "0.03134\n"),  # Sample Input
        (["0", "0"], "0.0501\n"),
        (["1", "1"], "0.19221\n"),
        (["-1", "-1"], "0.47281\n"),
        (["3.14", "3.14"], "0.11334\n"),
    ],
)
def test_1_3_1(inputs, expected, mocker, capsys):
    """
    Тесты для математического выражения с округлением до 5 знаков.
    """
    mocker.patch("builtins.input", side_effect=inputs)
    m_1_3_1()
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        # Sample Input 1: НЕ существует (0,0)-(1,1)-(2,2) на одной линии
        (["0", "0", "1", "1", "2", "2"], "error\n"),
        # Sample Input 2
        (["-12.8", "3.4", "-7.7", "8.6", "-14.6", "-3.5"], "0.9113 14.0042 22.8319\n"),
        # Граничный случай: равносторонний треугольник
        (
            ["3", "0", "-3", "0", "0", "5.196"],
            "1.732 3.4641 15.5882\n",
        ),
        # Прямоугольный треугольник 3-4-5
        (["0", "0", "3", "0", "0", "4"], "1.0 2.5 10.3776\n"),
    ],
)
def test_1_3_2(inputs, expected, mocker, capsys):
    """
    Тесты для геометрии треугольника: радиусы и медианы.
    """
    mocker.patch("builtins.input", side_effect=inputs)
    m_1_3_2()
    captured = capsys.readouterr()
    assert captured.out == expected
