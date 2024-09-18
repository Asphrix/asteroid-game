import sys
import pygame 
from constants import *
from Player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    score = 0
    score_font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    score_surf = score_font.render(f"Score:{score}", False, "white")


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 10)
    meteors = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              return
     
        
        screen.fill("black")
        for u in updatable:
            u.update(dt)
        for d in drawable:
            d.draw(screen)
        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game Over")
                pygame.quit()
                sys.exit()
            for shot in shots:
                if shot.check_collisions(asteroid):
                    shot.kill()
                    asteroid.split()
                    score += asteroid.split() // 10
                    score_surf = score_font.render(f"Score:{score}", False, "white")
                    
        screen.blit(score_surf, (20, 20))
        
        pygame.display.flip()

        

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        






if __name__ == "__main__":
    main()
