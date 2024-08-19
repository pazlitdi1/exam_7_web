from django.urls import path
from .views import HomeView, AboutView, ServicesView, AdvisersView, BlogView, FeaturesView, ClientsView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('advisers/', AdvisersView.as_view(), name='advisers'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('features/', FeaturesView.as_view(), name='features'),
    path('clients/', ClientsView.as_view(), name='clients'),

]