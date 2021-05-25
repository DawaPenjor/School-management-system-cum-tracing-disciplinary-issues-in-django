from django.contrib import admin
from .models import StaffDetail, StudentDetail, ClassTeacher, DisciplinaryIssue, CharacterCertificate, Course

admin.site.register(StaffDetail)
admin.site.register(StudentDetail)
admin.site.register(ClassTeacher)
admin.site.register(Course)
admin.site.register(DisciplinaryIssue)
admin.site.register(CharacterCertificate)
