string_1 = {
    "valid": {
        "abc",
        123
    },
    "invalid": {
        None,
        "!@#$%^&*()_+"
    }
}

string_2 = {
    "valid": {
        None,
        "pc",
        "mo"
    },
    "invalid": {
        1,
        "abc",
        "!@#$%^&*()_+"
    }
}

string_3 = {
    "valid": {
        None,
        "m",
        "f"
    },
    "invalid": {
        1,
        "abc",
        "!@#$%^&*()_+"
    }
}

string_4 = {
    "valid": {
        "???"
    },
    "invalid": {
        None,
        "abc",
        1

    }
}

string_5 = {
    "valid": {
        "%EA%B0%80",
        "1",
        "abc"
    },
    "invalid": {
        None,
        "!",
        "%EQ%B0%80"
    }
}

string_6 = {
    "valid": {
        None,
        "sim",
        "date"
    },
    "invalid": {
        1,
        "abc",
        "!@#$%^&*()_+"
    }
}

string_7 = {
    "valid": {
        "http://naver.com",
        "https://naver.com",
        "naver.com"
        "192.168.0.1",
        "192.168.0.1:9999"
    },
    "invalid": {
        None,
        1,
        "abc"
    }
}

string_8 = {
    "valid": {
        "abc",
        123
    },
    "invalid": {
        None,
        "!@#$%^&*()_+"
    }
}

string_9 = {
    "valid": {
        "valid_1": "date",
        "valid_2": "week",
        "valid_3": "month"
    },
    "invalid": {
        "integer": 123,
        "string": "abc",
        "Null": None
    }
}
