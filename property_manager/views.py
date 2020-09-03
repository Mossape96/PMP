import datetime

from Tools.scripts.gprof2html import header
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv

from django.template.loader import get_template

from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import io
from django.views.generic import View


def index(request):
    title = 'Welcome: This is Home'
    context = {
        'title': title
    }
    return render(request, 'index.html', context)


# Client Account Views


@login_required
def list_clients_accounts(request):
    header = 'Client Accounts'
    form = RegisterSearchForm(request.POST or None)
    queryset = Register.objects.all()
    context = {
        'form': form,
        'header': header,
        'queryset': queryset,
    }

    if request.method == 'POST':
        queryset = Register.objects.filter(client_account__icontains=form['client_account'].value(),
                                           client_name__icontains=form['client_name'].value()
                                           )
        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
        }
    return render(request, 'list_client_accounts.html', context)


@login_required
def add_new_client(request):
    form = RegisterCreateForm(request.POST or None)
    if form.is_valid():
        form.save \
            ()
        messages.success(request, 'Account Successfully Created')
        return redirect('/list_client_accounts')
    context = {
        'form': form,
        'title': 'Add new client'

    }

    return render(request, 'add_new_client.html', context)


@login_required
def client_account_detail(request, pk):
    queryset = Register.objects.get(id=pk)
    context = {
        "queryset": queryset,
    }
    return render(request, "client_account_detail.html", context)


@login_required
def withdraw_account(request, pk):
    queryset = Register.objects.get(id=pk)
    form = WithdrawForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.units_deposited = 0
        instance.units -= instance.units_withdrawn
        instance.withdrawal_authorised_by = str(request.user)

        messages.success(request, "Withdrawal SUCCESSFUL." + '  ' + str(instance.units) + " " + 'units' + '  '
                         + "remain in account" + ' ' + str(
            instance.client_account))
        instance.save()
        return redirect('/client_account_detail/' + str(instance.id))
    # return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": 'title',
        "queryset": queryset,
        "form": form,
        # "username": 'Withdrawal by: ' + str(request.user),
    }
    return render(request, "update_accounts.html", context)


@login_required
def deposit_account(request, pk):
    queryset = Register.objects.get(id=pk)
    form = DepositForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.units_withdrawn = 0
        instance.units += instance.units_deposited
        instance.deposit_authorised_by = str(request.user)
        instance.save()
        messages.success(request, "Deposit SUCCESSFUL. " + str(instance.units) + " " + 'units' + ' '
                                                                                                 "is the new balance for account" + ' ' + str(
            instance.client_account))

        return redirect('/client_account_detail/' + str(instance.id))
    # return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": 'Deposit ' + str(queryset.client_account),
        "instance": queryset,
        "form": form,
        # "username": 'Deposit By: ' + str(request.user),
    }
    return render(request, "update_accounts.html", context)


# Property Views


@login_required
def properties(request):
    template_name = 'properties_register'
    queryset = DeedsRegister.objects.all()
    context = {
        'template_name': template_name,
        'queryset': queryset
    }
    return render(request, 'property_register.html', context)


@login_required
def update_properties(request, pk):
    queryset = Register.objects.get(id=pk)
    form = PropertyUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = PropertyUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Updated Successfully')
            return redirect('/list_client_accounts')

    context = {
        'form': form
    }
    return render(request, 'update_accounts.html', context)


@login_required
def transaction_history(request, client_name=None):
    header = 'TRANSACTIONS'
    queryset = RegisterHistory.objects.all()
    form = RegisterSearchForm(request.POST or None)
    context = {
        'form': form,
        'header': header,
        'queryset': queryset,

    }

    form = RegisterSearchForm(request.POST or None)
    if request.method == 'POST':
        client_name = form['client_name'].value()
        queryset = RegisterHistory.objects.filter(
            client_account__icontains=form['client_account'].value(),
            last_updated__range=[
                form['start_date'].value(),
                form['end_date'].value()]
        )

        if client_name != '':
            queryset = queryset.filter(client_name=client_name)

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Transactions.pdf"'
            writer = csv.writer(response)
            writer.writerow(
                ['PROPERTY NAME',
                 'CLIENT ACCOUNT',
                 'CLIENT NAME',
                 'DEPOSITS',
                 'WITHDRAWALS',
                 'BALANCE',
                 'DEPOSIT MAKER',
                 'WITHDRAWAL MAKER',
                 'LAST UPDATED', ])
            instance = queryset
            for registerhistory in instance:
                writer.writerow(
                    [registerhistory.property,
                     registerhistory.client_account,
                     registerhistory.client_name,
                     registerhistory.units_deposited,
                     registerhistory.units_withdrawn,
                     registerhistory.units,
                     registerhistory.deposit_authorised_by,
                     registerhistory.withdrawal_authorised_by,
                     registerhistory.last_updated, ])
            return response

        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
        }

    return render(request, "transaction_history.html", context)
