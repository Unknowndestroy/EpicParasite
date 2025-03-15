import pygame
import random
import win32gui
import win32con

# Pygame başlat
pygame.init()

# Ekran boyutları (2560x1080)
screen_width = 2560
screen_height = 1080

# Tam ekran modu (NOFRAME ile pencere çerçevesi olmadan tam ekran)
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)

# Renkler
BLACK = (0, 0, 0)

# Parazit efekti için rastgele renkler oluştur
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Epic Games penceresini kontrol et
def is_epic_games_active():
    window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    return "Epic Games" in window_title  # Epic Games penceresini tanımla

# Ana döngü
running = True
parazit_aktif = True  # Parazit efektinin başlangıçta aktif olması
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # ESC ile çıkış
                running = False
            elif event.key == pygame.K_TAB and pygame.key.get_mods() & pygame.KMOD_ALT:  # Alt+Tab
                parazit_aktif = False  # Alt+Tab yaparken paraziti geçici olarak devre dışı bırak
            elif event.key == pygame.K_SPACE:  # Boşluk tuşu ile paraziti manuel olarak aç/kapat
                parazit_aktif = not parazit_aktif

    # Alt+Tab yapıldıysa ve Epic Games penceresi aktif değilse parazit efekti uygula
    if parazit_aktif and not is_epic_games_active():
        for y in range(0, screen_height, 10):
            for x in range(0, screen_width, 10):
                pygame.draw.rect(screen, random_color(), (x, y, 10, 10))
    else:
        # Epic Games penceresi aktifse veya parazit devre dışıysa ekranı temizle
        screen.fill(BLACK)

    # Ekranı güncelle
    pygame.display.flip()

# Pygame'i kapat
pygame.quit()
