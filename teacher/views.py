import markdown2, urllib.parse
from .models import Teacher
from .forms import LoginForm
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