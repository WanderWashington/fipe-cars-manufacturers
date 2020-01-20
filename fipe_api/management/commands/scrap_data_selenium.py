from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Permission
from django.utils.translation import gettext as _
from django.utils.translation import activate
from django.conf import settings
import requests as req
from fipe_api.models import Marca, Veiculo
import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class Command(BaseCommand):

    def handle(self, *args, **options):
        modelos_carros = []
        marca_id = 1
        browser = webdriver.Chrome()
        browser.get('')  #add fipeapi address

        select_tipo_veiculo = Select(browser.find_element_by_id('fipe_tipos'))
        select_tipo_veiculo.select_by_visible_text('Carros')
 
        time.sleep(5)

        select_marca = Select(browser.find_element_by_id('fipe_marcas'))
        options_marcas = select_marca.options

        for opcao in options_marcas:
            print(opcao.get_attribute('text'))
            print(len(opcao.get_attribute('value')))
            if opcao.get_attribute('value') != "" and opcao.get_attribute != '0':

                marca_id = opcao.get_attribute('value') # pegando o value para passar a referencia no obj
                select_marca.select_by_value(marca_id)
                time.sleep(10)
                select_modelo = Select(browser.find_element_by_id('fipe_modelos'))
                options_modelos = select_modelo.options

                for opcao_modelo in options_modelos:
                    modelos_carros.append({'code':opcao_modelo.get_attribute('value'), 'name':opcao_modelo.get_attribute('text'), 'manufacturer':marca_id})
                print(modelos_carros)
                try:
                    modelos_carros.pop(0)
                    id_manufacturer = int(modelos_carros[0]['manufacturer'])
                    for carro in modelos_carros:
                        manufacturer = Marca.objects.get(code=id_manufacturer)
                        Veiculo.objects.create(code=int(carro['code']), name=carro['name'], manufacturer=manufacturer)
                    modelos_carros=[]
                except Exception as e:
                    modelos_carros = []
                    print(e)
