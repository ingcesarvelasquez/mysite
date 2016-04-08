# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categoria_post',
            field=models.CharField(default='Tech', max_length=30, choices=[('Tech', 'Tecnologia'), ('Life', 'Vida y Estilo'), ('Gral', 'General')], verbose_name='Categoria de Post'),
        ),
    ]
