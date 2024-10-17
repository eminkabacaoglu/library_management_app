from django.urls import path
from books.views import BookDetailView,BookListCreateView,AuthorDetailView,AuthorListCreateView

urlpatterns = [
    path('', BookListCreateView.as_view(),),
    path('<int:pk>/', BookDetailView.as_view()),
    path('authors/', AuthorListCreateView.as_view(),),
    path('authors/<int:pk>/', AuthorDetailView.as_view(),),
]