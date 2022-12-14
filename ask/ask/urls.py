"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from qa.views import index, login_user, logout_user, signup, question, ask, answer, popular, new

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/', login_user, name='login_user'),
    url(r'^logout/', logout_user, name='logout_user'),
    url(r'^signup/', signup, name='signup'),
    url(r'^question/(?P<pk>\d+)/', question, name='question'),
    url(r'^answer/', answer, name='answer'),
    url(r'^ask/', ask, name='ask'),
    url(r'^popular/', popular, name='popular'),
    url(r'^new/', new, name='new'),
]
