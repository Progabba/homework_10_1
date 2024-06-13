import pytest

from src.decorators import log


def test_log_with_filename():
    @log(filename="test_log.txt")
    def test_func(x, y):
        return x + y

    # Вызов функции
    test_func(1, 2)

    with open("test_log.txt", "r") as file:
        log_content = file.read()
    assert "test_func" in log_content
    assert "test_func ok" in log_content


def test_log_with_exception():
    @log(filename="test_log.txt")
    def test_func(x, y):
        raise ValueError("Test error")

    # Вызов функции, которая вызывает исключение
    with pytest.raises(ValueError, match="Test error"):
        test_func(1, 2)

    # Проверка содержимого файла
    with open("test_log.txt", "r") as file:
        log_content = file.read()
        assert "test_func error: Test error. Inputs: (1, 2), {}\n" in log_content


def test_log_to_console(capsys):
    @log()
    def test_func(x, y):
        return x + y

    # Вызов функции
    test_func(1, 2)

    # Проверка содержимого консоли
    captured = capsys.readouterr()
    assert "test_func ok" in captured.out


def test_log_exception_to_console(capsys):
    @log()
    def test_func(x, y):
        raise ValueError("Test error")

    # Вызов функции, которая вызывает исключение
    with pytest.raises(ValueError, match="Test error"):
        test_func(1, 2)

    # Проверка содержимого консоли
    captured = capsys.readouterr()
    assert "test_func error: Test error. Inputs: (1, 2), {}" in captured.out
