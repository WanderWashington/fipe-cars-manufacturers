from django.db import models
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict


class PaginacaoNumero(PageNumberPagination):

    page_size_query_param = 'paginacao'

    def get_numero_de_paginas(self):

        # total de itens no solicitacao
        qtd = int(self.page.paginator.count)
        # quantidade de itens por pagina
        numero_itens = int(self.get_page_size(self.request))

        pagina_adicional = qtd % numero_itens
        numero_paginas = qtd // numero_itens

        if qtd == 0:
            return "1"

        if numero_itens >= qtd:
            return "1"

        if pagina_adicional > 0:
            return numero_paginas + 1
        else:
            return numero_paginas

    def get_paginated_response(self, data):

        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data),
            ('num_paginas', self.get_numero_de_paginas())
        ]))


class Marca(models.Model):
    code = models.SmallIntegerField()
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Veiculo(models.Model):
    code = models.SmallIntegerField(null=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    manufacturer = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name = 'marca', null=True)

    def __str__(self):
        return self.name

