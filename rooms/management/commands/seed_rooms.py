import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):
    help = "This command tells me that he loves me"

    def add_arguments(self, parser):
        self.add_base_argument(
            parser, "--number", default=2, type=int, help="how many?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()

        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests" : lambdea x: random.randint(1,8),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        # print(created_clean)
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            # print(room)
            for i in range(3, random.randint(10,17)):
                room_models.Photo.objects.create(
                    caption = seeder.faker.sentence(),
                    file = room
                    file= f'/room_photos/{random.randint(1,31)}.webp'
                )
        self.stdout.write(self.style.SUCCESS(f"{number} created!"))
