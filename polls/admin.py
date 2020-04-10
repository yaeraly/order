from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    fieldsets = [
        ('Question',         {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
