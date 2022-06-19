from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Класс CustomUserAdmin для редактирования
    модели CustomUser в интерфейсе админ-зоны.
    """
    list_dispaly = ('__all__',)
    list_filter = ('email', 'username')
