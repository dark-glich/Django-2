"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.views.static import serve


from django.urls import path
from login_form.views import SignupView, SigninView
from article.views import ProductList, ArticleDetail

urlpatterns = [
    #sign up
    path('signin/', SignupView, name='signup'),
    #login
    path('', SigninView, name='home'),
    path('login/', SigninView, name='signin'),
    #article list
    path('home/', ProductList, name='list'),
    #article
    path('article/<int:my_id>/', ArticleDetail, name='article'),
    #admin
    path('admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',
        serve, {'document_root':
            settings.MEDIA_ROOT,}),]