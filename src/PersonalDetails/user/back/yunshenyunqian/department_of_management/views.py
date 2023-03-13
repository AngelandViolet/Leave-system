from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json
from .models import  managementIdpassword
# Create your views here.
def manager_log(request):
    if request.method == "POST":
        resp = json.loads(request.body)
        manager_id = resp['manager_id']
        pass_word = resp['password']
        the_judge = managementIdpassword.objects.filter(manager_id=manager_id, password=pass_word)
        if len(the_judge) != 0:
            return HttpResponse('用户端登录成功')
        else:
            return HttpResponse("用户端登陆失败")