import pygame as pg
from random import randint, random, choice
import pygame as pg
from random import randint, random, choice
import math
from functions import *

class Ball:

	radius = 15
	speed = 25


	def __init__(self, surf, color):
		self.surf = surf
		self.color = color
		self.angle = random() * math.pi / 4
		self.start_x = surf.get_width() // 2
		self.start_y = surf.get_height() // 2
		self.x = self.start_x
		self.y = self.start_y
		self.x0 = self.start_x
		self.y0 = self.start_y
		self.direction = randint(0, 3) # 0 - право вверх, 1 - право низ, 2 - лево низ, 3 - лево вверх
		self.time = 0
		self.step_time = 0.2
		self.speed = Ball.speed / ((1200//2)**2 + (650)**2)**(1/2) * (surf.get_width()**2 + surf.get_height()**2)**(1/2)
		pg.draw.circle(self.surf, self.color, (self.x, self.y), Ball.radius)

	def move(self, rocket_left, rocket_right):
		if self.direction == 0:
			speed_x = self.speed * math.cos(self.angle)
			speed_y = -self.speed * math.sin(self.angle)
			self.x = self.x0 + speed_x * self.time
			self.y = self.y0 + speed_y * self.time
			rele_pause = self.check_pos(rocket_left, rocket_right)
			self.time += self.step_time

		elif self.direction == 1:
			speed_x = self.speed * math.cos(self.angle)
			speed_y = self.speed * math.sin(self.angle)
			self.x += speed_x * self.time
			self.y += speed_y * self.time
			self.x = self.x0 + speed_x * self.time
			self.y = self.y0 + speed_y * self.time
			rele_pause = self.check_pos(rocket_left, rocket_right)
			self.time += self.step_time

		elif self.direction == 2:
			speed_x = -self.speed * math.cos(self.angle)
			speed_y = self.speed * math.sin(self.angle)
			self.x += speed_x * self.time
			self.y += speed_y * self.time
			self.x = self.x0 + speed_x * self.time
			self.y = self.y0 + speed_y * self.time
			rele_pause = self.check_pos(rocket_left, rocket_right)
			self.time += self.step_time

		elif self.direction == 3:
			speed_x = -self.speed * math.cos(self.angle)
			speed_y = -self.speed * math.sin(self.angle)
			self.x += speed_x * self.time
			self.y += speed_y * self.time
			self.x = self.x0 + speed_x * self.time
			self.y = self.y0 + speed_y * self.time
			rele_pause = self.check_pos(rocket_left, rocket_right)
			self.time += self.step_time

		pg.draw.circle(self.surf, self.color, (self.x, self.y), Ball.radius)

		return rele_pause


	def check_pos(self, rocket_left, rocket_right):
		rele_pause = True
		if self.y - Ball.radius <= 0:
			self.time = 0
			self.angle = self.angle
			if self.direction == 0:
				self.direction = 1
			elif self.direction == 3:
				self.direction = 2
			self.x0 = self.x
			self.y0 = self.y

		elif self.y + Ball.radius >= self.surf.get_height():
			self.time = 0
			self.angle = self.angle
			if self.direction == 1:
				self.direction = 0
			elif self.direction == 2:
				self.direction = 3
			self.x0 = self.x
			self.y0 = self.y

		elif self.x - Ball.radius <= 0:
			if self.y >= rocket_left.y and self.y <= rocket_left.y + rocket_left.height:
				self.direction = choice([0, 1])
				self.x0 = self.x
				self.y0 = self.y
			else:
				rele_pause = False
				rocket_right.y = rocket_right.y_start
				rocket_left.y = rocket_left.y_start
				self.y = self.y0 = self.start_y
				self.x = self.x0 = self.start_x
				self.direction = choice([0, 1, 2, 3])
				s1, s2 = read_score()
				s2 += 1
				write_score(s1, s2)
			self.time = 0
			self.angle = random() * math.pi / 4



		elif self.x + Ball.radius >= self.surf.get_width():
			if self.y >= rocket_right.y and self.y <= rocket_right.y + rocket_right.height:
				self.direction = choice([2, 3])
				self.x0 = self.x
				self.y0 = self.y
			else:
				rele_pause = False
				rocket_right.y = rocket_right.y_start
				rocket_left.y = rocket_left.y_start
				self.y = self.y0 = self.start_y
				self.x = self.x0 = self.start_x
				self.direction = choice([0, 1, 2, 3])
				s1, s2 = read_score()
				s1 += 1
				write_score(s1, s2)
			self.time = 0
			self.angle = random() * math.pi / 4

		return rele_pause
