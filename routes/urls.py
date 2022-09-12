from django.urls import path
from routes.views import ListObjectsView, DetailObjectsView, SearchResultsView, NeedUpdateView, PostDeleteView, PostCreateView, ProgectLoginView, RegisterUserView, ProgectLogoutView, PageObjectsView

urlpatterns = [
    path('', ListObjectsView.as_view()),
    path('detail/<int:pk>', DetailObjectsView.as_view(), name='detail'),
    path('search/', SearchResultsView.as_view(), name="search_results"),
    path('edit/<int:pk>', NeedUpdateView.as_view(), name = 'edit'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name = 'delete'),
    path('create/', PostCreateView.as_view(), name = 'create'),
    path('login/', ProgectLoginView.as_view(), name = 'login'),
    path('register/', RegisterUserView.as_view(), name = 'register'),
    path('logout/', ProgectLogoutView.as_view(), name = 'logout'),
    path('page/<int:pk>', PageObjectsView.as_view(), name='page'),
]