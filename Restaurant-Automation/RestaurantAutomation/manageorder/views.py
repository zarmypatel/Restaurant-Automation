from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views import generic
from dbconnection.models import *
from django.template.context_processors import *
import pdfkit

#Create your views here.
class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		all_items = MenuItem.objects.all()
		p='pizza'
		b='burger'
		m='maggie'
		d='drinks'
		pizza = list(MenuItem.objects.filter(item_category=p))
		burger = list(MenuItem.objects.filter(item_category=b))
		maggie = list(MenuItem.objects.filter(item_category=m))
		drinks = list(MenuItem.objects.filter(item_category=d))
		
		if request.session.has_key('member_id'):
			return render(request,'home.html',{'items':all_items,'pizza':pizza,'burger':burger,'maggie':maggie,'drinks':drinks})
		else:
			context ={'error_msg' : "Login First",}
			return render(request,'login.html',context)


def addorder(request):
	c={}
	c.update(csrf(request))
	all_items = MenuItem.objects.all()
	all_customers = Customer.objects.all()
	name = request.POST.get('name')
	mob = request.POST.get('mob')
	email = request.POST.get('email')
	

	if request.session.has_key('order_no'):
		print(request.session['order_no'])
		request.session['order_no']=int(request.session['order_no'])+1
	else:
		request.session['order_no']=1
		print(request.session['order_no'])

	order_no=request.session['order_no']

	print(order_no)
	x=1
	for c1 in all_customers:
		if c1.customer_email == email:
			c = c1
			x = 0
	if x==1:
		c=Customer(customer_name=name,customer_mobileNo=mob,customer_email=email)
		c.save()
	print(c)
	for i in all_items:
		if i.item_name in request.POST:
			print("check2")
			item = MenuItem.objects.get(item_id = i.item_id)
			id = i.item_id
			print(id)
			q = request.POST.get(''+str(id))
			o = Order(customer=c,menuitem=item,item_quantity=q,order_no=order_no)
			o.save()
			co=CurrentOrder(order_no=order_no,menu_item=item.item_name,item_quantity=q,customer_id=c.customer_id,order_id=o.order_id)
			co.save()
			print(co)
			
	return HttpResponseRedirect('/manageorder/displaybill/')

def displayBill(request):
	order_no=request.session['order_no']
	curr=CurrentOrder.objects.all()
	
	m=[]
	for co in curr:
		if(co.order_no==order_no):
			item=MenuItem.objects.get(item_name=co.menu_item)
			customer=Customer.objects.get(customer_id=co.customer_id)
			n=co.menu_item
			q=co.item_quantity
			p=item.item_price
			t=int(q)*int(p)
			m.append([n,p,q,t])
	a=0
	for temp in m:
		a+=int(temp[3])
	b=Bill(customer=customer,amount=a)
	b.save()
	print(a)
	return render(request,'bill.html',{'m':m,'customer':customer.customer_name,'amount':a,'bill_no':b.bill_id,'date':b.date_time,'staff':Staff.objects.get(member_id=request.session['member_id']).member_name})



def Login(request):
	return render(request,'login.html',context=None)


def Auth_User(request):
	email=request.POST.get('email')
	password=request.POST.get('password')
	print(email)
	print(password)	
	user_list=Staff.objects.all()

	for user in user_list :
		print(user.member_password)
		print(user.member_email)
		if user.member_email==email and user.member_password==password :
			request.session['member_id']=user.member_id
			return HttpResponseRedirect('../index/')		
		
	context ={'error_msg' : "E-mail or Password is Incorrect",}
	return render(request,'login.html',context)

def Logout(request):
	if request.session.has_key('member_id'):
		del request.session['member_id']
		request.session.modified = True
		context ={'error_msg' : "Logout Successfully",}
		return render(request,'login.html',context)

def Change_Pass(request):
	return render(request,'changePassword.html')


def Change_Password(request):
	if request.session['member_id']:
		cid=request.session['member_id']
		ch=Staff.objects.get(member_id = cid)
		if request.POST.get('old_password')==ch.member_password:
			if request.POST.get('new_password') == request.POST.get('rnew_password'):
				c={}
				c.update(csrf(request))

				
				ch.member_password=request.POST.get('new_password')
				ch.save()
				msg="Password Successfully Changed"

			return render(request,'home.html',{'msg':msg})
	return render(request,'login.html',context)

def htmlTopdf(request):

	with open('../bill.html') as f:
	    pdfkit.from_file(f, 'out.pdf')
