from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from core import models, datatools, forms, filters
from .datatools.index import *


# def get_account_list(request):
#     # поиск по ID
#     user_id = request.GET.get('user_id')
#     if user_id:
#         accounts = models.Account.objects.filter(user_id__exact=user_id)
#     else:
#         accounts = models.Account.objects.all()
#     context = {'accounts': accounts}
#     return render(request=request, template_name='core/account_list.html', context=context)


class AccountList(TitleMixin, ListView):
    model = models.Account
    template_name = 'core/account_list.html'
    context_object_name = 'accounts'
    title = 'Список аккаунтов'

    def get_filters(self):
        return filters.AccountSearch(self.request.GET)

    def get_queryset(self):
        # фильтр с помощью встроенного функционала
        # user = self.request.GET.get('user')
        # school = self.request.GET.get('school')
        # acc = models.Account.objects.all()
        # if user or school:
        #     return acc.filter(user__name__icontains=user, school__name__icontains=school)
        # return acc
        return self.get_filters().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filters()
        # context['form_search'] = forms.AccountSearch(self.request.GET or None)
        return context


class AccountDetail(TitleMixin, DetailView):
    model = models.Account
    template_name = 'core/account_detail.html'
    context_object_name = 'account'
    title = 'Детальный аккаунт'


class AccountCreate(TitleMixin, CreateView):
    model = models.Account
    template_name = 'core/account_create.html'
    form_class = forms.AccountForm
    title = 'Создание аккаунта'
    success_url = reverse_lazy('core:accounts')


class AccountUpdate(TitleMixin, UpdateView):
    model = models.Account
    template_name = 'core/account_update.html'
    form_class = forms.AccountForm
    title = 'Обновление аккаунта'
    success_url = reverse_lazy('core:accounts')


class AccountDelete(TitleMixin, DeleteView):
    model = models.User
    template_name = 'core/account_delete.html'
    fields = "__all__"
    title = 'Удаление пользователя'
    success_url = reverse_lazy('core:accounts')


def get_main_page(request):
    return render(request=request, template_name='core/main.html')

# def get_account_detail(request, pk):
#     account = get_object_or_404(models.Account, pk=pk)
# Велосипед по изъятию значений из queryset, от которого удалось избавиться
#     count_courses = account.course.all().count()
#     course = account.course.all()
#     name_course = ' '
#     for one_course in range(count_courses):
#         name_course = name_course + course[one_course].name + '; '
# Конец велосипеда
#     context = {'account': account, 'courses': name_course}
#     return render(request=request, template_name='core/account_detail.html', context=context)
