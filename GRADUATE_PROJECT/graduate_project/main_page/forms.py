# from wtforms.validators import DataRequired, Email, EqualTo, Length
# from django import forms
#
#
# class RegistrationForm(forms.ModelForm):
#     first_name = forms.CharField(help_text="First name", validators=[DataRequired()])
#     last_name = forms.CharField(help_text="Last name", validators=[DataRequired()])
#     login = forms.CharField(help_text="Login", validators=[DataRequired()])
#     email = forms.EmailField(help_text="email", validators=[Email])
#     password = forms.CharField(help_text="Password", validators=[DataRequired()])
#     password2 = forms.CharField(help_text="Repeat password", validators=[DataRequired(), EqualTo(password)])