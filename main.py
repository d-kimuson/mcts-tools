from icecream import ic


def greet(name: str) -> None:
    ic(name)
    print("Hello, {}!".format(name))


if __name__ == '__main__':
    greet("World")
