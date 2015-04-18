# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('area', models.CharField(max_length=32)),
                ('status', models.CharField(choices=[('OS', 'On-shelf'), ('BR', 'Borrowed'), ('RN', 'Renewed'), ('OD', 'Overdue'), ('RS', 'Reserved'), ('LS', 'Lost')], max_length=2, default='OS')),
                ('times_borrowed', models.PositiveIntegerField(default=0)),
                ('times_overdued', models.PositiveIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=75)),
                ('cellgroup', models.CharField(max_length=128)),
                ('status', models.CharField(choices=[('I', 'Idle'), ('B', 'Borrowing'), ('D', 'Overduing')], max_length=1, default='I')),
                ('borrow_count', models.PositiveIntegerField(default=0)),
                ('overdue_count', models.PositiveIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('borrow_date', models.DateField()),
                ('borrow_manager', models.CharField(max_length=32, default='CCBC')),
                ('due_date', models.DateField()),
                ('renew_date', models.DateField(null=True)),
                ('return_date', models.DateField(null=True)),
                ('return_manager', models.CharField(max_length=32, default='')),
                ('book', models.ForeignKey(to='ccbclib.Book')),
                ('borrower', models.ForeignKey(to='ccbclib.Borrower')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
