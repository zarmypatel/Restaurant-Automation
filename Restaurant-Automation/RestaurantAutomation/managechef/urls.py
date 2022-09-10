from django.conf.urls import url
from managechef import views
urlpatterns = [
	

	url(r'^ChefLogin/$',views.chefLogin),
	url(r'^auth/$',views.Auth_User),
	url(r'^logout/$',views.Logout),
	url(r'^viewOrder/$',views.viewOrder),
	url(r'^change_password/$',views.Change_Password),
	url(r'^change_pass/$',views.Change_Pass),
	url(r'^updateOrder/$',views.order_done),
]