'''Interacting with Django's Admin app'''
from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    '''Modification to Choice in Question page'''
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    '''Modification to Question page'''
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],
                              'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
