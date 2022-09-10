from manageorder import views
from django.conf.urls import url
urlpatterns = [
	url(r'^index/$',views.HomePageView.as_view()),
	url(r'^addorder/$',views.addorder),
	url(r'^displaybill/$',views.displayBill),
	url(r'^auth/$',views.Auth_User),
	url(r'^logout/$',views.Logout),
	url(r'^Login/$',views.Login),
	url(r'^change_password/$',views.Change_Password),
	url(r'^change_pass/$',views.Change_Pass),
	url(r'^print/$',views.htmlTopdf),

]