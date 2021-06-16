# Generated by Django 3.2 on 2021-05-20 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='owner',
            field=models.TextField(default='unknown'),
        ),
        migrations.AlterField(
            model_name='card',
            name='cvv',
            field=models.CharField(max_length=4, verbose_name='cvv'),
        ),
        migrations.AlterField(
            model_name='card',
            name='kzt',
            field=models.DecimalField(decimal_places=1, max_digits=10, verbose_name='kzt'),
        ),
        migrations.AlterField(
            model_name='card',
            name='rub',
            field=models.DecimalField(decimal_places=1, max_digits=10, verbose_name='rub'),
        ),
        migrations.AlterField(
            model_name='card',
            name='usd',
            field=models.DecimalField(decimal_places=1, max_digits=10, verbose_name='usd'),
        ),
    ]
