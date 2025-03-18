from django.urls import path
from callboard import views



urlpatterns = [
    #Login url
    path("login/", views.UserLoginAPIView.as_view(), name="user_login"),
    path("register/", views.UserRegisterAPIView().as_view(), name="user_register"),
    path("logout/", views.UserLogoutAPIView.as_view(), name="user_logout"),
    #Advertisment url
    path("advertisment/", views.AdvertismentCreateView.as_view(), name='advertisment-list-create'),
    path("advertisment/my/<int:pk>/", views.AdvertismentDetailView.as_view(), name='advertisment-detail'),
    path("advertisment/all/", views.AdvertismentListView.as_view(), name='all-advertisment-list'),  
    path("advertisment/delete/<int:pk>/", views.AdvertismentDeleteView.as_view(), name='advertisment-delete'), 
    path("advertisment/update/<int:pk>/", views.AdvertismentUpdateView.as_view(), name='advertisment-update'),  
    path("advertisment/book/<int:pk>/", views.BookAdvertismentViews.as_view(), name="book-advertisment"),
    #Items url
    path("items/category", views.CategoryViewSet.as_view(), name='category'),
    path("items/requests/all", views.AllRequestsViews.as_view(), name="all-requests"),
    path('items/approved/<int:pk>/', views.ApproveAdvertismentView.as_view(), name="approved-request"),
    path('items/comments/', views.CommentView.as_view(), name="comments")
]