#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err:
        stderr.write("Exception: {}\n".format(err))
        return False
    except TypeError as err:
        stderr.write("Exception: {}\n".format(err))
        return False
