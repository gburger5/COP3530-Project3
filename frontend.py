import time
import pygame
from main import merge_sort, quick_sort, heapsort, tim_sort

# Window Setup + Frequent Variables
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 1200
BACKGROUND_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (50, 50, 50)
SELECTED_COLOR = (100, 100, 255)
BUTTON_HOVER = (70, 70, 70)

# Pygame intialized
pygame.init()
title_font = pygame.font.Font('04B_20__.TTF', 35)
font = pygame.font.Font('04B_20__.TTF', 32)
smaller_font = font = pygame.font.Font('04B_20__.TTF', 12)
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sorting Efficicency Comparison")

with open('GRU_Customer_Electric_Consumption_2012-2022_20241201.csv', 'r') as file: # Takes in each KWH measurement from ~12mil rows of data
    data = []
    next(file) # Skips header
    for line in file:
        row = line.split(',')
        kwh = float(row[6])
        data.append(kwh)

def make_button(x, y, width, height, text): # Making a Button
    return {
        'rect' : pygame.Rect(x, y, width, height),
        'text' : text,
        'hovered' : False,
        'selected' : False
    }


def draw_button(button): # Drawing a Button
    if button['selected']:
        color = SELECTED_COLOR
    else:
        if button['hovered']:
            color = BUTTON_HOVER
        else:
            color = BUTTON_COLOR
    pygame.draw.rect(window, color, button['rect'])
    pygame.draw.rect(window, TEXT_COLOR, button['rect'], 2)

    text_surface = smaller_font.render(button['text'], True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=button['rect'].center)
    window.blit(text_surface, text_rect)


def home_screen(): # Main Menu Screen
    button_height = 60
    button_width = 250
    button_space = 20
    x_start = (WINDOW_WIDTH - (2 * button_width + button_space)) // 2
    y_start = (WINDOW_HEIGHT - (2 * button_height + button_space)) // 2

    # Creating Button for Every Sort + Start Button
    sorting_buttons = [ 
        make_button(x_start, y_start, button_width, button_height, "Merge Sort"),
        make_button(x_start + button_width + button_space, y_start, button_width, button_height, "Quick Sort"),
        make_button(x_start, y_start+ button_height + button_space, button_width, button_height, "Heap Sort"), # Replace
        make_button(x_start + button_width + button_space, y_start + button_height + button_space, button_width, button_height, "Tim Sort") # Replace
    ]

    start_button = make_button(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 150, 200, 50, "Start Sorting")
    chosen_sorts = []

    running = True
    while running:
        window.fill(BACKGROUND_COLOR)

        # Drawing Title
        title = title_font.render("Energy Sorting Comparison", True, TEXT_COLOR)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 100))
        window.blit(title, title_rect)

        # Drawing Rules
        rules = smaller_font.render("Select Two Sorts To Compare", True, TEXT_COLOR)
        rules_rect = rules.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 200))
        window.blit(rules, rules_rect)

        # Drawing Total Sort Selections
        total_text = smaller_font.render(f"Selected: {len(chosen_sorts)}/2", True, TEXT_COLOR)
        total_rect = total_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 175))
        window.blit(total_text, total_rect)

        # Handling Button Clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            
            mouse_position = pygame.mouse.get_pos()

            # Handling Hover Effect
            for button in sorting_buttons:
                button['hovered'] = button['rect'].collidepoint(mouse_position)
            start_button['hovered'] = start_button['rect'].collidepoint(mouse_position)

            # Handling Clicking Buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in sorting_buttons:
                    if button['rect'].collidepoint(mouse_position):
                        if button['selected']:
                            button['selected'] = False
                            chosen_sorts.remove(button['text'])
                        elif len(chosen_sorts) < 2:
                            button['selected'] = True
                            chosen_sorts.append(button['text'])

                if len(chosen_sorts) == 2 and start_button['rect'].collidepoint(mouse_position):
                    running = False
                    return chosen_sorts
                
        # Drawing Buttons
        for button in sorting_buttons:
            draw_button(button)

        # Draw Start Button
        if len(chosen_sorts) == 2:
            draw_button(start_button)

        pygame.display.flip()

def main_screen(data, chosen_sorts): # Takes in Selected Sorts From Frontend To Do Calculations
    window.fill(BACKGROUND_COLOR)

    # Dictionary Mapping Sort Names to Functions
    sorting_algorithms = {
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Heap Sort": heapsort, # Updated
        "Tim Sort": tim_sort # Updated
    }

    # Loading Screen (Replace With Some Type Of Visualization)
    loading_text = title_font.render("Sorting in progress...", True, TEXT_COLOR)
    loading_rect = loading_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    window.blit(loading_text, loading_rect)
    pygame.display.flip()

    # Run Two Sorts
    time_results = []
    for sorting_name in chosen_sorts:
        start_time = time.time()
        sorted_date = sorting_algorithms[sorting_name](data.copy()) # Copy Won't Impact Original Data
        sorting_time = time.time() - start_time
        print(sorting_time)
        time_results.append((sorting_name, sorting_time))
    # Calculating Faster Time    
    faster_time = 0
    if time_results[0][1] > time_results[1][1]:
        faster_time = time_results[1][1]
    else:
        faster_time = time_results[0][1]
    # Display Results
    running = True
    while running:
        window.fill(BACKGROUND_COLOR)

        # Drawing Title
        title = title_font.render("Sorting Results", True, TEXT_COLOR)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 100))
        window.blit(title, title_rect)

        # Drawing Results
        y_position = WINDOW_HEIGHT // 3
        for sorting_name, sorting_time in time_results:
            if sorting_time == faster_time:
                color = (0, 255, 0)  # Green for faster
            else:
                color = (255, 0, 0)  

            sort_text = font.render(f"{sorting_name} Time: {sorting_time:.2f} seconds", True, color)
            sort_text_rect = sort_text.get_rect(center=(WINDOW_WIDTH // 2, y_position))
            window.blit(sort_text, sort_text_rect)
            y_position += 100

        # Drawing Exit Instructions
        exit_text = smaller_font.render("Press ESC or click X to exit", True, TEXT_COLOR)
        exit_rect = exit_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 100))
        window.blit(exit_text, exit_rect)

        pygame.display.flip()

        # Event Handling + Exiting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

    

def main(): # Main Game Loop
    chosen_sorts = home_screen()
    if chosen_sorts is None:
        pygame.quit()
        return
    
    game_on = True
    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
        
        main_screen(data, chosen_sorts)
        pygame.quit()

if __name__ == "__main__":
    main()



