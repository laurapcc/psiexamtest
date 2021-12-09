from django.core.management.base import BaseCommand
from applicacion.models import (Usuario, Tweet, Retweet)
from django.contrib.auth.models import User
import datetime

class Command(BaseCommand):
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = """populate database
           """

    
    def handle(self, *args, **kwargs):
        self.cleanDataBase()   # clean database
        self.usuario()
        self.tweet()
        self.retweet()


    def cleanDataBase(self):
        User.objects.all().delete()
        Usuario.objects.all().delete()
        Tweet.objects.all().delete()
        Retweet.objects.all().delete()


    def usuario(self):
        " Insert usuario"
        u1 = Usuario.objects.create(id=1001, username='usuario_01')
        u1.save()
        u2 = Usuario.objects.create(id=1002, username='usuario_02')
        u2.save()
        u3 = Usuario.objects.create(id=1003, username='usuario_03')
        u3.save()


    def tweet(self):
        " Insert tweet"
        t = Tweet.objects.create(id=1001, texto='texto de mensaje 01',
                                  usuario=Usuario.objects.get(id=1002),
                                  fecha='2021-01-05')
        t.save()
        t = Tweet.objects.create(id=1002, texto='texto de mensaje 02',
                                  usuario=Usuario.objects.get(id=1001),
                                  fecha=datetime.datetime(2021,1,10))
        t.save()
        t = Tweet.objects.create(id=1003, texto='texto de mensaje 03',
                                  usuario=Usuario.objects.get(id=1002),
                                  fecha=datetime.datetime(2021,1,12))
        t.save()
        t = Tweet.objects.create(id=1004, texto='texto de mensaje 04',
                                  usuario=Usuario.objects.get(id=1002),
                                  fecha=datetime.datetime(2021,1,15))
        t.save()


    def retweet(self):
        " Insert retweet"
        rt = Retweet.objects.create(id=1001,
                                    tweet=Tweet.objects.get(id=1001),
                                    usuario=Usuario.objects.get(id=1003),
                                    fechaDeRetweet=datetime.datetime(2021,1,5))
        rt.save()
        rt = Retweet.objects.create(id=1002,
                                    tweet=Tweet.objects.get(id=1001),
                                    usuario=Usuario.objects.get(id=1001),
                                    fechaDeRetweet=datetime.datetime(2021,1,11))
        rt.save()
        rt = Retweet.objects.create(id=1003,
                                    tweet=Tweet.objects.get(id=1002),
                                    usuario=Usuario.objects.get(id=1003),
                                    fechaDeRetweet=datetime.datetime(2021,1,12))
        rt.save()
        rt = Retweet.objects.create(id=1004,
                                    tweet=Tweet.objects.get(id=1003),
                                    usuario=Usuario.objects.get(id=1003),
                                    fechaDeRetweet=datetime.datetime(2021,1,16))
        rt.save()

