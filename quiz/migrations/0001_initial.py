# Generated by Django 4.2 on 2023-04-12 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseTable",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("CourseID", models.CharField(max_length=20)),
                ("CourseName", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="DepartmentTable",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("DepartmentName", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="ProgrammeTable",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ProgrammeName", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="UserTable",
            fields=[
                (
                    "prefix",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Mr.", "Mr."),
                            ("Mrs.", "Mrs."),
                            ("Dr.", "Dr."),
                            ("Ms.", "Ms."),
                            ("Miss", "Miss"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "username",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("password", models.CharField(max_length=300)),
                (
                    "role",
                    models.CharField(
                        choices=[("Teacher", "Teacher"), ("Student", "Student")],
                        max_length=40,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Approved", "Approved"),
                            ("Rejected", "Rejected"),
                        ],
                        max_length=40,
                    ),
                ),
                ("name", models.CharField(max_length=40)),
                ("email", models.CharField(max_length=40)),
                ("mobile", models.CharField(max_length=20)),
                (
                    "ques",
                    models.CharField(
                        choices=[
                            (
                                "What was your first pet name?",
                                "What was your first pet name?",
                            ),
                            ("Where were you born?", "Where were you born?"),
                            (
                                "What is the first film you watched in a theatre?",
                                "What is the first film you watched in a theatre?",
                            ),
                            (
                                "What was your favourite subject in high school?",
                                "What was your favourite subject in high school?",
                            ),
                            (
                                "Where did you go on your favorite vacation as a child?",
                                "Where did you go on your favorite vacation as a child?",
                            ),
                        ],
                        max_length=400,
                    ),
                ),
                ("ans", models.CharField(max_length=100)),
                (
                    "department",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quiz.departmenttable",
                    ),
                ),
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
        migrations.CreateModel(
            name="adminTable",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ques",
                    models.CharField(
                        choices=[
                            (
                                "What was your first pet name?",
                                "What was your first pet name?",
                            ),
                            ("Where were you born?", "Where were you born?"),
                            (
                                "What is the first film you watched in a theatre?",
                                "What is the first film you watched in a theatre?",
                            ),
                            (
                                "What was your favourite subject in high school?",
                                "What was your favourite subject in high school?",
                            ),
                            (
                                "Where did you go on your favorite vacation as a child?",
                                "Where did you go on your favorite vacation as a child?",
                            ),
                        ],
                        max_length=400,
                    ),
                ),
                ("ans", models.CharField(max_length=100)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]