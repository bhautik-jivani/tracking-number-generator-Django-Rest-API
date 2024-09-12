from django.urls import path

from number_generator_app import views

urlpatterns = [
    path('next-tracking-number/', views.NextTrackingNumberView.as_view()),
    path('tracking-details/', views.TrackingDetailsView.as_view({'get': 'list'})),
    path('tracking-details/<int:id>/', views.TrackingDetailsView.as_view({'get': 'retrieve'})),
]