

def generate_hashtag(curr_str: str) -> str | bool:
    """Функция для генерации хэштегов"""
    str1 = curr_str.title().replace(' ', '')
    if len(str1) == 0:
        return False
    else:
        return f'#{str1}' if len(f'#{str1}') < 140 else False




