from behave import *
import requests

from features.pages.get_endpoint_users import GetBody


@given(u'seja acessado via GET a api de Usuarios')
def step_impl(context):
    global page
    page = GetBody()


@when(u'for efetuado validacoes na API "{endpoint}"')
def step_impl(context, endpoint):
    page.get_endpoint(endpoint)


@then(u'devo gerar relatorios das validacoes')
def step_impl(context):
    page.validation_path_value()
