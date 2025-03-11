from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "title", "first_name", "last_name", "other_names", "gender", "email", "date_of_birth",
                  "nationality")
        field_classes = {"username": UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        input_types = {
            forms.CharField: 'text',
            forms.EmailField: 'email',
            forms.DateField: 'date',
            forms.DateTimeField: 'datetime-local',
            forms.IntegerField: 'number',

        }
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['type'] = input_types.get(field.__class__, 'text')


class DynamicWidget(forms.Widget):

    def render(self, name, value, attrs=None, renderer=None):
        input_types = {
            forms.CharField: 'text',
            forms.EmailField: 'email',
            forms.DateField: 'date',
            forms.DateTimeField: 'datetime-local',
            forms.IntegerField: 'number',

        }
        input_type = input_types.get(self.field.__class__, 'text')
        return f"<input type={input_type} name='{name}' class='form-control'"
