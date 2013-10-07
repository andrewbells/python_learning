'''The program extracts values of student number and grade from
a .txt file (grades_program.txt) and creates a dictionary using these values'''

import tkinter.filedialog

def main():
    
    grade_file = open(tkinter.filedialog.askopenfilename())
    print (read_grades(grade_file))
    grade_file.close()
    
    

def read_grades(gradefile):

    
    ## skip over the header.
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()
    

    ## Read the grades, accumulating them into a dict.
    grade_to_ids = {}
    line = gradefile.readline()

    while line != '':
        student_id = line[:4]
        grade = float(line[4:].strip())

        if grade not in grade_to_ids:
            grade_to_ids[grade] = [student_id]
        else:
            grade_to_ids[grade].append(student_id)
            
        line = gradefile.readline()

    return grade_to_ids



if __name__ == '__main__':
    main()
