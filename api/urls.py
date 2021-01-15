from django.urls import path
from . import views

urlpatterns = [
   path('', views.apiOverview, name="api-overview"),
   path('review-list/', views.reviewList, name="review-list"),
   path('review-detail/<int:id>/', views.reviewDetail, name="review-detail"),
   path('review-create/', views.reviewCreate, name="review-create"),
   path('review-update/<int:id>/', views.reviewUpdate, name="review-update"),
   path('review-delete/<int:id>/', views.reviewDelete, name="review-delete"),
    path('message-list/', views.messageList, name="message-list"),
     path('message-create/', views.messageCreate, name="message-create"),
]
