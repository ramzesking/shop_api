from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import SimpleRouter
from product.views import ProductViewSet
from category.views import CategoryViewSet
from cart.views import CartApiView


router = SimpleRouter()
router.register('products', ProductViewSet)
router.register('categories', ProductViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/account/', include('account.urls')),
    path('api/v1/cart/', CartApiView.as_view()),
    path('api/v1/orders/', include('order.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

