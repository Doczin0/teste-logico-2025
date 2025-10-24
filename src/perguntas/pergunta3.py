from typing import Iterable

def existe_par_com_soma(valores: Iterable[int], x: int) -> bool:
   
    vistos = set()
    for v in valores:
        if (x - v) in vistos:
            return True
        vistos.add(v)
    return False


if __name__ == "__main__":
    arr = [1, 15, 2, 7, 2, 5, 7, 1, 4]
    for alvo in (3, 4, 9, 10, 17, 30):
        print(alvo, "=>", existe_par_com_soma(arr, alvo))

