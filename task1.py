from typing import Optional


def find_domain(current_url: str) -> Optional[str]:
    """Функция которая извлекает доменное имя из URL-адреса"""
    start_index = current_url.find('://')
    if start_index == -1:
        return None
    else:
        start_index += 3
    end_index = current_url.find('/', start_index)
    result = current_url[start_index:end_index].split('.')[-2]
    return result
