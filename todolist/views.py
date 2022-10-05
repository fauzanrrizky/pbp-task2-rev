from ast import Delete
from django.shortcuts import render

# Import untuk fungsi register
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Import fungsi login
from django.contrib.auth import authenticate, login

# Import fungsi logout
from django.contrib.auth import logout

# Fungsi untuk merestriksi akses halaman todolist
from django.contrib.auth.decorators import login_required

# Fungsi untuk menambahkan cookies
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Import forms
from todolist.forms import ToDoListForm

# Import models
from todolist.models import ToDoList

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data = ToDoList.objects.filter(user=request.user)
    context = {
    'username' : request.user.username,
    'data' : data,
    # 'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html",context)



# Fungsi untuk create task
@login_required(login_url='/todolist/login/')
def create_task(request):
    form = ToDoListForm(request.POST)
    if form.is_valid() and request.method == "POST":
        ToDoList.objects.create(title=form.cleaned_data["title"], description=form.cleaned_data["description"], date=datetime.datetime.now(), user=request.user)
        return redirect("todolist:show_todolist")
    form = ToDoListForm()
    return render(request, "create-task.html", context={"form":form})

# Fungsi untuk remove task
@login_required(login_url='/todolist/login/')
def remove_task(request,id):
    ToDoList.objects.get(id=id).delete()
    return redirect('todolist:show_todolist')

# Fungsi untuk lihat status
@login_required(login_url='/todolist/login/')
def status_task(request,id):
    todo = ToDoList.objects.get(id=id)
    todo.is_finished = not(todo.is_finished)
    todo.save()
    return redirect('todolist:show_todolist')

# Fungsi register
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

# Fungsi login
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

# Fungsi logout
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response