import csv
from collections import defaultdict
import re
from collections import Counter
from heapq import nlargest





student_fields = ['Name', 'Maths', 'Biology', 'English', 'Physics','Chemistry','Hindi']
student_database = 'Student_marks_list.csv'


minTemp, maxTemp = [],[]

 
def display_menu():
    print("***************************************")
    print(" Student Mark CSV Datasets")
    print("***************************************")
    print("1. Find the topper in each subject")
    print("2. Top 3 Student in Class ")
    print("3. Topper in Maths")
    print("4. Topper in Biology")
    print("5. Quit")
 
 
def max_mark():
    print("******************************")
    print("Find max marck in each subject")
    print("******************************")
    global student_fields
    global student_database
    

    
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f,delimiter=',')
        
        Name,Maths, Biology,English,Physics,Chemistry,Hindi = [],[],[],[],[],[],[]
        
        for row  in reader:
            
            try:
                Maths.append(int(row[1]))
                Biology.append(int(row[2]))
                English.append(int(row[3]))
                Physics.append(int(row[4]))
                Chemistry.append(int(row[5]))
                Hindi.append(int(row[6]))
                Name.append(row[0])
                
                
        
            except ValueError:
                print ("Rows",row)
                
                

        #ted = Name.stdmaths
        print ("Maths Higher Mark : ", max(Maths))
        print ("Biology Higher Mark : ", max(Biology))
        print ("English Higher Mark : ", max(English))
        print ("Physics Higher Mark : ", max(Physics))
        print ("Chemistry Higher Mark : ", max(Chemistry))
        print ("Hindi Higher Marl : ", max(Hindi))

        
    print("---Student Name Topper each Subject---")
    stdname = input("Enter the Maths Higher Mark: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if stdname == row[1]:
                    print("----- Student Found -----")
                    print("Maths Topper Student Name: ", row[0])
                    print("Maths Mark: ", row[1])
                    
                    break
        else:
            print("Student Name not found in our database")
            
    stdname2 = input("Enter the Biology Higher Mark: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if stdname2 == row[2]:
                    print("----- Student Found -----")
                    print("Biology Topper Student Name: ", row[0])
                    print("Biology Mark: ", row[2])
                    
                    break
        else:
            print("Student Name not found in our database")

    stdname3 = input("Enter the English Higher Mark: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if stdname3 == row[3]:
                    print("----- Student Found -----")
                    print("English Topper Student Name: ", row[0])
                    print("English Mark: ", row[3])
                    
                    break
        else:
            print("Student Name not found in our database")

    stdname4 = input("Enter the Physics Higher Mark: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if stdname4 == row[4]:
                    print("----- Student Found -----")
                    print("Physics Topper Student Name: ", row[0])
                    print("Physics Mark: ", row[4])
                    
                    break
        else:
            print("Student Name not found in our database")

    stdname5 = input("Enter the Chemistry Higher Mark: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if stdname5 == row[5]:
                    print("----- Student Found -----")
                    print("Chemistry Topper Student Name: ", row[0])
                    print("Chemistry Mark: ", row[5])
                    
                    break
        else:
            print("Student Name not found in our database")


        
    stdname6 = input("Enter the Hindi Higher Mark: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if stdname6 == row[6]:
                    print("----- Student Found -----")
                    print("Hindi Topper Student Name: ", row[0])
                    print("Hindi Mark: ", row[6])
                    break
        else:
            print("Student Name not found in our database")
            
 
    
    input("Press any key to continue")
    return
 
 
def top_3():
    global student_fields
    global student_database
 
    print("--- Top 3 Student Records ---")
 
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f,delimiter=',')
        
        Name,Maths, Biology,English,Physics,Chemistry,Hindi,Total = [],[],[],[],[],[],[],[]
        
        for row  in reader:
            
            try:
                Maths.append(int(row[1]))
                Biology.append(int(row[2]))
                English.append(int(row[3]))
                Physics.append(int(row[4]))
                Chemistry.append(int(row[5]))
                Hindi.append(int(row[6]))
                Name.append(row[0])
                Total.append(int(row[7]))
                
                
        
            except ValueError:
                print ("Rows",row)
                
                

        #ted = Name.stdmaths
        print("All Student Total Value:")
        print(Total, "\n")
        ThreeHighest = nlargest(3, Total)
        print("Top 3 highest Mark:")
        print("Marks: Values")
        for val in ThreeHighest:
            print(val)

        
    print("---Topper 1---")
    stdname = input("Enter the First Higher Mark: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if stdname == row[7]:
                    print("----- Student Found -----")
                    print("Topper 1: ", row[0])
                    
                    break
        else:
            print("Student Name not found in our database")

    
    print("---Topper 2---")
    stdname1 = input("Enter the Secound Higher Mark: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if stdname1 == row[7]:
                    print("----- Student Found -----")
                    print("Topper 2: ", row[0])
                    
                    break
        else:
            print("Student Name not found in our database")

    print("---Topper 3---")
    stdname2 = input("Enter the Third Higher Mark: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if stdname2 == row[7]:
                    print("----- Student Found -----")
                    print("Topper 3: ", row[0])
                    
                    break
        else:
            print("Student Name not found in our database")
        
        
        
        
    input("Press any key to continue")
 
 
def maths_topper():
    global student_fields
    global student_database


    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f,delimiter=',')
        
        Name,Maths = [],[]
        
        for row  in reader:
            
            try:
                Maths.append(int(row[1]))
                Name.append(row[0])
                
                
        
            except ValueError:
                print ("Rows",row)
                
                

        
        print ("Topper in Maths Mark : ", max(Maths))
        
 
    print("---Maths Topper---")
    stdname = input("Enter the Maths Higher Mark: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if stdname == row[1]:
                    print("----- Student Found -----")
                    print("Maths Topper Student Name: ", row[0])
                    print("Topper Mark: ", row[1])
                    
                    break
        else:
            print("Student Name not found in our database")
    input("Press any key to continue")
 
 
def biology_topper():
    global student_fields
    global student_database
 
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f,delimiter=',')
        
        Name,Biology = [],[]
        
        for row  in reader:
            
            try:
                Biology.append(int(row[3]))
                Name.append(row[0])
                
                
        
            except ValueError:
                print ("Rows",row)
                
                

        
        print ("Topper in Biology Mark : ", max(Biology))
        
 
    print("---Biology Topper---")
    stdname = input("Enter the Biology Higher Mark: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if stdname == row[1]:
                    print("----- Student Found -----")
                    print("Biology Topper Student Name: ", row[0])
                    print("Topper Mark: ", row[3])
                    
                    break
        else:
            print("Student. not found in our database")
 
    input("Press any key to continue")
 
 

 
while True:
    display_menu()
 
    choice = input("Enter your choice: ")
    if choice == '1':
        max_mark()
    elif choice == '2':
        top_3()
    elif choice == '3':
        maths_topper()
    elif choice == '4':
        biology_topper()
    
    else:
        break
 
print("***************************************")
print(" Thank you for using our Python Program")
print("***************************************")
    
