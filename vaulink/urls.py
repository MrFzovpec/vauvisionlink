from django.contrib import admin
from django.urls import path
import vau_form.views as form
import vau_page.views as landing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', form.index),
    path('<artistId>/', landing.artist_card)
]
