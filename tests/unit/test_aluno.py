from unittest.mock import MagicMock

from aluno.aluno import Aluno, contar_aprovados


# =============================================================
# PARTE 1 - Encontre os bugs
# Escreva um teste para cada bug descrito no guia da atividade.
# =============================================================
def test_calcular_media_usa_quantidade_real_de_notas():
    aluno = Aluno(nome="Ana", notas=[10, 8])

    assert aluno.calcular_media() == 9


def test_situacao_aprova_aluno_com_media_igual_a_seis():
    aluno = Aluno(nome="Bruno", notas=[6, 6, 6, 6])

    assert aluno.situacao() == "Aprovado"


def test_menor_nota_retorna_a_menor_nota_do_aluno():
    aluno = Aluno(nome="Carla", notas=[7, 4, 9, 6])

    assert aluno.menor_nota() == 4


def test_calcular_media_arredondada_arredonda_para_o_inteiro_mais_proximo():
    aluno = Aluno(nome="Daniel", notas=[7, 8, 8, 8])

    assert aluno.calcular_media_arredondada() == 8


# =============================================================
# PARTE 2 - Implemente com TDD
# Siga o ciclo: escreva o teste -> implemente -> refatore
# =============================================================

# Requisito 1 - contar_aprovados(lista_de_alunos) -> int
def test_contar_aprovados_com_todos_aprovados():
    alunos = [
        Aluno(nome="Ana", notas=[7, 8, 9, 10]),
        Aluno(nome="Bruno", notas=[6, 6, 7, 7]),
    ]

    assert contar_aprovados(alunos) == 2


def test_contar_aprovados_com_todos_reprovados():
    alunos = [
        Aluno(nome="Carla", notas=[4, 5, 5, 4]),
        Aluno(nome="Daniel", notas=[1, 3, 4, 5]),
    ]

    assert contar_aprovados(alunos) == 0


def test_contar_aprovados_com_lista_mista():
    alunos = [
        Aluno(nome="Eva", notas=[9, 8, 7, 6]),
        Aluno(nome="Fabio", notas=[3, 4, 5, 4]),
        Aluno(nome="Giovana", notas=[6, 6, 6, 6]),
    ]

    assert contar_aprovados(alunos) == 2


def test_contar_aprovados_com_lista_vazia():
    assert contar_aprovados([]) == 0


# Requisito 2 - situacao_final(total_aulas) -> str
def test_situacao_final_reprova_por_falta_acima_de_25_porcento_mesmo_com_media_alta():
    aluno = Aluno(nome="Helena", notas=[10, 9, 9, 10], faltas=11)

    assert aluno.situacao_final(total_aulas=40) == "Reprovado por falta"


def test_situacao_final_aprova_com_poucas_faltas_e_media_alta():
    aluno = Aluno(nome="Igor", notas=[8, 7, 6, 7], faltas=3)

    assert aluno.situacao_final(total_aulas=40) == "Aprovado"


def test_situacao_final_reprova_por_nota_com_poucas_faltas_e_media_baixa():
    aluno = Aluno(nome="Julia", notas=[4, 5, 5, 4], faltas=3)

    assert aluno.situacao_final(total_aulas=40) == "Reprovado por nota"


def test_situacao_final_com_25_porcento_de_faltas_verifica_a_media():
    aluno = Aluno(nome="Laura", notas=[6, 6, 6, 6], faltas=10)

    assert aluno.situacao_final(total_aulas=40) == "Aprovado"


def test_situacao_final_com_faltas_pouco_acima_de_25_porcento_reprova_por_falta():
    aluno = Aluno(nome="Marcos", notas=[6, 6, 6, 6], faltas=11)

    assert aluno.situacao_final(total_aulas=40) == "Reprovado por falta"


# Requisito 3 - enviar_boletim(email_service)
def test_enviar_boletim_chama_servico_de_email_para_aluno_reprovado():
    aluno = Aluno(nome="Nina", notas=[4, 5, 5, 4])
    email_service = MagicMock()

    aluno.enviar_boletim(email_service)

    email_service.enviar.assert_called_once_with("Nina", 4.5)


def test_enviar_boletim_nao_chama_servico_de_email_para_aluno_aprovado():
    aluno = Aluno(nome="Otavio", notas=[8, 7, 7, 8])
    email_service = MagicMock()

    aluno.enviar_boletim(email_service)

    email_service.enviar.assert_not_called()
