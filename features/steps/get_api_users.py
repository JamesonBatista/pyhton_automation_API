from behave import *

from features.pages.get_endpoint_users import *


@given(u'seja acessado via GET a api de Usuarios')
def step_impl(context):
    global page
    page = GetBody()


@when(u'for efetuado validacoes na API "{endpoint}"')
def step_impl(context, endpoint):
    page.get_endpoint(endpoint)


@when(u'for efetuado validacao de contrato')
def step_impl(context):
    page.validation_schema_json()


@then(u'devo gerar relatorios das validacoes')
def step_impl(context):
    page.validation_path_value()
