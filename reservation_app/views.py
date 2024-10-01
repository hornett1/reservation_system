from django.shortcuts import render
from .models import *

def user_list(request):
    users = User.objects.all()
    return render(request, 'books/book_list.html', {'books': users})
