# Generated by Django 5.2 on 2025-04-27 03:03

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('descriptions', models.CharField(max_length=300)),
                ('amount', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
