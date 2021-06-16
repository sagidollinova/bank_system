from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from BankSystem import views as auth, settings
from Customer import views as prof

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth.login),
    path('register/', auth.register),
    path('profile/', prof.profile),
    path('transfer/', prof.transfer),
    path('convert-money/', prof.convert_money),
    path('write-income/', prof.write_income),
    path('change-password/', prof.change_password),
    path('photo-upload/', prof.photo_upload),
    path('logout/', prof.logout_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
