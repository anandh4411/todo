from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password, check_password
from home.models import Task, User

# Create your views here.

def home(request):
    if 'user_id' in request.session:
        user_id = request.session["user_id"]
        queryset = Task.objects.filter(user__pk=user_id)
        return render(request, 'home.html', {"tasks" : queryset})
    else:
        return redirect(signup)

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        queryset = User.objects.all()

        for user in queryset:
            if user.phone == phone:
                if user.email == email:
                    if check_password(password, user.password):
                        request.session['user_id'] = user.id
                        request.session['user_name'] = user.name
                        return redirect(home)
        return render(request, 'auth-failed.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            user = User()
            user.name = name
            user.email = email
            user.phone = phone
            user.password = make_password(password)
            user.save()
            return redirect(home)
        else:
            return render(request, 'auth-failed.html')

def logout(request):
    del request.session['user_id']
    del request.session['user_name']
    return redirect(home)
        
def task_add(request):
    if request.method == 'POST':
        task = request.POST['task']
        estimated_time = request.POST['estimated_time']
        user_id = request.session["user_id"]
        user = User.objects.get(id=user_id)
        task_instance = Task()
        task_instance.task = task
        task_instance.estimated_time = estimated_time
        task_instance.elapsed_time = 0
        task_instance.user = user
        task_instance.save()
        return redirect(home)

def task_delete(request):
    id = request.GET.get('id', None)
    task = Task.objects.get(id=id)
    task.delete()
    return redirect(home)

def task_update(request):
    if request.method == 'GET':
        data = {}
        id = request.GET.get('id', None)
        data["id"] = id
        task_instance = Task.objects.get(id=id)
        data["task"] = task_instance
        return render(request, 'task-update.html', data)

    if request.method == 'POST':
        id = request.POST['id']
        task = request.POST['task']
        estimated_time = request.POST['estimated_time']
        elapsed_time = request.POST['elapsed_time']
        Task.objects.filter(id=id).update(task=task, estimated_time=estimated_time, elapsed_time=elapsed_time)
        return redirect(home)