from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This command tells me that he loves me"

    # def add_arguments(self, parser):
    #     self.add_base_argument(parser, "--times", help="how much time?")

    def handle(self, *args, **options):
        # print(args, options)
        times = options.get("times")
        # print("i love you")
        for t in range(0, int(times)):
            # self.stdout.write(self.style.SUCCESS("I love you"))
            self.stdout.write(self.style.WARNING("I love you"))
