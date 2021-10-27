# Generated by Django 2.2.6 on 2021-10-27 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0007_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="pub_date",
            field=models.DateTimeField(
                auto_now_add=True, db_index=True, verbose_name="Дата публикации"
            ),
        ),
    ]
