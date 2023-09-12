from django.urls import path,include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from . import views

schema_view = get_schema_view(
    openapi.Info(
        title = "Libary api",
        default_version= '1.0.0',
        description= 'Api documentation of app'
    ),
    public=True
)


urlpatterns = [
    path("",schema_view.with_ui('swagger',cache_timeout=0)),

    path("category/",views.CategoryList.as_view(),name='list-category'),
    path("category/<int:pk>/",views.CategoryView.as_view(),name='view-category'),
    path("category/add/",views.CategoryCreate.as_view(),name='add-category'),
    path("category/update/<int:pk>/",views.CategoryUpdate.as_view(),name='update-category'),
    path("category/delete/<int:pk>/",views.CategoryDestroy.as_view(),name='delete-category'),
    path("category/books/<int:category_id>/",views.BookCategoryList.as_view(),name='category-books'),


    path("book/",views.BookList.as_view(),name='list-book'),
    path("book/<int:pk>/",views.BookView.as_view(),name='view-book'),
    path("book/add/",views.BookCreate.as_view(),name='add-book'),
    path("book/update/<int:pk>/",views.BookUpdate.as_view(),name='update-book'),
    path("book/delete/<int:pk>/",views.BookDestroy.as_view(),name='delete-book'),

    path('account/',include('account.urls'))

]