from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import invitationCode, SignLog, theStudy, changeData, leaveData, operateTime
from django.utils import timezone
import json
import hashlib
from . import auth
from django.contrib import messages

import datetime

from random import choice
from string import ascii_uppercase as uc, digits as dg


# Create your views here.
# 随机生成验证码
def make_codes(request):
    # 验证码生成
    if request.method == 'GET':
        for i in range(50):
            part1 = ''.join(choice(uc) for j in range(4))  # 三个大写的英文
            part2 = ''.join(choice(dg) for j in range(4))  # 三个随机数字
            part3 = part1 + part2
            c = invitationCode.objects.create(invitation_codes=part3)
            c.save()
    return HttpResponse("创建邀请码成功")


# 时间转换
def transfer(old_time):
    if old_time == '第一大节':
        return 1
    elif old_time == '第二大节':
        return 2
    elif old_time == '第三大节':
        return 3
    elif old_time == '第四大节':
        return 4
    else:
        return int(old_time)


# 返回前端的用户信息
def show_user_information(request):
    if request.method == 'POST':
        resp = json.loads(request.body)
        user_id = resp['user_id']
        # user_id = request.session['user_id']
        target_objects = SignLog.objects.get(user_id=user_id)
        user_name = target_objects.user_name
        user_sector = target_objects.user_sector
        user_period = target_objects.user_period
        data = {}
        data['user_name'] = user_name
        data['user_sector'] = user_sector
        data['user_period'] = user_period
        json_str = json.dumps(data, ensure_ascii=False)
        return HttpResponse(json_str, content_type='application/json')


# 用户注册函数
def user_sign(request):
    if request.method == 'POST':
        json_str = json.loads(request.body.decode('utf-8'))
        print(json_str)
        user_id = json_str['user_id']
        user_pass = json_str['user_pass']
        user_name = json_str['user_name']
        user_sector = json_str['user_sector']
        user_period = json_str['user_period']
        invitation_code = json_str['invitation_code']
        # 验证邀请码是否正确
        code_judge = invitationCode.objects.filter(invitation_codes=invitation_code)
        if len(code_judge) == 0:
            return HttpResponse('该验证码已失效或输入错误')
        old_users_id = SignLog.objects.filter(user_id=user_id)
        if old_users_id:
            return HttpResponse("该用户名已被注册")
        # 哈希算法将密码转化为不可逆的值
        m = hashlib.md5()  # 生成哈希算法对象
        m.update(user_pass.encode())
        # 注册账号，向数据表中录入信息
        user = SignLog(user_id=user_id, user_pass=m.hexdigest(), user_name=user_name, user_sector=user_sector,
                       user_period=user_period)
        user.save()
        print("注册的id是" + user_id)
        return HttpResponse(201)


# 用户登录函数
def user_log(request):
    if request.method == 'GET':
        # 查看session(1day)
        print(request.session.get('user_id'))
        if request.session.get('user_id'):
            user_id = request.session['user_id']
            print("本次GET登录的id是:" + request.session.get('user_id'))
            return HttpResponse("已登录")
        # 无session，查看cookies(14days)
        elif request.COOKIES.get('user_id') or request.COOKIES.get('pri_id'):
            print("COOKIES中找到id")
            # 恢复session
            request.session['user_id'] = request.COOKIES.get('user_id')
            print("本次GET登录的id是:" + request.COOKIES.get('user_id'))
            return HttpResponse('已登录')
        else:
            return HttpResponse(status=403)
    if request.method == "POST":
        json_str = json.loads(request.body.decode("utf-8"))
        user_id = json_str['user_id']
        user_pass = json_str['user_pass']
        # 哈希算法将密码转化为不可逆的值, 再与库中存储进行比对
        m = hashlib.md5()  # 生成哈希算法对象
        m.update(user_pass.encode())
        target_user = SignLog.objects.filter(user_id=user_id, user_pass=m.hexdigest())
        target_user_1 = SignLog.objects.filter(user_id=user_id)
        if len(target_user_1) == 0:
            return HttpResponse(status=202)
        if target_user:
            request.session['user_id'] = user_id
            print("登陆的id是" + request.session['user_id'])
            # data = dict()
            # data["userid"] = user_id
            # token = auth.create_token(data)
            # return JsonResponse({
            #     "token": token
            # })
            local_id = {'user_id': f"{user_id}"}
            json_dic = json.dumps(local_id, ensure_ascii=False)
            return HttpResponse(json_dic, content_type='application/json')
        else:
            print(11111)
            respon = HttpResponse(status=201)
            print(respon)
            return respon


# 请假
def ask_leave(request):
    if request.method == 'POST':
        json_str = json.loads(request.body.decode('utf-8'))
        # user_id = request.session['user_id']
        user_id = json_str['user_id']
        print("/////////")
        print(user_id)
        leave_date = json_str['leave_date']
        leave_class = json_str['leave_class']
        leave_reason = json_str['leave_reason']
        if len(leave_reason) == 0:
            return HttpResponse("请假原因不得为空", status=201)
        else:
            c = theStudy.objects.filter(user_id=user_id, study_date=leave_date, study_class=leave_class, is_leave=0,
                                        is_change=0)
            if c:
                c.update(is_leave=1)
                d = leaveData.objects.create(user_id=user_id, leave_time=leave_date, leave_class=leave_class,
                                             leave_reason=leave_reason)
                d.save()
                return HttpResponse("修改成功")
            else:
                return HttpResponse("未查询到研学信息", status=202)


# 撤销请假
def cancel_leave(request):
    if request.method == 'POST':

        json_str = json.loads(request.body.decode('utf-8'))
        # user_id = request.session['user_id']
        user_id = json_str['user_id']
        date = json_str['leave_date']
        target_1 = theStudy.objects.filter(user_id=user_id, study_date=date, is_leave=1)
        target_2 = leaveData.objects.filter(user_id=user_id, leave_time=date, is_delete=0)
        if len(target_1) == 0 or len(target_2) == 0:
            return HttpResponse("信息错误", status=201)
        else:
            target_1.update(is_leave=0)
            target_2.delete()
            return HttpResponse("撤销请假成功")


# 时间判断函数,判断调研学时间是否合理
def time_is_ok(old_time):
    curr = datetime.datetime.now()
    adjust_hour = 8 + 2 * (transfer(old_time) - 1)
    return curr.hour < adjust_hour


# 日期判断函数
def date_is_ok(old_date):
    d1 = timezone.now().strftime("%Y-%m-%d")
    print(d1)
    print(old_date)

    return old_date >= d1


# 调换
def ask_change(request):
    if request.method == 'POST':
        json_str = json.loads(request.body)
        old_date = json_str['old_date']
        old_class = json_str['old_class']
        change_reason = json_str['change_reason']
        if date_is_ok(old_date=old_date):
            # if time_is_ok(old_time=old_class):
            if len(change_reason) == 0:
                return HttpResponse("请假原因不得为空", status=201)
            else:
                # user_id = request.session['user_id']
                user_id = json_str['user_id']
                new_date = json_str['new_date']
                new_class = json_str['new_class']
                c = theStudy.objects.filter(user_id=user_id, study_date=old_date, study_class=old_class, is_leave=0,
                                            is_change=0)
                if c:
                    c.update(is_change=1)
                    d = changeData.objects.create(user_id=user_id, old_time=old_date, old_class=old_class,
                                                  new_time=new_date, new_class=new_class,
                                                  change_reason=change_reason)
                    d.save()
                    return HttpResponse("调换研学成功")
                else:
                    return HttpResponse("未查询到数据", status=202)
        # elif date_is_ok(old_date=old_date) == 3 and time_is_ok(old_time=old_class) == 0:
        #     return HttpResponse("该日研学时间已过", status=201)

        else:
            return HttpResponse("未在规定时间内调换", status=203)


# 撤销调换
def cancel_change(request):
    curr = datetime.datetime.now()
    if request.method == 'POST':
        json_str = json.loads(request.body)
        print(json_str)
        # user_id = request.session['user_id']
        user_id = json_str['user_id']
        print(user_id)
        old_date = json_str['old_date']
        old_class = json_str['old_class']
        new_date = json_str['new_date']
        new_class = json_str['new_class']
        targeted_user_2 = theStudy.objects.filter(user_id=user_id, study_date=old_date,
                                                  study_class=old_class, is_leave=0, is_change=1)
        targeted_user = changeData.objects.filter(user_id=user_id, new_time=new_date, new_class=new_class,
                                                  is_delete=0)
        adjusted_hour = 8 + 2 * (transfer(new_class) - 1)
        print(targeted_user)
        print(targeted_user_2)
        if len(targeted_user) == 0:
            return HttpResponse("未找到该调换信息", status=201)
        else:
            if date_is_ok(old_date) is not True:
                return HttpResponse('研学日期已过，无法调换', status=202)
            else:
                if adjusted_hour < curr.hour:
                    targeted_user.delete()
                    targeted_user_2.update(is_change=0)
                    return HttpResponse("撤销研学成功")
                else:
                    return HttpResponse("研学时间已过", status=203)


# 用户端显示所有操作数据
def show_all_data(request):
    if request.method == 'POST':
        json_str = json.loads(request.body)
        user_id = json_str['user_id']
        #user_id = request.session['user_id']
        print('本次请求的id是:' + user_id)

        # all_base = all_base_data.objects.filter(user_id=user_id, is_delete=True)
        all_change = changeData.objects.filter(user_id=user_id, is_delete=False)
        all_leave = leaveData.objects.filter(user_id=user_id, is_delete=False)
        data = {}
        if all_change:
            data_list_2 = []
            for k in all_change:
                single_change = {}
                old_time = f'{k.old_time}第{k.old_class}节'
                single_change['old_time'] = old_time
                new_time = f'{k.new_time}第{k.new_class}节'
                single_change['new_time'] = new_time
                single_change['reason'] = k.change_reason
                # single_change = serializers.serialize('json', single_change)
                data_list_2.append(single_change)
            # 输出用户的调换数据
            data['change_data'] = data_list_2
            # data.append(data_list_2)
        else:
            data['change_data'] = 'Not find'
        if all_leave:
            data_list_3 = []
            for j in all_leave:
                single_leave = {}
                old_time_2 = f'{j.leave_time}第{j.leave_class}节'
                single_leave['time'] = old_time_2
                single_leave['reason'] = j.leave_reason
                # single_leave = serializers.serialize('json', single_leave)
                data_list_3.append(single_leave)
            # 输出用户的请假数据
            data['leave_data'] = data_list_3
        else:
            data['leave_data'] = "not find"
        # data = serializers.serialize(data)
        # 以json形式返回数据
        json_str = json.dumps(data, ensure_ascii=False)
        print(type(json_str))
        resp = HttpResponse(json_str, content_type='application/json')
        # return JsonResponse(data=json_str, safe=False, content_type='application/json')
        print(type(resp))
        return resp
