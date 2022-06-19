from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

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
router.register('users/subscriptions',
                views.SubscribtionViewSet,
                basename='subscription'
                )
router.register(r'users/(?P<user_id>\d+)/subscribe',
                views.SubscribeViewSet,
                basename='user_id'
                )


urlpatterns = [
   path('', include(router.urls)),
]
