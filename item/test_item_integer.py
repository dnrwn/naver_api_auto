integer_1 = {
    "valid": {
        "Null": None,
        "1": 1,
        "1000": 1000
    },
    "invalid": {
        "0": 0,
        "string": "abc",
        "1001": 1001
    }
}

integer_2 = {
    "valid": {
        "Null": None,
        "1": 1,
        "1000": 100
    },
    "invalid": {
        "0": 0,
        "string": "abc",
        "1001": 101
    }
}

integer_3 = {
    "valid": {
        "Null": None,
        "1": 0
    },
    "invalid": {
        "0": 1,
        "string": "abc"
    }
}

integer_4 = {
    "valid": {
        "Null": None,
        "1": 1
    },
    "invalid": {
        "0": 0,
        "string": "abc"
    }
}
