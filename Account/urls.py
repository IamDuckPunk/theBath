from django.conf.urls import url, include
from Account import views as account_views
from Account import forms as account_forms

urlpatterns = [

    url(r'(?P<username>\w+)/edit/$',
        account_forms.UserUpdateForm.as_view(), name='edit_profile'),

    # thebath/profiles/DuckPunk/edit
    url(r'(?P<username>\w+)/$',
        account_views.profile, name='profile'),

   



]
