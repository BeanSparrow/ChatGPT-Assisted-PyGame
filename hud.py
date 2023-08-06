# On Screen Visuals
import pygame

WHITE = (255, 255, 255)

def draw_score(game):
    # Draw the score on the top left corner
    score_font = pygame.font.Font(None, 72)
    score_text = score_font.render(f"Score: {game.settings.score}", True, WHITE)
    game.screen.blit(score_text, (10, 10))  # Display score at (10, 10)

def draw_timer(game):
    # Draw the timer
    minutes, milliseconds = divmod(game.settings.total_game_time, 60000)  # 60000 milliseconds = 1 minute
    seconds = milliseconds // 1000
    milliseconds %= 1000
    timer_font = pygame.font.Font(None, 72)
    timer_text = timer_font.render(f"Time: {int(minutes):02}:{int(seconds):02}", True, WHITE)
    timer_rect = timer_text.get_rect(topright=(game.settings.screen_width - 10, 10))  # Position the timer in the top right corner
    game.screen.blit(timer_text, timer_rect)