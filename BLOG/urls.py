from django.conf import settings
from BLOG.apps import BlogConfig

from django.conf.urls.static import static
from django.urls import path

from BLOG.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

# from myapp.views import HomePageView

app_name = BlogConfig.name

urlpatterns = [path("", BlogListView.as_view(), name='blog_list'),
               path("<int:pk>/", BlogDetailView.as_view(), name='blog_detail'),
               path('create', BlogCreateView.as_view(), name='blog_create'),
               path('<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
               path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete')
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
