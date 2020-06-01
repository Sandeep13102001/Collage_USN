import string
from os import system
import time


def login():
    system("cls")
    name = input("Enter Student name : ").upper()
    usn = input("USN : ").upper()
    sems(name, usn)
    return 0


def sems(name, usn):
    system("cls")
    print(f"Which SEMESTER {name} belong's to ")
    num = int(
        input(
            "1 : Semester.\n2 : Semester.\n3 : Semester.\n4 : Semester.\n5 : Semester.\n6 : Semester.\n7 : Semester.\n8 : Semester.\nchoise : "
        )
    )
    if num == 1:
        print("FIRST SEMESTER\n")
        sem(name, usn)
    elif num == 2:
        print("SECOND SEMESTER\n")
        sem(name, usn)
    elif num == 3:
        cyl_name = "Third SEM"
        subject = [
            "M3",
            "Data Structures and Applications",
            "Analog and Digital Electronics",
            "Computer Organization",
            "Software Engineering",
            "Discrete Mathematical Structures",
        ]
        sub_code = ["18MAT31", "18CS32", "18CS33", "18CS34", "18CS35", "18CS36"]
        sub_item = Sub_push(subject, cyl_name, sub_code)
        ptr(sub_item, name, usn)
        return 0
    elif num == 4:
        cyl_name = "Forth SEM"
        return 0
    else:
        pass


def sem(name, usn):
    system("cls")
    print(f"Which SEMESTER {name} belong's to ")
    num = int(input("1.Physics cycle.\n2.Chemistry cycle.\nchoise : "))
    if num == 1:
        cyl_name = "Physics cycle"
        subject = ["M1", "Physics", "Civil", "Electrical", "English"]
        sub_code = ["18MAT11", "18PHY12", "18CIV14", "18ELE13", "18EGH18"]
        sub_item = Sub_push(subject, cyl_name, sub_code)
        ptr(sub_item, name, usn)
        return 0

    else:
        cyl_name = "Chemistry cycle"
        subject = [
            "M1",
            "Chemistry",
            "Electronics",
            "Computer science",
            "Mechanical",
            "English",
        ]
        sub_code = ["18MAT21", "18CHE22", "18ELN24", "18CPS23", "18ME25", "18EGH28"]
        sub_item = Sub_push(subject, cyl_name, sub_code)
        ptr(sub_item, name, usn)
        return 0


def Sub_push(subject, cyl_name, sub_code):
    T_sub_marks = push_sub(subject, cyl_name, sub_code)
    return T_sub_marks


def push_sub(subject, cyl_name, sub_code):
    Ia_marks = []
    T_sub = []
    merge_list = tuple(zip(subject, sub_code))
    for i in merge_list:
        j = list(i)
        Ia_marks = marks(j[1], cyl_name, j[0])
        ass_ = ass(j[1])
        T_sub.append(cal(Ia_marks, ass_, j[0], j[1]))

    return T_sub


def marks(subject_list, cyl_name, sub_code):
    system("cls")
    print(cyl_name)
    print(f"Enter 3 internal {subject_list} marks")
    tmarks = 0
    for i in range(1, 4):
        print(f"marks {i} : ", end="")
        marks = int(input())
        while marks > 30:
            system("cls")
            print("Enter marks below 30 ")
            print(f"marks {i} : ", end="")
            marks = int(input())
        tmarks = tmarks + marks
        avg = tmarks / 3

    return tmarks, avg


def ass(sub_code):
    print(f"Enter {sub_code} Assigment marks : ", end="")
    Ass_marks = int(input())
    while Ass_marks > 10:
        system("cls")
        print("Enter marks below 10 ")
        print(f"marks : ", end="")
        Ass_marks = int(input())
    return Ass_marks


def cal(Ia_marks, assi, subject, sub_codes):
    sub_marks = []
    avg_marks = []
    ass_marks = []
    sub = []
    sub_code = []
    sub_marks.append(Ia_marks[0])
    avg_marks.append(round(Ia_marks[1], 2))
    ass_marks.append(assi)
    sub.append(subject)
    sub_code.append(sub_codes)

    return sub_marks, avg_marks, ass_marks, sub, sub_code


def ptr(T_sub_marks, name, usn):
    system("cls")
    print("\n\t\t\tName of the student : ", name)
    print("\t\t\tUSN : ", usn)
    print("\t\t\tMarks of the Student\n")
    for item in T_sub_marks:
        j = list(item)
        print(
            "Subject code  : ",
            *j[4],
            "\nSubject       : ",
            *j[3],
            "\nTotal marks   : ",
            *j[0],
            "\nAverage marks : ",
            *j[1],
        )
        print("\n")


# main
login()


"""
    print("Login in into your account.")
    log = input("login ID : ")
    pwd = input("password : ")

    if log == "log!@#" and pwd == "qwerty":
        print("welcome")
    else:
    print("invalid")
"""
