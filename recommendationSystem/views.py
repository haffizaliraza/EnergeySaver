from django.shortcuts import render
from django.views import View
from .forms import *
from decimal import Decimal
from django.shortcuts import render, redirect
from django.views import View
from .forms import HouseInfoForm, RoomForm
from django.forms import formset_factory
from django.http import HttpResponse


count=0
checked_labels=[]
# Define the chart data
chart_data = {
    450: {'LEDs': (4, 5), 'CFLs': (8, 12), 'Incandescents': 40},
    750: {'LEDs': (6, 8), 'CFLs': (13, 18), 'Incandescents': 60},
    1100: {'LEDs': (9, 13), 'CFLs': (18, 22), 'Incandescents': (75, 100)},
    1600: {'LEDs': (16, 20), 'CFLs': (23, 30), 'Incandescents': 100},
    2600: {'LEDs': (25, 28), 'CFLs': (30, 55), 'Incandescents': 150}
}


class HouseInfoView(View):
    def get(self, request):
        form_class = HouseInfoForm()
        return render(request,'index.html',{'form':form_class})

    def post(self, request):
        global checked_labels
        checked_labels=[]

        form = HouseInfoForm(request.POST)
        if form.is_valid():
            checked_rooms = form.cleaned_data.get('room_choices', [])
            
            checked_labels = [dict(ROOM_CHOICES)[choice] for choice in checked_rooms]
            
            print("Checked Labels:", checked_labels)

        return redirect('Second-form')



class BulbFormView(View):
    def get(self, request):
        global checked_labels
        room_data = [{'name': room_name, 'form': RoomForm(prefix=f'room_{i}')} for i, room_name in enumerate(checked_labels)]
        return render(request, "seconForm.html", {'room_data': room_data})

    def post(self, request):
        room_data = [{'name': room_name, 'form': RoomForm(request.POST, prefix=f'room_{i}')} for i, room_name in enumerate(checked_labels)]

        if all(data['form'].is_valid() for data in room_data):
            recommendations = {}  # Initialize a dictionary for recommendations

            total_cost = 0  # Initialize the total cost to zero

            for data in room_data:
                cleaned_data = data['form'].cleaned_data
                incandescent_wattage = float(cleaned_data.get('incandescent_wattage', 0))
                compact_fluorescent_wattage = float(cleaned_data.get('compact_fluorescent_wattage', 0))
                led_wattage = float(cleaned_data.get('led_wattage', 0))

                # Calculate cost for each bulb type and add to the total cost
                incandescent_cost = (incandescent_wattage * 4 * 365 * 1 / 1000 * 0.30) + 2
                compact_fluorescent_cost = (compact_fluorescent_wattage * 4 * 365 * 1 / 1000 * 0.30) + 0.4
                led_cost = (led_wattage * 4 * 365 * 1 / 1000 * 0.30) + 0.4

                total_cost += incandescent_cost + compact_fluorescent_cost + led_cost

                                # Calculate equivalent LED wattage based on the chart
                equivalent_led = {
                    'Incandescent': '',
                    'CFL': '',
                    'LED': led_wattage  # LED is already in use
                }

                if incandescent_wattage:
                    equivalent_led['Incandescent'] = '4-5 watt LED'

                if compact_fluorescent_wattage:
                    equivalent_led['CFL'] = '6-8 watt LED'

                recommendations[data['name']] = equivalent_led

            # Redirect or return a response as appropriate
            return render(request, "seconForm.html", {'room_data': room_data, 'total_cost': total_cost,'recommendations': recommendations})

        # If any form is invalid, re-render the form with errors
        return render(request, "seconForm.html", {'room_data': room_data})


