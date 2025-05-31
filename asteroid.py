import pygame
from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

	def update(self, dt):
   		self.position += self.velocity * dt
		
	def split(self):
    		# Always destroy the current asteroid
		self.kill()

		# If it's already the smallest size, just die
		if self.radius <= ASTEROID_MIN_RADIUS:
			return

		# Calculate new smaller radius
		new_radius = self.radius - ASTEROID_MIN_RADIUS

		# Create two new velocities at slight angles
		angle = random.uniform(20, 50)
		v1 = self.velocity.rotate(angle) * 1.2
		v2 = self.velocity.rotate(-angle) * 1.2

		# Spawn two new asteroids at the same position
		from asteroid import Asteroid  # avoid circular import issues

		a1 = Asteroid(self.position.x, self.position.y, new_radius)
		a1.velocity = v1

		a2 = Asteroid(self.position.x, self.position.y, new_radius)
		a2.velocity = v2

