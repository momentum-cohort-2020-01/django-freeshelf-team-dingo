# Generated by Django 3.0.3 on 2020-03-01 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200301_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, choices=[('html', 'HTML'), ('css', 'CSS'), ('javascript', 'JavaScript'), ('json', 'JSON'), ('ajax', 'AJAX'), ('python', 'Python'), ('django', 'Django')], default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Category'),
        ),
    ]
