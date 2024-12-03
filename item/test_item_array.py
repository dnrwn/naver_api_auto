### array 예시의 경우 value 부분에 대괄호로 덮어져 있음
# array json : ["a":"a"], ["a","b"]
# array string : ["a"]
array_string_1 = {
    "valid": {
        "1": {"a"},
        "2": {"a", "b"},
        "3": {"a", "b", "c"},
        "4": {"a", "b", "c", "d"},
        "5": {"a", "b", "c", "d", "e"},
        "6": {"a", "b", "c", "d", "e", "f"},
        "7": {"a", "b", "c", "d", "e", "f", "g"},
        "8": {"a", "b", "c", "d", "e", "f", "g", "h"},
        "9": {"a", "b", "c", "d", "e", "f", "g", "h", "i"},
        "10": {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"},
        "11": {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"},
        "12": {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"},
        "13": {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"},
        "14": {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"},
        "15": {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"},
        "16": {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"},
        "17": {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q"},
        "18": {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r"},
        "19": {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"},
        "20": {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"}
    },
    "invalid": {
        "Null": None,
        "JSON": {"A": "A", "B": "B"},
        "integer": 1,
        "21": {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u"},
        "0": {}
    }
}

array_json_1 = {
    "valid": {
        "1": {"a": "a"},
        "2": {"a": "a", "b": "b"},
        "3": {"a": "a", "b": "b", "c": "c"},
        "4": {"a": "a", "b": "b", "c": "c", "d": "d"},
        "5": {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e"}
    },
    "invalid": {
        "Null": None,
        "integer": 1,
        "string": "ABC",
        "6": {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f"},
        "0": {}
    }
}

array_json_2 = {
    "valid": {
        "1": {"a": "a"},
        "2": {"a": "a", "b": "b"},
        "3": {"a": "a", "b": "b", "c": "c"},
    },
    "invalid": {
        "Null": None,
        "integer": 1,
        "string": "ABC",
        "4": {"a": "a", "b": "b", "c": "c", "d": "d"},
        "0": {}
    }
}

array_json_3 = {
    "valid": {
        "Null": None,
        "1": {"10"},
        "2": {"10", "20"},
        "3": {"10", "20", "30"},
        "4": {"10", "20", "30", "40"},
        "5": {"10", "20", "30", "40", "50"},
        "6": {"10", "20", "30", "40", "50", "60"},
    },
    "invalid": {
        "string": "ABC",
        "integer": 123,
        "7": {"10", "20", "30", "40", "50", "60", "70"},
        "0": {},
        "9": {"9"},
        "61": {"61"}
    }
}

array_string_2 = {
    "valid": {
        "Null": None,
        "1": {"1"},
        "2": {"1", "2"},
        "3": {"1", "2", "3"},
        "4": {"1", "2", "3", "4"},
        "5": {"1", "2", "3", "4", "5"},
        "6": {"1", "2", "3", "4", "5", "6"},
        "7": {"1", "2", "3", "4", "5", "6", "7"},
        "8": {"1", "2", "3", "4", "5", "6", "7", "8"},
        "9": {"1", "2", "3", "4", "5", "6", "7", "8", "9"},
        "10": {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"},
        "11": {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"},
    },
    "invalid": {
        "JSON": {"A": "A", "B": "B"},
        "integer": 1,
        "12": {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"},
        "0": {}
    }
}

array_string_3 = {

}

array_string_4 = {

}