# Generated by Django 3.2.9 on 2022-02-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('symbol', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=150)),
                ('external_id', models.CharField(max_length=100, null=True)),
                ('status', models.IntegerField(max_length=4)),
                ('logo', models.CharField(max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=8, max_digits=20)),
                ('change_abs', models.DecimalField(decimal_places=8, max_digits=20)),
                ('change_pct', models.DecimalField(decimal_places=2, max_digits=12)),
                ('supply', models.IntegerField(max_length=20)),
                ('volume', models.IntegerField(max_length=20)),
                ('market_cap', models.IntegerField(max_length=20)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
            ],
        ),
    ]