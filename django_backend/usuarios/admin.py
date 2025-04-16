from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Perfil

# Registrar el modelo de Perfil
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'edad', 'bio')
    search_fields = ('usuario__username', 'usuario__email')

# Personalizar la visualización de los usuarios
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

# Re-registrar el modelo User
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
