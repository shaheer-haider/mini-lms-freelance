from django.contrib import admin
from assignment.models import Assignment
from completion.models import Completion
from page.models import Page

# Register your models here.


class CompletionAdmin(admin.ModelAdmin):
    list_display = ('user', "course",
                    "completed",
                    )


admin.site.register(Completion, CompletionAdmin)
admin.site.register(Assignment)
admin.site.register(Page)
