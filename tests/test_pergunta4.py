from perguntas.pergunta4 import completar_intervalo_inplace

def test_q4_exemplo():
    arr = [9, 2, 3, 1, 4]
    completar_intervalo_inplace(arr)
    assert arr == list(range(0, 10))

def test_q4_lista_vazia():
    arr = []
    completar_intervalo_inplace(arr)
    assert arr == []
