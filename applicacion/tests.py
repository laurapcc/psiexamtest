from django.test import TestCase
from applicacion.management.commands.popular import Command
from .models import Tweet, Usuario, Retweet
from django.urls import reverse



class ModelTests(TestCase):
    def setUp(self):
        populate = Command()
        populate.cleanDataBase()

        u = Usuario.objects.create(id=1001, username='usuarioTw1')
        u.save()
        u = Usuario.objects.create(id=1002, username='usuarioTw12')
        u.save()

        t = Tweet.objects.create(id=1001, texto='texto de mensaje 01',
                                 usuario=Usuario.objects.get(id=1001),
                                 fecha='2021-01-25')
        t.save()

        rt = Retweet.objects.create(id=1001,
                                    tweet=Tweet.objects.get(id=1001),
                                    usuario=Usuario.objects.get(id=1002),
                                    fechaDeRetweet='2021-01-25')
        rt.save()


    def test01(self):
        response = self.client.get(reverse('usuario'))
        response_txt = response.content.decode("utf-8")
        self.assertIn('No hay tweets :(', response_txt)

