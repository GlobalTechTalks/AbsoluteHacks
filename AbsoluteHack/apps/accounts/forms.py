from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100 , required = True)
    email_id = forms.EmailField(required = True)
    








class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=100,required = True)
    last_name = forms.CharField(max_length=100 , required = True)
    username = forms.CharField(max_length=100 , required = True)
    email_id = forms.EmailField(required = True)
    organisation = forms.CharField(max_length=100 , required = True) 
    DOB = forms.DateField(required = True)
    mobile = forms.CharField(
        required = True,
        label = 'Mobile Number'
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        label='Password'
    )


    # class Meta:
    #     model = User
        
