from random import choice

from django.http import HttpResponseNotFound, HttpResponse, Http404
from django.shortcuts import render, redirect


# without render
# def show_departments(request, *args, **kwargs):
#     order_by = request.GET.get('order_by', 'name')
#     body = f'path: {request.path}, args = {args}, kwargs= {kwargs}, order_by: {order_by}'
#     return HttpResponse(body)

# with render function
def show_departments(request, *args, **kwargs):
    context = {
        'method': request.method,
        'order_by': request.GET.get('order_by', 'name'),
    }

    return render(request, 'departments/all.html', context)


def redirect_to_first_department(request):
    possible_order = ['name', 'age', 'id']
    order_by = choice(possible_order)
    # to = f'/departments/?order+by={order_by}'

    return redirect('show departments')


def show_not_found(request):
    # v1
    return HttpResponseNotFound('Slivi za smet is not found')

    # v2
    # status_code = 400
    # return HttpResponse('Error chushki', status=status_code)

    # v3
    # raise Http404('Raise not found')



