import pygame
import time
import numpy as np

# Colors
BG_COLOR = (10, 10, 10)
GRID_COLOR = (50, 50, 50)
DIE_NEXT_COLOR = (170,170,170)
ALIVE_NEXT_COLOR = (255,255,255)

def update(screen,cells,size,with_progress=False):
    updated_cells = np.zeros((cells.shape[0],cells.shape[1])) # Create a new array to store the updated cells. cells.shape[0] is the number of rows and cells.shape[1] is the number of columns.

    for row,col in np.ndindex(cells.shape):
        num_alive = np.sum(cells[row-1:row+2,col-1:col+2])-cells[row,col] # Count the number of alive cells in the 3x3 neighborhood of the current cell.
        color = BG_COLOR if cells[row,col] == 0 else ALIVE_NEXT_COLOR # If the current cell is alive, set the color to ALIVE_NEXT_COLOR, otherwise set it to BG_COLOR.
        if cells[row,col] ==1:
            if num_alive < 2 or num_alive > 3:
                if with_progress:
                    color = DIE_NEXT_COLOR
            elif 2 <= num_alive <= 3:
                updated_cells[row,col] = 1
        else:
            if num_alive == 3:
                if with_progress:
                    color = ALIVE_NEXT_COLOR
                updated_cells[row,col] = 1
        pygame.draw.rect(screen,color,(col*size,row*size,size,size)) # Draw a rectangle at the position (col*size,row*size) with the size size x size and the color color.
    return updated_cells

def main():
    pygame.init()
    pygame.display.set_caption("Game of Life")
    screen = pygame.display.set_mode((800,600))

    cells = np.zeros((60,80)) # Create a 60x80 array of zeros.

    screen.fill(GRID_COLOR) # Fill the screen with the color GRID_COLOR.
    update(screen,cells,10) # Update the screen with the cells array.
    pygame.display.flip() # Update the display.
    pygame.display.update() # Update the display.
    running = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen,cells,10)
                    pygame.display.update()
                
                elif event.key == pygame.K_c:
                    running = False
                    cells = np.zeros((60,80))
                    update(screen,cells,10)
                    pygame.display.update()

                elif event.key == pygame.K_q:
                    pygame.quit()
                    return

            if pygame.mouse.get_pressed()[0]:
                x,y = pygame.mouse.get_pos()
                cells[y//10,x//10] = 1 # Set the cell at the position (y//10,x//10) to 1.
                update(screen,cells,10)
                pygame.display.update()
    
        screen.fill(GRID_COLOR)
        if running:
            cells = update(screen,cells,10,with_progress=True)
            pygame.display.update()
        
        time.sleep(0.001)


if __name__ == "__main__":
    main()
