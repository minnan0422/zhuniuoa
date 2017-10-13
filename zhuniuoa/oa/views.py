from django.shortcuts import render,get_object_or_404,redirect
from .models import Overtime_work,Time_off,Total_time
from .forms import Work_Time_Form,Off_Time_Form
# Create your views here.


def work_time(request):

    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden" name="next" value="{{ next }}"/>
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = Work_Time_Form(request.POST)


        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库

            form.save()
            print(form.Meta.model.work_time)


            # 注册成功，跳转回首页
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/index')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = Work_Time_Form()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    # 将记录用户注册前页面的 redirect_to 传给模板，以维持 next 参数在整个注册流程中的传递

    return render(request, 'oa/jbsj.html', context={'form': form, 'next': redirect_to})
#加班记录查询函数
def work_list(request,oa_user):
    #oa_user = int(oa_user)
    select_list = Overtime_work.objects.filter(oa_user_id=oa_user)
    #post_list = Overtime_work.objects.all()
    print(select_list)
    return render(request, 'oa/select.html', context={'select_list': select_list})

def select(request):
    return render(request,'oa/select.html')

#请假函数
def off_time(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        form = Off_Time_Form(request.POST)
        if form.is_valid():
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/index')
    else:
        form = Off_Time_Form()
    return render(request, 'oa/off_time.html', context={'form': form, 'next': redirect_to})


#请假记录查询函数
def  off_list(request,oa_user):
    select_list = Time_off.objects.filter(oa_user_id=oa_user)
    #post_list = Overtime_work.objects.all()
    print(select_list)
    return render(request, 'oa/select_off.html', context={'select_list': select_list})

#剩余调休时间
def total_time(request,oa_user):
    work_list = Overtime_work.objects.filter(oa_user_id=oa_user)
    list1=[]
    for work in work_list:
        list1.append(work.work_time)
    s1 = sum(list1)
   # print(s1)
    off_list = Time_off.objects.filter(oa_user_id=oa_user)
    list2=[]
    for off in off_list:
        list2.append(off.off_time)
    s2 = sum(list2)
    total_list = s1 - s2
    if total_list < 0:
        total_list = 0
        return render(request, 'oa/total_time.html', context={'total_list': total_list})
    else:
        Total_time.objects.filter(oa_user_id=oa_user).update(total_time=total_list)
    return render(request, 'oa/total_time.html', context={'total_list': total_list})
