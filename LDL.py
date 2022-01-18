def interface():
    print("Blood Test Analysis for LDL")
    keep_running = True
    while keep_running:
        print("Options")
        #print("1-LDL")
        print("9-Quit")
        choice = input("Enter your choice: ")
        if choice == "9":
            keep_running = False
        #elif choice == "1":
            #HDL_driver()
    return  



def accept_input(test_name):
    entry = input("Enter the {}test result: ".format(test_name))
    return int(entry)

def check_LDL(LDL_value):
    if LDL_value < 130:
        answer = "Normal"
    elif 159 >= LDL_value >= 130:
        answer = "Borderline High"
    elif 189 >= LDL_value >= 160:
        answer = "Borderline Low"
    else:
        answer = "Very High"
    return answer
    
def print_result(test_name, test_value, test_class):
    out_string = "The test value of {} for {} is {}".format(test_value, test_name, test_class)
    print(out_string)
    return

def LDL_driver():
    LDL_value = accept_input("LDL")
    classificaton_LDL = check_LDL(LDL_value)
    print_result("LDL", LDL_value, classificaton_LDL)
    return

interface()