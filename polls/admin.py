from django.contrib import admin

# Register your models here.
from polls.models import Movie, Customer, Category, Movie_desc, Fon, Video

admin.site.register(Movie)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Movie_desc)
admin.site.register(Fon)
admin.site.register(Video)


