from django.contrib import admin

from .models import (FavoriteList, Ingredient, IngredientInRecipe, Recipe,
                     ShoppingCart, Subscription, Tag)


class IngredientAdmin(admin.ModelAdmin):
    """
    Класс IngredientAdmin для редактирования
    модели Ingredient в  интерфейсе админ-зоны.
    """
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)
    search_fields = ('name__istartswith', 'name__contains')

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(
            IngredientAdmin, self
        ).get_search_results(request, queryset, search_term)
        queryset1 = queryset.filter(name__istartswith=search_term)
        queryset2 = queryset.filter(name__contains=search_term)
        queryset = queryset1.union(queryset2, all=True)
        return queryset, use_distinct


class RecipeAdmin(admin.ModelAdmin):
    """
    Класс RecipeAdmin для редактирования
    модели Recipe в  интерфейсе админ-зоны.
    """
    list_display = ('author', 'name', 'count_favorite')
    list_filter = ('author', 'name', 'tags')
    search_fields = ('name', 'author__username')

    def count_favorite(self, obj):
        """
        Метод `count_favorite` для вывода общего
        числа добавления рецепта в избранное.
        """
        return FavoriteList.objects.filter(recipe=obj).count()


class TagAdmin(admin.ModelAdmin):
    """
    Класс TagAdmin для редактирования
    модели Tag в  интерфейсе админ-зоны.
    """
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name", )}
    search_fields = ('name',)


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
    search_fields = ('recipe__name', 'ingredient__name')


class FavoriteListAdmin(admin.ModelAdmin):
    """
    Класс FavoriteListAdmin для редактирования
    модели FavoriteList в интерфейсе админ-зоны.
    """
    list_display = ('user', 'recipe')
    search_fields = (
        'user__username',
        'user__email',
        'recipe__name'
        )


class ShoppingCartAdmin(admin.ModelAdmin):
    """
    Класс ShoppingCartAdmin для редактирования
    модели ShoppingCart в интерфейсе админ-зоны.
    """
    list_display = ('user', 'recipe')
    search_fields = (
        'user__username',
        'user__email',
        'recipe__name'
        )


class SubscriptionAdmin(admin.ModelAdmin):
    """
    Класс SubscriptionAdmin для редактирования
    модели Subscription в интерфейсе админ-зоны.
    """
    list_display = ('user', 'author')
    search_fields = (
        'user__username',
        'user__email'
        )


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientInRecipe, IngredientInRecipeAdmin)
admin.site.register(FavoriteList, FavoriteListAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
