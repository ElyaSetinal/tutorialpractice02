from django.db import models


class Dolist(models.Model):
    class Meta:
        verbose_name_plural = "할 일 목록"  # admin page category's name

    # To do list model
    do_object = models.TextField(verbose_name="할 일", max_length=100, null=False)
    create_time = models.DateTimeField(verbose_name="작성일자", auto_now_add=True)
    finish_time = models.DateTimeField(verbose_name="완료일자", null=True)

    def __str__(self):  # 클래스의 정보를 name으로 호출하는 함수
        return f'{self.do_object}'
