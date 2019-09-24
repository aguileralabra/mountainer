from django.shortcuts import render

def post_list(request):
    return render(request, 'mountain/post_list.html', {})
	
def galeria(request):
    return render(request, 'mountain/galeria.html', {})
