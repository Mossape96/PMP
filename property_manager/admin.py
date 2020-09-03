from django.contrib import admin
from .models import *
from .forms import RegisterCreateForm

admin.site.site_header = 'Property Management Portal'


class RegisterCreateAdmin(admin.ModelAdmin):
    list_display = ['property', 'trust_deed_number', 'client_name', 'client_account', 'units', 'nominal_value_per_unit',
                    'location']
    form = RegisterCreateForm
    list_filter = ['property']
    search_fields = ['property', 'client_name', 'client_account']


admin.site.register(Register, RegisterCreateAdmin)
admin.site.register(DeedsRegister)
