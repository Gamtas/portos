from django import forms
from .models import Equipment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ['type', 'serial_no', 'id']
        # widgets = {
        #     'type': forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}),
        #     'serial_no': forms.TextInput(attrs={'class': 'form-control'})
        # }



class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

    favorite_food = forms.CharField(
        label = "What is your favorite food?",
        max_length = 8,
        required = True,
    )

    favorite_color = forms.CharField(
        label = "What is your favorite color?",
        max_length = 80,
        required = True,
    )

    favorite_number = forms.IntegerField(
        label = "Favorite number",
        required = False,
    )

    notes = forms.CharField(
        label = "Additional notes or feedback",
        required = False,
    )

    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'

        self.helper.add_input(Submit('submit', 'Submit'))