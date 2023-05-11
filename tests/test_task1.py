from task1 import find_domain


def test_find_domain_func():
    assert find_domain('http://wwww.github.com/carbonfive/raygun') == 'github'
    assert find_domain('http://www.zombie-bites.com') == 'zombie-bites'
    assert find_domain('https://www.cnet.com') == 'cnet'
    assert find_domain('fjgkdkdg.23432') is None
    assert find_domain('https:fdfdfdf') is None
    assert find_domain('https://roadmap.sh/python') == 'roadmap'
    assert find_domain('https://neostudy.neoflex.ru/course') == 'neoflex'
    assert find_domain('https://www.udemy.com/') == 'udemy'
    assert find_domain('https://vk.com/feed') == 'vk'

