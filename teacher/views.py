import markdown2, urllib.parse
from .models import Teacher
from school.models import School
from .forms import LoginForm, RegisterForm, SetInfoForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    latest_teacher_list = Teacher.objects.get_queryset()
    loginForm = LoginForm()
    context = {'latest_teacher_list': latest_teacher_list, 'loginform': loginForm}
    return render(request, 'index.html', context)

def school(request, school_id):
	'''
	try:   # since visitor input a url with invalid id
		article = Article.objects.get(pk=article_id)  # pk??? 
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	''' # shortcut:
	school = get_object_or_404(School, id=school_id)
	loginform = LoginForm()

	return render(request, 'school_page.html', {
		'school': school,
		'loginform':loginform,
})

def log_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['uid']
            password = form.cleaned_data['pwd']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                url = request.POST.get('source_url', '/teacher')
                return redirect(url)
            else:
                return render(request, 'login.html', {'form': form, 'error': "password or username is not ture!"})

        else:
            return render(request, 'login.html', {'form': form})


@login_required
def log_out(request):
    url = request.POST.get('source_url', '/teacher/')
    logout(request)
    return redirect(url)


def register(request):
    error1 = "this name is already exist"
    valid = "this name is valid"

    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if request.POST.get('raw_username', 'erjgiqfv240hqp5668ej23foi') != 'erjgiqfv240hqp5668ej23foi':  # if ajax
            try:
                user = Teacher.objects.get(realName=request.POST.get('raw_username', ''))
            except ObjectDoesNotExist:
                return render(request, 'register.html', {'form': form, 'msg': valid})
            else:
                return render(request, 'register.html', {'form': form, 'msg': error1})

        else:
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 != password2:
                    return render(request, 'register.html', {'form': form, 'msg': "two password is not equal"})
                else:
                    user = Teacher(realName=username, email=email, password=password1)
                    user.save()
                    # return render(request, 'login.html', {'success': "you have successfully registered!"})
                    return redirect('/teacher/login')
            else:
                return render(request, 'register.html', {'form': form})