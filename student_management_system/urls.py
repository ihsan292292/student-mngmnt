from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views,Hod_views,Staff_views,Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.INDEX,name='index'),
    path('base/',views.BASE,name='base'),

    #login
    path('login/',views.LOGIN,name='login'),
    path('dologin',views.dologin,name='dologin'),
    path('dologout',views.dologout,name='logout'),

    #Profilw update
    path('profile',views.PROFILE,name='profile'),
    path('profile/update',views.PROFILE_UPDATE,name='profile_update'),

    #Hod panel url
    path('Hod/Home',Hod_views.HOME,name="hod_home"),

    path('Hod/Student/Add',Hod_views.ADD_STUDENT,name='add_student'),
    path('Hod/Student/View',Hod_views.VIEW_STUDENT,name='view_student'),
    path('Hod/Student/Edit/<str:id>',Hod_views.EDIT_STUDENT,name='edit_student'),
    path('Hod/Student/Update',Hod_views.UPDATE_STUDENT,name='update_student'),
    path('Hod/Student/Delete/<str:admin>',Hod_views.DELETE_STUDENT,name='delete_student'),


    path('Hod/Course/Add',Hod_views.ADD_COURSE,name='add_course'),
    path('Hod/Course/View',Hod_views.VIEW_COURSE,name='view_course'),
    path('Hod/Course/Edit/<str:id>',Hod_views.EDIT_COURSE,name='edit_course'),
    path('Hod/Course/Update',Hod_views.UPDATE_COURSE,name='update_course'),
    path('Hod/Course/Delete/<str:id>',Hod_views.DELETE_COURSE,name='delete_course'),


    path('Hod/Staff/Add',Hod_views.ADD_STAFF,name='add_staff'),
    path('Hod/Staff/View',Hod_views.VIEW_STAFF,name='view_staff'),
    path('Hod/Staff/Edit/<str:id>',Hod_views.EDIT_STAFF,name='edit_staff'),
    path('Hod/Staff/Update',Hod_views.UPDATE_STAFF,name='update_staff'),
    path('Hod/Staff/Delete/<str:id>',Hod_views.DELETE_STAFF,name='delete_staff'),

    
    path('Hod/Subject/Add',Hod_views.ADD_SUBJECT,name='add_subject'),
    path('Hod/Subject/View',Hod_views.VIEW_SUBJECT,name='view_subject'),
    path('Hod/Subject/Edit/<str:id>',Hod_views.EDIT_SUBJECT,name='edit_subject'),
    path('Hod/Subject/Update',Hod_views.UPDATE_SUBJECT,name='update_subject'),
    path('Hod/Subject/Delete/<str:id>',Hod_views.DELETE_SUBJECT,name='delete_subject'),

    path('Hod/Session/Add',Hod_views.ADD_SESSION,name='add_session'),
    path('Hod/Session/View',Hod_views.VIEW_SESSION,name='view_session'),
    path('Hod/Session/Edit/<str:id>',Hod_views.EDIT_SESSION,name='edit_session'),
    path('Hod/Session/Update',Hod_views.UPDATE_SESSION,name='update_session'),
    path('Hod/Session/Delete/<str:id>',Hod_views.DELETE_SESSION,name='delete_session'),

    path('Hod/Staff/Send_Notification',Hod_views.STAFF_SEND_NOTIFICATION,name='staff_send_notification'),
    path('Hod/Staff/Save_Notification',Hod_views.SAVE_STAFF_NOTIFICATION,name='save_staff_notification'),

    path('Hod/Staff/Leave_view',Hod_views.Staff_leave_view,name="staff_leave_view"),
    path('Hod/Staff/Approve_leave/<str:id>',Hod_views.STAFF_APPROVE_LEAVE,name="staff_approve_leave"),
    path('Hod/Staff/Disapprove_leave/<str:id>',Hod_views.STAFF_DISAPPROVE_LEAVE,name="staff_disapprove_leave"),

    path('Hod/Staff/Feedback',Hod_views.STAFF_FEEDBACK,name='staff_feedback_replay'),
    path('Hod/Staff/Feedback/Save',Hod_views.STAFF_FEEDBACK_SAVE,name='staff_feedback_replay_save'),

    path('Hod/Student/send_notification',Hod_views.STUDENT_SEND_NOTIFICATION,name='student_send_notification'),
    path('Hod/Student/save_notification',Hod_views.SAVE_STUDENT_NOTIFICATION,name='save_student_notification'),

    path('Hod/Student/Feedback',Hod_views.STUDENT_FEEDBACK,name='student_feedback_replay'),
    path('Hod/Student/Feedback/Save',Hod_views.STUDENT_FEEDBACK_SAVE,name='student_feedback_replay_save'),

    path('Hod/Student/Leave_view',Hod_views.STUDENT_LEAVE_VIEW,name="student_leave_view"),
    path('Hod/Student/Approve_leave/<str:id>',Hod_views.STUDENT_APPROVE_LEAVE,name="student_approve_leave"),
    path('Hod/Student/Disapprove_leave/<str:id>',Hod_views.STUDENT_DISAPPROVE_LEAVE,name="student_disapprove_leave"),

    path('Hod/Student/View_attendance',Hod_views.VIEW_ATTENDANCE,name="view_attendance"),


    #Staff urls 
    path('Staff/Home',Staff_views.HOME,name='staff_home'),
    path('Staff/Notifications',Staff_views.NOTIFICATION,name='notifications'),
    path('Staff/mark_as_done/<str:status>',Staff_views.STAFF_NOTIFICATION_MARK_AS_DONE,name='staff_notification_mark_as_done'),
    path('Staff/Apply_leave',Staff_views.STAFF_APPLY_LEAVE,name='staff_apply_leave'),
    path('Staff/Apply_leave_save',Staff_views.STAFF_APPLY_LEAVE_SAVE,name='staff_apply_leave_save'),

    path('Staff/Feedback',Staff_views.STAFF_FEEDBACK,name='staff_feedback'), 
    path('Staff/Feedback/Save',Staff_views.STAFF_FEEDBACK_SAVE,name='staff_feedback_save'),

    path('Staff/Take_Attendance',Staff_views.STAFF_TAKE_ATTENDANCE,name='staff_take_attendance'),
    path('Staff/Save_Attendance',Staff_views.STAFF_ATTENDANCE_SAVE,name='staff_attendance_save'),
    path('Staff/View_Attendance',Staff_views.STAFF_VIEW_ATTENDANCE,name='staff_view_attendance'),

    path('Staff/Add/Result',Staff_views.STAFF_ADD_RESULT,name='staff_add_result'),
    path('Staff/Save/Result',Staff_views.STAFF_SAVE_RESULT,name='staff_save_result'),

    #Student urls
    path('Student/Home',Student_views.HOME,name='student_home'),
    path('Student/Notification',Student_views.STUDENT_NOTIFICATION,name='student_notification'),
    path('Student/mark_as_done/<str:status>',Student_views.STUDENT_NOTIFICATION_MARK_AS_DONE,name='student_notification_mark_as_done'),
    
    path('Student/Feedback',Student_views.STUDENT_FEEDBACK,name='student_feedback'),
    path('Student/Feedback/Save',Student_views.STUDENT_FEEDBACK_SAVE,name='student_feedback_save'),

    path('Student/leave',Student_views.STUDENT_LEAVE,name='student_leave'),
    path('Student/Leave/Save',Student_views.STUDENT_LEAVE_SAVE,name='student_leave_save'),
    path('Student/Leave/View',Student_views.STUDENT_VIEW_ATTENDANCE,name='view_student_leave'),

    path('Student/View/Result',Student_views.STUDENT_VIEW_RESULT,name='student_view_result'),

] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)