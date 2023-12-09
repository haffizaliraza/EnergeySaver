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
    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.initial = 0

    incandescent_bulbs = forms.IntegerField(
        label='Number of Incandescent Bulbs',
        required=False,
    )
    incandescent_wattage = forms.DecimalField(
        label='Wattage of each Incandescent Bulb (in watts)',
        required=False,
    )
    compact_fluorescent_bulbs = forms.IntegerField(
        label='Number of Compact Fluorescent Bulbs',
        required=False,
    )
    compact_fluorescent_wattage = forms.DecimalField(
        label='Wattage of each Compact Fluorescent Bulb (in watts)',
        required=False,
    )
    led_bulbs = forms.IntegerField(
        label='Number of LED Bulbs',
        required=False,
    )
    led_wattage = forms.DecimalField(
        label='Wattage of each LED Bulb (in watts)',
        required=False,
    )

class HouseInfoForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(HouseInfoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.initial = 0

    square_feet = forms.DecimalField(
        label='How many square feet is the house?',
    )
    num_rooms = forms.IntegerField(
        label='How many rooms are in the house?',
    )
    room_choices = forms.MultipleChoiceField(
        label='Select rooms in the house:',
        choices=ROOM_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
    )
