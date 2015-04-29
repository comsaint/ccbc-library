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
                ('idbook', models.AutoField(serialize=False, primary_key=True)),
                ('code_colour', models.CharField(blank=True, null=True, choices=[('Blue', 'Blue'), ('Red', 'Red'), ('Black', 'Black'), ('Green', 'Green'), ('White', 'White'), ('Orange', 'Orange'), ('Yellow', 'Yellow'), ('Pink', 'Pink'), ('Gray', 'Gray'), ('Black lines', 'Black lines')], default=None, max_length=16)),
                ('code_number', models.CharField(unique=True, default=None, max_length=6)),
                ('name', models.CharField(max_length=128)),
                ('quantity', models.IntegerField(default=0)),
                ('publisher', models.CharField(blank=True, null=True, default=None, max_length=128)),
                ('author', models.CharField(blank=True, null=True, default=None, max_length=128)),
                ('lang', models.CharField(choices=[('C', 'Chinese'), ('E', 'English')], max_length=8)),
                ('book_area', models.CharField(choices=[('信仰個人成長', '信仰個人成長'), ('靈修', '靈修'), ('宣教', '宣教'), ('護教', '護教'), ('見證', '見證'), ('佈道', '佈道'), ('家庭、兩性關係', '家庭、兩性關係'), ('情緒', '情緒'), ('祈禱', '祈禱'), ('敬拜', '敬拜'), ('兒童(宗教)', '兒童(宗教)'), ('兒童(其他)', '兒童(其他)'), ('少年', '少年'), ('UNKNOWN', 'UNKNOWN')], default='UNKNOWN', max_length=128)),
                ('statusflag', models.CharField(choices=[('NM', 'Normal'), ('SP', 'Special')], default='NM', max_length=16)),
            ],
            options={
                'ordering': ['code_number'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('idborrower', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, null=True, default=None, max_length=75)),
                ('cellgroup', models.CharField(max_length=128)),
                ('statusflag', models.CharField(choices=[('NM', 'Normal'), ('SP', 'Special')], default='NM', max_length=16)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('idtransaction', models.AutoField(serialize=False, primary_key=True)),
                ('borrow_date', models.DateField()),
                ('borrow_manager', models.CharField(default=None, max_length=32)),
                ('renew_date', models.DateField(blank=True, null=True, default=None)),
                ('renew_manager', models.CharField(blank=True, null=True, default=None, max_length=32)),
                ('return_date', models.DateField(blank=True, null=True, default=None)),
                ('return_manager', models.CharField(blank=True, null=True, default=None, max_length=32)),
                ('book', models.ForeignKey(related_name='book', to='ccbclib.Book')),
                ('borrower', models.ForeignKey(related_name='borrower', to='ccbclib.Borrower')),
            ],
            options={
                'ordering': ['-idtransaction'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='borrower',
            unique_together=set([('name', 'phone')]),
        ),
    ]
