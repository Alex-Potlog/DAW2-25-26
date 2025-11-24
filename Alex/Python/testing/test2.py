import random


def atac_critic(dany: int) -> int:
    es_critic = int(random.random() * 5) == 0
    if es_critic:
        return (dany * 2)
    return dany


def tirar(dice_notation: str, k: int = 1):
    llistadaus = dice_notation.split("d")
    quantitat = int(llistadaus[0])
    daus = int(llistadaus[1])
    tirades = []
    maxim = 0
    mitjana = 0
    for _ in range(k):
        tirada = 0
        for _ in range(quantitat):
            tirada = int(random.random() * daus) + 1
            print(f"Acaba de sortir el {tirada}!")
            tirades.append(tirada)
            if tirada > maxim:
                maxim = tirada
            mitjana += tirada
    mitjana = mitjana / (quantitat * k)
    resultats = {
        "mitjana": mitjana,
        "maxim": maxim
    }
    return resultats


def test1():
    assert atac_critic(30) in [30, 60]


def test2():
    resultats = tirar("4d6", 10)
    assert 1 <= resultats["maxim"] <= 6
    assert 1 <= resultats["mitjana"] <= 6
    resultats = tirar("2d10", 5)
    assert 1 <= resultats["maxim"] <= 10
    assert 1 <= resultats["mitjana"] <= 10
    resultats = tirar("1d20", 20)
    assert 1 <= resultats["maxim"] <= 20
    assert 1 <= resultats["mitjana"] <= 20


if __name__ == "__main__":
    test1()
    test2()
