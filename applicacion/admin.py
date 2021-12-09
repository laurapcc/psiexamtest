from django.contrib import admin
from .models import Usuario, Tweet, Retweet

admin.site.register(Usuario)
admin.site.register(Tweet)
admin.site.register(Retweet)
