from django.contrib import admin
from django.utils import timezone

from .models import Dolist

# Register your models here.
'''
class Dolist(models.Model):
    do_object = models.TextField(verbose_name="할 일", max_length=100, null=False)
    create_time = models.DateTimeField(verbose_name="작성일자", auto_now_add=True)
    finish_time = models.DateTimeField(verbose_name="완료일자", null=True)
'''


@admin.register(Dolist)
class DolistAdmin(admin.ModelAdmin):
    list_display = ["do_object", "create_time", "finish_time", ]
    readonly_fields = ["create_time", "finish_time", ]

    actions = ["gotodone", "gotodo", ]

    @admin.action(description="해당 할 일을 완료로 변경")
    def gotodone(modeladmin, request, queryset):
        queryset.update(finish_time=timezone.localtime()) 

    @admin.action(description="완료 상태를 해제합니다.")
    def gotodo(modeladmin, request, queryset):
        queryset.update(finish_time=None) 
