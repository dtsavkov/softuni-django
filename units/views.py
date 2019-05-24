from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin       # verify that the user is logged in

from .models import Units, UnitType
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


# ------------------------------------------------------------------------------------
# Units CRUD
# ------------------------------------------------------------------------------------


class UnitCreate(LoginRequiredMixin, generic.CreateView):
    form_class = CreateUnitForm
    template_name = 'unit_create.html'
    success_url = '/units/'

    def form_valid(self, form):             # provide user on UNIT creation         # form_valid = validate & save form
        # do find Profile User from current user
        user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        # ADD to form instance user the Profile User
        form.instance.user = user
        return super().form_valid(form)     # super() = return CreateView with updated form (add user)


class UnitsList(generic.ListView):
    model = Units                           # return all units
    template_name = 'units_list.html'
    context_object_name = 'units'


class UnitsUserList(LoginRequiredMixin, generic.ListView):
    model = Units                           # return units of current user
    template_name = 'units_list.html'
    context_object_name = 'units'

    def get_queryset(self):
        profile_user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]  # get instance of ProfileUser
        units = Units.objects.all().filter(user=profile_user)
        if units:
            return units
        return []


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


class UnitEdit(LoginRequiredMixin, generic.UpdateView):
    model = Units
    form_class = CreateUnitForm
    template_name = 'unit_create.html'
    success_url = '/units/'

    def form_valid(self, form):
        user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)

    def get(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        instance = Units.objects.get(pk=pk)
        form = CreateUnitForm(request.POST or None, instance=instance)
        return render(request, 'unit_create.html', {'form': form})


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


# ------------------------------------------------------------------------------------
# Unit Type CRUD
# ------------------------------------------------------------------------------------

# OK
class UnitTypeCreate(generic.CreateView):
    model = UnitType
    form_class = UnitTypeForm
    template_name = 'unit_type_create.html'
    success_url = '/units/'

    def get(self, request):
        if not request.user.is_superuser:
            return render(request, 'permission_denied.html')
        form = UnitTypeForm
        return render(request, 'unit_type_create.html', {'form': form})


# OK
class UnitTypeList(generic.ListView):
    model = UnitType                           # return all unit types
    template_name = 'unit_type_list.html'
    context_object_name = 'unit_types'


# OK
class UnitTypeEdit(LoginRequiredMixin, generic.UpdateView):
    model = UnitType
    form_class = UnitTypeForm
    template_name = 'unit_type_create.html'
    success_url = '/units/'

    def form_valid(self, form):
        user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)

    def get(self, request, pk):
        if not request.user.is_superuser:
            return render(request, 'permission_denied.html')
        instance = UnitType.objects.get(pk=pk)
        form = UnitTypeForm(request.POST or None, instance=instance)
        return render(request, 'unit_type_create.html', {'form': form})


# OK
class UnitTypeDelete(generic.DeleteView):
    model = UnitType
    login_url = 'accounts/login/'

    def get(self, request, pk):
        if not request.user.is_superuser:
            return render(request, 'permission_denied.html')
        return render(request, 'unit_type_delete.html', {'unit_type': self.get_object()})

    def delete(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, 'permission_denied.html')
        unit_type_id = kwargs["pk"]
        unit_type_to_delete = UnitType.objects.get(pk=unit_type_id)
        unit_type_to_delete.delete()
        return HttpResponseRedirect('/units/')

