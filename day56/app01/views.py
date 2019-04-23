from django.shortcuts import render,HttpResponse,redirect
from app01 import models
import json
# Create your views here.
def students(request):
    stu_list=models.Students.objects.all()
    cls_list=models.Classes.objects.all()
    return render(request,'student.html',{'stu_list':stu_list,'cls_list':cls_list})

def add_student(request):
    response = {'status': True, 'message': None,'data':None}

    try:
        u=request.POST.get('username')
        a=request.POST.get('age')
        g=request.POST.get('gender')
        c=request.POST.get('cls_id')

        obj=models.Students.objects.create(
            username=u,
            age=a,
            gender=g,
            cs_id=c
        )
        response['data']=obj.id
    except Exception as e:
        response['status']=False
        response['message']='用户输入错误'
    result=json.dumps(response,ensure_ascii=False)
    return HttpResponse(result)

def del_student(request):
    ret={'status':True}
    try:

        nid=request.GET.get('nid')
        models.Students.objects.filter(id=nid).delete()
    except Exception as e:
        ret['status']=False

    return HttpResponse(json.dumps(ret))

def edit_student(request):
    response={'code':1000,'message':None}
    try:
        nid=request.POST.get('nid')
        user=request.POST.get('user')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        cls_id=request.POST.get('cls_id')
        models.Students.objects.filter(id=nid).update(
            username=user,
            age=age,
            gender=gender,
            cs_id=cls_id
        )
    except Exception as e:
        response['code']=1001
        response['message']=str(e)

    return HttpResponse(json.dumps(response))