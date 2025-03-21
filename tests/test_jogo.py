"""
Módulo de testes para a classe Bola.
Contém testes unitários para verificar o comportamento da bola no jogo.
"""

from jogo import Bola


def test_bola_move_direcao_certa():
    """
    Testa se a bola se move na direção correta.
    Verifica se as coordenadas x e y são atualizadas corretamente após o movimento.
    """
    bola = Bola(x=100, y=100, vel_x=5, vel_y=3)
    bola.mover()
    assert bola.x == 105
    assert bola.y == 103


def test_bola_quica_nas_bordas_horizontais():
    """
    Testa se a bola quica corretamente nas bordas horizontais.
    Verifica se a direção horizontal (vel_x) é invertida quando a bola atinge a borda.
    """
    bola = Bola(x=30, y=100, vel_x=-5, vel_y=0)  # bem na borda esquerda
    bola.mover()
    assert bola.vel_x == 5  # deve inverter direção


def test_bola_quica_nas_bordas_verticais():
    """
    Testa se a bola quica corretamente nas bordas verticais.
    Verifica se a direção vertical (vel_y) é invertida quando a bola atinge a borda.
    """
    bola = Bola(x=100, y=30, vel_x=0, vel_y=-5)  # bem no topo
    bola.mover()
    assert bola.vel_y == 5  # deve inverter direção
