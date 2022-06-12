from django.conf.urls.static import static
from django.urls import path, include

from locallibrary import settings
from polls import views
from polls.views import ArticleDetailView, ArticleListView

urlpatterns = [
    path('', views.index, name ="index"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('table/', views.Table, name="table"),
    path('gmail/', views.sendMail, name="gmail"),
    path('inf/', views.Inf, name="customer"),
    path('update/', views.update, name="update"),
    # path('insert/', views.Insert, name="insert"),
    path('delete/', views.delete, name="delete"),
    path('video/', views.Video_show, name ="video"),
    path("<slug:slug>", ArticleDetailView.as_view(), name="article_detail"),  # new
    path("slug/", ArticleListView.as_view(), name="article_list"),
    path('tags/', views.tags, name ="tags"),
    path('update2/<int:video_id>', views.id_index),
    path('upload/', views.upload, name = 'insert'),
]
if settings.DEBUG:
        urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
