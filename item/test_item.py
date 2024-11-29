input_value_valid = {
    'select_int': {
        0: 2
    },
    'delete_int': {
        1: 3
    },
    'int': {
        0: -2147483648,
        1: 2147483647
    },
    'str5': {
        0: 'a',
        1: 'ABCDE',
        2: ''
    },
    'str10': {
        0: 'a',
        1: 'ABCDEFGHIJ',
        2: ''
    },
    'boolean': {
        0: 1,
        1: 0
    }
}
input_value_invalid = {
    'int': {
        0: -2147483649,
        1: 2147483648,
        2: ''
    },
    'str5': {
        0: 'aaaaaa'
    },
    'str10': {
        0: 'aaaaaaaaaaa'
    },
    'boolean': {
        0: 2,
        1: 'aaaaaaa',
        2: ''
    }
}
