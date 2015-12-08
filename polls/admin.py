# coding=utf-8
from django.contrib import admin
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# Register your models here.
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('问题内容', {'fields': ['question_text']}),
        ('问题信息', {'fields': ['pub_date', 'question_num']},),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
