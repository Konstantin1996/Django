from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from login.forms import UserCreateForm
# Create your views here.

def enter(request):

    username = request.POST.get('username',False)
    pswrd = request.POST.get('password',False)

    user = auth.authenticate(username=username, password=pswrd)

    if request.POST:
        if user is not None:
            auth.login(request,user)
            return redirect('/blog')
        else:
            content = {
                'loginerror':'Неправильный логин или пароль'
            }
            return render(request, 'login/login.html', content)
    else:
        return render(request, 'login/login.html')



def register(request):
    if request.POST:
        print('post request')
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = auth.authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password1'] )
            auth.login(request, new_user)
            print('try to register')
            return redirect('article:index')
        else:
            context = {
                'form': form,
                'regdescr': 'Пароль должен содержать как минимум 8 символов, не должен быть распространенным и содержать хотя бы одну цифру.',
                'regerror': 'Вы ввели неверный логин или пароль',
            }
            print('getrequest')
            return render(request,'login/register.html',context)
    else:
        form = UserCreateForm()
        context = {
            'form': form,
            'regdescr': 'Пароль должен содержать как минимум 8 символов, не должен быть распространенным и содержать хотя бы одну цифру.',
        }
        print('here')
        return render(request, 'login/register.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/blog')