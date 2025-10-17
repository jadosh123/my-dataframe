from collections.abc import Mapping


def type_checker(data: list):
    """
    A type checking function for the series, it returns the datatype.
    """
    # Most general type as placeholder until we determine the type
    data_types = set()

    for element in data:
        data_types.add(type(element))

    for dtype in data_types:
        if dict in data_types:
            return dict
        elif str in data_types:
            return str
        elif float in data_types:
            return float
        else:
            return int


if __name__ == "__main__":
    tmp = [1, 'hello', 3, 4.5, dict(tmp=1)]
    dtype = type_checker(tmp)
    print(dtype)