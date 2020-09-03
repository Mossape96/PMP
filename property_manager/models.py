from django.db import models


class Register(models.Model):
    property = models.CharField(max_length=50, blank=True, null=True)
    client = models.CharField(max_length=50, blank=True, null=True)
    client_account = models.CharField(max_length=50, blank=True, null=True, unique=False)
    client_name = models.CharField(max_length=50, blank=True, null=True)
    client_email = models.EmailField()
    client_address = models.CharField(max_length=50, blank=True)
    client_contact = models.CharField(max_length=50, blank=True, null=True)
    units = models.IntegerField(default='0', blank=True, null=True)
    units_deposited = models.IntegerField(default='0', blank=True, null=True)
    deposit_authorised_by = models.CharField(max_length=50, blank=True, null=True)
    units_withdrawn = models.IntegerField(default='0', blank=True, null=True)
    withdrawal_authorised_by = models.CharField(max_length=50, blank=True, null=True)
    transfer_to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    creation_date = models.DateTimeField(max_length=50, blank=True, null=True)
    trust_deed_number = models.CharField(max_length=50, blank=False, null=False)
    location = models.CharField( max_length=50, blank=True)
    nominal_value_per_unit = models.DecimalField(default=0, max_digits=12, decimal_places=2, null=True)
    total_units = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name_plural = "Account Manager"

    def __str__(self):
        return '{}'' - ''{}'.format(self.client_name, self.client_account)


class RegisterHistory(models.Model):
    property = models.CharField(max_length=50, blank=True, null=True)
    client = models.CharField(max_length=50, blank=True, null=True)
    client_account = models.CharField(max_length=50, blank=True, null=True, unique=True)
    client_name = models.CharField(max_length=50, blank=True, null=True)
    client_email = models.EmailField(null=True)
    client_address = models.CharField(max_length=50, blank=True, null=True)
    client_contact = models.CharField(max_length=50, blank=True, null=True)
    units = models.IntegerField(default='0', blank=True, null=True)
    units_deposited = models.IntegerField(default='0', blank=True, null=True)
    deposit_authorised_by = models.CharField(max_length=50, blank=True, null=True)
    units_withdrawn = models.IntegerField(default='0', blank=True, null=True)
    withdrawal_authorised_by = models.CharField(max_length=50, blank=True, null=True)
    transfer_to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    creation_date = models.DateTimeField(max_length=50, blank=True, null=True)
    trust_deed_number = models.CharField(max_length=50, blank=False, null=True)
    location = models.CharField(default=0, max_length=50, blank=True)
    nominal_value_per_unit = models.DecimalField(default=0, max_digits=12, decimal_places=2, null=True)
    total_units = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)


class DeedsRegister(models.Model):
    property_title = models.CharField(max_length=200)
    trust_deed_no = models.CharField(max_length=50, blank=False, null=True)
    location = models.CharField(default=0, max_length=200)
    nominal_value_per_unit = models.DecimalField(default=0, max_digits=12, decimal_places=2, null=True)
    total_units = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Deeds Register"

    def __str__(self):
        return '{}'' - ''{}'.format(self.property_title, self.trust_deed_no)
