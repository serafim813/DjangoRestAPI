from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from DjangoRestApisPostgreSQL import config
import psycopg2
import ast
import re

dsn = {
    'dbname': 'test',
    'user': config.user,
    'password': config.password,
    'host': config.host,
    'port': config.port
}
schema = config.schema

@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def tutorial_detail(request, pk):
    result = re.match(r'^/api/v1/user/(?P<pk>[0-9]+)$', str(request).split("'")[1])
    if (request.method == 'GET') and (len(str(result)) != 4):
        with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
            k = (str(request).split("'")[1]).split('/')[-1]
            k = 'select * from '+ schema +'.user_get(' + k +')'
            cursor.execute(k)
            result = str(cursor.fetchone())
            result = result[1:-2]
            result = ast.literal_eval(result)
        return JsonResponse(result)
    result = re.match(r'^/api/v1/user/(?P<pk>[0-9]+)$', str(request).split("'")[1])
    if (request.method == 'PUT') and (len(str(result)) != 4):
        with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
            k = (str(request).split("'")[1]).split('/')[-1]
            tutorial_data = JSONParser().parse(request)
            tutorial_data = str(tutorial_data).replace("'", '"')
            k = 'select * from '+ schema +'.user_upd(' + k + ",'" + str(tutorial_data) + "')"
            cursor.execute(k)
            result = str(cursor.fetchone())
            result = result[1:-2]
            result = ast.literal_eval(result)
        return JsonResponse(result)
    result = re.match(r'^/api/v1/user/(?P<pk>[0-9]+)$', str(request).split("'")[1])
    if (request.method == 'DELETE') and (len(str(result)) != 4):
        with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
            k = (str(request).split("'")[1]).split('/')[-1]
            k = 'select * from '+ schema +'.user_del(' + k +')'
            cursor.execute(k)
            result = str(cursor.fetchone())
            result = result[1:-2]
            result = ast.literal_eval(result)
        return JsonResponse(result)
    result = re.match(r'^/api/v1/comment/(?P<pk>[0-9]+)$', str(request).split("'")[1])
    if (request.method == 'GET') and (len(str(result)) != 4):
        with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
            k = (str(request).split("'")[1]).split('/')[-1]
            k = 'select * from '+ schema +'.comment_get(' + k +')'
            cursor.execute(k)
            result = str(cursor.fetchone())
            result = result[1:-2]
            result = ast.literal_eval(result)
        return JsonResponse(result)

    result = re.match(r'^/api/v1/user/(?P<pk>[0-9]+)/comment/$', str(request).split("'")[1])
    if (request.method == 'GET') and (len(str(result)) != 4):
        with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
            k = (str(request).split("'")[1]).split('/')[-3]
            x = '0'
            k = 'select * from '+ schema +'.user_comment_get(' + k + ', ' + x +')'
            cursor.execute(k)
            result = str(cursor.fetchone())
            result = result[2:-3]
            result = ast.literal_eval(result)
        return JsonResponse(result, safe=False)
    result = re.match(r'^/api/v1/user/(?P<x>[0-9]+)/comment/(?P<pk>[0-9]+)$', str(request).split("'")[1])
    print(request.method)
    if (request.method == 'GET') and (len(str(result)) != 4):
        with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
            k = (str(request).split("'")[1]).split('/')[-3]
            x = (str(request).split("'")[1]).split('/')[-1]
            k = 'select * from '+ schema +'.user_comment_get(' + k + ', ' + x +')'
            cursor.execute(k)
            result = str(cursor.fetchone())
            result = result[1:-2]
            result = ast.literal_eval(result)
        return JsonResponse(result)


    result = re.match(r'^/api/v1/user/(?P<pk>[0-9]+)/comment/$', str(request).split("'")[1])
    if (request.method == 'POST') and (len(str(result)) != 4):
        with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
            k = (str(request).split("'")[1]).split('/')[-3]
            tutorial_data = JSONParser().parse(request)
            tutorial_data = str(tutorial_data).replace("'",'"')
            k = 'select * from '+ schema +'.user_comment_ins(' + k + ", '" + str(tutorial_data) + "')"
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
            t = 'select * from '+ schema +'.comment_get(' + k + ')'
            cursor.execute(t)
            result = str(cursor.fetchone())
            result = result[1:-2]
            result = result.split(' ')[3][:-1]
            k = 'select * from '+ schema +'.comment_upd('+ result + ", " + k + ", '" + str(tutorial_data) + "')"
            cursor.execute(k)
            result = str(cursor.fetchone())
            result = result[1:-2]
            result = ast.literal_eval(result)
        return JsonResponse(result)
    result = re.match(r'^/api/v1/comment/(?P<pk>[0-9]+)$', str(request).split("'")[1])
    if (request.method == 'DELETE') and (len(str(result)) != 4):
        with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
            k = (str(request).split("'")[1]).split('/')[-1]
            t = 'select * from '+ schema +'.comment_get(' + k + ')'
            cursor.execute(t)
            result = str(cursor.fetchone())
            result = result[1:-2]
            result = result.split(' ')[3][:-1]
            k = 'select * from '+ schema +'.user_comment_del('+ result + ", " + k + ")"
            cursor.execute(k)
            result = str(cursor.fetchone())
            result = result[1:-2]
            result = ast.literal_eval(result)
        return JsonResponse(result)


@api_view(['GET', 'POST'])
def tutorial_list(request):
    result = re.match(r'^/api/v1/user/comment/$', str(request).split("'")[1])
    if (request.method == 'GET') and (len(str(result)) != 4):
        with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
            k = 'select * from '+ schema +'.user_comment_get(0,0)'
            cursor.execute(k)
            result = str(cursor.fetchone())
            result = result[1:-2]
            result = ast.literal_eval(result)
        return JsonResponse(result, safe=False)
    result = re.match(r'^/api/v1/user/$', str(request).split("'")[1])
    print(request.method)
    if (request.method == 'POST') and (len(str(result)) != 4):
        with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
            tutorial_data = JSONParser().parse(request)
            tutorial_data = str(tutorial_data).replace("'",'"')
            k = 'select * from '+ schema +'.user_ins('+"'" + str(tutorial_data) + "')"
            cursor.execute(k)
            result = str(cursor.fetchone())
            result = result[1:-2]
            result = ast.literal_eval(result)
            print(result)
        return JsonResponse(result, safe=False)
