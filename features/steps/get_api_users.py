from behave import *

from test.pages.get_endpoint_users import GetBody


@given(u'seja acessado via GET a api de Usuarios')
def step_impl(context):
    global page
    page = GetBody()


@when(u'for efetuado validacoes na API "{endpoint}"')
def step_impl(context, endpoint):
    page.step_endpoint(endpoint)


@when(u'for efetuado validacao de contrato')
def step_impl(context):
    page.step_validation_schema_json()


@then(u'devo gerar relatorios das validacoes')
def step_impl(context):
    page.step_validation_json_schema()
