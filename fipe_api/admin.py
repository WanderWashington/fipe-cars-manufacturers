from django.contrib import admin
# from core.models import User
from .models import Marca
from .models import Veiculo
from django.contrib.auth.models import Permission
# from . import forms
#from import_export.admin import ImportExportModelAdmin
from django.views import View


class UserAdmin(admin.ModelAdmin):
    pass

#admin.site.register(AlunoTemp, UserAdmin)
admin.site.register(Marca, UserAdmin)
admin.site.register(Veiculo, UserAdmin)
# admin.site.register(User, UserAdmin)
