from perguntas.pergunta1 import mover_uns_para_esquerda_inplace

def test_q1_exemplo():
    arr = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
    mover_uns_para_esquerda_inplace(arr)
    assert arr[:4] == [1, 1, 1, 1]
    assert arr[4:] == [2, 5, 2, 5, 2, 7, 9, 13, 127, 21]

def test_q1_sem_uns():
    arr = [2,3,4]
    mover_uns_para_esquerda_inplace(arr)
    assert arr == [2,3,4]

def test_q1_todos_uns():
    arr = [1,1,1]
    mover_uns_para_esquerda_inplace(arr)
    assert arr == [1,1,1]

