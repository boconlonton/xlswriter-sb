from contextlib import contextmanager


@contextmanager
def open_file(f_name: str):
    """A context manager works with file-like object

    Args:
        f_name (str): file_path
    """
    f = open(f_name, 'r')
    try:
        yield f
    finally:
        f.close()
