import string
from os import system


def login():
    system("cls")
    name = input("Enter Student name : ").upper()
    # usn = input("USN : ").upper()
    print(f"Which cycle {name} belong's to")
    num = int(input("1.physics.\n2.chemistry.\nchoise : "))
    cycle(num)


def cycle(num):
    if num == 1:
        cyl_name = "Physics cycle"
        subject = ["M1", "Physics", "Electrical", "English"]
        len_sub = len(subject)
        T_sub_marks = push_sub(subject, len_sub, cyl_name)
        print(T_sub_marks)
        # ptr(T_sub_marks, subject, cyl_name)

    else:
        cyl_name = "Chemistry cycle"
        subject = ["M1", "Chemistry", "Electronics", "Computer science", "English"]
        len_sub = len(subject)
        T_sub_marks = push_sub(subject, len_sub, cyl_name)
        ptr(T_sub_marks, subject, cyl_name)


def push_sub(subject, len_sub, cyl_name):
    Ia_marks = []
    T_sub = []
    for item in subject:
        Ia_marks = marks(item, len_sub, cyl_name)
        ass_ = ass(item)
        T_sub.append(cal(Ia_marks, ass_, subject))
    return T_sub


def marks(subject_list, len_sub, cyl_name):
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


def ass(subject):
    print(f"Enter {subject} Assigment marks : ", end="")
    Ass_marks = int(input())
    while Ass_marks > 10:
        system("cls")
        print("Enter marks below 10 ")
        print(f"marks : ", end="")
        Ass_marks = int(input())
    return Ass_marks


def cal(Ia_marks, assi, subject):
    sub_marks = []
    avg_marks = []
    ass_marks = []
    sub = []
    sub_marks.append(Ia_marks[0])
    avg_marks.append(round(Ia_marks[1], 2))
    ass_marks.append(assi)
    sub.append(subject)

    return sub_marks, avg_marks, ass_marks, sub


def ptr(T_sub_marks, subject, cyl_name):
    print("SUBJECT       T_MARKS       T_AVG       ASSIMENT")
    for item in subject:
        t_sub = list(T_sub_marks)
        i = 0
        for i in t_sub:
            j = list(i)
            print(f"{item}   :   {j[0]}   :   {j[1]}   :   {j[2]}")


# main
login()


"""print("Login in into your account.")
log = input("login ID : ")
pwd = input("password : ")

if log == "log!@#" and pwd == "qwerty":
    print("welcome")
else:
    print("invalid")
"""
