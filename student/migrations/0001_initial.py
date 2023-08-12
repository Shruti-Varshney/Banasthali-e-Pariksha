# Generated by Django 4.2 on 2023-04-12 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("quiz", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                ("user", models.CharField(max_length=40)),
                ("password", models.CharField(max_length=300)),
                ("name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("mobile", models.CharField(max_length=20)),
                ("smartID", models.AutoField(primary_key=True, serialize=False)),
                (
                    "programme",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quiz.programmetable",
                    ),
                ),
            ],
        ),
    ]
