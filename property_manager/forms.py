from django import forms
from .models import Register, RegisterHistory, DeedsRegister


class RegisterCreateForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['property', 'location', 'trust_deed_number', 'client_name', 'client_account', 'units',
                  'nominal_value_per_unit', 'total_units']

        def clean_property(self):
            property = self.cleaned_data.get('property')
            if not property:
                raise forms.ValidationError('This field is required')
            return property

        def clean_client_name(self):
            client_name = self.cleaned_data.get('client_name')
            if not client_name:
                raise forms.ValidationError('This field is required')
            return client_name

        def clean_client_account(self):
            client_account = self.cleaned_data.get('client_account')
            if not client_account:
                raise forms.ValidationError('This field is required')
            return client_account


class RegisterSearchForm(forms.ModelForm):
    export_to_CSV= forms.BooleanField(required=False)
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)

    class Meta:
        model = Register
        fields = ['client_account', 'client_name', 'start_date', 'end_date']


class PropertyUpdateForm(forms.ModelForm):
    class Meta:
        model = DeedsRegister
        fields = ['property_title', 'trust_deed_no', 'location', 'nominal_value_per_unit', 'total_units']


class WithdrawForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['units_withdrawn']


class DepositForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['units_deposited']


class TransactionSearchForm(forms.ModelForm):
    export_to_PDF = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)

    class Meta:
        model = Register
        fields = ['client_account', 'client_name', 'start_date', 'end_date']


class RegisterHistorySearchForm(forms.ModelForm):
    export_to_PDF = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)

    class Meta:
        model = RegisterHistory
        fields = ['client_name', 'client_account', 'start_date', 'end_date']

