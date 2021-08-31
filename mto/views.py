from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
import psycopg2


def student_create(request):
    with connection.cursor() as cursor1:
        cursor1.execute("INSERT INTO mto_student (first_name,last_name) VALUES ('ramya','paul')")
        # cursor1.execute("UPDATE APP1_Menu set age = 40 where ID = 26")


        cursor1.execute("SELECT * FROM mto_student")
        row = cursor1.fetchall()
        print(row)
        cursor1.close()
        connection.close()

    return HttpResponse(row) 

def Project_create(request):
    with connection.cursor() as cursor1:
        cursor1.execute("INSERT INTO mto_project (name,student_id) VALUES ('Python Project ',7)")
        


        cursor1.execute("SELECT * FROM mto_project")
        row = cursor1.fetchall()
        print(row)
        cursor1.close()
        connection.close()

    return HttpResponse(row) 