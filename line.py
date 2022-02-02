
def user_input():
    # taking two inputs at a time
    x1 = input("Enter the first point x value: ")
    y1 = input("Enter the first point y value: ")
    x2 = input("Enter the second point x value: ")
    y2 = input("Enter the second point y value: ")
    x = input("Enter the x intercept: ")
    out_string = "You have input points ({},{}) and ({},{}), and a x "
    "intercept of {}".format(x1, y1, x2, y2, x)
    print(out_string)
    return int(x1), int(y1), int(x2), int(y2), int(x)


def calculate_slope(x1, y1, x2, y2, x):
    m = (y2 - y1) / (x2 - x1)
    return m


def x_intercept(y1, m, x1):
    b = y1 - (m*x1)
    return b


def y_intercept(m, x, b):
    y = (m*x + b)
    return(y)


def print_results(y):
    out_string = "The line will be intercepted at y = {}".format(y)
    print(out_string)


def line_point(x1, y1, x2, y2, x):
    # x1, y1, x2, y2, x = user_input()
    m = calculate_slope(x1, y1, x2, y2, x)
    b = x_intercept(y1, m, x1)
    y = y_intercept(m, x, b)
    print_results(y)
