easyQ = [
    [
        "What will be the output of the following Python code? \nl=[1, 0, 2, 0, 'hello', '', []] \nlist(filter(bool, nl))",
        "[1, 0, 2, ‘hello’, '', []]",
        "Error",
        "[1, 2, ‘hello’]",
        "[1, 0, 2, 0, ‘hello’, '', []]"
    ],
    [
        "What will be the output of the following Python expression if the value of x is 34? \nprint(“%f”%x)",
        "34.00",
        "34.000000",
        "34.0000",
        "34.00000000"

    ],
    [
        "What will be the value of X in the following Python expression? \nX = 2+9*((3*12)-8)/10",
        "30.8",
        "27.2",
        "28.4",
        "30.0"
    ],
    [
        "Which of these in not a core data type?",
        "Tuples",
        "Dictionary",
        "Lists",
        "Class"
    ],
    [
        "Which of the following represents the bitwise XOR operator?",
        "&",
        "!",
        "^",
        "|"
    ]
]
easy_answer = [
    "[1, 2, ‘hello’]",
    "34.000000",
    "27.2",
    "Class",
    "^"
]


mediumQ = [
                [
                    "Which of the following is not an exception handling keyword in Python?",
                     "accept",
                     "finally",
                     "except",
                     "try"
                ],
                [
                    "Suppose list1 is [3, 5, 25, 1, 3], what is min(list1)?",
                    "3",
                    "5",
                    "25",
                    "1"
                ],
                [
                    "Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1]?",
                    "Error",
                    "None",
                    "25",
                    "2"
                ],
                [
                    "print(0xA + 0xB + 0xC):",
                    "0xA0xB0xC",
                    "Error",
                    "0x22",
                    "33"
                ],
                [
                    "Which of the following is invalid?",
                    "_a = 1",
                    "__a = 1",
                    "__str__ = 1",
                    "none of the mentioned"
                ],
            ]
medium_answer = [
            "accept",
            "1",
            "25",
            "33",
            "none of the mentioned"
            ]

hardQ = [
    [
        "All keywords in Python are in _________",
        "lower case",
        "UPPER CASE",
        "Capitalized",
        "None of the mentioned"
    ],
    [
        "Which of the following cannot be a variable?",
        "__init__",
        "in",
        "it",
        "on"
    ],
    [
        "Which of the following is a Python tuple?",
        "[1, 2, 3]",
        "(1, 2, 3)",
        "{1, 2, 3}",
        "{}"
    ],
    [
        "What is returned by math.ceil(3.4)?",
        "3",
        "4",
        "4.0",
        "3.0"
    ],
    [
        "What will be the output of print(math.factorial(4.5))?",
        "24",
        "120",
        "error",
        "24.0"
    ]

]
hard_answer = [
    "None of the mentioned",
    "in",
    "(1,2,3)",
    "4",
    "error"
]