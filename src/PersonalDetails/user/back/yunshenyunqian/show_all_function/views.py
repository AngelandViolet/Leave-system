from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import all_base_data, change_data, leave_data
import json
# Create your views here.
# 所有信息
def show_all_data(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id', 'Not find')
        print('本次请求的id是:'+user_id)
        all_base = all_base_data.objects.filter(user_id=user_id, is_delete=True)
        all_change = change_data.objects.filter(user_id=user_id, is_delete=True)
        all_leave = leave_data.objects.filter(user_id=user_id, is_delete=True)
        data = {}
        if all_base:
            data_list_1 = []
            for i in all_base:
                single_data = {}
                single_data['user_id'] = i.user_id
                single_data['name'] = i.name
                date3 = f'{i.date}第{i.time}节'
                single_data['date&time'] = date3
                data_list_1.append(single_data)
            # 输出用户的基础数据
            data['base_data'] = data_list_1
        else:
            data['base_data'] = 'Not find!!!'
        if all_change:
            data_list_2 = []
            for k in all_change:
                single_change = {}
                old_time = f'{k.old_date}第{k.old_time}节'
                single_change['old_time'] = old_time
                new_time = f'{k.new_date}第{k.new_time}节'
                single_change['new_time'] = new_time
                single_change['reason'] = k.reason
                data_list_2.append(single_change)
            # 输出用户的调换数据
            data['change_data'] = data_list_2
        else:
            data['change_data'] = 'Not find!!!'
        if all_leave:
            data_list_3 = []
            for j in all_leave:
                single_leave = {}
                old_time_2 = f'{j.old_date}第{j.old_time}节'
                single_leave['old_time'] = old_time_2
                single_leave['reason'] = j.reason
                data_list_3.append(single_leave)
            # 输出用户的请假数据
            data['leave_data'] = data_list_3
        else:
            data['leave_data'] = 'Not find!!!'
        # 以json形式返回数据
        json_str = json.dumps(data, ensure_ascii=False)
        return HttpResponse(json_str)
    if request.method == 'OPTIONS':
        return HttpResponse('内网穿透连接成功')
# 撤销调换操作功能
def cancel_change(request):
    try:
        resp = json.loads(request.body)
        user_id = resp['user_id']
        old_date = resp['old_date']
        old_time = resp['old_time']
        new_date = resp['new_date']
        new_time = resp['new_time']
        old_object = all_base_data.objects.get(user_id=user_id, date=old_date, time=old_time, is_delete=False)
        new_object = change_data.objects.get(user_id=user_id, new_date=new_date, new_time=new_time, is_delete=True)
        old_object.is_delete = True
        old_object.save()
        new_object.is_delete = False
        new_object.save()
        return HttpResponse('撤销成功!')
    except Exception as e:
        print(f"the error is {e}")
        return HttpResponse('请求异常，请稍后再试')
# 撤销请假操作的功能
def cancel_leave(request):
    try:
        resp = json.loads(request.body)
        user_id = resp["user_id"]
        date = resp["date"]
        time = resp["time"]
        old_object = all_base_data.objects.get(user_id=user_id, date=date, time=time, is_delete=False)
        leave_object = leave_data.objects.get(user_id=user_id, old_date=date, old_time=time, is_delete=True)
        old_object.is_delete = True
        leave_object.is_delete = False
        old_object.save()
        leave_object.save()
        return HttpResponse("撤销成功!")
    except Exception as e:
        print(f"the error is {e}")
        return HttpResponse('请求异常，请稍后再试')

# 展示出所有的调换信息
def show_change_data(request):
    if request.method == 'POST':
        resp = json.loads(request.body)
        user_id = resp['user_id']
        all_change = change_data.objects.filter(user_id=user_id)
        if all_change:
            data_list = []
            for i in all_change:
                single_data = {}
                single_data['user_id'] = i.user_id
                single_data['name'] = i.name
                single_data['old_date'] = i.old_date
                single_data['old_time'] = i.old_time
                single_data['new_date'] = i.new_date
                single_data['new_time'] = i.new_time
                single_data['reason'] = i.reason
                data_list.append(single_data)
            data = {}
            data['data'] = data_list
            json_str = json.dumps(data)
            return HttpResponse(json_str)
        else:
            response = {}
            response['response'] = 'Not finding!!!'
            json_str = json.dumps(response)
            return HttpResponse(json_str)
