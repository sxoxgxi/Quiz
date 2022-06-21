from django.contrib import admin

from .models import Categories, Questions, Answers
# Register your models here.


class ShowAnswer(admin.StackedInline):
    model = Answers


class QuestionsAdmin(admin.ModelAdmin):
    inlines = [ShowAnswer]


admin.site.register(Categories)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Answers)
