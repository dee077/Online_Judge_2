from django.contrib import admin

# Register your models here.
from .models import Problem, Submission

class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'submission_count')
    search_fields = ('title', 'difficulty')

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Submission)