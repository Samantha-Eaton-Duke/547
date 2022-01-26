def add_patient(patient_name, patient_id, age):
    new_patient = [patient_name, patient_id, age, []]
    # [] allows you to make an undefined list where you can add future test results
    return new_patient


def main():
    #create an empty list
    db = [] 
    x = add_patient("Ann Ables", 342, 40)
    db.append(x)
    y = add_patient("Bob Boyles", 50, 50)
    db.append(y)
    z = add_patient("Chris Columbus", 111, 35)
    db.append(z)
    db.append(add_patient("David Dinkins", 22, 72))
    #Will add information straight to the database list
    
    found_patient = find_patient(db, 111)
    print(found_patient)
    print(db)
    add_test_to_patient(db, 111, "HDL", 100)
    print(db)
    return db 
    
    
    #print(x)
    #print(y)
    #print(z)
    #print(db)
    
    #print(db[1:3])
    # prints the 2nd and 3rd list index items
    
    #print(db[-1])
    #prints the last entry in the list
    
    
    #for patient in db:
     #   print(patient[0])
        #prints only their name, the frist item in the list
        
def find_patient(db, id_no):
    for patient in db:
        if patient[1] == id_no:
            return patient
    return
    
    
# add test case to patient
def add_test_to_patient(db, id_no, test_name, test_results):
    patient = find_patient(db, id_no)
    test_tuple = (test_name, test_results)
    # add test_tuple to db
    patient[3].append(test_tuple)
    # changes the [] value in db

def print_directory(db):
# print a db of every patients room
    rooms = ["Room 13", "Room 12", "Room 99", "Room 3"]
    for room, patient in zip(rooms, db):
        print("{} - {}".format(patient[0], room))

if __name__ == "__main__":
    db = main()
    print_directory(db)