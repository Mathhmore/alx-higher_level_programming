#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    errmsg = ""
    result = []
    a = 0
    b = 0
    c = 0
    for i in range(0, list_length):
        r = 0
        try:
            r = (my_list_1[i] / my_list_2[i])
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result.append(r)
    return result
