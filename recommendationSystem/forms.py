from django import forms

ROOM_CHOICES = [
    ('Living Room', 'Living Room'),
    ('Bedroom', 'Bedroom'),
    ('Bathroom', 'Bathroom'),
    ('Kitchen', 'Kitchen'),
    ('Dining Room', 'Dining Room'),
    ('Other', 'Other'),
]

LIGHTING_CHOICES = [
    ('Incandescent', 'Incandescent'),
    ('Compact Fluorescent Bulbs', 'Compact Fluorescent Bulbs'),
    ('LED Bulbs', 'LED Bulbs'),
]

class RoomForm(forms.Form):
    incandescent_bulbs = forms.IntegerField(
        label='Number of Incandescent Bulbs',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    incandescent_wattage = forms.DecimalField(
        label='Wattage of each Incandescent Bulb (in watts)',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    compact_fluorescent_bulbs = forms.IntegerField(
        label='Number of Compact Fluorescent Bulbs',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    compact_fluorescent_wattage = forms.DecimalField(
        label='Wattage of each Compact Fluorescent Bulb (in watts)',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    led_bulbs = forms.IntegerField(
        label='Number of LED Bulbs',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    led_wattage = forms.DecimalField(
        label='Wattage of each LED Bulb (in watts)',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

class HouseInfoForm(forms.Form):
    square_feet = forms.DecimalField(
        label='How many square feet is the house?',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    num_rooms = forms.IntegerField(
        label='How many rooms are in the house?',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    room_choices = forms.MultipleChoiceField(
        label='Select rooms in the house:',
        choices=ROOM_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
    )
