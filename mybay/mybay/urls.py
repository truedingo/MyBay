"""mybay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mybay_app import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from mybay import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_view.as_view(), name='home'),
    url(r'^signup/', views.signup_view.as_view(), name='signup'),
    url(r'^items/', views.item_view.as_view(), name='item'),
    url(r'logout/', views.logout_view, name='logout'),
    url(r'^user_delete/', views.user_delete_view.as_view(), name='userdelete'),
    url(r'^user_edit/', views.user_edit_view.as_view(), name='useredit'),
    url(r'^item_edit/', views.item_edit_view.as_view(), name='itemedit'),
    url(r'^main_page/', views.home_page_view.as_view(), name='mainpage'),
    url(r'^my_profile/', views.profile_view.as_view(), name='profile')
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

