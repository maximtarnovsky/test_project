# файл decorators

import os


def log(filename=None):
    """Декоратор регистрирует детали выполнения функций"""

    def wrapper(func):

        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is None:
                    print(f"{func.__name__} ok")
                else:
                    if len(filename) > 0:
                        path_to_file = os.path.join(os.path.dirname(__file__), "../logs", filename)
                        with open(path_to_file, "w", encoding="utf-8") as file:
                            file.write(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename is None:
                    print(f"{func.__name__} error: {e}. Inputs: ({args}), {kwargs}")
                else:
                    path_to_file = os.path.join(os.path.dirname(__file__), "../logs", filename)
                    with open(path_to_file, "w", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: ({args}), {kwargs}")

        return inner

    return wrapper


@log(None)
def my_function(x, y):
    # raise ValueError("Something went wrong")
    return x + y


my_function(1, 2)


# # Ожидаемый вывод в лог-файл:
# mylog.txt # при успешном выполнении
#
# my_function ok
#
# # Ожидаемый вывод при ошибке:
# {func.__name__} error: {e}. Inputs: (1, 2), {}
#
# # Где
# тип ошибки заменяется на текст ошибки.


# файл test_decorators

import tempfile

# from src.decorators import log

def test_log_ok(capsys):
    """Тестирует выполнение декорированной функции"""

    @log()
    def func(x, y):
        return x + y

    result = func(1, 2)
    assert result == 3


def test_log_ok_file_log(capsys):
    """Тестирует запись в файл после успешного выполнения"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def func(x, y):
        return x + y

    func(1, 2)

    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()

    assert "func ok" in logs


def test_log_exception(capsys):
    """Тестирует вывод после ошибки в консоль"""

    @log()
    def func(x, y):

        return x + y

    func(1, "2")
    captured = capsys.readouterr()
    assert "func error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: ((1, '2')), {}\n" in captured.out


def test_log_exception_file_log():
    """Тестирует запись в файл после ошибки"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def func(x, y):
        return x + y

    func(1, "2")
    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()
    assert "func error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: ((1, '2')), {}" in logs



