import sys
def student_details(name, usn, program, semester):
    return f"Student Name: {name}\nUSN: {usn}\nProgram: {program}\nSemester: {semester}"

if __name__ == "__main__":
    name = sys.argv[1]
    usn = sys.argv[2]
    program = sys.argv[3]
    semester = sys.argv[4]

    print("STUDENT REGISTRATION")
    print(student_details(name, usn, program, semester))