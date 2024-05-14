from django.conf import settings
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import base, ProductListView, ProductDetailView, contacts, BlogListView, BlogDetailView, \
    BlogCreateView, BlogUpdateView, BlogDeleteView
from django.conf.urls.static import static
from django.urls import path

# from myapp.views import HomePageView

app_name = CatalogConfig.name

urlpatterns = [path("", ProductListView.as_view(), name='product_list'),
               path("<int:pk>/", ProductDetailView.as_view(), name='product_detail'),
               path('contacts/', contacts, name='contacts'),
               path("", BlogListView.as_view(), name='blog_list'),
               path("<int:pk>/", BlogDetailView.as_view(), name='blog_detail'),
               path('create/', BlogCreateView.as_view(), name='blog_create'),
               path('<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
               path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



