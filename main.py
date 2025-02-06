import pygame
import sys
import math

class FireStaff:
    def __init__(self, power, image_path):
        self.power = power
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=(400, 300))

    def cast_spell(self):
        return f"Unleashing a fire spell with power {self.power}!"

    def draw(self, screen, angle):
        rotated_image = pygame.transform.rotate(self.image, angle)
        new_rect = rotated_image.get_rect(center=self.rect.center)
        screen.blit(rotated_image, new_rect.topleft)

class Projectile:
    def __init__(self, position, angle):
        self.position = position
        self.angle = angle
        self.speed = 10
        self.color = (255, 0, 0)
        self.radius = 5

    def update(self):
        self.position[0] += self.speed * math.cos(math.radians(self.angle))
        self.position[1] -= self.speed * math.sin(math.radians(self.angle))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), self.radius)

# Example usage
if __name__ == "__main__":
    staff = FireStaff(power=10, image_path="Assets/INFERNO.png")
    print(staff.cast_spell())

    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    screen_width = 800
    screen_height = 600

    # Colors
    black = (0, 0, 0)

    # Set up the display
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Epic Staffs")

    # Set up the clock for FPS
    clock = pygame.time.Clock()
    FPS = 60

    projectiles = []
    rotation_offset = -45

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                angle = math.degrees(math.atan2(300 - mouse_y, mouse_x - 400))
                projectiles.append(Projectile([400, 300], angle))
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rotation_offset -= 5
                elif event.key == pygame.K_RIGHT:
                    rotation_offset += 5

        # Fill the screen with black
        screen.fill(black)

        # Get mouse position and calculate angle
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.degrees(math.atan2(300 - mouse_y, mouse_x - 400)) + rotation_offset

        # Draw the staff
        staff.draw(screen, angle)

        # Update and draw projectiles
        for projectile in projectiles:
            projectile.update()
            projectile.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()