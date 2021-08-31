from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse

import psycopg2

# Create your views here.
def index(request):
    return HttpResponse('Hello, Rathnam!')

def student_create(request):
    with connection.cursor() as cursor1:
        cursor1.execute("INSERT INTO relations_Student (name,roll) VALUES ('rathnam',25)")
        # cursor1.execute("UPDATE APP1_Menu set age = 40 where ID = 26")


        cursor1.execute("SELECT * FROM relations_Student")
        row = cursor1.fetchall()
        print(row)
        cursor1.close()
        connection.close()

    return HttpResponse(row)

def student_profile_create(request):
    with connection.cursor() as cursor1:
        cursor1.execute("INSERT INTO relations_Student_Profile (student_id,roll) VALUES (4,25)")
        # cursor1.execute("UPDATE APP1_Menu set age = 40 where ID = 26")


        cursor1.execute("SELECT * FROM relations_Student_Profile")
        row = cursor1.fetchall()
        print(row)
        cursor1.close()
        connection.close()

    return HttpResponse(row) 


def student_update(request):
    with connection.cursor() as cursor1:
        cursor1.execute("UPDATE relations_Student set name = 'rathnam paul',roll=26 where ID = 1")
        # cursor1.execute("UPDATE APP1_Menu set age = 22, name = 'rathnam koninti' where ID = 26")

        cursor1.execute("SELECT * FROM relations_Student")
        row = cursor1.fetchall()
        print(row)
        cursor1.close()
        connection.close()

    return HttpResponse(row) 
def student_delete(request):
    with connection.cursor() as cursor1:
        # cursor1.execute("DELETE APP1_Menu set age = 26 where ID = 26")
        # cursor1.execute("UPDATE APP1_Menu set age = 22, name = 'rathnam koninti' where ID = 26")

        cursor1.execute("DELETE FROM relations_Student where ID = 3")
        cursor1.execute("SELECT * FROM relations_Student")
        row = cursor1.fetchall()
        print(row)
        cursor1.close()
        connection.close()

    return HttpResponse(row) 

