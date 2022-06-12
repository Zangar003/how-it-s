from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail

from django.db import connection
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from locallibrary import settings
from .forms import AddPostForm, Id_need, MovieCreate
from .models import Fon, Customer, Video, Movie


#
def dictfeatchall(cursor):
    desc = cursor.description
    return[
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()

    ]
def index(request):
    cursor = connection.cursor()
    fon = Fon.objects.all()
    cursor.execute("Select p.id, p.title, p.country, p.photo,p.price,  d.description, c.name from polls_movie p"
                   +" Inner join polls_movie_desc d on p.desc_id = d.id"
                   +" Inner join polls_category c On p.category_id = c.id Order by p.id DESC;")
    r = dictfeatchall(cursor)

    # form = AddPostForm(request.POST, request.FILES)
    # form.is_valid()
    # username = form.cleaned_data.get("First_name")
    if request.method == 'POST':

        name = request.POST['text']

        cursor = connection.cursor()
        cursor.execute(f"SELECT First_name, Last_name, email, photo, phon_number, card_number, address, password, money FROM POLLS_CUSTOMER WHERE first_name = '{name}';")
        n = dictfeatchall(cursor)
        return render(request, 'index.html', {'data2': n, 'name': name, 'data': r, 'fon': fon})
    return render(request, 'index.html', {'data': r, 'fon': fon})
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']

        user = authenticate(username = username, password = pass1)


        if user is not None or None:
            login(request, user)
            return render(request, 'index.html', {'user':username})

        else:
            messages.error(request, 'Bad Created')
            return redirect('signin')
    return render(request, 'registration/signin.html')

def signout(request):
    logout(request)
    messages.success(request,"logged sussesfuly")
    return redirect('index')

def Table(request):
    cursor = connection.cursor()
    cursor.execute(
        "Select p.id , p.title, p.country, p.photo, p.price, d.description, c.name from polls_movie p"
        +" Inner join polls_movie_desc d on p.desc_id = d.id "
        + " Inner join polls_category c On p.category_id = c.id Order by p.id Desc;")
    r = dictfeatchall(cursor)

    return render(request, 'data/Table.html', {'table': r})

def sendMail(request):

    # create a variable to keep track of the form
    messageSent = False

    # check if form has been submitted
    if request.method == 'POST':
        # check if data from the form is clean

            subject = request.POST['subject']
            message = request.POST['mess']
            gmail = request.POST['input']

            list = gmail.split(',')
            # send the email to the recipent
            send_mail(subject, message,
                      settings.DEFAULT_FROM_EMAIL,list , fail_silently=False)



            messageSent = True

            return render(request, 'gmail/index.html', { 'messageSent': messageSent,})
    return render(request, 'gmail/index.html')
def signup(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get("First_name")
            lastname = form.cleaned_data.get("Last_name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            send_mail('You are succecful gegisted', "Success",
                      settings.DEFAULT_FROM_EMAIL, [email])
            try:
                Customer.objects.create(**form.cleaned_data)
                my = User.objects.create_user(username, email, password)
                my.first_name = username
                my.last_name = lastname
                my.save()
                messages.success(request, 'your account has been successfully created.')
                return redirect('signin')
            except:
                form.add_error(None, 'Error')
    else:
        form = AddPostForm()
    return render(request, 'registration/signup.html', {'form':form})

def Inf(request):
    i = False
    if request.method == 'POST':

        name = request.POST['text']
        i = True

        cursor = connection.cursor()
        cursor.execute(f"SELECT First_name, Last_name, email, photo, phon_number, card_number, address, password, money FROM POLLS_CUSTOMER WHERE first_name = '{name}';")


        r = dictfeatchall(cursor)

        return render(request, 'costomers/about_customers.html', {'data':r, 'name':i})
    return render(request, 'costomers/about_customers.html')

def update(request):
    cursor = connection.cursor()
    if request.method == 'POST':
        id = request.POST['id']
        title = request.POST['title']
        country = request.POST['country']
        category = request.POST['category']
        desc = request.POST['desc']
        price = request.POST['price']
        r = int(category)
        a= int(desc)
        i = int(id)

        cursor.execute(f"UPDATE polls_movie SET TITLE = '{title}', COUNTRY = '{country}', CATEGORY_ID = {r}, DESC_ID = {a}, PRICE ='{price}' WHERE id = {i};")
        cursor.execute(f"Select id, title, country, price, category_id, desc_id from polls_movie where id ={i}")
        r = dictfeatchall(cursor)
        return render(request, 'update/update.html', {"data": r})

    return render(request, 'update/update.html')

def Insert(request):
    cursor = connection.cursor()
    if request.method == 'POST':
        id = request.POST['id']
        title = request.POST['title']
        country = request.POST['country']
        category = request.POST['category']
        desc = request.POST['desc']
        price = request.POST['price']
        photo = request.POST['photo']
        video = request.POST['video']
        slug = request.POST['slug']
        i = int(id)

        cursor.execute(f"insert into polls_movie(id, title, country,category_id , desc_id, video_id ,price, photo,  slug) Values({id}, '{title}','{country}', {category}, {desc}, {video}, '{price}', '{photo}', '{slug}')")

        cursor.execute(f"Select id, title, country, price, category_id, desc_id from polls_movie where id ={i}")
        r = dictfeatchall(cursor)
        return render(request, 'insert/insert.html', {'data':r})
    return render(request, 'insert/insert.html')

def delete(request):
    g = False
    cursor = connection.cursor()
    if request.method == 'POST':
        id = request.POST['id']
        i = int(id)
        cursor.execute(f"delete from polls_movie where id = {i}")
        g = True
        return render(request, 'delete/delete.html', {'r':g})
    return render(request, 'delete/delete.html')

def Video_show(request):
    vi = Video.objects.all()
    return render(request, 'video/video.html', {'vi':vi})

from django.views.generic import ListView, DetailView

class ArticleListView(ListView):
    model = Movie
    template_name = "slug/article_list.html"


class ArticleDetailView(DetailView):
    model = Movie
    template_name = "slug/article_detail.html"
def tags(request):
    return render(request, 'tags/index.html')

def id_index(request, video_id):
    book_id = int(video_id)
    book_id = book_id+1
    return render(request, 'vid.html', {'book_form':book_id})

def upload(request):
    upload = MovieCreate()
    if request.method == 'POST':
        upload = MovieCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'book/Upload_form.html', {'upload_form':upload})

