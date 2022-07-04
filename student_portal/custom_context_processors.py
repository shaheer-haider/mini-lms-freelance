def userGroups(request):
    isStudent = request.user.groups.filter(name='student').exists()
    isInterviewer = request.user.groups.filter(name='interviewer').exists()
    isInstructor = request.user.groups.filter(name='instructor').exists()
    context = {
        "isStudent": isStudent,
        "isInterviewer": isInterviewer,
        "isInstructor": isInstructor,
        }
    return context