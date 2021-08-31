from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
import psycopg2


def doctor(request):
    with connection.cursor() as cursor1:
        cursor1.execute("INSERT INTO doctor (doctors) VALUES ('Naveen patnayak')")
        # cursor1.execute("INSERT INTO mtm_Patient (doctor,patient) VALUES ('ramya paul', 'p1')")
        


        # cursor1.execute("SELECT * FROM mtm_Patient")
        row = cursor1.fetchall()
        print(row)
        cursor1.close()
        connection.close()

    return HttpResponse(row) 