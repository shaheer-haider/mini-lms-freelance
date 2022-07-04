from django.contrib import admin
from page.models import PostFileContent
from quiz.models import Quizzes
from assignment.models import AssignmentFileContent

# Register your models here.
admin.site.register(PostFileContent)
admin.site.register(AssignmentFileContent)
