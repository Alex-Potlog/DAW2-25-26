import random


def atac_critic(dany: int) -> int:
    """Retorna dany o dany*2 amb probabilitat 20% per al crític."""
    if random.randint(0, 100) <= 20:
        return dany*2
    return dany
    raise NotImplementedError("Implementa atac_critic(dany)")


def tirar(dice_notation: str, k: int = 1):
    """Interpreta notació NdM, fa k repeticions,
    imprimeix resultats i retorna (millor, mitjana)."""

    tirades_daus = dice_notation.split("d")
    tirada_mes_gran = 0
    valor = 0
    for _ in range(k):
        valor_tirada: int = tirades_daus[1]
        quants_daus: int = tirades_daus[0]
        tirada = random.randint(1, valor_tirada)
        if tirada > tirada_mes_gran:
            tirada_mes_gran = tirada
        valor = valor + quants_daus*tirada
    mitjana = valor/(k+quants_daus)
    print(tirada_mes_gran, mitjana)
    return tirada_mes_gran, mitjana
    raise NotImplementedError("Implementa tirar(dice_notation, k)")


def test_atac_critic_no_critic(monkeypatch):
    """Test atac NO critic"""
    # Reempla random.randint con una función que siempre devuelve 50
    monkeypatch.setattr('random.randint', lambda a, b: 50)
    assert atac_critic(20) == 20
    assert atac_critic(10) == 10


def test_atac_critic_si_critic(monkeypatch):
    """Test atac SI critic"""
    # Reempla random.randint con una función que siempre devuelve 10
    monkeypatch.setattr('random.randint', lambda a, b: 10)
    assert atac_critic(20) == 40
    assert atac_critic(10) == 20


def test_tirar_monkeypatch(monkeypatch):
    """Test de tirar usando monkeypatch con contador"""
    valores = [3, 8, 5]
    contador = [0]  # Usamos lista para poder modificarla en la función

    def mock_randint(a, b):
        valor = valores[contador[0] % len(valores)]
        contador[0] += 1
        return valor

    monkeypatch.setattr('random.randint', mock_randint)
    millor, _ = tirar("1d10", k=3)
    assert millor == 8
