from django.shortcuts import render
from orders.models import Order
from customers.models import Customer
from customers.views import send_email

from robots.models import Robot
from .forms import OrderForm

def index(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            robot_serial = form.cleaned_data['robot_serial']

            customer, created = Customer.objects.get_or_create(email=email)

            order = Order(customer=customer, robot_serial=robot_serial)
            order.save()
            
            robot = Robot.objects.filter(serial=robot_serial).first()
            if robot:
                send_email(sender=robot, instance=order)
            return render(request, 'orders/index.html')
    else:
        form = OrderForm()

    return render(request, 'orders/index.html', {'form': form})
