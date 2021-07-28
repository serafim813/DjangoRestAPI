from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

import psycopg2
import ast
import re

dsn = {
    'dbname': 'movies_database',
    'user': 'postgres',
    'password': 1234,
    'host': '127.0.0.1',
    'port': 5432
}

@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def tutorial_detail(request, pk):
    result = re.match(r'^/api/v1/user/(?P<pk>[0-9]+)$', str(request).split("'")[1])
    if (request.method == 'GET') and (len(str(result)) != 4):
        with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
            k = (str(request).split("'")[1]).split('/')[-1]
            k = 'select * from test.user_get(' + k +')'
            cursor.execute(k)
            result = str(cursor.fetchone())
            result = result[1:-2]
            result = ast.literal_eval(result)
        return JsonResponse(result)
    result = re.match(r'^/api/v1/comment/(?P<pk>[0-9]+)$', str(request).split("'")[1])
    if (request.method == 'GET') and (len(str(result)) != 4):
        with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
            k = (str(request).split("'")[1]).split('/')[-1]
            k = 'select * from test.comment_get(' + k +')'
            cursor.execute(k)
            result = str(cursor.fetchone())
            result = result[1:-2]
            result = ast.literal_eval(result)
        return JsonResponse(result)

    result3 = re.match(r'^/api/v1/user/(?P<pk>[0-9]+)/comment/$', str(request).split("'")[1])
    if (request.method == 'GET') and (len(str(result3)) != 4):
        with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
            k = (str(request).split("'")[1]).split('/')[-3]
            result3 = re.match(r'^(?P<pk>[0-9]+)$', (str(request).split("'")[1]).split('/')[-1])
            #if len(str(result)) != 4:
            x = '0'
            k = 'select * from test.user_comment_get(' + k + ', ' + x +')'
            cursor.execute(k)
            result = str(cursor.fetchone())
            result = result[2:-3]
            print(result)
            result = ast.literal_eval(result)
            k = {"id":456, "id_user":34452, "txt":"My comment"},{"id":460, "id_user":34452, "txt":"Foo!"}
            #querset = Tutorial.objects.filter(result)
        return JsonResponse(result, safe=False)
    result = re.match(r'^/api/v1/user/(?P<x>[0-9]+)/comment/(?P<pk>[0-9]+)$', str(request).split("'")[1])
    if (request.method == 'GET') and (len(str(result)) != 4):
        with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
            k = (str(request).split("'")[1]).split('/')[-3]
            x = (str(request).split("'")[1]).split('/')[-1]
            k = 'select * from test.user_comment_get(' + k + ', ' + x +')'
            cursor.execute(k)
            result = str(cursor.fetchone())
            result = result[1:-2]
            result = ast.literal_eval(result)
        return JsonResponse(result)


    result = re.match(r'^/api/v1/user/(?P<x>[0-9]+)/comment/$', str(request).split("'")[1])
    if (request.method == 'POST') and (len(str(result)) != 4):
        with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
            k = (str(request).split("'")[1]).split('/')[-3]
            tutorial_data = JSONParser().parse(request)
            tutorial_data = str(tutorial_data).replace("'",'"')
            k = 'select * from test.user_comment_ins(' + k + ", '" + str(tutorial_data) + "')"
            cursor.execute(k)
            result = str(cursor.fetchone())
            result = result[1:-2]
            result = ast.literal_eval(result)
        return JsonResponse(result)
    result = re.match(r'^/api/v1/comment/(?P<pk>[0-9]+)$', str(request).split("'")[1])
    if (request.method == 'PUT') and (len(str(result)) != 4):
        with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
            tutorial_data = JSONParser().parse(request)
            tutorial_data = str(tutorial_data).replace("'", '"')
            k = (str(request).split("'")[1]).split('/')[-1]
            t = 'select * from test.comment_get(' + k + ')'
            cursor.execute(t)
            result = str(cursor.fetchone())
            result = result[1:-2]
            result = result.split(' ')[3][:-1]
            k = 'select * from test.comment_upd('+ result + ", " + k + ", '" + str(tutorial_data) + "')"
            cursor.execute(k)
            result = str(cursor.fetchone())
            result = result[1:-2]
            result = ast.literal_eval(result)
        return JsonResponse(result)
    result = re.match(r'^/api/v1/comment/(?P<pk>[0-9]+)$', str(request).split("'")[1])
    if (request.method == 'DELETE') and (len(str(result)) != 4):
        with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
            k = (str(request).split("'")[1]).split('/')[-1]
            t = 'select * from test.comment_get(' + k + ')'
            cursor.execute(t)
            result = str(cursor.fetchone())
            result = result[1:-2]
            result = result.split(' ')[3][:-1]
            k = 'select * from test.user_comment_del('+ result + ", " + k + ")"
            cursor.execute(k)
            result = str(cursor.fetchone())
            result = result[1:-2]
            result = ast.literal_eval(result)
        return JsonResponse(result)


