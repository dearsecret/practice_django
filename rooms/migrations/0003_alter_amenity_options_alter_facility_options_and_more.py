# Generated by Django 4.1 on 2022-08-24 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0002_amenity_facility_houserule_remove_room_room_type_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="amenity",
            options={"verbose_name_plural": "Amenities"},
        ),
        migrations.AlterModelOptions(
            name="facility",
            options={"verbose_name_plural": "Facilities"},
        ),
        migrations.AlterModelOptions(
            name="houserule",
            options={"verbose_name": "House Rule"},
        ),
        migrations.AlterModelOptions(
            name="roomtype",
            options={"verbose_name": "Room Type"},
        ),
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.TimeField(auto_now_add=True)),
                ("updated", models.TimeField(auto_now=True)),
                ("caption", models.CharField(max_length=80)),
                ("file", models.ImageField(upload_to="")),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rooms.room"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
