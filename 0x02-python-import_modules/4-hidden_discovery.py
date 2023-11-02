#!/usr/bin/python3

"""program that prints all the names defined by
the compiled module hidden_4.pyc """
if __name__ == "__main__":
    import hidden_4

    nms = dir(hidden_4)
    """iterate through the directory"""
    for nm in nms:
        if nm[:2] != "__":
            print(nm)
