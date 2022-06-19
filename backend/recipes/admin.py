from django.contrib import admin

from .models import (FavoriteList, Ingredient, IngredientInRecipe, Recipe,
                     ShoppingCart, Subscription, Tag)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """
    Класс IngredientAdmin для редактирования
    модели Ingredient в  интерфейсе админ-зоны.
    """
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """
    Класс RecipeAdmin для редактирования
    модели Recipe в  интерфейсе админ-зоны.
    """
    list_display = ('author', 'name', 'count_favorite')
    list_filter = ('author', 'name', 'tags')

    def count_favorite(self, obj):
        """
        Метод `count_favorite` для вывода общего
        числа добавления рецепта в избранное.
        """
        return FavoriteList.objects.filter(recipe=obj).count()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Класс TagAdmin для редактирования
    модели Tag в  интерфейсе админ-зоны.
    """
    list_display = ('name', )
    prepopulated_fields = {"slug": ("name", )}


@admin.register(IngredientInRecipe)
class IngredientInRecipeAdmin(admin.ModelAdmin):
    """
    Класс IngredientInRecipeAdmin для редактирования
    модели IngredientInRecipe в интерфейсе админ-зоны.
    """
    list_display = (
        'recipe',
        'ingredient',
        'amount'
    )
    list_display_links = ('recipe',)


@admin.register(FavoriteList)
class FavoriteListAdmin(admin.ModelAdmin):
    """
    Класс FavoriteListAdmin для редактирования
    модели FavoriteList в интерфейсе админ-зоны.
    """
    pass


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """
    Класс ShoppingCartAdmin для редактирования
    модели ShoppingCart в интерфейсе админ-зоны.
    """
    pass


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """
    Класс SubscriptionAdmin для редактирования
    модели Subscription в интерфейсе админ-зоны.
    """
    pass
