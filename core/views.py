from pydoc import render_doc


from django.shortcuts import render

def home(request):
    return render(request, 'index.html')