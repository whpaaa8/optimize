import pandas as pd
from django.core import serializers
from django.forms import ModelForm
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import UserInfo


# Create your views here.


def user_list(request):
    # 获取所有用户数据
    data_list = serializers.serialize("json", UserInfo.objects.all())
    # print(data_list)

    return HttpResponse(data_list, content_type="application/json")


def login(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    try:
        res = UserInfo.objects.get(username=username)
        # print(username, password)
        # print(res.uname)
        # 验证密码
        if res.check_password(password):
            return JsonResponse({'data': {'uname': res.uname}, 'message': 'Success'})
        else:
            return HttpResponse("Failed")
    except:
        return HttpResponse("Failed")


class UserForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = "__all__"


# phones = pd.read_excel("")
@csrf_exempt
def register(request):
    # print(request.headers)
    # print(request.body)
    # phone = request.POST.get('username')
    # if phone not in phones:
    #     return HttpResponse("Forbidden")
    form = UserForm(request.POST)
    # print(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("Success")
    else:
        return HttpResponse("Failed")
