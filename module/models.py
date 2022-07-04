from django.db import models
from django.contrib.auth.models import User

from page.models import Page
from quiz.models import Quizzes
from assignment.models import Assignment

# Create your models here.

class Module(models.Model):
	title = models.CharField(max_length=150)
	# video = models.FileField(null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='module_owner')
	hours = models.PositiveIntegerField()
	pages = models.ManyToManyField(Page)
	quizzes = models.ManyToManyField(Quizzes)
	assignments = models.ManyToManyField(Assignment)

	def __str__(self):
		return self.title


class ModuleProgress(models.Model):
	module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='module_progress')
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress_owner')
	completed = models.BooleanField(default=False)
	def __str__(self):
		return self.title
