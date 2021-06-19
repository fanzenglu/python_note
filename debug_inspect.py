"""
author: ZengLu
email: pyth666@163.com
project: test
ide: PyCharm
date: 2021/6/19
"""
import inspect
import os


def get_component_name():

    """Get a list of records for a frame and all higher (calling) frames.
    Each record contains a frame object, filename, line number, function
    name, a list of lines of context, and index within the context.
    :return:
    """

    component_name = "common"
    for code in inspect.stack():
        if code.index == None:
            continue
        filename = code.filename
        filepath = os.path.abspath(filename)
        print(filepath)
        paths = filepath.strip(os.path.sep).split(os.path.sep)
        if "site-packages" not in paths or "dsm" not in paths:
            continue
        try:
            _name = paths[paths.index("dsm") + 1]
        except IndexError:
            continue
        if _name == "common":
            continue
        elif _name:
            component_name = _name
            break
    return component_name

