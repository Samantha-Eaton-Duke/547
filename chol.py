def interface():
    print("Cholesterol Test Analysis")
    keep_running = True
    while keep_running:
        print("Options")
        print("1-Cholesterol")
        print("9-Quit")
        choice = input("Enter your choice: ")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            cholesterol_driver()
    return


def accept_input(test_name):
    entry = input("Enter the {}test result: ".format(test_name))
    return int(entry)


def check_cholesterol(cholesterol_value):
    if cholesterol_value < 200:
        answer = "Normal"
    elif 239 >= cholesterol_value >= 200:
        answer = "Borderline High"
    else:
        answer = "High"
    return answer


def print_result(test_name, test_value, test_class):
    out_string = "The test value of {} for {} is {}".format(
        test_value, test_name, test_class)
    print(out_string)
    return


def cholesterol_driver():
    cholesterol_value = accept_input("Cholesterol")
    classificaton = check_cholesterol(cholesterol_value)
    print_result("Cholesterol", cholesterol_value, classificaton)
    return


interface()
