#pgzero
import random

WIDTH = 1000
HEIGHT = 600

TITLE = "Malevich Puzzle"
FPS = 30

# Objects
restart_button = Actor('images/button', (820, 230))
collection_button = Actor('images/button', (820, 380))

cat_small = Actor('images/cat', (180, 340))
dragon_small = Actor('images/dragon_small', (500, 340))
corgi_small = Actor('images/corgi_small', (820, 340))
# Pieces of the image
part1 = Actor('images/image_part_001')
part2 = Actor('images/image_part_002')
part3 = Actor('images/image_part_003')
part4 = Actor('images/image_part_004')
part5 = Actor('images/image_part_005')
part6 = Actor('images/image_part_006')
part7 = Actor('images/image_part_007')
part8 = Actor('images/image_part_008')

#Variables
mode = "collection"
#parts_positions = {1: 1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, "empty": 9}
parts_positions = {}
adjacent = {
    1: [2, 4], 2: [1, 3, 5], 3: [2, 6],
    4: [1, 5, 7], 5: [2, 4, 6, 8], 6: [3, 5, 9],
    7: [4, 8], 8: [5, 7, 9], 9: [6, 8]
}
coordinates = {
    1: [140, 140], 2: [338, 140], 3: [536, 140],
    4: [140, 338], 5: [338, 338], 6: [536, 338],
    7: [140, 536], 8: [338, 536], 9: [536, 536]
}

def is_correct():
    global parts_positions
    if parts_positions[1]==1 and parts_positions[2]==2 and parts_positions[3]==3:
        if parts_positions[4]==4 and parts_positions[5]==5 and parts_positions[6]==6:
            if parts_positions[7]==7 and parts_positions[8]==8:
                return True
                
def start():
    global mode, parts_positions
    taken = []
    ''' exec('part'+str(i)+'.x = coordinates[parts_positions['+str(i)+']][0]')
        exec('part'+str(i)+'.y = coordinates[parts_positions['+str(i)+']][1]')'''
    #1 piece
    parts_positions[1] = random.randint(1, 9)
    while parts_positions[1] in taken:
        parts_positions[1] = random.randint(1, 9)
    taken.append(parts_positions[1])
    part1.x = coordinates[parts_positions[1]][0]
    part1.y = coordinates[parts_positions[1]][1]
    #2nd piece
    parts_positions[2] = random.randint(1, 9)
    while parts_positions[2] in taken:
        parts_positions[2] = random.randint(1, 9)
    taken.append(parts_positions[2])
    part2.x = coordinates[parts_positions[2]][0]
    part2.y = coordinates[parts_positions[2]][1]
    #3 piece
    parts_positions[3] = random.randint(1, 9)
    while parts_positions[3] in taken:
        parts_positions[3] = random.randint(1, 9)
    taken.append(parts_positions[3])
    part3.x = coordinates[parts_positions[3]][0]
    part3.y = coordinates[parts_positions[3]][1]
    #4 piece
    parts_positions[4] = random.randint(1, 9)
    while parts_positions[4] in taken:
        parts_positions[4] = random.randint(1, 9)
    taken.append(parts_positions[4])
    part4.x = coordinates[parts_positions[4]][0]
    part4.y = coordinates[parts_positions[4]][1]
    #5 piece
    parts_positions[5] = random.randint(1, 9)
    while parts_positions[5] in taken:
        parts_positions[5] = random.randint(1, 9)
    taken.append(parts_positions[5])
    part5.x = coordinates[parts_positions[5]][0]
    part5.y = coordinates[parts_positions[5]][1]
    #6 piece
    parts_positions[6] = random.randint(1, 9)
    while parts_positions[6] in taken:
        parts_positions[6] = random.randint(1, 9)
    taken.append(parts_positions[6])
    part6.x = coordinates[parts_positions[6]][0]
    part6.y = coordinates[parts_positions[6]][1]
    #7 piece 
    parts_positions[7] = random.randint(1, 9)
    while parts_positions[7] in taken:
        parts_positions[7] = random.randint(1, 9)
    taken.append(parts_positions[7])
    part7.x = coordinates[parts_positions[7]][0]
    part7.y = coordinates[parts_positions[7]][1]
    #8 piece
    parts_positions[8] = random.randint(1, 9)
    while parts_positions[8] in taken:
        parts_positions[8] = random.randint(1, 9)
    taken.append(parts_positions[8])
    part8.x = coordinates[parts_positions[8]][0]
    part8.y = coordinates[parts_positions[8]][1]
    
    parts_positions["empty"] = random.randint(1, 9)
    while parts_positions["empty"] in taken:
            parts_positions["empty"] = random.randint(1, 9)
#Drawing
def draw():
    global mode
    if mode == "start":
        start()
        mode = "game"
    elif mode == 'game':
        screen.fill((256, 250, 250))
        part1.draw()
        part2.draw()
        part3.draw()
        part4.draw()
        part5.draw()
        part6.draw()
        part7.draw()
        part8.draw()
        restart_button.draw()
        screen.draw.text("Начать заново", center=(820, 223), color="#020202", fontsize = 24)
        collection_button.draw()
        screen.draw.text("Выбрать рисунок", center=(820, 373), color="#020202", fontsize = 24)
        screen.draw.text("Пятнашки", center=(820, 100), color="#020202", fontsize = 50, background="#FFE4B5")
        if is_correct():
            mode = "win"
    elif mode == "win":
        screen.fill((256, 246, 216))
        screen.draw.text("Победа!", center=(500, 250), color="#020202", fontsize = 60)
    elif mode == "collection":
        screen.fill((236, 256, 216))
        screen.draw.text("Выбери животное Малевича:)", center=(500, 100), color="#020202", fontsize = 40)
        cat_small.draw()
        screen.draw.text("Кот", center=(180, 220), color="#404040", fontsize = 18)
        dragon_small.draw()
        screen.draw.text("Дракон", center=(500, 220), color="#404040", fontsize = 18)
        corgi_small.draw()
        screen.draw.text("Временно недоступно", center=(820, 220), color="#404040", fontsize = 18)
        
    else:
        screen.fill((256, 246, 216))
        screen.draw.text("Error!", center=(500, 2500), color="#020202", fontsize = 60)
        
        
#Clicks handling
def on_mouse_down(button, pos):
    global mode
    if button == mouse.LEFT and mode == 'game':
        if part1.collidepoint(pos):
            if parts_positions["empty"] in adjacent[parts_positions[1]]:
                tmp = parts_positions[1]
                parts_positions[1] = parts_positions["empty"]
                parts_positions["empty"] = tmp
                part1.x = coordinates[parts_positions[1]][0]
                part1.y = coordinates[parts_positions[1]][1]
        elif part2.collidepoint(pos):
            if parts_positions["empty"] in adjacent[parts_positions[2]]:
                tmp = parts_positions[2]
                parts_positions[2] = parts_positions["empty"]
                parts_positions["empty"] = tmp
                part2.x = coordinates[parts_positions[2]][0]
                part2.y = coordinates[parts_positions[2]][1]
        elif part3.collidepoint(pos):
            if parts_positions["empty"] in adjacent[parts_positions[3]]:
                tmp = parts_positions[3]
                parts_positions[3] = parts_positions["empty"]
                parts_positions["empty"] = tmp
                part3.x = coordinates[parts_positions[3]][0]
                part3.y = coordinates[parts_positions[3]][1]
        elif part4.collidepoint(pos):
            if parts_positions["empty"] in adjacent[parts_positions[4]]:
                tmp = parts_positions[4]
                parts_positions[4] = parts_positions["empty"]
                parts_positions["empty"] = tmp
                part4.x = coordinates[parts_positions[4]][0]
                part4.y = coordinates[parts_positions[4]][1]
        elif part5.collidepoint(pos):
            if parts_positions["empty"] in adjacent[parts_positions[5]]:
                tmp = parts_positions[5]
                parts_positions[5] = parts_positions["empty"]
                parts_positions["empty"] = tmp
                part5.x = coordinates[parts_positions[5]][0]
                part5.y = coordinates[parts_positions[5]][1]
        elif part6.collidepoint(pos):
            if parts_positions["empty"] in adjacent[parts_positions[6]]:
                tmp = parts_positions[6]
                parts_positions[6] = parts_positions["empty"]
                parts_positions["empty"] = tmp
                part6.x = coordinates[parts_positions[6]][0]
                part6.y = coordinates[parts_positions[6]][1]
        elif part7.collidepoint(pos):
            if parts_positions["empty"] in adjacent[parts_positions[7]]:
                tmp = parts_positions[7]
                parts_positions[7] = parts_positions["empty"]
                parts_positions["empty"] = tmp
                part7.x = coordinates[parts_positions[7]][0]
                part7.y = coordinates[parts_positions[7]][1]
        elif part8.collidepoint(pos):
            if parts_positions["empty"] in adjacent[parts_positions[8]]:
                tmp = parts_positions[8]
                parts_positions[8] = parts_positions["empty"]
                parts_positions["empty"] = tmp
                part8.x = coordinates[parts_positions[8]][0]
                part8.y = coordinates[parts_positions[8]][1]
        if restart_button.collidepoint(pos):
            mode="start"
        if collection_button.collidepoint(pos):
            mode="collection"
    if button == mouse.LEFT and mode == 'collection':
        if dragon_small.collidepoint(pos):
            part1.image = "images/image2_part_001"
            part2.image = "images/image2_part_002"
            part3.image = "images/image2_part_003"
            part4.image = "images/image2_part_004"
            part5.image = "images/image2_part_005"
            part6.image = "images/image2_part_006"
            part7.image = "images/image2_part_007"
            part8.image = "images/image2_part_008"
            mode = "start"
        elif cat_small.collidepoint(pos):
            part1.image = "images/image_part_001"
            part2.image = "images/image_part_002"
            part3.image = "images/image_part_003"
            part4.image = "images/image_part_004"
            part5.image = "images/image_part_005"
            part6.image = "images/image_part_006"
            part7.image = "images/image_part_007"
            part8.image = "images/image_part_008"
            mode = "start"
        