from typing import List

def mover_uns_para_esquerda_inplace(lst: List[int]) -> None:
   
    ones = sum(1 for x in lst if x == 1)
    others = [x for x in lst if x != 1]
    lst[:] = [1] * ones + others


if __name__ == "__main__":
    arr = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
    mover_uns_para_esquerda_inplace(arr)
    print(arr)
   
