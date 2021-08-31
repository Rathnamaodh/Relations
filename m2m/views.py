from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
import psycopg2


def doctor(request):
    with connection.cursor() as cursor1:
        cursor1.execute("INSERT INTO m2m_Doctor (doctors) VALUES ('Anu')")
        # cursor1.execute("INSERT INTO mtm_Patient (doctor,patient) VALUES ('ramya paul', 'p1')")
        


        cursor1.execute("SELECT * FROM m2m_Doctor")
        row = cursor1.fetchall()
        print(row)
        cursor1.close()
        connection.close()

    return HttpResponse(row) 
def patient(request):
    with connection.cursor() as cursor1:
        cursor1.execute("INSERT INTO m2m_Patient (name) VALUES ('patient5')")
      
        


        cursor1.execute("SELECT * FROM m2m_Patient")
        row = cursor1.fetchall()
        print(row)
        cursor1.close()
        connection.close()

    return HttpResponse(row) 
def patient_doctor(request):
    with connection.cursor() as cursor1:
        # cursor1.execute("INSERT INTO m2m_patient_doctors (patient_id,doctor_id) VALUES (3,1)")
      
        


        cursor1.execute("SELECT * FROM m2m_Patient_doctors where patient_id = 2")
        row = cursor1.fetchall()
        print(row)
        cursor1.close()
        connection.close()

    return HttpResponse(row) 