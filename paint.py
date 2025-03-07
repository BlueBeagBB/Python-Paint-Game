import pygame
import sys

pygame.init()

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo de Pintura - HP para Tintas")

cores = {
    "preto": {"cor": (0, 0, 0), "hp": 100},
    "vermelho": {"cor": (255, 0, 0), "hp": 100},
    "verde": {"cor": (0, 255, 0), "hp": 100},
    "azul": {"cor": (0, 0, 255), "hp": 100},
    "amarelo": {"cor": (255, 255, 0), "hp": 100},
    "ciano": {"cor": (0, 255, 255), "hp": 100},
    "magenta": {"cor": (255, 0, 255), "hp": 100},
}

cor_atual = "preto" 
raio_pincel = 5
consumo_por_pintura = 1 

def desenha_menu():
    x, y, largura_cor, altura_cor = 10, 10, 40, 40
    for nome, info in cores.items():
        pygame.draw.rect(tela, info["cor"], (x, y, largura_cor, altura_cor))
        
        fonte = pygame.font.Font(None, 24)
        texto = fonte.render(f"{info['hp']}", True, (0, 0, 0))
        tela.blit(texto, (x, y - 20))
        
        x += largura_cor + 10

    pygame.draw.rect(tela, (150, 150, 150), (700, 10, 80, 40))
    fonte = pygame.font.Font(None, 24)
    texto = fonte.render("Recarga", True, (0, 0, 0))
    tela.blit(texto, (710, 20))

def verifica_clique_menu(pos):
    global cor_atual
    x, y, largura_cor, altura_cor = 10, 10, 40, 40
    for nome, info in cores.items():
        if x <= pos[0] <= x + largura_cor and y <= pos[1] <= y + altura_cor:
            cor_atual = nome 
        x += largura_cor + 10

    if 700 <= pos[0] <= 780 and 10 <= pos[1] <= 50:
        for nome in cores:
            cores[nome]["hp"] = 100

tela.fill((255, 255, 255))
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1: 
                verifica_clique_menu(evento.pos)
        elif evento.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]: 
                if cores[cor_atual]["hp"] > 0:
                    pygame.draw.circle(tela, cores[cor_atual]["cor"], evento.pos, raio_pincel)
                    cores[cor_atual]["hp"] -= consumo_por_pintura 

    desenha_menu()

    pygame.display.flip()

pygame.quit()
sys.exit()
