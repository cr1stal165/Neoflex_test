from task3 import generate_hashtag


def test_generate_hashtag_func():
    assert generate_hashtag(' Hello there thanks for trying my Kata') == '#HelloThereThanksForTryingMyKata'
    assert generate_hashtag(' Hello World ') == '#HelloWorld'
    assert generate_hashtag('') is False
    assert generate_hashtag('Good Luck           senior') == '#GoodLuckSenior'
    assert generate_hashtag('1') == '#1'
    assert generate_hashtag('          stop tHe CaR                   ') == '#StopTheCar'
    assert generate_hashtag('Hello there thanks for trying my Kata  Hello there thanks for trying my Kata  Hello '
                            'there thanks for trying my Kata  Hello there thanks for trying my Kata there thanks for '
                            'trying my Kata  Hello there thanks for trying my Kata') is False


