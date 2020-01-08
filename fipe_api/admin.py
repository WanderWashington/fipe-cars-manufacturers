from django.contrib import admin
from .models import Marca
from .models import Veiculo
from django.contrib.auth.models import Permission
from django.views import View


class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Marca, UserAdmin)
admin.site.register(Veiculo, UserAdmin)

