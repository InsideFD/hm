import datetime


def log(filename=None):
    """
    Декоратор для логирования работы функций.

    Args:
        filename: Имя файла для записи логов. Если None - вывод в консоль.

    Returns:
        Декорированную функцию
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            # Формируем сообщение
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            func_name = func.__name__

            try:
                result = func(*args, **kwargs)
                message = f"{timestamp} - {func_name} ok\n"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message)
                else:
                    print(message, end="")

                return result

            except Exception as e:
                error_message = f"{timestamp} - {func_name} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message)
                else:
                    print(error_message, end="")

                raise e

        return wrapper

    return decorator
