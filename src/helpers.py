def isint(val: int) -> bool:
    """
    Check if a given input can be converted to an Integer.
    :param val: Input to check.
    :return: True if value can be converted to an Integer.
    """
    try:
        int(val)
        return True
    except ValueError:
        return False


def isinitialized(register: str, register_copy: dict) -> bool:
    """
    Check if a given register is already initialized.
    :param register: Register to check.
    :param register_copy: Dictionary of existing registers.
    :return: True if register is already initialized.
    """
    try:
        register_copy[register]
        return True
    except KeyError:
        return False


def get_runtime(func: callable, *args: any) -> int:
    """
    Returns the time difference between the start and end of a specific function.
    :param func: Function that is desired to run.
    :param args: Any arguments that function needs to run.
    :return: Runtime rounded to ms.
    """
    import time
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, round((end - start)* 1000)


def strip_docs(doc: str) -> str:
    """
    Removes all additional information on the docs (i.e. params and returns).
    :param doc: Full docstring of a function.
    :return: Stripped docstring with only main information.
    """
    return doc[:doc.find(':')]


def get_file_extension(filename: str) -> str:
    """
    Finds the extension of a file given its full name.
    :param filename: Complete filename.
    :return: The extension file type of the file.
    """
    return filename.split('.')[-1]
