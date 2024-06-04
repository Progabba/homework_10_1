from functools import wraps


def log(filename=None):
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

    my_function(1, 2, 3)