from django.urls import path
from school_management_system_app import views, adm_views

urlpatterns = [
    # admin page
    path('adm_home', adm_views.adm_home, name='adm_home'),
    path('add_staff', adm_views.add_staff, name='add_staff'),
    path('add_student', adm_views.add_std, name='add_std'),
    path('add_disciplinary_issue', adm_views.disciplinaryissue,
         name='disciplinaryissue'),
    path('add_character_certificate', adm_views.charactercertificate,
         name='charactercertificate'),

    # Course
    path('add_course', adm_views.add_course, name='add_course'),
    path('all_course', adm_views.all_course, name='all_course'),
    path('all_course/delete/<id>', adm_views.del_course, name='del_course'),


    # Class Teacher
    path('add_class_teacher', adm_views.add_class_teacher,
         name='add_class_teacher'),
    path('class_teacher', adm_views.class_teacher, name='class_teacher'),
    path('class_teacher/delete/<Emp_id>',
         adm_views.delete_class_teacher, name='delete_class_teacher'),


    # export csv
    path('std_export_csv', adm_views.std_export_csv, name='std_export_csv'),
    path('staff_export_csv', adm_views.staff_export_csv, name='staff_export_csv'),

    # Administration
    path('adm/', adm_views.adm, name='adm'),
    path('adm/<str:Emp_id>/', adm_views.adm_detail, name='adm_detail'),
    path('adm/edit/<str:Emp_id>/',
         adm_views.edit_adm_detail, name='edit_adm_detail'),
    path('adm/delete/<str:Emp_id>/',
         adm_views.delete_adm, name='delete_adm'),

    # Teaching Staff
    path('teacher/', adm_views.teacher, name='teacher'),
    path('teacher/<str:Emp_id>/', adm_views.teacher_detail, name='teacher_detail'),
    path('teacher/edit/<str:Emp_id>/',
         adm_views.edit_adm_detail, name='edit_teacher_detail'),
    path('teacher/delete/<str:Emp_id>/',
         adm_views.delete_teacher, name='delete_teacher'),

    # Non Teaching Staff
    path('non_teacher/', adm_views.non_teacher, name='non_teacher'),
    path('non_teacher/<str:Emp_id>/',
         adm_views.non_teacher_detail, name='non_teacher_detail'),
    path('teacher/edit/<str:Emp_id>/',
         adm_views.edit_non_teacher_detail, name='edit_non_teacher_detail'),
    path('non_teacher/delete/<str:Emp_id>/',
         adm_views.delete_non_teacher, name='delete_non_teacher'),

    # Support Staff
    path('support_staff/', adm_views.support_staff, name='support_staff'),
    path('support_staff/<str:Emp_id>/',
         adm_views.support_staff_detail, name='support_staff_detail'),
    path('support_staff/edit/<str:Emp_id>/',
         adm_views.edit_support_staff_detail, name='edit_support_staff_detail'),
    path('support_staff/delete/<str:Emp_id>/',
         adm_views.delete_support_staff, name='delete_support_staff'),

    # Class Seven
    path('seven/', adm_views.seven, name='seven'),
    path('seven/<str:std_code>/', adm_views.std_detail_seven,
         name='std_detail_seven'),
    path('seven/edit/<str:std_code>/',
         adm_views.edit_std_seven, name='edit_std_seven'),
    path('seven/delete/<str:std_code>/',
         adm_views.delete_std_seven, name='delete_std_seven'),

    # Class Eight
    path('eight/', adm_views.eight, name='eight'),
    path('eight/<str:std_code>/', adm_views.std_detail_eight,
         name='std_detail_eight'),
    path('eight/edit/<str:std_code>/',
         adm_views.edit_std_eight, name='edit_std_eight'),
    path('eight/delete/<str:std_code>/',
         adm_views.delete_std_eight, name='delete_std_eight'),

    # Class Nine
    path('nine/', adm_views.nine, name='nine'),
    path('nine/<str:std_code>/', adm_views.std_detail_nine, name='std_detail_nine'),
    path('nine/edit/<str:std_code>/',
         adm_views.edit_std_nine, name='edit_std_nine'),
    path('nine/delete/<str:std_code>/',
         adm_views.delete_std_nine, name='delete_std_nine'),

    # Class Ten
    path('ten/', adm_views.ten, name='ten'),
    path('ten/<str:std_code>/', adm_views.std_detail_ten, name='std_detail_ten'),
    path('ten/edit/<str:std_code>/',
         adm_views.edit_std_ten, name='edit_std_ten'),
    path('ten/delete/<str:std_code>/',
         adm_views.delete_std_ten, name='delete_std_ten'),

    # Class eleven
    path('eleven/', adm_views.eleven, name='eleven'),
    path('eleven/<str:std_code>/', adm_views.std_detail_eleven,
         name='std_detail_eleven'),
    path('eleven/edit/<str:std_code>/',
         adm_views.edit_std_eleven, name='edit_std_eleven'),
    path('eleven/delete/<str:std_code>/',
         adm_views.delete_std_eleven, name='delete_std_eleven'),

    # Class twelve
    path('twelve/', adm_views.twelve, name='twelve'),
    path('twelve/<str:std_code>/', adm_views.std_detail_twelve,
         name='std_detail_twelve'),
    path('twelve/edit/<str:std_code>/',
         adm_views.edit_std_twelve, name='edit_std_twelve'),
    path('twelve/delete/<str:std_code>/',
         adm_views.delete_std_twelve, name='delete_std_twelve'),


]
