import math
import random
import pygame
from pygame import mixer
import gameObjects
import sqlite3

# Connect to SQLite database
def connect_db():
    return sqlite3.connect("leaderboard.db")

# Initialize the table
def init_db():
    conn = connect_db()
    cursor = conn.cursor()

    # Create the leaderboard table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            score INTEGER NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()
init_db()

# Add a user with their score
def add_user(username, score):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO leaderboard (username, score) VALUES (?, ?)", (username, score))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"User '{username}' already exists.")
    finally:
        conn.close()

# Update a user's score
def update_score(username, score):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE leaderboard SET score = ? WHERE username = ?", (score, username))
    conn.commit()
    print(f"User '{username}' score updated to {score}.")
    conn.close()

# Display the leaderboard
def display_leaderboard():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Fetch all users sorted by score in descending order
    cursor.execute("SELECT username, score FROM leaderboard ORDER BY score DESC")
    rows = cursor.fetchall()

    print("\nLeaderboard:")
    print("-------------")
    for rank, (username, score) in enumerate(rows, start=1):
        print(f"{rank}. {username}: {score} points")
    print("-------------\n")

    conn.close()

def play_game():
    # creating target objects
    target1 = gameObjects.target(round(random.randrange(50, 750), -1), round(random.randrange(50, 550), -1),
                                 'icon/target.png')
    target2 = gameObjects.target(round(random.randrange(50, 750), -1), round(random.randrange(50, 550), -1),
                                 'icon/target.png')
    target3 = gameObjects.target(round(random.randrange(50, 750), -1), round(random.randrange(50, 550), -1),
                                 'icon/target.png')
    bonus_target = gameObjects.target(round(random.randrange(50, 750), -1), round(random.randrange(50, 550), -1),
                                      'icon/question-mark.png')
    sec_bonus_target = gameObjects.target(round(random.randrange(50, 750), -1), round(random.randrange(50, 550), -1),
                                          'icon/timer.png')

    # intialize pygame
    pygame.init()

    # creat the screen
    screen = pygame.display.set_mode((800, 700))

    # game icon & title
    pygame.display.set_caption("Mini Game")
    pygame.display.set_icon(pygame.image.load('icon/gun.png'))

    # backround music and sounds
    mixer.music.load('sounds/background.mp3')
    mixer.music.set_volume(0.1)
    mixer.music.play(-1)
    shooting_sound = mixer.Sound('sounds/shoot.wav')
    rand_target_sound = mixer.Sound('sounds/rand-prize.wav')
    target_sound = mixer.Sound('sounds/target.wav')
    finish_sound = mixer.Sound('sounds/finish.wav')

    # display game objects
    def show_object(obj):
        screen.blit(pygame.image.load(obj.icon), (obj.positionx, obj.positiony))

    def show_shots(obj, position):
        screen.blit(pygame.image.load(obj.icon), position)

    # calculate distance
    def distance(obj1, obj2):
        res = math.sqrt(
            ((obj1.positionx - 2) - (obj2.positionx - 11)) ** 2 + ((obj1.positiony - 2) - (obj2.positiony - 11)) ** 2)
        return res

    # check if target is hit
    def is_hit(player):
        if distance(player, target1) < 10:
            return ([True, target1])
        elif distance(player, target2) < 10:
            return ([True, target2])
        elif distance(player, target3) < 10:
            return ([True, target3])
        elif distance(player, bonus_target) < 10:
            return ([True, bonus_target])
        elif distance(player, sec_bonus_target) < 10:
            return ([True, sec_bonus_target])
        return ([False, None])

    # show timer and scores
    font = pygame.font.Font('freesansbold.ttf', 14)
    ending_font = pygame.font.Font('freesansbold.ttf', 50)

    def display_game_stats(player, timer, score, bullets, positionx, positiony):
        game_stats = font.render(f'{player} - score : {score} - timer : {timer} - bullets: {bullets}', True,
                                 (255, 255, 255))
        screen.blit(game_stats, (positionx, positiony))

    # bg image
    bg = pygame.image.load('icon/bg.png')
    bg = pygame.transform.scale(bg, (800, 600))

    #game loop
    running = True

    # Create a clock object to manage time
    clock = pygame.time.Clock()

    # Initialize the last tick
    last_tick = pygame.time.get_ticks()

    while running:
        if (not player1.have_timer() and not player2.have_timer()) or (not player1.have_bullets() and not player2.have_bullets() or (not player1.have_timer() and not  player2.have_bullets()) or (not player1.have_bullets() and not player2.have_timer())):
            screen.fill((0,0,0))
            # finish_sound.play()
            if player1.get_score() > player2.get_score():
                winner = player1
            elif player1.get_score() < player2.get_score():
                winner = player2
            else:
                winner = None
            if winner is not None:
                ending = ending_font.render(f'{winner.name} won!!', True, (255,255,255))
                screen.blit(ending,(280,300))
            else:
                ending = ending_font.render(f'tie!!', True, (255,255,255))
                screen.blit(ending, (350, 300))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    running = False
        else:
            # Get the current time
            current_tick = pygame.time.get_ticks()

            # Check if one second has passed
            if current_tick - last_tick >= 1000:
                player1.dec_timer()
                player2.dec_timer()
                last_tick = current_tick


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                #move player 1 and limit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and player1.positionx > 0:
                        player1.move(True,False)
                    if event.key == pygame.K_RIGHT and player1.positionx < 780:
                        player1.move(True,True)
                    if event.key == pygame.K_UP and player1.positiony > 0:
                        player1.move(False,False)
                    if event.key == pygame.K_DOWN and player1.positiony < 580:
                        player1.move(False, True)

                    # player 1 shoot target
                    if event.key == pygame.K_SPACE and player1.have_bullets() and player1.have_timer():
                        player1.shoot()
                        shooting_sound.play()
                        res = is_hit(player1)
                        if res[0] and res[1] != bonus_target and res[1] != sec_bonus_target:
                            target_sound.play()
                            res[1].set_position()
                            if player1.lastShot:
                                player1.score_prize()
                            else:
                                player1.set_score(player1.shots[len(player1.shots) - 2], player1.shots[len(player1.shots) - 1])
                            player1.lastShot = True
                        elif res[0] and res[1] == bonus_target:
                            rand_target_sound.play()
                            player1.set_bonus()
                            bonus_target.set_position()
                            player1.lastShot = False
                        elif res[0] and res[1] == sec_bonus_target:
                            rand_target_sound.play()
                            player2.lose_timer()
                            sec_bonus_target.set_position()
                            player1.lastShot = False
                        else:
                            player1.lastShot = False

                    #move player 2 and limit
                    if event.key == pygame.K_a and player2.positionx > 0:
                        player2.move(True, False)
                    if event.key == pygame.K_d and player2.positionx < 780:
                        player2.move(True, True)
                    if event.key == pygame.K_w and player2.positiony > 0:
                        player2.move(False, False)
                    if event.key == pygame.K_s and player2.positiony < 580:
                        player2.move(False, True)

                    # player 2 shoot target
                    if event.key == pygame.K_x and player2.have_bullets() and player2.have_timer():
                        player2.shoot()
                        shooting_sound.play()
                        res = is_hit(player2)
                        if res[0] and res[1] != bonus_target and res[1] != sec_bonus_target:
                            target_sound.play()
                            res[1].set_position()
                            if player2.lastShot:
                                player2.score_prize()
                            else:
                                player2.set_score(player2.shots[len(player2.shots) - 2], player2.shots[len(player2.shots) - 1])
                            player2.lastShot = True
                        elif res[0] and res[1] == bonus_target:
                            rand_target_sound.play()
                            player2.set_bonus()
                            bonus_target.set_position()
                            player2.lastShot = False
                        elif res[0] and res[1] == sec_bonus_target:
                            rand_target_sound.play()
                            player1.lose_timer()
                            sec_bonus_target.set_position()
                            player2.lastShot = False
                        else:
                            player2.lastShot = False

            #set background color & image
            screen.fill((0, 0, 0))
            screen.blit(bg, (0,0))

            #display objects
            show_object(target1)
            show_object(target2)
            show_object(target3)
            show_object(bonus_target)
            show_object(sec_bonus_target)
            for i in player1.shots[1:]:
                show_shots(player1, (i[0],i[1]))
            for i in player2.shots[1:]:
                show_shots(player2, (i[0],i[1]))
            display_game_stats(player1.name,player1.get_timer(),player1.get_score(),player1.get_bullets(), 40,650)
            display_game_stats(player2.name, player2.get_timer(), player2.get_score(), player2.get_bullets(), 450, 650)
            pygame.display.update()
            if (not player1.have_timer() and not player2.have_timer()) or (not player1.have_bullets() and not player2.have_bullets()):
                finish_sound.play()
    update_score(pn1,player1._score)
    update_score(pn2,player2._score)

while True:
    ans = input('play game : 1\nleaderboard : 2\n exit : 3\n')
    if ans == '1':
        # getting players name
        while True:
            pn1 = input('enter name of first player: ')
            pn2 = input('enter name of second player: ')
            add_user(pn1, 0)
            add_user(pn2, 0)
            if pn1 != pn2:
                break
            else:
                print('enter different names')

        # creat player object
        player1 = gameObjects.Player(pn1, round(random.randrange(50, 750), -1), round(random.randrange(50, 550), -1),
                                     'icon/blue-dot.png')
        player2 = gameObjects.Player(pn2, round(random.randrange(50, 750), -1), round(random.randrange(50, 550), -1),
                                     'icon/red-dot.png')
        play_game()

    elif ans == '2':
        display_leaderboard()

    elif ans == '3':
        break
