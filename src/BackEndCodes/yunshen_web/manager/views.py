from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import managerIdPass
from user.models import theStudy, changeData, leaveData, operateTime, SignLog
import json
# Create your views here.

# 管理端登录
def manager_log(request):
    if request.method == 'POST':
        resp = json.loads(request.body.decode('utf-8'))
        manager_id = resp['manager_id']
        manager_pass = resp['manager_pass']
        target_objects = managerIdPass.objects.filter(manager_id=manager_id, manager_pass=manager_pass)
        if len(target_objects) == 0:
            return HttpResponse(status=204)
        if target_objects:
            print("管理端登陆成功")
            return HttpResponse("管理端登陆成功", status=203)

# 管理端展示所有用户调换研学信息
def show_change_data(request):
    print(1111111111)
    if request.method == "GET":
        data_list = changeData.objects.all()
        b = []
        for a in data_list:
            user_id = a.user_id
            test_object = SignLog.objects.get(user_id=user_id)
            user_name = test_object.user_name
            user_sector = test_object.user_sector
            old_time = a.old_time
            old_class = a.old_class
            new_class = a.new_class
            new_time = a.new_time
            change_reason = a.change_reason
            result = {"user_name": user_name, "user_sector": user_sector, "old_class": old_class,
                      "old_time": old_time, "new_class": new_class, "new_time": new_time,
                      "change_reason": change_reason}
            b.append(result)

        print(b)
        return HttpResponse(json.dumps(b, ensure_ascii=False), content_type="application/json")


def show_leave_data(request):
    if request.method == "GET":
        data_list = leaveData.objects.all()
        b = []
        for a in data_list:
            user_id = a.user_id
            test_object = SignLog.objects.get(user_id=user_id)
            user_name = test_object.user_name
            user_sector = test_object.user_sector
            leave_time = a.leave_time
            leave_class = a.leave_class
            leave_reason = a.leave_reason
            result = {"user_name": user_name, "user_sector": user_sector,
                      "leave_time": leave_time,
                      "leave_class": leave_class, "leave_reason": leave_reason}

            b.append(result)
        print(b)
        # 转换为 JSON 字符串并返回
        return HttpResponse(json.dumps(b, ensure_ascii=False), content_type="application/json")

# 管理端展示某个人的数据
def show_all_data(request):
    if request.method == 'POST':
        json_str = json.loads(request.body)
        user_id = json_str['user_id']
        print('本次请求的id是:'+user_id)

        # all_base = all_base_data.objects.filter(user_id=user_id, is_delete=True)
        all_change = changeData.objects.filter(user_id=user_id, is_delete=False)
        all_leave = leaveData.objects.filter(user_id=user_id, is_delete=False)
        data = {}
        # if all_base:
        #     data_list_1 = []
        #     for i in all_base:
        #         single_data = {}
        #         single_data['user_id'] = i.user_id
        #         single_data['name'] = i.name
        #         date3 = f'{i.date}第{i.time}节'
        #         single_data['date&time'] = date3
        #         data_list_1.append(single_data)
        #     # 输出用户的基础数据
        #     data['base_data'] = data_list_1
        # else:
        #     data['base_data'] = 'Not find!!!'
        if all_change:
            data_list_2 = []
            for k in all_change:
                single_change = {}
                old_time = f'{k.old_time}第{k.old_class}节'
                single_change['old_time'] = old_time
                new_time = f'{k.new_time}第{k.new_class}节'
                single_change['new_time'] = new_time
                single_change['reason'] = k.change_reason
                #single_change = serializers.serialize('json', single_change)
                data_list_2.append(single_change)
            # 输出用户的调换数据
            data['change_data'] = data_list_2
            #data.append(data_list_2)
        else:
            data['change_data'] = 'Not find'
        if all_leave:
            data_list_3 = []
            for j in all_leave:
                single_leave = {}
                old_time_2 = f'{j.leave_time}第{j.leave_class}节'
                single_leave['time'] = old_time_2
                single_leave['reason'] = j.leave_reason
                #single_leave = serializers.serialize('json', single_leave)
                data_list_3.append(single_leave)
            # 输出用户的请假数据
            data['leave_data'] = data_list_3
        else:
            data['leave_data'] = "not find"
        #data = serializers.serialize(data)
        # 以json形式返回数据
        json_str = json.dumps(data, ensure_ascii=False)
        print(type(json_str))
        resp = HttpResponse(json_str, content_type='application/json')
        #return JsonResponse(data=json_str, safe=False, content_type='application/json')
        print(type(resp))
        return resp





