# Generated by Django 2.2.5 on 2019-09-15 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(max_length=50, null=True)),
                ('sex', models.BooleanField(default=0)),
                ('age', models.PositiveIntegerField(null=True)),
                ('openId', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'person',
            },
        ),
    ]
