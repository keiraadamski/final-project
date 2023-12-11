import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions and frame per second
WIDTH, HEIGHT = 800, 600
FPS = 60

# Font and color configurations
FONT_SIZE = 36
BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)
BUTTON_COLOR_OPTIONS = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 0)]
WORD_LIST = ['red', 'green', 'blue', 'yellow']
FONT_PATH = "ShareTechMono-Regular.ttf"

# Initialize Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Testing the Stroop Effect")
clock = pygame.time.Clock()

# Load font
font = pygame.font.Font(FONT_PATH, FONT_SIZE)

# Function to draw text on the screen
def draw_text(surface, text, color, position):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    surface.blit(text_surface, text_rect)

# Function to conduct the Stroop test
def stroop_test():
    start_time = time.time()
    correct_count = 0

    while time.time() - start_time < 60:
        remaining_time = max(0, 60 - int(time.time() - start_time))
        word = random.choice(WORD_LIST)
        color = random.choice(BUTTON_COLOR_OPTIONS)

        # Draw screen elements
        screen.fill(BACKGROUND_COLOR)
        draw_text(screen, f"Example:", TEXT_COLOR, (WIDTH//2, HEIGHT//3 - 50))
        draw_text(screen, f"{word}", color, (WIDTH//2, HEIGHT//3))
        draw_text(screen, "Choose the color the word is printed in:", TEXT_COLOR, (WIDTH//2, HEIGHT//3 + 50))
        draw_text(screen, f"Time: {remaining_time}", TEXT_COLOR, (WIDTH//2, 30))

        # Draw color buttons
        button_positions = [(WIDTH//4, 2*HEIGHT//3), (WIDTH//4 + 150, 2*HEIGHT//3), 
                            (WIDTH//4 + 300, 2*HEIGHT//3), (WIDTH//4 + 450, 2*HEIGHT//3)]
        for pos, col in zip(button_positions, BUTTON_COLOR_OPTIONS):
            pygame.draw.rect(screen, col, (pos[0] - 50, pos[1] - 25, 100, 50))

        pygame.display.flip()

        # Get user input
        user_input = None
        while user_input is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for idx, pos in enumerate(button_positions):
                        if pos[0] - 50 < mouse_pos[0] < pos[0] + 50 and pos[1] - 25 < mouse_pos[1] < pos[1] + 25:
                            user_input = BUTTON_COLOR_OPTIONS[idx]

        # Check if user input is correct
        if user_input == color:
            correct_count += 1

    return correct_count

def main():
    pygame.display.set_caption("Testing the Stroop Effect")
    correct_answers = stroop_test()

    # Ending screen
    screen.fill(BACKGROUND_COLOR)
    draw_text(screen, f"Game Over!", TEXT_COLOR, (WIDTH//2, HEIGHT//3 - 50))
    draw_text(screen, f"You got {correct_answers} correct answers.", TEXT_COLOR, (WIDTH//2, HEIGHT//2))
    pygame.display.flip()

    # Wait for a few seconds before closing the window
    pygame.time.wait(3000)

# Run the program
if __name__ == "__main__":
    main()
