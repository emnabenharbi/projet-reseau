import pygame
import sys
from pygame.locals import *

class GameMenu:
    def __init__(self):
        pygame.init()
        self.width, self.height = 600, 400  # Taille augmentée pour meilleure lisibilité
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tic Tac Toe - Menu")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 32)
        self.selected_mode = None
        
        # Options de menu avec leurs rectangles cliquables
        self.options = [
            {"text": "1. Humain vs Humain (Local)", "rect": None, "key": K_1, "mode": "local_pvp"},
            {"text": "2. Humain vs IA", "rect": None, "key": K_2, "mode": "vs_ai"},
            {"text": "3. Jouer en ligne", "rect": None, "key": K_3, "mode": "online"},
            {"text": "4. Quitter", "rect": None, "key": K_4, "mode": "quit"}
        ]
        
        # Couleurs
        self.colors = {
            "background": (240, 240, 240),
            "text": (0, 0, 0),
            "hover": (100, 150, 255)
        }
        
    def draw_menu(self):
        self.screen.fill(self.colors["background"])
        title = self.font.render("Choisissez un mode de jeu", True, self.colors["text"])
        self.screen.blit(title, (self.width//2 - title.get_width()//2, 50))
        
        for i, option in enumerate(self.options):
            text_color = self.colors["hover"] if option["rect"] and option["rect"].collidepoint(pygame.mouse.get_pos()) else self.colors["text"]
            text = self.font.render(option["text"], True, text_color)
            
            # Calculer la position et stocker le rectangle cliquable
            text_rect = text.get_rect(center=(self.width//2, 150 + i*70))
            self.options[i]["rect"] = text_rect
            
            self.screen.blit(text, text_rect)
            
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                
                if event.type == KEYDOWN:
                    for option in self.options:
                        if event.key == option["key"]:
                            self.selected_mode = option["mode"]
                            running = False
                
                if event.type == MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche
                    for option in self.options:
                        if option["rect"] and option["rect"].collidepoint(mouse_pos):
                            self.selected_mode = option["mode"]
                            running = False
            
            self.draw_menu()
            self.clock.tick(60)  # 60 FPS pour une animation fluide
        
        pygame.quit()
        return self.selected_mode

if __name__ == "__main__":
    menu = GameMenu()
    mode = menu.run()
    
    if mode == "quit":
        sys.exit()
    
    print(f"Mode sélectionné : {mode}")
    
    # Relancer pygame pour le jeu principal
    pygame.init()
    
    if mode == "local_pvp":
        from client import TicTacToeGUI
        game = TicTacToeGUI(is_ai_game=False)
        game.run()
    elif mode == "vs_ai":
        import tkinter as tk
        from ai import TicTacToeGUI, DRLAgent
        root = tk.Tk()
        agent = DRLAgent("tictactoe_ppo")
        app = TicTacToeGUI(root, agent)
        root.mainloop()
    elif mode == "online":
        print("Mode en ligne - À implémenter")
        # from client_online import OnlineGame
        # game = OnlineGame()
        # game.run()
