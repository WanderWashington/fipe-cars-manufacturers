from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Permission
from django.utils.translation import gettext as _
from django.utils.translation import activate
from django.conf import settings
import requests as req
from fipe_api.models import Marca, Veiculo
import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('marcas.json') as f:
            data = json.load(f)
        for marca in data:
            Marca.objects.create(code=int(marca['id']), name=marca['name'])
            print(marca['id'])
