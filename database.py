from blood_calculator import check_HDL, check_LDL
print("This is the database module and python calls it {}".format(__name__))


HDL_value = 55

classification = check_HDL(HDL_value)
print("55 is {}".format(classification))

x = check_LDL(200)
