# Generated by Django 4.0.5 on 2022-07-06 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baseFile', models.FileField(max_length=500, upload_to='')),
                ('uploadTo', models.FileField(upload_to='')),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='notificationContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customId', models.CharField(max_length=50)),
                ('taxIdentificationNumber', models.CharField(max_length=20)),
                ('accountNumber', models.CharField(max_length=50)),
                ('transactionDate', models.DateField()),
                ('transactionDocumentType', models.CharField(max_length=100)),
                ('icaRetention', models.FloatField()),
                ('ivaRetention', models.FloatField()),
                ('rentaRetention', models.FloatField()),
                ('amountPaid', models.FloatField()),
                ('totalValueInvoice', models.FloatField()),
                ('note', models.CharField(max_length=1000)),
            ],
        ),
    ]
