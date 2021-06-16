import encrypted_fields.fields

from django.db import models


class Card(models.Model):
    cardNumber = models.CharField('cardNumber', max_length=16)
    expirationDate = models.CharField('expirationDate', max_length=5)
    cvv = models.CharField('cvv', max_length=4)
    kzt = models.DecimalField('kzt', max_digits=10, decimal_places=1)
    rub = models.DecimalField('rub', max_digits=10, decimal_places=1)
    usd = models.DecimalField('usd', max_digits=10, decimal_places=1)
    owner = models.TextField(default='unknown')


class User(models.Model):
    nick = models.TextField()
    email = models.EmailField()
    password = encrypted_fields.fields.EncryptedCharField(max_length=40)
    media_gallery = models.ImageField(blank=True, null=True, upload_to='photos/')

