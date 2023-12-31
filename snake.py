import pygame,sys,random
from pygame.math import Vector2


class SNAKE:
	def __init__(self):
		self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
		self.direction = Vector2(0, 0)
		self.new_block = False

		self.head_up = pygame.image.load('Graphics/train_up.png').convert_alpha()
		self.head_up = pygame.transform.scale(self.head_up, (50, 50))
		self.head_down = pygame.image.load('Graphics/train_down.png').convert_alpha()
		self.head_down = pygame.transform.scale(self.head_down, (50, 50))
		self.head_right = pygame.image.load('Graphics/train_right.png').convert_alpha()
		self.head_right = pygame.transform.scale(self.head_right, (50, 50))
		self.head_left = pygame.image.load('Graphics/train_left.png').convert_alpha()
		self.head_left = pygame.transform.scale(self.head_left, (50, 50))
		
		self.tail_up = pygame.image.load('Graphics/train_up.png').convert_alpha()
		self.tail_up = pygame.transform.scale(self.tail_up, (50, 50))
		self.tail_down = pygame.image.load('Graphics/train_down.png').convert_alpha()
		self.tail_down = pygame.transform.scale(self.tail_down, (50, 50))
		self.tail_right = pygame.image.load('Graphics/train_right.png').convert_alpha()
		self.tail_right = pygame.transform.scale(self.tail_right, (50, 50))
		self.tail_left = pygame.image.load('Graphics/train_left.png').convert_alpha()
		self.tail_left = pygame.transform.scale(self.tail_left, (50, 50))

		self.body_vertical = pygame.image.load('Graphics/train_vertical.png').convert_alpha()
		self.body_vertical = pygame.transform.scale(self.body_vertical, (50, 50))
		self.body_horizontal = pygame.image.load('Graphics/train_horizontal.png').convert_alpha()
		self.body_horizontal = pygame.transform.scale(self.body_horizontal, (50, 50))

		self.body_tr = pygame.image.load('Graphics/train_vertical.png').convert_alpha()
		self.body_tr = pygame.transform.scale(self.body_tr, (50, 50))
		self.body_tl = pygame.image.load('Graphics/train_vertical.png').convert_alpha()
		self.body_tl = pygame.transform.scale(self.body_tl, (50, 50))
		self.body_br = pygame.image.load('Graphics/train_horizontal.png').convert_alpha()
		self.body_br = pygame.transform.scale(self.body_br, (50, 50))
		self.body_bl = pygame.image.load('Graphics/train_horizontal.png').convert_alpha()
		self.body_bl = pygame.transform.scale(self.body_bl, (50, 50))

		self.yay_sound = pygame.mixer.Sound('Sound/yay-6120.mp3')

	def draw_snake(self):
		self.update_head_graphics()
		self.update_tail_graphics()

		for index,block in enumerate(self.body):
			x_pos = int(block.x * cell_size)
			y_pos = int(block.y * cell_size)
			block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

			if index == 0:
				screen.blit(self.head,block_rect)
			elif index == len(self.body) - 1:
				screen.blit(self.tail,block_rect)
			else:
				previous_block = self.body[index + 1] - block
				next_block = self.body[index - 1] - block
				if previous_block.x == next_block.x:
					screen.blit(self.body_vertical,block_rect)
				elif previous_block.y == next_block.y:
					screen.blit(self.body_horizontal,block_rect)
				else:
					if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
						screen.blit(self.body_tl,block_rect)
					elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
						screen.blit(self.body_bl,block_rect)
					elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
						screen.blit(self.body_tr,block_rect)
					elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
						screen.blit(self.body_br,block_rect)

	def update_head_graphics(self):
		head_relation = self.body[1] - self.body[0]
		if head_relation == Vector2(1,0): self.head = self.head_left
		elif head_relation == Vector2(-1,0): self.head = self.head_right
		elif head_relation == Vector2(0,1): self.head = self.head_up
		elif head_relation == Vector2(0,-1): self.head = self.head_down

	def update_tail_graphics(self):
		tail_relation = self.body[-2] - self.body[-1]
		if tail_relation == Vector2(1,0): self.tail = self.tail_left
		elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
		elif tail_relation == Vector2(0,1): self.tail = self.tail_up
		elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

	def move_snake(self):
		if self.new_block == True:
			body_copy = self.body[:]
			body_copy.insert(0,body_copy[0] + self.direction)
			self.body = body_copy[:]
			self.new_block = False
		else:
			body_copy = self.body[:-1]
			body_copy.insert(0,body_copy[0] + self.direction)
			self.body = body_copy[:]

	def add_block(self):
		self.new_block = True

	def play_yay_sound(self):
		self.yay_sound.play()

	def reset(self):
		self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		self.direction = Vector2(0,0)


class FRUIT:
	def __init__(self):
		self.randomize()
		self.npc = self.choose_random_npc()

	def choose_random_npc(self):
		npc_list = [LEGO1, LEGO2, LEGO3, LEGO4, LEGO5, LEGO6, LEGO7, LEGO8, LEGO9, LEGO11, LEGO12, LEGO13]
		random_npc = random.choice(npc_list)
		return random_npc

	def draw_fruit(self):
		self.choose_random_npc()
		fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
		screen.blit(self.npc, fruit_rect)
		#pygame.draw.rect(screen,(126,166,114),fruit_rect)

	def randomize(self):
		self.x = random.randint(0,cell_number - 1)
		self.y = random.randint(0,cell_number - 1)
		self.pos = Vector2(self.x,self.y)


class MAIN:
	def __init__(self):
		self.snake = SNAKE()
		self.fruit = FRUIT()
		self.npc = FRUIT.choose_random_npc(self.fruit)

	def update(self):
		self.snake.move_snake()
		self.check_collision()
		self.check_fail()

	def draw_elements(self):
		# self.draw_grass()
		self.fruit.draw_fruit()
		self.snake.draw_snake()
		self.draw_score()

	def check_collision(self):
		if self.fruit.pos == self.snake.body[0]:
			self.fruit.draw_fruit()
			self.fruit.randomize()
			self.snake.add_block()
			self.snake.play_yay_sound()

		for block in self.snake.body[1:]:
			if block == self.fruit.pos:
				self.fruit.randomize()

	def check_fail(self):
		if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
			self.game_over()

		for block in self.snake.body[1:]:
			if block == self.snake.body[0]:
				self.game_over()

	def game_over(self):
		self.snake.reset()

	# def draw_grass(self):
	# 	grass_color = (167,209,61)
	# 	for row in range(cell_number):
	# 		if row % 2 == 0:
	# 			for col in range(cell_number):
	# 				if col % 2 == 0:
	# 					grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
	# 					pygame.draw.rect(screen,grass_color,grass_rect)
	# 		else:
	# 			for col in range(cell_number):
	# 				if col % 2 != 0:
	# 					grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
	# 					pygame.draw.rect(screen,grass_color,grass_rect)

	def draw_score(self):
		score_text = str(len(self.snake.body) - 3)
		score_surface = game_font.render(score_text,True,(56,74,12))
		score_x = int(cell_size * cell_number - 60)
		score_y = int(cell_size * cell_number - 40)
		score_rect = score_surface.get_rect(center = (score_x,score_y))
		apple_rect = self.npc.get_rect(midright = (score_rect.left,score_rect.centery))
		bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)

		pygame.draw.rect(screen,(167,209,61),bg_rect)
		screen.blit(score_surface,score_rect)
		screen.blit(LEGO1, apple_rect)
		pygame.draw.rect(screen,(56,74,12),bg_rect,2)


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()
bg = pygame.image.load('Graphics/snake_background.jpeg')
bg = pygame.transform.scale(bg, (cell_number * cell_size,cell_number * cell_size))

LEGO1 = pygame.image.load('Graphics/LEGO_1.png')
LEGO1 = pygame.transform.scale(LEGO1, (50, 50))
LEGO2 = pygame.image.load('Graphics/LEGO_2.png').convert_alpha()
LEGO2 = pygame.transform.scale(LEGO2, (50, 50))
LEGO3 = pygame.image.load('Graphics/LEGO_3.png').convert_alpha()
LEGO3 = pygame.transform.scale(LEGO3, (50, 50))
LEGO4 = pygame.image.load('Graphics/LEGO_4.png').convert_alpha()
LEGO4 = pygame.transform.scale(LEGO4, (50, 50))
LEGO5 = pygame.image.load('Graphics/LEGO_5.png').convert_alpha()
LEGO5 = pygame.transform.scale(LEGO5, (50, 50))
LEGO6 = pygame.image.load('Graphics/LEGO_6.png').convert_alpha()
LEGO6 = pygame.transform.scale(LEGO6, (50, 50))
LEGO7 = pygame.image.load('Graphics/LEGO_7.png').convert_alpha()
LEGO7 = pygame.transform.scale(LEGO7, (50, 50))
LEGO8 = pygame.image.load('Graphics/LEGO_8.png').convert_alpha()
LEGO8 = pygame.transform.scale(LEGO8, (50, 50))
LEGO9 = pygame.image.load('Graphics/LEGO_9.png').convert_alpha()
LEGO9 = pygame.transform.scale(LEGO9, (50, 50))
LEGO10 = pygame.image.load('Graphics/LEGO_10.png').convert_alpha()
LEGO10 = pygame.transform.scale(LEGO10, (50, 50))
LEGO11 = pygame.image.load('Graphics/LEGO_11.png').convert_alpha()
LEGO11 = pygame.transform.scale(LEGO11, (50, 50))
LEGO12 = pygame.image.load('Graphics/LEGO_13.png').convert_alpha()
LEGO12 = pygame.transform.scale(LEGO12, (50, 50))
LEGO13 = pygame.image.load('Graphics/LEGO_14.png').convert_alpha()
LEGO13 = pygame.transform.scale(LEGO13, (50, 50))

npc_list = [LEGO1, LEGO2, LEGO3, LEGO4, LEGO5, LEGO6, LEGO7, LEGO8, LEGO9, LEGO11, LEGO12, LEGO13]
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == SCREEN_UPDATE:
			main_game.update()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				if main_game.snake.direction.y != 1:
					main_game.snake.direction = Vector2(0,-1)
			if event.key == pygame.K_RIGHT:
				if main_game.snake.direction.x != -1:
					main_game.snake.direction = Vector2(1,0)
			if event.key == pygame.K_DOWN:
				if main_game.snake.direction.y != -1:
					main_game.snake.direction = Vector2(0,1)
			if event.key == pygame.K_LEFT:
				if main_game.snake.direction.x != 1:
					main_game.snake.direction = Vector2(-1,0)

	# screen.fill((175,215,70))
	screen.blit(bg, (0, 0))
	main_game.draw_elements()
	pygame.display.update()
	clock.tick(60)
