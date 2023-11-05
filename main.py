# develop by: @ragu 


(
    # assign Intended free code
    variable := "Hello intended free code",
    print(variable),

    # if condition Intended free code
    print("condition is true") if () else print("condition is false"),

    # for loop Intended free code
    list(map(lambda x: print(x), range(10))),

    # multiline for loop Intended free code
    list(map(lambda x: (
        # multiline if condition Intended free code
        print("It is divisible by 2") if x % 2 == 0 else (
            print("It is divisible by 3") if x % 3 == 0 else (
                print("It is divisible by 5") if x % 5 == 0 else None
            )
        )
    ), range(10))),

    # function Intended free code
    function := lambda x: print(x * 4),
    function("Hello function"),

    # multiline function Intended free code
    multiline_function := lambda x: (
        print(x * 4),
        print(x * 5)
    ),
    multiline_function("Hello multiline function"),

    # import module Intended free code
    random := __import__("random"),
    print(random.randint(0, 10)),

    time := __import__("time"),
    print(time.strftime("%d/%m/%Y %H:%M:%S")),

    os := __import__("os"),
    print(f"Hi {os.getlogin()}"),

    # class Intended free code
    class_ := type("class", (), {"variable": "Hello class"}),
    print(class_.variable),

    # multiline class Intended free code
    multiline_class := type("multiline_class", (), {
        "variable": "Hello multiline class",
        "function": lambda x: len(x),
        "function2": lambda x: "".join(list(map(lambda x: x if x not in "aeiou" else "", x)))
    }),
    print(multiline_class.variable),
    print(multiline_class.function("Hello multiline class")),
    print(multiline_class.function2("Hello multiline class")),

    # file handling Intended free code
    file := open("file.txt", "w"),
    file.write("Hello file handling"),
    file.close(),
)
