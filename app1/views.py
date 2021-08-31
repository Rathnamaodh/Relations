from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse

import psycopg2
# Create your views here.


def all_records_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM APP1_Menu")
        row = cursor.fetchall()
        print(row)

    return HttpResponse(row)     
def create_sql(request):
    with connection.cursor() as cursor1:
        cursor1.execute("INSERT INTO APP1_Menu (name,age) VALUES ('rathnam 123',25)")
        # cursor1.execute("UPDATE APP1_Menu set age = 40 where ID = 26")


        cursor1.execute("SELECT * FROM APP1_Menu")
        row = cursor1.fetchall()
        print(row)
        cursor1.close()
        connection.close()

    return HttpResponse(row) 

def update_sql(request):
    with connection.cursor() as cursor1:
        cursor1.execute("UPDATE APP1_Menu set age = 26 where ID = 26")
        # cursor1.execute("UPDATE APP1_Menu set age = 22, name = 'rathnam koninti' where ID = 26")

        cursor1.execute("SELECT * FROM APP1_Menu")
        row = cursor1.fetchall()
        print(row)
        cursor1.close()
        connection.close()

    return HttpResponse(row) 


def delete_sql(request):
    with connection.cursor() as cursor1:
        # cursor1.execute("DELETE APP1_Menu set age = 26 where ID = 26")
        # cursor1.execute("UPDATE APP1_Menu set age = 22, name = 'rathnam koninti' where ID = 26")

        cursor1.execute("DELETE FROM APP1_Menu where ID = 25")
        cursor1.execute("SELECT * FROM APP1_Menu")
        row = cursor1.fetchall()
        print(row)
        cursor1.close()
        connection.close()

    return HttpResponse(row) 

