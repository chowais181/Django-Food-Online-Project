from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from marketplace import views as MarketplaceViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('',include('accounts.urls')),
    path('marketplace/', include('marketplace.urls')),
    # CART
    path('cart/', MarketplaceViews.cart, name='cart'),

    # Checkout
    path('checkout/', MarketplaceViews.checkout, name='checkout'),

    # ORDERS
    path('orders/', include('orders.urls')),

    # SEARCH
    path('search/', MarketplaceViews.search, name='search'),

] +  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
