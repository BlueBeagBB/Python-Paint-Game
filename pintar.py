import pygame
import sys

# Inicializar o pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo de Pintura - HP para Tintas")

# Cores e HP inicial para cada cor
cores = {
    "preto": {"cor": (0, 0, 0), "hp": 100},
    "vermelho": {"cor": (255, 0, 0), "hp": 100},
    "verde": {"cor": (0, 255, 0), "hp": 100},
    "azul": {"cor": (0, 0, 255), "hp": 100},
    "amarelo": {"cor": (255, 255, 0), "hp": 100},
    "ciano": {"cor": (0, 255, 255), "hp": 100},
    "magenta": {"cor": (255, 0, 255), "hp": 100},
}

cor_atual = "preto"  # Nome da cor atual selecionada
raio_pincel = 5
consumo_por_pintura = 1  # HP reduzido por cada pintura

# Função para desenhar o menu de cores e seus HPs
def desenha_menu():
    x, y, largura_cor, altura_cor = 10, 10, 40, 40
    for nome, info in cores.items():
        pygame.draw.rect(tela, info["cor"], (x, y, largura_cor, altura_cor))
        
        # Exibir o HP da cor acima do quadrado
        fonte = pygame.font.Font(None, 24)
        texto = fonte.render(f"{info['hp']}", True, (0, 0, 0))
        tela.blit(texto, (x, y - 20))
        
        x += largura_cor + 10

    # Botão de recarga
    pygame.draw.rect(tela, (150, 150, 150), (700, 10, 80, 40))
    fonte = pygame.font.Font(None, 24)
    texto = fonte.render("Recarga", True, (0, 0, 0))
    tela.blit(texto, (710, 20))

# Função para verificar clique no menu de cores e botão de recarga
def verifica_clique_menu(pos):
    global cor_atual
    x, y, largura_cor, altura_cor = 10, 10, 40, 40
    for nome, info in cores.items():
        if x <= pos[0] <= x + largura_cor and y <= pos[1] <= y + altura_cor:
            cor_atual = nome  # Atualiza a cor atual selecionada
        x += largura_cor + 10

    # Botão de recarga - restaura o HP de todas as cores
    if 700 <= pos[0] <= 780 and 10 <= pos[1] <= 50:
        for nome in cores:
            cores[nome]["hp"] = 100

# Loop principal do jogo
tela.fill((255, 255, 255))  # Fundo branco
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Clique com o botão esquerdo
                verifica_clique_menu(evento.pos)
        elif evento.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:  # Se estiver pressionando o botão esquerdo do mouse
                # Verifica se a cor atual tem HP suficiente
                if cores[cor_atual]["hp"] > 0:
                    pygame.draw.circle(tela, cores[cor_atual]["cor"], evento.pos, raio_pincel)
                    cores[cor_atual]["hp"] -= consumo_por_pintura  # Consome HP da cor atual

    # Desenha o menu e os HPs
    desenha_menu()

    # Atualiza a tela
    pygame.display.flip()

# Encerra o pygame
pygame.quit()
sys.exit()