# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from Models.models import Users


def index(request):
    view_data = {}
    view_data['hello'] = 'Hello World!'
    return render(request, 'index.html', view_data)


def db_insert(request):
    # 把GET或POST過來的資料轉為UTF8
    request.encoding = 'utf-8'
    # 檢查GET參數裡面有沒有name的參數
    if 'name' in request.GET:
        # 建立起 INSERT Models_users (name) VALUES ('xxxx') 的QUERY
        user_name = request.GET['name']
        new_record = Users(name=user_name)
        # 執行QUERY
        new_record.save()
        response = user_name + ' was inserted into DB!'
    else:
        response = 'ERROR'

    return HttpResponse("<p>" + response + "</p>")


def db_select_all(request):
    response = ""
    # 執行 SELECT * FROM Models_users
    list = Users.objects.all()

    # 把每一列都印出來
    for user_info in list:
        response += str(user_info.id) + ':' + user_info.name + " "
    return HttpResponse("<p>" + response + "</p>")


def db_select_by_name(request):
    request.encoding = 'utf-8'
    response = ""
    if 'name' in request.GET:
        # 把GET的值取出
        user_name = request.GET['name']
        # filter就是 WHERE
        list = Users.objects.all().filter(name=user_name)
        for user_info in list:
            response += "<p>" + str(user_info.id) + \
                ':' + user_info.name + "</p><br/>"
    else:
        response = 'ERROR'

    return HttpResponse(response)


def db_update(request):
    request.encoding = 'utf-8'
    response = ""
    if 'id' in request.GET and 'name' in request.GET:
        user_id = request.GET['id']
        user_name = request.GET['name']
        # 在Django中相當直覺，感覺上就好像是先把某個要更新的值取出然後在對他.update()的感覺:P
        Users.objects.filter(id=user_id).update(name=user_name)
        response = 'Updated!'
    else:
        response = 'ERROR'

    return HttpResponse(response)


def db_delete_by_id(request):
    request.encoding = 'utf-8'
    response = ""
    if 'id' in request.GET:
        user_id = request.GET['id']
        Users.objects.filter(id=user_id).delete()
        response = 'Deleted!'
    else:
        response = 'ERROR'

    return HttpResponse(response)
