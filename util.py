def draw_text(x, y, font, text, color, screen):
    t = font.render(text, False, color)
    screen.blit(t, (x, y))