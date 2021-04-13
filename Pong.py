from pygame import *

from random import randint
from time import time as timer #импортируем функцию для засекания времени, чтобы интерпретатор не искал эту функцию в pygame модуле time, даём ей другое название сами
#подгружаем отдельно функции для работы со шрифтом
img_back = "galaxy.jpg" #фон игры


 
win_width = 700
win_height = 500
display.set_caption("Pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
window.blit(background,(0,0))
 

 
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
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
   #метод "выстрел" (используем место игрока, чтобы создать там пулю)
racket1 = Player("pngegg.png", 40,250,15,100,5)
racket2 = Player("pngegg.png", 600,250,15,100,5)

#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
run = True
finish = False
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
        racket2.reset()
        racket1.reset()
        display.update()

 