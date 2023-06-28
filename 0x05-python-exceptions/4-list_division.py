#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    errmsg = ""
    result = []
    a = 0
    b = 0
    c = 0
    for i in range(0, list_length):
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            if a == 0:
                errmsg = "division by 0"
            else:
                errmsg = ""
            result.append(0)
            a += 1
        except TypeError:
            if b == 0:
                errmsg = "wrong type"
                b += 1
            else:
                errmsg = ""
            result.append(0)
        except IndexError:
            if c == 0:
                errmsg = "out of range"
            else:
                errmsg = ""
            result.append(0)
            c += 1
        finally:
            if errmsg != "":
                print(errmsg)
    return result
