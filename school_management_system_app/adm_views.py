from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import StaffDetail, StudentDetail, ClassTeacher, DisciplinaryIssue, CharacterCertificate, Course
from .forms import StaffRegistrationForm, StdRegistration, AddCourse, ClassTeacherRegistrationForm, DisciplinaryIssueform, CharacterCertificateForm
from .filters import StaffFilter, StudentFilter
from django.core.paginator import Paginator
from django.http import HttpResponse
import csv


@login_required
def adm_home(request):
    male_seven = StudentDetail.objects.filter(
        standard=7, gender='Male')
    female_seven = StudentDetail.objects.filter(
        standard=7, gender='Female')
    total_seven = StudentDetail.objects.filter(
        standard=7)

    male_eight = StudentDetail.objects.filter(
        standard=8, gender='Male')
    female_eight = StudentDetail.objects.filter(
        standard=8, gender='Female')
    total_eight = StudentDetail.objects.filter(
        standard=8)

    male_nine = StudentDetail.objects.filter(standard=9, gender='Male')
    female_nine = StudentDetail.objects.filter(
        standard=9, gender='Female')
    total_nine = StudentDetail.objects.filter(
        standard=9)

    male_ten = StudentDetail.objects.filter(standard=10, gender='Male')
    female_ten = StudentDetail.objects.filter(
        standard=10, gender='Female')
    total_ten = StudentDetail.objects.filter(
        standard=10)

    male_eleven = StudentDetail.objects.filter(
        standard=11, gender='Male')
    female_eleven = StudentDetail.objects.filter(
        standard=11, gender='Female')
    total_eleven = StudentDetail.objects.filter(
        standard=11)

    male_twelve = StudentDetail.objects.filter(
        standard=12, gender='Male')
    female_twelve = StudentDetail.objects.filter(
        standard=12, gender='Female')
    total_twelve = StudentDetail.objects.filter(
        standard=12)

    male = StudentDetail.objects.filter(gender='Male')
    female = StudentDetail.objects.filter(gender='Female')
    total = StudentDetail.objects.all()

    # staff-adm
    male_adm = StaffDetail.objects.filter(
        category='Administration', gender='Male')
    female_adm = StaffDetail.objects.filter(
        category='Administration', gender='Female')
    total_adm = StaffDetail.objects.filter(category='Administration')

    # staff_teachers
    male_teacher = StaffDetail.objects.filter(
        category='Teaching Staff', gender='Male')
    female_teacher = StaffDetail.objects.filter(
        category='Teaching Staff', gender='Female')
    total_teacher = StaffDetail.objects.filter(category='Teaching Staff')

    # staff_non_teachers
    male_non_teacher = StaffDetail.objects.filter(
        category='Non Teaching Staff', gender='Male')
    female_non_teacher = StaffDetail.objects.filter(
        category='Non Teaching Staff', gender='Female')
    total_non_teacher = StaffDetail.objects.filter(
        category='Non Teaching Staff')

    # support staff
    male_support_staff = StaffDetail.objects.filter(
        category='Supporting Staff', gender='Male')
    female_support_staff = StaffDetail.objects.filter(
        category='Supporting Staff', gender='Female')
    total_support_staff = StaffDetail.objects.filter(
        category='Supporting Staff')

    # Total Staff
    male_staff = StaffDetail.objects.filter(gender='Male')
    female_staff = StaffDetail.objects.filter(gender='Female')
    total_staff = StaffDetail.objects.all()

    return render(request, 'administrator/adm_home.html',
                  {'male_seven': male_seven, 'female_seven': female_seven, 'total_seven': total_seven,
                   'male_eight': male_eight, 'female_eight': female_eight, 'total_eight': total_eight,
                   'male_nine': male_nine, 'female_nine': female_nine, 'total_nine': total_nine,
                   'male_ten': male_ten, 'female_ten': female_ten, 'total_ten': total_ten,
                   'male_eleven': male_eleven, 'female_eleven': female_eleven, 'total_eleven': total_eleven,
                   'male_twelve': male_twelve, 'female_twelve': female_twelve, 'total_twelve': total_twelve,
                   'male': male, 'female': female, 'total': total,

                   'male_adm': male_adm, 'female_adm': female_adm, 'total_adm': total_adm,
                   'male_teacher': male_teacher, 'female_teacher': female_teacher, 'total_teacher': total_teacher,
                   'male_non_teacher': male_non_teacher, 'female_non_teacher': female_non_teacher, 'total_non_teacher': total_non_teacher,
                   'male_support_staff': male_support_staff, 'female_support_staff': female_support_staff, 'total_support_staff': total_support_staff,
                   'male_staff': male_staff, 'female_staff': female_staff, 'total_staff': total_staff,
                   })

# Add class teacher
@login_required
def add_class_teacher(request):
    if request.method == 'POST':
        form = ClassTeacherRegistrationForm(request.POST or None, request.FILES)
        if form.is_valid():
            add_teacher = form.save(commit=False)
            add_teacher.user = request.user
            form.save()
            messages.success(request, 'Class Teacher Registered Successfully!')
            return render(request, 'administrator/add_class_teacher.html', {'form':form})
        else:
            messages.error(request,
                           'Could not add the Class Teacher.Try Again!.')
            return render(request, 'administrator/add_class_teacher.html', {'form': form})
    else:
        form = ClassTeacherRegistrationForm()
    return render(request, 'administrator/add_class_teacher.html', {'form':form})

# Add course
@login_required
def add_course(request):
    if request.method == 'POST':
        form = AddCourse(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course added successfully!')
            return render(request, 'administrator/add_course.html', {'form':form})
        else:
            messages.error(request, 'Couldnot add the course. Try again!')
            return render(request, 'administrator/add_course.html', {'form':form})
    else:
        form = AddCourse()
    return render(request, 'administrator/add_course.html', {'form':form})

# All course
@login_required
def all_course(request):
    all_course = Course.objects.all()
    return render(request, 'administrator/all_course.html', {'all_course':all_course})

# Delete Course
@login_required
def del_course(request, id):
    del_course = get_object_or_404(Course, pk=id)
    del_course.delete()
    return redirect('all_course')


#Class Teacher Detail
@login_required
def class_teacher(request):
    class_teacher = ClassTeacher.objects.all()
    return render(request, 'administrator/class_teacher.html', {'class_teacher':class_teacher})

# Delete class Teacher
@login_required
def delete_class_teacher(request, Emp_id):
    class_teacher = get_object_or_404(ClassTeacher, pk=Emp_id)
    class_teacher.delete()
    return redirect('class_teacher')


# Add Staff
@login_required
def add_staff(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST or None, request.FILES)
        if form.is_valid():
            addstaff = form.save(commit=False)
            addstaff.user = request.user
            form.save()
            messages.success(request, 'Staff added successfully!')
            return render(request, 'administrator/add_staff.html', {'form': form})
        else:
            messages.error(request,
                           'Could not add the staff. Please check the errors below.')
            return render(request, 'administrator/add_staff.html', {'form': form})

    else:
        form = StaffRegistrationForm()
    return render(request, 'administrator/add_staff.html', {'form': form})


# Disciplinary Issue update
@login_required
def disciplinaryissue(request):
    if request.method == 'POST':
        form = DisciplinaryIssueform(request.POST or None)
        if form.is_valid():
            addstd = form.save(commit=False)
            addstd.user = request.user
            form.save()
            messages.success(request, 'Disciplinary issue added successfully!')
            return render(request, 'administrator/disciplinaryissue.html', {'form': form})
        else:
            messages.error(request,
                           'Error: Could not add disciplinary issue!')
            return render(request, 'administrator/disciplinaryissue.html', {'form': form})
    else:
        form = DisciplinaryIssueform()
    return render(request, 'administrator/disciplinaryissue.html', {'form': form})

# Character certificate update
@login_required
def charactercertificate(request):
    if request.method == 'POST':
        form = CharacterCertificateForm(request.POST or None)
        if form.is_valid():
            addstd = form.save(commit=False)
            addstd.user = request.user
            form.save()
            messages.success(
                request, 'Character certificate added successfully!')
            return render(request, 'administrator/charactercertificate.html', {'form': form})
        else:
            messages.error(request,
                           'Error: Could not add Character certificate of the student!')
            return render(request, 'administrator/charactercertificate.html', {'form': form})
    else:
        form = CharacterCertificateForm()
    return render(request, 'administrator/charactercertificate.html', {'form': form})


# Administration home page
@login_required
def adm(request):
    male = StaffDetail.objects.filter(category='Administration', gender='Male')
    female = StaffDetail.objects.filter(
        category='Administration', gender='Female')
    total = StaffDetail.objects.filter(category='Administration')
    all_field = StaffDetail.objects.filter(
        category='Administration').order_by('name')
    myFilter = StaffFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 10)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'administrator/administration.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total

                   })

# View Administration
@login_required
def adm_detail(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    return render(request, 'administrator/staff_detail.html', {'staff': staff})

# Edit administration detail
@login_required
def edit_adm_detail(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    if request.method == 'POST':
        form = StaffRegistrationForm(
            request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff detail updated successfully!')
            return render(request, 'administrator/edit_staff_detail.html', {'staff': staff, 'form': form})
        else:
            messages.error(request, 'Staff detail update failed. Try again!')
            return render(request, 'administrator/edit_staff_detail.html', {'staff': staff, 'form': form})
    else:
        form = StaffRegistrationForm(instance=staff)
        return render(request, 'administrator/edit_staff_detail.html', {'staff': staff, 'form': form})

# Delete administration Detail
@login_required
def delete_adm(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    staff.delete()
    return redirect('adm')

# Teacher home page
@login_required
def teacher(request):
    male = StaffDetail.objects.filter(category='Teaching Staff', gender='Male')
    female = StaffDetail.objects.filter(
        category='Teaching Staff', gender='Female')
    total = StaffDetail.objects.filter(category='Teaching Staff')
    all_field = StaffDetail.objects.filter(
        category='Teaching Staff').order_by('name')
    myFilter = StaffFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 10)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'administrator/teacher.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total
                   })
# View Teacher
@login_required
def teacher_detail(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    return render(request, 'administrator/staff_detail.html', {'staff': staff})

# Edit Teacher detail
@login_required
def edit_teacher_detail(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    if request.method == 'POST':
        form = StaffRegistrationForm(
            request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff detail updated successfully!')
            return render(request, 'administrator/edit_staff_detail.html', {'staff': staff, 'form': form})
        else:
            messages.error(request, 'Staff detail update failed. Try again!')
            return render(request, 'administrator/edit_staff_detail.html', {'staff': staff, 'form': form})
    else:
        form = StaffRegistrationForm(instance=staff)
        return render(request, 'administrator/edit_staff_detail.html', {'staff': staff, 'form': form})

# Delete Teacher Detail
@login_required
def delete_teacher(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    staff.delete()
    return redirect('teacher')


# Non Teacher home page
@login_required
def non_teacher(request):
    male = StaffDetail.objects.filter(
        category='Non Teaching Staff', gender='Male')
    female = StaffDetail.objects.filter(
        category='Non Teaching Staff', gender='Female')
    total = StaffDetail.objects.filter(category='Non Teaching Staff')
    all_field = StaffDetail.objects.filter(
        category='Non Teaching Staff').order_by('name')
    myFilter = StaffFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 10)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'administrator/non_teacher.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total
                   })
# View Non Teacher
@login_required
def non_teacher_detail(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    return render(request, 'administrator/staff_detail.html', {'staff': staff})

# Edit Non Teacher detail
@login_required
def edit_non_teacher_detail(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    if request.method == 'POST':
        form = StaffRegistrationForm(
            request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff detail updated successfully!')
            return render(request, 'administrator/edit_staff_detail.html', {'staff': staff, 'form': form})
        else:
            messages.error(request, 'Staff detail update failed. Try again!')
            return render(request, 'administrator/edit_staff_detail.html', {'staff': staff, 'form': form})
    else:
        form = StaffRegistrationForm(instance=staff)
        return render(request, 'administrator/edit_staff_detail.html', {'staff': staff, 'form': form})

# Delete Non Teacher Detail
@login_required
def delete_non_teacher(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    staff.delete()
    return redirect('non_teacher')

# Support Staff home page
@login_required
def support_staff(request):
    male = StaffDetail.objects.filter(
        category='Supporting Staff', gender='Male')
    female = StaffDetail.objects.filter(
        category='Supporting Staff', gender='Female')
    total = StaffDetail.objects.filter(category='Supporting Staff')
    all_field = StaffDetail.objects.filter(
        category='Supporting Staff').order_by('name')
    myFilter = StaffFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 10)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'administrator/support_staff.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total
                   })
# View Teacher
@login_required
def support_staff_detail(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    return render(request, 'administrator/staff_detail.html', {'staff': staff})

# Edit Teacher detail
@login_required
def edit_support_staff_detail(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    if request.method == 'POST':
        form = StaffRegistrationForm(
            request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff detail updated successfully!')
            return render(request, 'administrator/edit_staff_detail.html', {'staff': staff, 'form': form})
        else:
            messages.error(request, 'Staff detail update failed. Try again!')
            return render(request, 'administrator/edit_staff_detail.html', {'staff': staff, 'form': form})
    else:
        form = StaffRegistrationForm(instance=staff)
        return render(request, 'administrator/edit_staff_detail.html', {'staff': staff, 'form': form})

# Delete Teacher Detail
@login_required
def delete_support_staff(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    staff.delete()
    return redirect('support_staff')

# ***********************************************************************
# Student management

# Add Student
@login_required
def add_std(request):
    if request.method == 'POST':
        form = StdRegistration(request.POST or None, request.FILES)
        if form.is_valid():
            addstd = form.save(commit=False)
            addstd.user = request.user
            form.save()
            messages.success(request, 'Student added successfully!')
            return render(request, 'administrator/add_std.html', {'form': form})
        else:
            messages.error(request,
                           'Could not add the student. Please check the errors below.')
            return render(request, 'administrator/add_std.html', {'form': form})

    else:
        form = StdRegistration()
    return render(request, 'administrator/add_std.html', {'form': form})

# class seven home page
@login_required
def seven(request):
    male = StudentDetail.objects.filter(standard=7, gender='Male')
    female = StudentDetail.objects.filter(standard=7, gender='Female')
    total = StudentDetail.objects.filter(standard=7)
    all_field = StudentDetail.objects.filter(
        standard=7).order_by('name')
    myFilter = StudentFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 15)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'administrator/seven.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total
                   })

# class seven student detail
@login_required
def std_detail_seven(request, std_code):
    std = get_object_or_404(StudentDetail, pk=std_code)
    disissue = DisciplinaryIssue.objects.filter(Student=std)
    character_certificate = CharacterCertificate.objects.filter(Student=std)
    return render(request, 'administrator/std_detail.html', {
        'std': std,
        'disissue': disissue,
        'character_certificate': character_certificate,
    })

# edit class seven student detail
@login_required
def edit_std_seven(request, std_code):
    teacher = ClassTeacher.objects.all()
    std = get_object_or_404(StudentDetail, pk=std_code)
    if request.method == 'POST':
        form = StdRegistration(request.POST, request.FILES, instance=std)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student detail updated successfully!')
            return render(request, 'administrator/edit_std.html', {'std': std, 'form': form, 'teacher': teacher})
        else:
            messages.error(request, 'Student detail update failed. Try again!')
            return render(request, 'administrator/edit_std.html', {'std': std, 'form': form, 'teacher': teacher})
    else:
        form = StdRegistration(instance=std)
        return render(request, 'administrator/edit_std.html', {'std': std, 'form': form, 'teacher': teacher})

# delete class seven student detail
@login_required
def delete_std_seven(request, std_code):
    std = get_object_or_404(StudentDetail, pk=std_code)
    std.delete()
    return redirect('seven')


# class eight home page
@login_required
def eight(request):
    male = StudentDetail.objects.filter(standard=8, gender='Male')
    female = StudentDetail.objects.filter(standard=8, gender='Female')
    total = StudentDetail.objects.filter(standard=8)
    all_field = StudentDetail.objects.filter(
        standard=8).order_by('name')
    myFilter = StudentFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 15)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'administrator/eight.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total
                   })
# class eight student detail
@login_required
def std_detail_eight(request, std_code):
    std = get_object_or_404(StudentDetail, pk=std_code)
    disissue = DisciplinaryIssue.objects.filter(Student=std)
    character_certificate = CharacterCertificate.objects.filter(Student=std)
    return render(request, 'administrator/std_detail.html', {
        'std': std,
        'disissue': disissue,
        'character_certificate': character_certificate,
    })

# edit class eight student detail
@login_required
def edit_std_eight(request, std_code):
    teacher = ClassTeacher.objects.all()
    std = get_object_or_404(StudentDetail, pk=std_code)
    if request.method == 'POST':
        form = StdRegistration(request.POST, request.FILES, instance=std)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student detail updated successfully!')
            return render(request, 'administrator/edit_std.html', {'std': std, 'form': form, 'teacher': teacher})
        else:
            messages.error(request, 'Student detail update failed. Try again!')
            return render(request, 'administrator/edit_std.html', {'std': std, 'form': form, 'teacher': teacher})
    else:
        form = StdRegistration(instance=std)
        return render(request, 'administrator/edit_std.html', {'std': std, 'form': form, 'teacher': teacher})

# delete class eight student detail
@login_required
def delete_std_eight(request, std_code):
    std = get_object_or_404(StudentDetail, pk=std_code)
    std.delete()
    return redirect('eight')

# class nine home page
@login_required
def nine(request):
    male = StudentDetail.objects.filter(standard=9, gender='Male')
    female = StudentDetail.objects.filter(standard=9, gender='Female')
    total = StudentDetail.objects.filter(standard=9)
    all_field = StudentDetail.objects.filter(
        standard=9).order_by('name')
    myFilter = StudentFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 15)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'administrator/nine.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total
                   })

# class nine student detail
@login_required
def std_detail_nine(request, std_code):
    std = get_object_or_404(StudentDetail, pk=std_code)
    disissue = DisciplinaryIssue.objects.filter(Student=std)
    character_certificate = CharacterCertificate.objects.filter(Student=std)
    return render(request, 'administrator/std_detail.html', {
        'std': std,
        'disissue': disissue,
        'character_certificate': character_certificate,
    })

# edit class nine student detail
@login_required
def edit_std_nine(request, std_code):
    teacher = ClassTeacher.objects.all()
    std = get_object_or_404(StudentDetail, pk=std_code)
    if request.method == 'POST':
        form = StdRegistration(request.POST, request.FILES, instance=std)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student detail updated successfully!')
            return render(request, 'administrator/edit_std.html', {'std': std, 'form': form, 'teacher': teacher})
        else:
            messages.error(request, 'Student detail update failed. Try again!')
            return render(request, 'administrator/edit_std.html', {'std': std, 'form': form, 'teacher': teacher})
    else:
        form = StdRegistration(instance=std)
        return render(request, 'administrator/edit_std.html', {'std': std, 'form': form, 'teacher': teacher})

# delete class nine student detail
@login_required
def delete_std_nine(request, std_code):
    std = get_object_or_404(StudentDetail, pk=std_code)
    std.delete()
    return redirect('nine')

# class ten home page
@login_required
def ten(request):
    male = StudentDetail.objects.filter(standard=10, gender='Male')
    female = StudentDetail.objects.filter(standard=10, gender='Female')
    total = StudentDetail.objects.filter(standard=10)
    all_field = StudentDetail.objects.filter(
        standard=10).order_by('name')
    myFilter = StudentFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 15)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'administrator/ten.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total
                   })

# class ten student detail
@login_required
def std_detail_ten(request, std_code):
    std = get_object_or_404(StudentDetail, pk=std_code)
    disissue = DisciplinaryIssue.objects.filter(Student=std)
    character_certificate = CharacterCertificate.objects.filter(Student=std)
    return render(request, 'administrator/std_detail.html', {
        'std': std,
        'disissue': disissue,
        'character_certificate': character_certificate,
    })

# edit class ten student detail
@login_required
def edit_std_ten(request, std_code):
    teacher = ClassTeacher.objects.all()
    std = get_object_or_404(StudentDetail, pk=std_code)
    if request.method == 'POST':
        form = StdRegistration(request.POST, request.FILES, instance=std)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student detail updated successfully!')
            return render(request, 'administrator/edit_std.html', {'std': std, 'form': form, 'teacher': teacher})
        else:
            messages.error(request, 'Student detail update failed. Try again!')
            return render(request, 'administrator/edit_std.html', {'std': std, 'form': form, 'teacher': teacher})
    else:
        form = StdRegistration(instance=std)
        return render(request, 'administrator/edit_std.html', {'std': std, 'form': form, 'teacher': teacher})

# delete class ten student detail
@login_required
def delete_std_ten(request, std_code):
    std = get_object_or_404(StudentDetail, pk=std_code)
    std.delete()
    return redirect('ten')

# class eleven home page
@login_required
def eleven(request):
    male = StudentDetail.objects.filter(standard=11, gender='Male')
    female = StudentDetail.objects.filter(standard=11, gender='Female')
    total = StudentDetail.objects.filter(standard=11)
    all_field = StudentDetail.objects.filter(
        standard=11).order_by('name')
    myFilter = StudentFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 15)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'administrator/eleven.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total
                   })

# class eleven student detail
@login_required
def std_detail_eleven(request, std_code):
    std = get_object_or_404(StudentDetail, pk=std_code)
    disissue = DisciplinaryIssue.objects.filter(Student=std)
    character_certificate = CharacterCertificate.objects.filter(Student=std)
    return render(request, 'administrator/std_detail.html', {
        'std': std,
        'disissue': disissue,
        'character_certificate': character_certificate,
    })

# edit class eleven student detail
@login_required
def edit_std_eleven(request, std_code):
    std = get_object_or_404(StudentDetail, pk=std_code)
    teacher = ClassTeacher.objects.all()
    if request.method == 'POST':
        form = StdRegistration(request.POST, request.FILES, instance=std)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student detail updated successfully!')
            return render(request, 'administrator/edit_std.html', {'std': std, 'form': form, 'teacher': teacher})
        else:
            messages.error(request, 'Student detail update failed. Try again!')
            return render(request, 'administrator/edit_std.html', {'std': std, 'form': form, 'teacher': teacher})
    else:
        form = StdRegistration(instance=std)
        return render(request, 'administrator/edit_std.html', {'std': std, 'form': form, 'teacher': teacher})

# delete class eleven student detail
@login_required
def delete_std_eleven(request, std_code):
    std = get_object_or_404(StudentDetail, pk=std_code)
    std.delete()
    return redirect('eleven')

# class twelve home page
@login_required
def twelve(request):
    male = StudentDetail.objects.filter(standard=12, gender='Male')
    female = StudentDetail.objects.filter(standard=12, gender='Female')
    total = StudentDetail.objects.filter(standard=12)
    all_field = StudentDetail.objects.filter(
        standard=12).order_by('name')
    myFilter = StudentFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 15)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'administrator/twelve.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total
                   })

# class twelve student detail
@login_required
def std_detail_twelve(request, std_code):
    std = get_object_or_404(StudentDetail, pk=std_code)
    disissue = DisciplinaryIssue.objects.filter(Student=std)
    character_certificate = CharacterCertificate.objects.filter(Student=std)
    return render(request, 'administrator/std_detail.html', {
        'std': std,
        'disissue': disissue,
        'character_certificate': character_certificate,
    })

# edit class twelve student detail
@login_required
def edit_std_twelve(request, std_code):
    teacher = ClassTeacher.objects.all()
    std = get_object_or_404(StudentDetail, pk=std_code)
    if request.method == 'POST':
        form = StdRegistration(request.POST, request.FILES, instance=std)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student detail updated successfully!')
            return render(request, 'administrator/edit_std.html', {'std': std, 'form': form, 'teacher': teacher})
        else:
            messages.error(request, 'Student detail update failed. Try again!')
            return render(request, 'administrator/edit_std.html', {'std': std, 'form': form, 'teacher': teacher})
    else:
        form = StdRegistration(instance=std)
        return render(request, 'administrator/edit_std.html', {'std': std, 'form': form, 'teacher': teacher})

# delete class twelve student detail
@login_required
def delete_std_twelve(request, std_code):
    std = get_object_or_404(StudentDetail, pk=std_code)
    std.delete()
    return redirect('twelve')

# Exporting to csv

# Student Detail Download
@login_required
def std_export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="student_data.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'STUDENT CODE', 'NAME', 'GENDER', 'STANDARD', 'SECTION', 'COURSE', 'DATE OF BIRTH',
        'ADMISSION NUMBER', 'DATE OF ADMISSION', 'EMAIL', 'CID', 'CLASS TEACHER', 'PREVIOUS SCHOOL',
        'MOBILE NUMBER', 'PERMANENT ADDRESS', 'BOARDER/DAYSCHOLAR', 'REGULAR/REPEATER',
        'FATHER NAME', 'MOTHER NAME', 'FATHER OCCUPATION', 'MOTHER OCCUPATION', 'PARENTS MOBILE NUMBER'
    ])
    std = StudentDetail.objects.all().order_by('standard')
    for std in std:
        writer.writerow([
            std.student_code, std.name, std.gender, std.standard, std.section, std.course,
            std.date_of_birth, std.admission_no, std.date_of_admission, std.email,
            std.CID, std.class_teacher, std.previous_school, std.mobile_number,
            std.permanent_address, std.BoarderOrDayscholar, std.RegularOrRepeater,
            std.father_name, std.mother_name, std.fathers_occupation, std.mothers_occupation,
            std.parents_mobile_number])
    return response

# Download Staff Detail
@login_required
def staff_export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="staff_data.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'EMPLOYEE ID', 'NAME', 'GENDER', 'DATE OF BIRTH', 'CID',
        'CATEGORY', 'POSITION TITLE', 'POSITION LEVEL', 'GRADE', 'APPOINTMENT DATE',
        'JOINING DATE TO SCHOOL', 'TRANSFERED FROM', 'EMPLOYEMENT TYPE',
        'NATIONALITY', 'SUBJECT', 'QUALIFICATION', 'CONTACT NUMBER', 'EMAIL',
        'PERMANENT ADDRESS'
    ])
    staff = StaffDetail.objects.all().order_by('category')
    for staff in staff:
        writer.writerow([
            staff.Employee_ID, staff.name, staff.gender, staff.date_of_birth, staff.CID,
            staff.category, staff.position_title, staff.position_level, staff.grade,
            staff.appointment_date,
            staff.joining_date_of_present_school, staff.transfered_from, staff.Employment_type,
            staff.nationality, staff.subject, staff.qualification, staff.contact_number, staff.email,
            staff.permanent_address])
    return response
