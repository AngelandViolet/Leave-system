from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json
from .models import logAndsign, invitationCodes
# Create your views here.
def user_log(request):
    if request.method == 'POST':
        resp = json.loads(request.body)
        user_id = resp["user_id"]
        password = resp["password"]
        the_judge = logAndsign.objects.filter(user_id=user_id, password=password)
        if len(the_judge) != 0:
            return HttpResponse("登录成功")
        else:
            return HttpResponse("用户名或密码错误！")

def user_sign(request):
    if request.method == 'POST':
        resp = json.loads(request.body)
        user_id = resp["user_id"]
        password = resp["password"]
        invitation_code = resp["invitation_code"]
        the_judge_1 = invitationCodes.objects.filter(invitation_code=invitation_code)
        if len(the_judge_1) != 0:
            the_judge_2 = logAndsign.objects.filter(user_id=user_id)
            if len(the_judge_2) == 0:
                obj = logAndsign(user_id=user_id, password=password)
                obj.save()
                return HttpResponse("注册成功")
            else:
                return HttpResponse("该用户名已被注册")
        else:
            return HttpResponse("邀请码错误或已失效！")
