from src.perguntas.pergunta1 import mover_uns_para_esquerda_inplace
from src.perguntas.pergunta2 import montar_arvore_exemplo, caminho_ate_palavra
from src.perguntas.pergunta3 import existe_par_com_soma
from src.perguntas.pergunta4 import completar_intervalo_inplace



def demo_q1():
    arr = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
    mover_uns_para_esquerda_inplace(arr)
    print("Q1 =>", arr)


def demo_q2():
    root = montar_arvore_exemplo()
    for alvo in ("Goiaba", "Cebola", "Abacaxi", "Maçã", "Inexistente"):
        print(f"Q2 => {alvo}:", caminho_ate_palavra(root, alvo))


def demo_q3():
    arr = [1, 15, 2, 7, 2, 5, 7, 1, 4]
    for alvo in (3, 4, 9, 10, 17, 30):
        print(f"Q3 => soma={alvo}:", existe_par_com_soma(arr, alvo))


def demo_q4():
    arr = [9, 2, 3, 1, 4]
    completar_intervalo_inplace(arr)
    print("Q4 =>", arr)


if __name__ == "__main__":
    demo_q1()
    demo_q2()
    demo_q3()
    demo_q4()
