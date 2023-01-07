from django.shortcuts import render,redirect
from app.models import Staff,Staff_Notification,Staff_leave,Staff_Feedback,Subject,Session_year,Student,Attendance,Attendance_Report,StudentResult
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def HOME(request):
    return render(request,'Staff/home.html')

@login_required(login_url='/')
def NOTIFICATION(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id

        notification = Staff_Notification.objects.filter(staff_id = staff_id)
        
        context = {
            'notification':notification,
        }
    return render(request,'Staff/notification.html',context)

@login_required(login_url='/')
def STAFF_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Staff_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('notifications')

@login_required(login_url='/')
def STAFF_APPLY_LEAVE(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:

        staff_id = i.id  
        staff_leave_history = Staff_leave.objects.filter(staff_id = staff_id)

        context = {
            'staff_leave_history':staff_leave_history
        }
    return render(request,'Staff/apply_leave.html',context)

@login_required(login_url='/')
def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        staff = Staff.objects.get(admin = request.user.id)
        leave = Staff_leave(
            staff_id = staff,
            date = leave_date,
            message = leave_message
        )
        leave.save()
        messages.success(request,"Leave successfully Sent !")
    return redirect('staff_apply_leave')

def STAFF_FEEDBACK(request):

    staff_id = Staff.objects.get(admin = request.user.id)

    feedback_history = Staff_Feedback.objects.filter(staff_id = staff_id)

    context = {
        'feedback_history':feedback_history
    }
    return render(request,'Staff/feedback.html',context)

def STAFF_FEEDBACK_SAVE(request):
    if request.method == 'POST':
        Feedback = request.POST.get('feedback')
        staff = Staff.objects.get(admin = request.user.id)
        feedback = Staff_Feedback(
            staff_id = staff,
            feedback = Feedback,
            feedback_reply = ""
        )
        feedback.save()
    return redirect('staff_feedback')

def STAFF_TAKE_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin = request.user.id)

    subject = Subject.objects.filter(staff = staff_id)
    session_year = Session_year.objects.all()
    action = request.GET.get('action')

    get_subject = None
    get_session = None
    students = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get(id = subject_id)
            get_session  = Session_year.objects.get(id = session_year_id)

            subject = Subject.objects.filter(id = subject_id)
            for i in subject:
                student_id = i.course.id
                students = Student.objects.filter(course_id = student_id)

    context={
        'subject':subject,
        'session_year':session_year,
        'get_subject':get_subject,
        'get_session':get_session,
        'action':action,
        'students':students
    }
    return render(request,'Staff/Take_attendance.html',context)

def STAFF_ATTENDANCE_SAVE(request):
    subject_id = request.POST.get('subject_id')
    session_year_id = request.POST.get('session_year_id')
    attendance_date = request.POST.get('attendance_date')
    student_id = request.POST.getlist('student_id')

    get_subject = Subject.objects.get(id = subject_id)
    get_subject_id = get_subject.id
    get_session_year = Session_year.objects.get(id = session_year_id)

    attendance1 = Attendance(
        subject_id = get_subject_id,
        attendance_date = attendance_date,
        Session_year_id = get_session_year.id
    )
    attendance1.save()
    for i in student_id:
        stud_id = i
        int_stud = int(stud_id)

        p_student = Student.objects.get(id = int_stud)
        attendance_report = Attendance_Report(
            student_id = p_student.id,
            attendance_id = attendance1.id
        )
        attendance_report.save()

    return redirect('staff_take_attendance')

def STAFF_VIEW_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin = request.user.id)
    
    subject = Subject.objects.filter(staff_id = staff_id)
    session_year = Session_year.objects.all()

    action = request.GET.get('action')
    get_subject = None
    get_session_year = None
    attendance_date = None
    attendance_report = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')

            get_subject = Subject.objects.get(id = subject_id)
            get_session_year = Session_year.objects.get(id = session_year_id)
            attendance = Attendance.objects.filter(subject_id = get_subject, attendance_date = attendance_date)
            for i in attendance:
                attendance_id = i.id
                attendance_report = Attendance_Report.objects.filter(attendance_id = attendance_id)

    context = {
        'subject':subject,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'attendance_date':attendance_date,
        'attendance_report':attendance_report
    }
    return render(request,'Staff/view_attendance.html',context)

def STAFF_ADD_RESULT(request):
    staff = Staff.objects.get(admin = request.user.id)
    subjects = Subject.objects.filter(staff = staff)
    session_year = Session_year.objects.all()
    action = request.GET.get('action')
    
    get_subject = None
    get_session = None
    students = None
    if action is not None:
        if request.method=='POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get(id = subject_id)
            get_session = Session_year.objects.get(id = session_year_id)

            subject = Subject.objects.filter(id = subject_id)
            for i in subject:
                student_id = i.course.id
                students = Student.objects.filter(course_id = student_id)


    context = {
        'subjects':subjects,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session':get_session,
        'students':students
    }
    return render(request,'Staff/add_result.html',context)

def STAFF_SAVE_RESULT(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        assignment_mark = request.POST.get('assignment_mark')
        exam_mark = request.POST.get('exam_mark')

        get_student = Student.objects.get(admin = student_id)
        get_subject = Subject.objects.get(id = subject_id)

        check_exists = StudentResult.objects.filter(subject = get_subject, student = get_student).exists()
        if check_exists:
            result = StudentResult.objects.get(subject = get_subject, student = get_student)
            result.assignment_mark = assignment_mark
            result.exam_mark = exam_mark
            result.save()
            messages.success(request,'Result are successfully Updated !')
            return redirect('staff_add_result')
        else:
            result = StudentResult(
                student = get_student,
                subject = get_subject,
                exam_mark = exam_mark,
                assignment_mark = assignment_mark
            )
            result.save()
            messages.success(request,'Result are successfully Added !')
            return redirect('staff_add_result')