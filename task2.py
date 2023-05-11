from typing import Optional


def move_zeros(curr: list) -> Optional[list]:
    """Функция для перемещения нулей в конец массива"""
    if len(curr) == 0:
        return None
    for i in range(len(curr) - 1):
        for j in range(len(curr) - 1):
            if curr[j] == 0:
                temp = curr[j]
                curr[j] = curr[j + 1]
                curr[j + 1] = temp
    return curr

