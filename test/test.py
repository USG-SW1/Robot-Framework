from robot.api.deco import keyword
@keyword("Hello World")
def hello_world():
    print("Hello, Robot Framework!")
    return "Hello, Robot Framework!"