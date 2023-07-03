#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        try:
            res.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            res.append(0)
            print("division by 0")
        except TypeError:
            res.append(0)
            print("wrong type")
        except IndexError:
            res.append(0)
            print("out of range")
        finally:
            continue
    return res