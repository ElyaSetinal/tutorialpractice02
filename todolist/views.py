from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Dolist

# Create your views here.


def dolistdisplay(request):
    todolist_obj = Dolist.objects.all()

    context = {
        'obj': todolist_obj
    }

    return render(request, "todolist_page.html", context)


def newlistcreate(request):
    new_obj = request.POST.get("todoobject")
    print(new_obj)
    Dolist.objects.create(do_object=new_obj)

    return redirect('dolist')


def workdone(request):
    done_obj = request.GET["todoNum"]

    Dolist.objects.filter(id=done_obj).update(finish_time=timezone.localtime())

    return redirect('dolist')


def donecancel(request):
    done_obj = request.GET["todoNum"]

    Dolist.objects.filter(id=done_obj).update(finish_time=None)

    return redirect('finishpage')


def donelistdisplay(request):
    todolist_obj = Dolist.objects.all()

    context = {
        'obj': todolist_obj
    }

    return render(request, "donelist_page.html", context)
