from django.forms import *
from django.core.exceptions import ValidationError
from .models import StaffDetail, StudentDetail, ClassTeacher, DisciplinaryIssue, CharacterCertificate, Course
from django import forms

# Staff Registration form


class StaffRegistrationForm(forms.ModelForm):
    class Meta:
        model = StaffDetail
        fields = [
            'Employee_ID', 'name', 'gender', 'date_of_birth', 'CID',
            'category', 'position_title', 'position_level', 'grade', 'appointment_date',
            'joining_date_of_present_school', 'transfered_from', 'Employment_type',
            'nationality', 'subject', 'qualification', 'contact_number', 'email',
            'permanent_address', 'profile_pic'
        ]
        widgets = {
            'Employee_ID': forms.NumberInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Enter your Employee Id'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your name'
                       }),
            'gender': forms.Select(
                attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            'CID': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter CID number'
                       }),
            'category': forms.Select(
                attrs={'class': 'form-control'}),
            'position_title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter Position Title'
                       }),
            'position_level': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your position level'}),
            'grade': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your grade in number'}),
            'appointment_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date',
                       'placeholder': 'Pick your appointment date'
                       }),
            'joining_date_of_present_school': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date',
                       'placeholder': 'When did you joined to this school?'
                       }),
            'transfered_from': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Your previous school'
                       }),
            'Employment_type': forms.Select(
                attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your nationality'
                       }),
            'subject': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your elective subject'
                       }),
            'qualification': forms.Textarea(
                attrs={'rows': 3, 'cols': 80, 'class': 'form-control',
                       'placeholder': 'Enter all your qualification'
                       }),
            'contact_number': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter 8 digit mobile number'
                       }),
            'email': forms.EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': '.....@education.gov.bt'
                       }),
            'permanent_address': forms.Textarea(
                attrs={'rows': 3, 'cols': 80, 'class': 'form-control',
                       'placeholder': 'Enter your permanent address: village, Gewog, Dzongkhag'
                       }),
            'profile_pic': forms.FileInput(
                attrs={'class': 'form-control'})
        }

    def clean_CID(self):
        cid = self.cleaned_data.get('CID')
        if len(cid) != 11:
            raise forms.ValidationError(
                "CID number should be UNIQUE 11 digits.")
        return cid

    def clean_contact_number(self):
        phone = self.cleaned_data.get('contact_number')
        if len(phone) != 8:
            raise forms.ValidationError("Mobile number should have 8 digits.")
        return phone

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "@education.gov.bt" not in email:
            raise forms.ValidationError(
                "We accept only education mail address.")
        return email

# Class teacher registration


class ClassTeacherRegistrationForm(forms.ModelForm):
    class Meta:
        model = ClassTeacher
        fields = [
            'name', 'standard', 'section', 'course'
        ]

        widgets = {
            'name': forms.Select(
                attrs={'class': 'form-control'}),
            'standard': forms.Select(
                attrs={'class': 'form-control'}),
            'section': forms.Select(
                attrs={'class': 'form-control'}),
            'course': forms.Select(
                attrs={'class': 'form-control'}),

        }

# Student Registration


class StdRegistration(forms.ModelForm):
    class Meta:
        model = StudentDetail
        fields = [
            'student_code',
            'name',
            'gender',
            'standard',
            'section',
            'course',
            'date_of_birth',
            'admission_no',
            'date_of_admission',
            'email',
            'CID',
            'class_teacher',
            'previous_school',
            'mobile_number',
            'permanent_address',
            'proctor_master',
            'BoarderOrDayscholar',
            'RegularOrRepeater',
            'profile_pic',
            'father_name',
            'mother_name',
            'fathers_occupation',
            'mothers_occupation',
            'parents_mobile_number'
        ]
        widgets = {
            'student_code': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Enter your Student Code'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your name'
                       }),
            'gender': forms.Select(
                attrs={'class': 'form-control'}),
            'standard': forms.Select(
                attrs={'class': 'form-control'}),
            'section': forms.Select(
                attrs={'class': 'form-control'}),
            'course': forms.Select(
                attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            'admission_no': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your admission number'
                       }),
            'date_of_admission': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date',
                       'placeholder': 'Pick your admission date'
                       }),
            'email': forms.EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': '.....@education.gov.bt'
                       }),
            'CID': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter CID number'
                       }),
            'class_teacher': forms.Select(
                attrs={'class': 'form-control'}),
            'previous_school': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your previous school'
                       }),
            'mobile_number': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter 8 digit mobile number'
                       }),
            'permanent_address': forms.Textarea(
                attrs={'rows': 3, 'cols': 80, 'class': 'form-control',
                       'placeholder': 'Enter your permanent address: village, Gewog, Dzongkhag'
                       }),
            'proctor_master': forms.Select(
                attrs={'class': 'form-control'}),
            'BoarderOrDayscholar': forms.Select(
                attrs={'class': 'form-control'}),
            'RegularOrRepeater': forms.Select(
                attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(
                attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Your father name'
                       }),
            'mother_name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Your mother name'
                       }),
            'father_name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Your father name'
                       }),
            'fathers_occupation': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter father occupation'
                       }),
            'mothers_occupation': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter mother occupation'
                       }),
            'parents_mobile_number': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter 8 digit mobile number'
                       }),
        }

    def clean_student_code(self):
        std_code = self.cleaned_data.get('student_code')
        if std_code == "":
            raise forms.ValidationError("Required Field.")
        return std_code

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == "":
            raise forms.ValidationError("Required Field.")
        return name

    def clean_CID(self):
        cid = self.cleaned_data.get('CID')
        if len(cid) != 11:
            raise forms.ValidationError(
                "CID number should be UNIQUE 11 digits.")
        return cid

    def clean_mobile_number(self):
        phone = self.cleaned_data.get('mobile_number')
        if len(phone) != 8:
            raise forms.ValidationError("Mobile number should have 8 digits.")
        return phone

    def clean_parents_mobile_number(self):
        phone = self.cleaned_data.get('parents_mobile_number')
        if len(phone) != 8:
            raise forms.ValidationError("Mobile number should have 8 digits.")
        return phone

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "@education.gov.bt" not in email:
            raise forms.ValidationError(
                "We accept only education mail address(xyz@education.gov.bt).")
        return email

    def clean_class_teacher(self):
        class_teacher = self.cleaned_data.get("class_teacher")
        if class_teacher == " ":
            raise forms.ValidationError(
                "fields cannot be left blank")
        return class_teacher

# Disciplinary issue Form


class DisciplinaryIssueform(forms.ModelForm):
    class Meta:
        model = DisciplinaryIssue
        fields = [
            'Student',
            'Violation_detail',
            'Violation_date',
            'Warning_decision',
            'Approved_by'
        ]
        widgets = {
            'Student': forms.Select(attrs={'class': 'form-control'}),
            'Violation_detail': forms.Textarea(
                attrs={'rows': 7, 'cols': 80, 'class': 'form-control',
                       'placeholder': 'Write about violation detail.'
                       }),
            'Violation_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date',
                       'placeholder': 'Pick violation date.'
                       }),
            'Warning_decision': forms.Textarea(
                attrs={'rows': 7, 'cols': 80, 'class': 'form-control',
                       'placeholder': 'Write about warning decision.'
                       }),
            'Approved_by': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Who approved warning decision?'
                       })
        }

# Character Certificate Form


class CharacterCertificateForm(forms.ModelForm):
    class Meta:
        model = CharacterCertificate
        fields = [
            'Student',
            'Category',
            'Description',
            'Awarded_on',
            'Awarded_by',
        ]
        widgets = {
            'Student': forms.Select(attrs={'class': 'form-control'}),
            'Category': forms.Select(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(
                attrs={'rows': 7, 'cols': 80, 'class': 'form-control',
                       'placeholder': 'Brief description about the certificate.'
                       }),
            'Awarded_on': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date',
                       'placeholder': 'When was the certificate awarded?.'
                       }),

            'Awarded_by': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Who awarded the certificate?'
                       })
        }

# Add Course


class AddCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course']

        widgets = {
            'course': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Add the course offered in the school.'
                       })
        }
