# Generated by Django 2.1.5 on 2020-10-26 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xpensesuser',
            name='feed',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='transaccion.Transaccion'),
        ),
    ]