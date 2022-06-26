from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views  # isort:skip

router = DefaultRouter()


router.register('recipes',
                views.RecipeViewSet,
                basename='recipe'
                )
router.register('ingredients',
                views.IngredientViewSet,
                basename='ingredient'
                )
router.register('tags',
                views.TagViewSet,
                basename='tag'
                )


urlpatterns = [
    path('', include(router.urls)),
    path('users/subscriptions/', views.SubscriptionViewSet.as_view()),
    path('users/<int:pk>/subscribe/', views.SubscribeView.as_view())
]
