from typing import List

def completar_intervalo_inplace(lst: List[int]) -> None:
   
    if not lst:
        return
    n = max(lst)
    lst[:] = list(range(0, n + 1))


if __name__ == "__main__":
    arr = [9, 2, 3, 1, 4]
    completar_intervalo_inplace(arr)
    print(arr)
