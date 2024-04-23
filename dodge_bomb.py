import os
import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1000, 600 #1600, 900 #元の数は少しい大きい
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#練習3：こうかとんや爆弾が外に出ないようにする
def check_bound(obj_rct) -> tuple[bool, bool]:
    """
    こうかとんRect、または、爆弾Rectの画面内外判定用の関数
    引数：こうかとんRect or 爆弾Rect
    戻り値：横方向判定結果、縦方向判定結果(True：画面内/False：画面外)
    """
    yoko, tate = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right:
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        tate = False
    return yoko, tate

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

        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
            
        screen.blit(kk_img, kk_rct)
        #爆弾表示
        bomb_rct.move_ip(vx, vy)
        screen.blit(bomb_img, bomb_rct)
        yoko, tate = check_bound(bomb_rct)
        if not yoko: #横方向にはみ出していたら
            vx *= -1
        if not tate: #縦方向にはみ出していたら
            vy *= -1
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
