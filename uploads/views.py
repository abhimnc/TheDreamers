from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render_to_response
from django.template import RequestContext

from uploads.models import Document
from uploads.forms import DocumentForm


def home(request):
    documents = Document.objects.all()
    return render(request, 'firstpro/templates/index.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })

def list(request):
 # Handle file upload 
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES) 
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save() 
            # Redirect to the document list after POST 
            return HttpResponseRedirect(reverse('paradox.uploads.views.list')) 
        else: 
            form = DocumentForm() # A empty, unbound form 
            # Load documents for the list page 
    documents = Document.objects.all() 
    # Render list page with the documents and the form 
    return render_to_response( 'list.html', {'documents': documents, 'form': form}, context_instance=RequestContext(request) )
