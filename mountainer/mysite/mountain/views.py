from django.shortcuts import render

def post_list(request):
    return render(request, 'mountain/post_list.html', {})
	
def formulario(request):
    return render(request, 'mountain/formulario.html', {})

def galeria(request):
    return render(request, 'mountain/galeria.html', {})

def contacto(request):
    return render(request, 'mountain/contacto.html', {})