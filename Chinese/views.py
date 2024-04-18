from django.shortcuts import render, redirect
from django.http import HttpResponse
from Chinese.models import Food, Category
from .forms import FoodForm, ContactForm
from django.core.files.storage import FileSystemStorage
from .forms import NameForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.decorators import login_required
# from .forms import ContactFormWithMugshot
# views.py


# views.py

# Create your views here.
# @login_required
def index(request):
    form = None
    # context = {'name': 'Alice'}  # 템플릿에 전달할 context 데이터
    if request.method == 'POST':
        category = Category.objects.get(name=request.POST.get('category'))
        
        name = request.POST.get('username')
        description = request.POST.get('description')
        price = request.POST.get('price')
        food_takeout = request.POST['takeout']

        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            if 'file' in request.FILES:
                form.save()
                  
            else:
                pass

        # 이미지 저장 및 url 설정 내용
        fs=FileSystemStorage()
        uploaded_file = request.FILES['picture']
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)

        new_name = Food(category=category, name=name, description = description, price=price, image_url = url)
        new_name.save()
    elif request.method == 'GET':
        pass
    else:
        form = FoodForm()
    return render(request, 'Chinese/index.html', {'form' : form})
    
# @login_required
def index_detail(request, pk):
    object = Food.objects.get(pk=pk)
    context = {
        'object':object
    }
    return render(request, 'Chinese/index_detail.html', context)

# @login_required
def index_delete(request, pk):
    object = Food.objects.get(pk=pk)
    object.delete()
    return redirect('index')  


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")
        

        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["sender"]
            cc_myself = form.cleaned_data["cc_myself"]

            recipients = ["info@example.com"]
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "Chinese/name.html", {"form": form})




