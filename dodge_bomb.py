import os
import sys
import pygame as pg
import random


WIDTH, HEIGHT = 1600, 900 #全画面表示の大きさ
os.chdir(os.path.dirname(os.path.abspath(__file__)))

DELTA = { #移動量辞書
    pg.K_UP:(0, -5),pg.K_DOWN:(0, +5), pg.K_LEFT:(-5, 0),pg.K_RIGHT:(+5, 0)
        }

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400

    #練習2:爆弾
    bomb_img = pg.Surface((20, 20)) #一辺が20の正方形Surfaceの↓
    pg.draw.circle(bomb_img, (255,0,0), (10, 10), 10) #中心に半径10の赤い円を描画
    bomb_img.set_colorkey((0, 0, 0)) #四隅の黒を透過
    bomb_rct = bomb_img.get_rect()
    bomb_rct.center = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    vx, vy = +5, +5 #速さ

    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0]) 

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, v in DELTA.items():  #まとめた書き方
            if key_lst[k]:
                sum_mv[0] += v[0]
                sum_mv[1] += v[1]
        # if key_lst[pg.K_UP]:
        #     sum_mv[1] -= 5
        # if key_lst[pg.K_DOWN]:
        #     sum_mv[1] += 5
        # if key_lst[pg.K_LEFT]:
        #     sum_mv[0] -= 5
        # if key_lst[pg.K_RIGHT]:
        #     sum_mv[0] += 5
        kk_rct.move_ip(sum_mv)
        screen.blit(kk_img, kk_rct)
        screen.blit(bomb_img, bomb_rct)
        bomb_rct.move_ip(vx, vy)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
