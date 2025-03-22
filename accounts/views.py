from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def register_view(request):
    if request.method == 'POST': #Se o metodo utilizado pelo usuario for POST (enviar dados de login)
        user_form = UserCreationForm(request.POST)  #O user_form tera um metodo POST
        if user_form.is_valid(): #Valida se o usuario informou tudo de forma valida
            user_form.save() #Salva os dados de registro do usuario
            return redirect('login') #Redireciona o usuario para a tela de login
    else:
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm
    else:
        login_form = AuthenticationForm()
        return render(request, 'login.html', {'login_form': login_form})
    
def logout_view(request):
    logout(request)
    return redirect('cars_list')