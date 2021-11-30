from fastapi import status
from fastapi.testclient import TestClient

from cervejarias.main import app


def test_quando_solicitar_lista_de_nomes_das_cervejas_e_estiver_autenticado_devo_receber_status_code_200():
    cliente = TestClient(app)
    response = cliente.get('/breweries')
    assert response.status_code == status.HTTP_200_OK


def test_quando_solicitar_lista_de_nomes_e_estiver_autenticado_o_retorno_deve_ser_um_dict():
    cliente = TestClient(app)
    response = cliente.get('/breweries')
    assert isinstance(response.json(), dict)


def test_quando_listar_nomes_o_formato_deve_ser_json():
    cliente = TestClient(app)
    response = cliente.get('/breweries')
    assert response.headers['Content-Type'] == 'application/json'


def test_quando_solicitar_lista_de_nomes_e_estiver_autenticado_o_conteudo_do_dict_deve_ser_uma_lista():
    cliente = TestClient(app)
    response = cliente.get('/breweries')
    assert isinstance(response.json()['cervejarias'], list)


def test_deve_aceitar_metodo_post():
    cliente = TestClient(app)
    resposta = cliente.post('/add_brewery')
    assert resposta.status_code != status.HTTP_405_METHOD_NOT_ALLOWED


def test_quando_tentar_acessar_uma_rota_sem_autenticacao_retornar_codigo_401():
    cliente = TestClient(app)
    rota_breweries = cliente.get('/breweries')
    assert rota_breweries.status_code == status.HTTP_401_UNAUTHORIZED

    rota_add_brewery = cliente.post('/add_brewery')
    assert rota_add_brewery.status_code == status.HTTP_401_UNAUTHORIZED
