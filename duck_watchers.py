import random
from math import cos, sin
import pygame.sprite
from pygame.math import Vector2
import os
cwd = os.getcwd()
from cardboard import *
#import sys
#sys.setrecursionlimit(10000)

main = Board(1980,1080,fps=60,bg=(0,0,0),fullscreen=None)

# Create a test Entity
camera = Camera()

cam = Entity(camera,(500,500),Sprite(path="images/player/main.png"),0,0)
main.set_font("PIXEL")

fishing_rod = Entity(camera, (0,-50),Sprite(path="images/player/fishing/aas.png"), 50,50)
player = Entity(camera,(500,571),Sprite(path="images/player/main.png"),70,100)
fish = Entity(camera, (50,-50),Sprite(path="images/fish.png"), 100,100)
# Create an sky gradient
camera.set_skybox("images/skygradient3.jpg")
water_tiles = []
# CREATE THE GROUND
ground1 = Entity(camera,(50,670),Sprite(path="images/grass_tile.png"),100,100)
ground2 = Entity(camera,(150,670),Sprite(path="images/grass_tile.png"),100,100)
ground3 = Entity(camera,(250,670),Sprite(path="images/grass_tile.png"),100,100)
ground4 = Entity(camera,(350,670),Sprite(path="images/grass_tile.png"),100,100)
ground5 = Entity(camera,(450,670),Sprite(path="images/grass_tile.png"),100,100)
ground6 = Entity(camera,(550,670),Sprite(path="images/grass_tile.png"),100,100)
ground7 = Entity(camera,(650,670),Sprite(path="images/grass_tile.png"),100,100)
# CREATE THE LITLE WATER stuff
water1 = Entity(camera, (750,670),Sprite(path="images/water_tile.png"),100,100)
water2 = Entity(camera, (850,670),Sprite(path="images/water_tile.png"),100,100)
water3 = Entity(camera, (950,670),Sprite(path="images/water_tile.png"),100,100)
water4 = Entity(camera, (1050,670),Sprite(path="images/water_tile.png"),100,100)
water5 = Entity(camera, (1150,670),Sprite(path="images/water_tile.png"),100,100)
water6 = Entity(camera, (1250,670),Sprite(path="images/water_tile.png"),100,100)
water_tiles.append(water1)
water_tiles.append(water2)
water_tiles.append(water3)
water_tiles.append(water4)
water_tiles.append(water5)
water_tiles.append(water6)
# ADD SOME STRUCERSSSS
tree1 = Entity(camera, (100,470),Sprite(path="images/tree_tile.png"),300,300)
fish_stall = Entity(camera, (300,525),Sprite(path="images/blocks/fish/stall1.png"),200,200)
chest = Entity(camera, (475,550),Sprite(path="images/chest.png"),150,150)
# lets add LIFE
duck1 = Entity(camera, (1050,580), Sprite(path="images/duck1.png"),100,100)
fishing_fence = Entity(camera,(630,545),Sprite(path="images/fishingfence.png"),150,150)
#Shop
shop_title = main.create_text("Store", (255, 255, 255), (0, 0, 0))
shop_title_rect = shop_title.get_rect()
shop_title_rect.x = -200
shop_title_rect.y = -50
sell_button = Button(100,0,pygame.image.load("images/sell_button.png"), 5)
# Items
food_button = Button(100,0,pygame.image.load("images/food2.png"), 4)
magic_hat_button = Button(100,0,pygame.image.load("images/hat1_button.png"), 4)
magic_hat2_button = Button(100,0,pygame.image.load("images/hat2.png"), 4)
magic_hat3_button = Button(100,0,pygame.image.load("images/hat3_button.png"), 4)
#
fish_counter = Entity(camera,(50,50),Sprite(path="images/fish_counter.png"),100,100)
board = Entity(camera,(-900,-270),Sprite(path="images/board.png"),700,500)
duck_state = "RIGHT"
players_state = "WALKING"
running = True
# CUSTOMIZATION MENU
custom_title = main.create_text("Duck outfit:", (204, 51, 153), (204, 255, 255))
custom_title_rect = shop_title.get_rect()
custom_title_rect.x = -200
custom_title_rect.y = -50
magic_hat_button_menu = Button(100,0,pygame.image.load("images/hat1.png"), 4)
magic_hat2_button_menu = Button(100,0,pygame.image.load("images/hat2_hat.png"), 4)
magic_hat3_button_menu = Button(100,0,pygame.image.load("images/hat3.png"), 4)
# ITEMS
food_item = Entity(camera,(-50,-50),Sprite(path="images/food.png"),100,100)
hearts = Entity(camera,(-50,-50),Sprite(path="images/hearts.png"),100,100)

# Animations
run_right_antimation = ["images/player/run_right/player_run_right1.png","images/player/run_right/player_run_right2.png","images/player/run_right/player_run_right3.png"]
run_right_sprites = []
for frame in run_right_antimation:
    framer = pygame.image.load(frame)
    run_right_sprites.append(pygame.transform.scale(framer, (player.width, player.height)))

run_left_animation = ["images/player/run_left/player_run_left1.png","images/player/run_left/player_run_left2.png","images/player/run_left/player_run_left3.png"]
run_left_sprites = []
for frame in run_left_animation:
    framer = pygame.image.load(frame)
    run_left_sprites.append(pygame.transform.scale(framer, (player.width, player.height)))

aas_an = ["images/player/fishing/idle/aas1.png","images/player/fishing/idle/aas2.png","images/player/fishing/idle/aas3.png","images/player/fishing/idle/aas4.png"]
aas_sp = []
for frame in aas_an:
    framer = pygame.image.load(frame)
    aas_sp.append(pygame.transform.scale(framer, (fishing_rod.width, fishing_rod.height)))

tree_an = ["images/blocks/tree/tree1.png","images/blocks/tree/tree2.png","images/blocks/tree/tree3.png","images/blocks/tree/tree4.png","images/blocks/tree/tree5.png"]
tree_sp = []
for frame in tree_an:
    framer = pygame.image.load(frame)
    tree_sp.append(pygame.transform.scale(framer, (tree1.width, tree1.height)))
water_an = ["images/blocks/water/water1.png","images/blocks/water/water2.png","images/blocks/water/water3.png","images/blocks/water/water4.png","images/blocks/water/water5.png","images/blocks/water/water6.png"]
water_sp = []
for frame in water_an:
    framer = pygame.image.load(frame)
    water_sp.append(pygame.transform.scale(framer, (water1.width, water1.height)))

fish_stall_an = ["images/blocks/fish/stall1.png","images/blocks/fish/stall2.png","images/blocks/fish/stall3.png","images/blocks/fish/stall4.png","images/blocks/fish/stall5.png","images/blocks/fish/stall6.png"]
fish_stall_sp = []
for frame in fish_stall_an:
    framer = pygame.image.load(frame)
    fish_stall_sp.append(pygame.transform.scale(framer, (fish_stall.width, fish_stall.height)))

line_rot = False
old_center = player.rect.center
caught_fish = 0
luck = 50
coins = 0
sound_man = Mixer(0.7)
hearts.rect.y = 600
duck_feeded = False
feeding = False
inventory = []
catch = False
duck_spell = ""
while running:
    main.loop_init()
    #print(duck_state)
    #camera.custom_draw(sky)

    camera.custom_draw(cam)


    camera.update()
    #enviroment animations
    counter = main.create_text(str(caught_fish), (255, 255, 255), (0, 0, 0))
    counter_rect = counter.get_rect()
    if players_state != "STORE":
        counter_rect.x = 125
        counter_rect.y = 50
        pygame.display.get_surface().blit(counter, counter_rect)
    pygame.display.get_surface().blit(shop_title, shop_title_rect)
    tree1.play_animation(tree_sp, 300)
    fish_stall.play_animation(fish_stall_sp,500)
    for water_tile in water_tiles:
        water_tile.play_animation(water_sp, 200)
    # animation player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and player.rect.x < 650 and players_state == "WALKING":
        player.rect.move_ip(10,0)
        sound_man.play_sound("sounds/sound_effects/step.mp3")
        player.play_animation(run_right_sprites, 50)
    if keys[pygame.K_a] and player.rect.x > 0  and players_state == "WALKING":
        player.play_animation(run_left_sprites, 50)
        sound_man.play_sound("sounds/sound_effects/step.mp3")
        player.rect.move_ip(-10,0)
    # duck movemen
    if duck_state == "RIGHT":
        if duck_spell == "1":

            pygame.display.get_surface().blit(pygame.transform.flip(pygame.transform.scale(pygame.image.load("images/hat1.png"), (100, 100)),
                                              True,False),  (duck1.rect.x + 25,duck1.rect.y - 50))

        elif duck_spell == "2":
            pygame.display.get_surface().blit(pygame.transform.flip(pygame.transform.scale(pygame.image.load("images/hat2_hat.png"), (100, 100)),
                                              True,False),  (duck1.rect.x + 25,duck1.rect.y - 50))
        elif duck_spell == "3":
            pygame.display.get_surface().blit(pygame.transform.flip(pygame.transform.scale(pygame.image.load("images/hat3.png"), (100, 100)),
                                              True,False),  (duck1.rect.x + 25,duck1.rect.y - 50))
        if duck1.rect.x < 1180:
            duck1.rect.move_ip(2.5, 0)
            duck1.image = pygame.image.load("images/duck1.png")
            duck1.image = pygame.transform.scale(duck1.image, (duck1.width, duck1.height))
        else:
            duck_state = "LEFT"
    if duck_state == "LEFT":
        if duck_spell == "1":
            pygame.display.get_surface().blit(pygame.transform.scale(pygame.image.load("images/hat1.png"), (100, 100)),
                                              (duck1.rect.x - 25, duck1.rect.y - 50))
        elif duck_spell == "2":
            pygame.display.get_surface().blit(pygame.transform.scale(pygame.image.load("images/hat2_hat.png"), (100, 100)),
                                              (duck1.rect.x - 25, duck1.rect.y - 50))
        elif duck_spell == "3":
            pygame.display.get_surface().blit(
                pygame.transform.scale(pygame.image.load("images/hat3.png"), (100, 100)),
                (duck1.rect.x - 25, duck1.rect.y - 50))
        if not pygame.sprite.collide_rect(duck1,ground7):# or not pygame.sprite.collide_rect(player,duck1):
            duck1.rect.move_ip(-2.5,0)
            duck1.image = pygame.image.load("images/duck2.png")
            duck1.image = pygame.transform.scale(duck1.image, (duck1.width, duck1.height))

        else:
            duck_state = "RIGHT"

    if keys[pygame.K_f] and player.rect.x > 650 and players_state == "WALKING":
        if "FOOD" in inventory:
            feeding = True


    # Feeding

    if feeding:
        food_item.rect.x = 920
        if not pygame.sprite.collide_rect(food_item,water3):

            food_item.rect.move_ip(0, 10)
        if pygame.sprite.collide_rect(food_item,duck1):
            food_item.rect.y = -100
            feeding = False
            duck_feeded = True
    if duck_feeded:
        hearts.rect.x = duck1.rect.x
        if hearts.rect.y > -100:

            hearts.rect.move_ip(0, -10)

    # Customazation logic
    if keys[pygame.K_e] and pygame.sprite.collide_rect(player,chest):
        players_state = "CUSTOMIZE"
        #
    # Store Logic

    if keys[pygame.K_e] and pygame.sprite.collide_rect(player,fish_stall):
        players_state = "STORE"
    if keys[pygame.K_q] and players_state == "STORE":
        players_state = "WALKING"
        board.rect.x = -5500
        board.rect.y = -4000
        shop_title_rect.x = -200
        shop_title_rect.y = -50
        fish_counter.rect.x = 0
    if keys[pygame.K_q] and players_state == "CUSTOMIZE":
        players_state = "WALKING"
        board.rect.x = -5500
        board.rect.y = -4000
        custom_title_rect.x = -5080
        custom_title_rect.y = -7000

    if players_state == "STORE":
        player.image = pygame.image.load("images/player/main.png")
        player.image = pygame.transform.scale(player.image, (player.width, player.height))
        board.rect.x = 550
        board.rect.y = 40
        shop_title_rect.x = 580
        shop_title_rect.y = 70
        sell_button.rect.x =820
        sell_button.rect.y = -20
        food_button.rect.x = 600
        food_button.rect.y = 200
        magic_hat_button.rect.x = 775
        magic_hat_button.rect.y = 200
        magic_hat2_button.rect.x = 925
        magic_hat2_button.rect.y = 200
        magic_hat3_button.rect.x = 1075
        magic_hat3_button.rect.y = 200
        fish_counter.rect.x = -920
        counter_rect.x = 1120
        counter_rect.y = 90
        pygame.display.get_surface().blit(counter, counter_rect)
        pygame.display.get_surface().blit(pygame.transform.scale(pygame.image.load("images/fish_counter.png"), (fish_counter.width, fish_counter.height)), (1000, 40))
        if sell_button.draw(pygame.display.get_surface()):
            coins += caught_fish
            caught_fish = 0
            sound_man.play_sound("sounds/sound_effects/sell.wav")
        if magic_hat_button.draw(pygame.display.get_surface()):
            if coins > 10 or coins == 10:
                inventory.append("MAGIC1")
                coins -= 10
                sound_man.play_sound("sounds/sound_effects/buy.wav")
            else:
                print("not enoguh coins")
                sound_man.play_sound("sounds/sound_effects/notenough.wav")
        if magic_hat2_button.draw(pygame.display.get_surface()):
            if coins > 20 or coins == 20:
                inventory.append("MAGIC2")
                coins -= 20
                sound_man.play_sound("sounds/sound_effects/buy.wav")
            else:
                print("not enoguh coins")
                sound_man.play_sound("sounds/sound_effects/notenough.wav")
        if magic_hat3_button.draw(pygame.display.get_surface()):
            if coins > 50 or coins == 50:
                inventory.append("MAGIC3")
                coins -= 50
                sound_man.play_sound("sounds/sound_effects/buy.wav")
            else:
                print("not enoguh coins")
                sound_man.play_sound("sounds/sound_effects/notenough.wav")
        #Coins

        pygame.display.get_surface().blit(pygame.transform.scale(pygame.image.load("images/coin.png"),
                                                                 (fish_counter.width, fish_counter.height)), (575, 100))
        coin_text = main.create_text(str(coins), (204, 153, 0), (0, 0, 0))
        coin_rect = counter.get_rect()
        coin_rect.x = 665
        coin_rect.y = 140
        pygame.display.get_surface().blit(coin_text, coin_rect)
        # Items
        if food_button.draw(pygame.display.get_surface()):
            if coins > 5 or coins == 5:
                inventory.append("FOOD")
                coins -= 5
                print("FOOD BOUGHT")
                sound_man.play_sound("sounds/sound_effects/buy.wav")
            else:
                print("NOT ENOUGH COINS")
                sound_man.play_sound("sounds/sound_effects/notenough.wav")

    # Custom menu
    if players_state == "CUSTOMIZE":
        player.image = pygame.image.load("images/player/main.png")
        player.image = pygame.transform.scale(player.image, (player.width, player.height))
        board.rect.x = 550
        board.rect.y = 40
        custom_title_rect.x = 580
        custom_title_rect.y = 70
        pygame.display.get_surface().blit(custom_title, (custom_title_rect.x,custom_title_rect.y))
        for item in inventory:
            if item == "MAGIC1":
                magic_hat_button_menu.rect.x = 580
                magic_hat_button_menu.rect.y = 100
                if magic_hat_button_menu.draw(pygame.display.get_surface()):
                    duck_spell = "1"
                    sound_man.play_sound("sounds/sound_effects/duckup.mp4")
            elif item == "MAGIC2":
                magic_hat2_button_menu.rect.x = 680
                magic_hat2_button_menu.rect.y = 100
                if magic_hat2_button_menu.draw(pygame.display.get_surface()):
                    duck_spell = "2"
                    sound_man.play_sound("sounds/sound_effects/duckup.mp4")
            elif item == "MAGIC3":
                magic_hat3_button_menu.rect.x = 780
                magic_hat3_button_menu.rect.y = 100
                if magic_hat3_button_menu.draw(pygame.display.get_surface()):
                    duck_spell = "3"
                    sound_man.play_sound("sounds/sound_effects/duckup.mp4")



    # Fishing logic
    if keys[pygame.K_e] and pygame.sprite.collide_rect(player,fishing_fence):
        players_state = "FISHING"
        sound_man.play_sound("sounds/sound_effects/fish_out.mp3")

    if keys[pygame.K_q] and players_state == "FISHING":
        players_state = "WALKING"
        sound_man.play_sound("sounds/sound_effects/fish_out.mp3")
        fishing_rod.rect.x = 0
        fishing_rod.rect.y = -50
        player.image = pygame.image.load("images/player/main.png")
        player.image = pygame.transform.scale(player.image, (player.width, player.height))
        fishing_fence.image = pygame.image.load("images/fishingfence.png")
        fishing_fence.image = pygame.transform.scale(fishing_fence.image, (fishing_fence.width, fishing_fence.height))

    if players_state == "FISHING":
        board.rect.y = 10000
        fishing_rod.rect.x = player.rect.x + 325
        fishing_rod.rect.y = player.rect.y + 55
        player.image = pygame.image.load("images/player/fishing/fishing.png")
        player.image = pygame.transform.scale(player.image, (player.width + 273, player.height))
        fishing_fence.image = pygame.image.load("images/fishingfence2.png")
        fishing_fence.image = pygame.transform.scale(fishing_fence.image, (fishing_fence.width, fishing_fence.height))

        #Animation
        fishing_rod.play_animation(aas_sp,250)

        # the fishing

        chance = random.randint(1, 10000)
        if chance < 40 + luck:
            fish.rect.x = fishing_rod.rect.x
            fish.rect.y = fishing_rod.rect.y
            catch = True

    if catch:
        if fish.rect.y > 500:
            fish.rect.move_ip(0, -20)
            sound_man.play_sound("sounds/sound_effects/fish_caught.mp3")
        else:
            catch = False
            caught_fish += 1
            fish.rect.y = -110
#            print(str(caught_fish))


    main.update()