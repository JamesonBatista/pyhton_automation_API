from behave import *

from test.pages.get_endpoint_users import GetBody


@given(u'seja acessado via GET a api de Usuarios')
def step_impl(context):
    global page
    page = GetBody()


@when(u'for efetuado validacoes na API "{endpoint}"')
def step_impl(context, endpoint):
    page.step_endpoint(endpoint)


@when(u'for efetuado validacao de contrato campo "{name}"')
def step_impl(context, name):
    page.step_validation_schema_json(name)


@then(u'devo gerar relatorios das validacoes "{address}" "{street}"')
def step_impl(context, address, street):
    page.step_validation_json_schema(address, street)
