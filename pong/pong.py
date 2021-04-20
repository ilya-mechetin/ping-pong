from pygame import *

from random import randint
from time import time as timer #импортируем функцию для засекания времени, чтобы интерпретатор не искал эту функцию в pygame модуле time, даём ей другое название сами
#подгружаем отдельно функции для работы со шрифтом
img_back = "green.jpg" #фон игры
goal1 = 0
goal2 = 0

 
win_width = 700
win_height = 500
display.set_caption("Pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
window.blit(background,(0,0))
font.init()
font = font.Font(None,70)
lose1 = font.render('Player 1 lose!', True,((180,0,0)))
lose2 = font.render('Player 2 lose!', True,((180,0,0)))

 
#фоновая музыка


 
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
#конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
          #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
      #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
#метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#класс главного игрока
class Player(GameSprite):
  #метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
   #метод "выстрел" (используем место игрока, чтобы создать там пулю)
racket1 = Player("pngegg.png", 40,250,15,100,5)
racket2 = Player("pngegg.png", 600,250,15,100,5)
ball = GameSprite("ball.png", 300,250,39,39,3)
#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
run = True
finish = False
speed_x = 2
speed_y = 2
while run:
   #событие нажатия на кнопку “Закрыть”
    for e in event.get():
        if e.type == QUIT:
            run = False

   #сама игра: действия спрайтов, проверка правил игры, перерисовка
    if not finish:
        
        #обновляем фон
        window.blit(background,(0,0))
        racket1.update_l()
        racket2.update_r()
        ball.update()
        ball.reset()
        racket2.reset()
        racket1.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.blit(font.render(str(goal1), True,(180,0,0)), (100, 40))
        window.blit(font.render(str(goal2), True,(180,0,0)), (600, 40))
        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x*= -1
        if ball.rect.y>win_height-60 or ball.rect.y<0:
            speed_y*= -1
        if ball.rect.x <0:
            window.blit(lose1,(100,100))
            goal1 = goal1 +1
            finish = True
        if ball.rect.x >win_width:
            window.blit(lose2,(100,100))
            goal2+=1
            
            finish = True
        display.update()
    else:
        
        ball.rect.x = 300
        ball.rect.y = 250
        time.delay(3000)
        finish = False


        
