from django.conf.urls import url

from . import views

app_name= 'accounts'
urlpatterns = [
    url(r'^signup/$', views.SignUp.as_view(), name='signup'),
    url(r'^profile/$', views.ProfileView, name='profile'),
    url(r'^profile/(?P<username>[a-zA-Z0-9_]+)$', views.ProfileViewOther, name='profile-other'),
    url(r'^profile/edit-profile/$', views.ProfileEdit, name='profile-edit'),
    url(r'^profile/add-post/$', views.addPost, name='add-post'),
    url(r'^profile/edit-profile/profile-pic-change/$', views.prfilepicchange, name='profile-pic'),
    url(r'^profile/(?P<username>[a-zA-Z0-9]+)$', views.ProfileViewOther, name='profile-other'),
    #url(r'^profile/post/create/$', views.ProfilePostCreat, name='PostCreat'),
    #url(r'^profile/post/(?P<pk>\d+)/update/$', views.ProfilePostUpdate, name='PostUpdate'),
    #url(r'^profile/post/(?P<pk>\d+)/delete/$', views.ProfilePostDelete, name='PostDelete '),
    url(r'^profile/(?P<username>[a-zA-Z0-9_]+)$', views.ProfileViewOther, name='profile-other'),
    url(r'^profile/(?P<username>[a-zA-Z0-9_]+)/profile-pic-change/$', views.prfilepicchange, name='profile-pic')
]
