from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden

from module.forms import NewModuleForm
from module.models import Module
from classroom.models import Course

from completion.models import Completion

# Create your views here.

def NewModule(request, course_id):
	user = request.user
	course = get_object_or_404(Course, id=course_id)

	if user != course.user:
		return HttpResponseForbidden()
	else:
		if request.method == 'POST':
			form = NewModuleForm(request.POST)
			if form.is_valid():
				title = form.cleaned_data.get('title')
				hours = form.cleaned_data.get('hours')
				m = Module.objects.create(title=title, hours=hours, user=user)
				course.modules.add(m)
				course.save()
				return redirect('modules', course_id=course_id)
		else:
			form = NewModuleForm()

	context = {
		'form': form,
	}

	return render(request, 'module/newmodule.html', context)


def CourseModules(request, course_id):
	user = request.user
	course = get_object_or_404(Course, id=course_id)

	page_completions = Completion.objects.filter(user=user, course=course).values_list('page__pk', flat=True)
	quiz_completions = Completion.objects.filter(user=user, course=course).values_list('quiz__pk', flat=True)
	assignment_completions = Completion.objects.filter(user=user, course=course).values_list('assignment__pk', flat=True)

	teacher_mode = False

	if user == course.user:
		teacher_mode = True
	course_modules = []
	onceFalse = False
	for module in course.modules.all():
		module.isCompleted = False
		module.isActive = True
		if onceFalse:
			module.isActive = False
		course_modules.append(module)
		module_pages = checkCompletion(module.pages.all(), page_completions)
		module_quizzes = checkCompletion(module.quizzes.all(), quiz_completions)
		module_completions = checkCompletion(module.assignments.all(), assignment_completions)
		if module_pages and module_quizzes and module_completions:
			module.isCompleted = True
		else:
			onceFalse = True
	courseCompleted = not onceFalse
	context = {
		'teacher_mode': teacher_mode,
		'course': course,
		'page_completions': page_completions,
		'quiz_completions': quiz_completions,
		'assignment_completions': assignment_completions,
		'course_modules': course_modules,
		'courseCompleted': courseCompleted
	}
	return render(request, 'module/modules.html', context)


def checkCompletion(sub_module, completion_list):
	completed = False
	for sub in range(len(sub_module)):
		if sub_module[sub].id in completion_list:
			completed = True
	return completed
