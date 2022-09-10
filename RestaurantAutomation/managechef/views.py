from django.shortcuts import render,render_to_response
from dbconnection.models import *
from django.http import HttpResponseRedirect 
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.views import generic


# Create your views here.

def chefLogin(request):
	return render(request,'chefLogin.html',context=None)

def Auth_User(request):
	email=request.POST.get('email')
	password=request.POST.get('password')
	print(email)
	print(password)	
	user_list=Chef.objects.all()

	for user in user_list :
		print(user.chef_password)
		print(user.chef_email)
		if user.chef_email==email and user.chef_password==password :
			request.session['chef_id']=user.chef_id
			return HttpResponseRedirect('../viewOrder')		
		
	context ={'error_msg' : "E-mail or Password is Incorrect",}
	return render(request,'chefLogin.html',context)

def viewOrder(request):
	orders=CurrentOrder.objects.all()
	return render(request, "view_order.html", {'order':orders})



def Logout(request):
	if request.session.has_key('chef_id'):
		del request.session['chef_id']
		request.session.modified = True
		context ={'error_msg' : "Logout Successfully",}
		return render(request,'chefLogin.html',context)

def Change_Pass(request):
	return render(request,'changePassword.html')


def Change_Password(request):
	if request.session['chef_id']:
		cid=request.session['chef_id']
		ch=Chef.objects.get(chef_id = cid)
		if request.POST.get('old_password')==ch.chef_password:
			if request.POST.get('new_password') == request.POST.get('rnew_password'):
				c={}
				c.update(csrf(request))

				
				ch.chef_password=request.POST.get('new_password')
				ch.save()
				msg="Password Successfully Changed"

			return render(request,'index.html',{'msg':msg})
	return render(request,'chefLogin.html',context)

def order_done(request):
	co=CurrentOrder.objects.get(order_id=request.POST.get('order_id'))
	co.delete()
	orders=CurrentOrder.objects.all()
	return render(request, "view_order.html", {'order':orders,'n':range(5)})
