Feature: Efetuando GET no endpoint de usuarios

  Background:
    Given seja acessado via GET a api de Usuarios

  Scenario: efetuando validacoes no retorno da API
    When for efetuado validacoes na API "users/1"
    And  for efetuado validacao de contrato campo "name"
    Then devo gerar relatorios das validacoes "address" "street"