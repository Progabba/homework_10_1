from functools import wraps


def log(filename=None):
    """
    Декоратор для логирования вызовов функции и их результатов.

    Если вызов функции завершился успешно, записывается сообщение о том, что функция выполнилась корректно.
    Если в процессе выполнения функции произошла ошибка, записывается сообщение об ошибке и входные параметры функции.

    Аргументы:
        filename (str, optional): Путь к файлу, в который будут записываться логи.
                                  Если не задан, логи будут выводиться в консоль.

    Пример:
        @log(filename="mylog.txt")
        def my_function(x, y):
            return x + y

        my_function(1, 2)

        # В результате выполнения функции my_function(1, 2) будет возвращено значение 3,
        # а в лог-файл mylog.txt будет записано сообщение в следующем формате:
        # my_function ok

        @log()
        def another_function(x, y):
            return x - y

        another_function(5, 3)

        # В результате выполнения функции another_function(5, 3) будет возвращено значение 2,
        # а в консоль будет выведено сообщение:
        # another_function ok

    Возвращает:
        function: Декорированная функция с добавленным логированием.
    """

    def decorator(func):
        wraps(func)

        def wrapper(*args, **kwargs):
            log_message = ""
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                raise
            finally:
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)

        return wrapper

    return decorator


if __name__ == "__main__":

    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    # @log()
    # def my_function(x, y):
    #     return x + y

    my_function(1, 2, 4)
