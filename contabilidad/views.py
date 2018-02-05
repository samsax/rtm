from django.shortcuts import render

# Create your views here.
def pago_list(request):
        return render(request, 'contabilidad/pago_list.html', {})