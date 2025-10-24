from perguntas.pergunta3 import existe_par_com_soma

def test_q3_exemplos():
    arr = [1, 15, 2, 7, 2, 5, 7, 1, 4]
    assert existe_par_com_soma(arr, 3)   # 1+2
    assert existe_par_com_soma(arr, 4)   # 1+3? (não tem 3), mas 2+2 sim
    assert existe_par_com_soma(arr, 9)   # 7+2, 5+4
    assert not existe_par_com_soma(arr, 30)

def test_q3_com_repetidos():
    arr = [5,5]
    assert existe_par_com_soma(arr, 10)
    assert not existe_par_com_soma(arr, 11)
