from constants import *  
from player import Player 
import pygame 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main(): 
	print("Starting Asteroids!") 
	print(f"Screen width: {SCREEN_WIDTH}") 
	print(f"Screen height: {SCREEN_HEIGHT}") 

	pygame.init() 
	clock = pygame.time.Clock() 
	dt = 0 
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
	
	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()	
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	
	Player.containers = (updateable, drawable)
	Shot.containers = (shots, updateable, drawable)
	Asteroid.containers = (asteroids, updateable, drawable)
	AsteroidField.containers = (updateable,)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()
		

	while True: 
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				return 

		updateable.update(dt)

		for asteroid in asteroids:
			if player.collides_with(asteroid):
				print("Game over!")
				return
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collides_with(shot):
					asteroid.kill()
					shot.kill()

	
		screen.fill((0, 0, 0)) 
		for sprite in drawable:
			sprite.draw(screen) 
		pygame.display.flip() 
		dt = clock.tick(60) / 1000 





if __name__ == "__main__": 
    main()

