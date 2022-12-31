import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
WINDOW_SIZE = (1000, 700)

# Create the window
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the title of the window
pygame.display.set_caption('Circle Collision')

# Set the default background color
screen.fill((255, 255, 255))

# Create a list to store the circles
circles = []

# Define the Circle class


class Circle:
    def __init__(self, x, y, radius, svg_file, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.svg_file = svg_file
        self.color = color
        self.rect = pygame.Rect(
            self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        self.velocity = (random.randint(-5, 5), random.randint(-5, 5))
        self.image = pygame.image.load(self.svg_file)
        # Set the flag to track whether the image has been changed or not
        self.collided = False

    def move(self):
        # Update the position of the circle based on its velocity
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius

        # Check if the circle is out of bounds
        if self.x - self.radius < 0 or self.x + self.radius > WINDOW_SIZE[0]:
            self.velocity = (-self.velocity[0], self.velocity[1])
        if self.y - self.radius < 0 or self.y + self.radius > WINDOW_SIZE[1]:
            self.velocity = (self.velocity[0], -self.velocity[1])

        # Reset the collided flag to False
        self.collided = False

    def check_collision(self, other):
        # Check for collisions with other circles
        if self.rect.colliderect(other.rect) and other != self:
            # If there is a collision and the circles have not already collided, change the direction and image of both circles
            if self.svg_file == 'scissors.png' and other.svg_file == 'paper.png':
                self.svg_file = 'scissors.png'
                self.image = pygame.image.load(self.svg_file)
                other.svg_file = 'scissors.png'
                other.image = pygame.image.load(other.svg_file)
            elif self.svg_file == 'paper.png' and other.svg_file == 'stone.png':
                self.svg_file = 'paper.png'
                self.image = pygame.image.load(self.svg_file)
                other.svg_file = 'paper.png'
                other.image = pygame.image.load(other.svg_file)
            elif self.svg_file == 'stone.png' and other.svg_file == 'scissors.png':
                self.svg_file = 'stone.png'
                self.image = pygame.image.load(self.svg_file)
                other.svg_file = 'stone.png'
                other.image = pygame.image.load(other.svg_file)
            elif self.svg_file == 'paper.png' and other.svg_file == 'scissors.png':
                self.svg_file = 'scissors.png'
                self.image = pygame.image.load(self.svg_file)
                other.svg_file = 'scissors.png'
                other.image = pygame.image.load(other.svg_file)
            elif self.svg_file == 'stone.png' and other.svg_file == 'paper.png':
                self.svg_file = 'paper.png'
                self.image = pygame.image.load(self.svg_file)
                other.svg_file = 'paper.png'
                other.image = pygame.image.load(other.svg_file)
            elif self.svg_file == 'scissors.png' and other.svg_file == 'stone.png':
                self.svg_file = 'stone.png'
                self.image = pygame.image.load(self.svg_file)
                other.svg_file = 'stone.png'
                other.image = pygame.image.load(other.svg_file)
            # Reverse the direction of both circles
            self.velocity = (-self.velocity[0], -self.velocity[1])
            other.velocity = (-other.velocity[0], -other.velocity[1])

    def draw(self):
        # Resize the SVG image to fit inside the circle
        image = pygame.transform.scale(
            self.image, (self.radius * 2, self.radius * 2))
        # Draw the SVG image on the screen
        screen.blit(image, (self.x - self.radius, self.y - self.radius))


# Create some circles and add them to the list
size = 20

circles.append(Circle(random.randint(10, 800), random.randint(
    10, 800), size, 'paper.png', (255, 255, 255)))
circles.append(Circle(random.randint(10, 800), random.randint(
    10, 800), size, 'stone.png', (255, 255, 255)))
circles.append(Circle(random.randint(10, 800), random.randint(
    10, 800), size, 'scissors.png', (255, 255, 255)))
circles.append(Circle(random.randint(10, 800), random.randint(
    10, 800), size, 'paper.png', (255, 255, 255)))
circles.append(Circle(random.randint(10, 800), random.randint(
    10, 800), size, 'stone.png', (255, 255, 255)))
circles.append(Circle(random.randint(10, 800), random.randint(
    10, 800), size, 'scissors.png', (255, 255, 255)))
circles.append(Circle(random.randint(10, 800), random.randint(
    10, 800), size, 'paper.png', (255, 255, 255)))
circles.append(Circle(random.randint(10, 800), random.randint(
    10, 800), size, 'stone.png', (255, 255, 255)))
circles.append(Circle(random.randint(10, 800), random.randint(
    10, 800), size, 'scissors.png', (255, 255, 255)))
circles.append(Circle(random.randint(10, 800), random.randint(
    10, 800), size, 'paper.png', (255, 255, 255)))
circles.append(Circle(random.randint(10, 800), random.randint(
    10, 800), size, 'stone.png', (255, 255, 255)))
circles.append(Circle(random.randint(10, 800), random.randint(
    10, 800), size, 'scissors.png', (255, 255, 255)))
circles.append(Circle(random.randint(10, 800), random.randint(
    10, 800), size, 'paper.png', (255, 255, 255)))
circles.append(Circle(random.randint(10, 800), random.randint(
    10, 800), size, 'stone.png', (255, 255, 255)))
circles.append(Circle(random.randint(10, 800), random.randint(
    10, 800), size, 'scissors.png', (255, 255, 255)))
circles.append(Circle(random.randint(10, 800), random.randint(
    10, 800), size, 'paper.png', (255, 255, 255)))
circles.append(Circle(random.randint(10, 800), random.randint(
    10, 800), size, 'stone.png', (255, 255, 255)))
circles.append(Circle(random.randint(10, 800), random.randint(
    10, 800), size, 'scissors.png', (255, 255, 255)))


# Set the default background color
screen.fill((255, 255, 255))

# Set the clock to control the frame rate
clock = pygame.time.Clock()


def check_win(circles):
    # Get the list of unique images
    unique_images = list(set([circle.svg_file for circle in circles]))
    # If there's only one unique image, it means that one image has won
    if len(unique_images) == 1:
        # Display the message on the screen
        font = pygame.font.Font(None, 36)
        text = font.render(f'{unique_images[0]} has won!', True, (0, 0, 0))
        screen.blit(text, (size0, size0))
        # Return True to indicate that the game has ended
        return True
    # Otherwise, return False to indicate that the game is still running
    return False


# In the game loop, check if the game has ended
if check_win(circles):
    running = False

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the circles
    for circle in circles:
        circle.move()
        for other in circles:
            circle.check_collision(other)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the circles
    for circle in circles:
        circle.draw()

    # Check if there is only one type of image left
    unique_images = set(circle.svg_file for circle in circles)
    if len(unique_images) == 1:
        # Display the winning image
        image = pygame.image.load(list(unique_images)[0])
        screen.blit(image, (0, 0))
        # Display the "n" message
        font = pygame.font.Font(None, 36)
        text = font.render("Somebody has won", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (400, 400)
        screen.blit(text, text_rect)
        # End the game loop
        break
    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)


# Quit Pygame
pygame.quit()
