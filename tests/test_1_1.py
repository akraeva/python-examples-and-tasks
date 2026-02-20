from src.module_1 import (
    m_1_1_1,
)


def test_1_1_1(capsys):
    """
    Тест проверяет, что функция выводит сообщение.
    """
    m_1_1_1()
    captured = capsys.readouterr()
    assert captured.out == "Я изучаю Python!\n"
