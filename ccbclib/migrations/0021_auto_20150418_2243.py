# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccbclib', '0020_auto_20150417_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_area',
            field=models.CharField(default='UNKNOWN', max_length=128, choices=[('信仰個人成長', '信仰個人成長'), ('靈修', '靈修'), ('宣教', '宣教'), ('護教', '護教'), ('見證', '見證'), ('佈道', '佈道'), ('家庭、兩性關係', '家庭、兩性關係'), ('情緒', '情緒'), ('祈禱', '祈禱'), ('敬拜', '敬拜'), ('兒童(宗教)', '兒童(宗教)'), ('兒童(其他)', '兒童(其他)'), ('少年', '少年'), ('UNKNOWN', 'UNKNOWN')]),
            preserve_default=True,
        ),
    ]
