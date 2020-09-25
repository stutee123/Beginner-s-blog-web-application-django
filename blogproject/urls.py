
from django.contrib import admin
from django.urls import path
import blogapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name='index'),
    path('contact/', blogapp.views.new, name='contact'),
    path('blogs/', blogapp.views.blogs, name='blogs'),
    path('details/<int:blog_id>', blogapp.views.details, name='details')
]
