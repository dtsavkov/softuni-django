from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect

from .models import Units
from .forms import UnitTypeForm, CreateUnitForm

from accounts.models import ProfileUser
from reviews.models import Review
from reviews.forms import ReviewForm


def has_access_to_modify(current_user, current_object):
    # profile_user = ProfileUser.objects.all().filter(user__pk=current_user.id)[0]  # get instance of ProfileUser
    # if current_object.user == profile_user or current_user.is_superuser:

    if current_user.is_superuser:
        return True
    elif current_user.id == current_object.user.id:
        return True
    return False


class UnitsList(generic.ListView):
    model = Units                           # return all units
    template_name = 'units_list.html'
    context_object_name = 'units'


class UnitsUserList(generic.ListView):
    model = Units                           # return units of current user
    template_name = 'units_list.html'
    context_object_name = 'units'

    def get_queryset(self):
        profile_user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]  # get instance of ProfileUser
        units = Units.objects.all().filter(user=profile_user)
        if units:
            return units
        return []


class UnitCreate(generic.CreateView):
    form_class = CreateUnitForm
    template_name = 'unit_create.html'
    success_url = '/units/'

    def form_valid(self, form):             # provide user on UNIT creation         # form_valid = validate & save form
        # do find Profile User from current user
        user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        # ADD to form instance user the Profile User
        form.instance.user = user
        return super().form_valid(form)     # super() = return CreateView with updated form (add user)


class UnitDetails(generic.DetailView):
    model = Units
    template_name = 'unit_details.html'
    context_object_name = 'unit'

    def get_context_data(self, *, object_list=None, **kwargs):   # give ability to handle REVIEWS
        context = super(UnitDetails, self).get_context_data(**kwargs)
        context['reviews'] = Review.objects.all().filter(unit=self.get_object())   # filtered queryset of reviews for current unit's instance
        context['form'] = ReviewForm()
        # context['form'].fields['author'].initial = self.request.user.id
        print(context)
        owner = context['object'].user
        current_user = self.request.user
        if has_access_to_modify(current_user, owner):
            context['is_modify_user'] = True
            return context
        context['is_modify_user'] = False
        return context


class UnitDelete(generic.DeleteView):
    model = Units
    login_url = 'accounts/login/'

    def get(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        return render(request, 'unit_delete.html', {'unit': self.get_object()})

    def post(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        unit_to_delete = self.get_object()
        unit_to_delete.delete()
        return HttpResponseRedirect('/units/')

