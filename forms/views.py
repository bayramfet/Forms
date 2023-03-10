# -------------- Simple View ------------------ #
from django.http import HttpResponse

def view_simple(request):
    return HttpResponse('''
        <h1>Baslik</h1>
        <b>Kalin Yazi</b>
        <p>Paragraf yazisi</p>
    ''')

# -------------- Template View ------------------ #
from django.shortcuts import render

def view_template(request):
    context = {
        'title': 'Bu bir basliktir.',
        'desc': 'Bu bir aciklamadir.',
        'number': 2023,
        'var_list': ['a', 'b', 'c'],
        'var_tupple': (0, 1, 2, 3),
        'var_dict': {
            'key1': 'val1',
            'key2': {
                'key3': 'val3'
            }
        }
    } 
    # return render(request, 'template_name.html', variables_for_templates)
    return render(request, 'view_template.html', context)

# -------------- Template View Form ------------------ #

from .forms import BasicForm
def view_template_form(request):
    form = BasicForm()
    context = {
        'form': form,
        'message': ''
    }

    if request.method == 'POST':
        # POST işlemleri
        context['message'] = 'POST islemi yapildi.'

    return render(request, 'view_template_form.html', context)

# -------------- Template View Form Model ------------------ #
from .forms import StudentForm
def view_template_form_model(request):
    form = StudentForm()
    context = {
        'form': form,
        'message': ''
    }

     if form.is_valid():
        # Create Record to Table:
        student = form.save()
        # Add Image to The Record:
        student.image = request.FILES.get('image')
        student.save()
        # context['message'] = 'Kaydedildi.'
        # messages:
        from django.contrib import messages
        messages.success(request, 'Kaydedildi.')
        # redirect:
        from django.shortcuts import redirect
        return redirect('view_template')
    
    return render(request, 'view_template_form_model.html', context)
