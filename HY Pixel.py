import random
n=int(input('''HY-Pixel
              \n Menu
            \n1.Minecraft
            \n2.hanged man
            \nSelect 1 or 2: '''))

if n==1:
    from ursina import *
    from ursina.prefabs.first_person_controller import FirstPersonController

    app = Ursina()
    grass_texture = load_texture('assets/grass_block.png')
    stone_texture = load_texture('assets/stone_block.png')
    brick_texture = load_texture('assets/brick_block.png')
    dirt_texture  = load_texture('assets/dirt_block.png')
    sky_texture   = load_texture('assets/skybox.png')
    arm_texture   = load_texture('assets/arm_texture.png')
    punch_sound   = Audio('assets/punch_sound',loop = False, autoplay = False)
    block_pick = 1

    window.fps_counter.enabled = True
    window.exit_button.visible = True

    def update():
            global block_pick

            if held_keys['right mouse'] or held_keys['left mouse']:
                hand.active()
            else:
                hand.passive()

            if held_keys['1']: block_pick = 1
            if held_keys['2']: block_pick = 2
            if held_keys['3']: block_pick = 3
            if held_keys['4']: block_pick = 4

    class Voxel(Button):
            def __init__(self, position = (0,0,0), texture = grass_texture):
                    super().__init__(
                            parent = scene,
                            position = position,
                            model = 'assets/block',
                            origin_y = 0.5,
                            texture = texture,
                            color = color.color(0,0,random.uniform(0.9,1)),
                            scale = 0.5)

            def input(self,key):
                    if self.hovered:
                            if key == 'right mouse down':
                                    punch_sound.play()
                                    if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                                    if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                                    if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
                                    if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)

                            if key == 'left mouse down':
                                    punch_sound.play()
                                    destroy(self)

    class Sky(Entity):
            def __init__(self):
                    super().__init__(
                            parent = scene,
                            model = 'sphere',
                            texture = sky_texture,
                            scale = 200,
                            double_sided = True)

    class Hand(Entity):
            def __init__(self):
                    super().__init__(
                            parent = camera.ui,
                            model = 'assets/arm',
                            texture = arm_texture,
                            scale = 0.2,
                            rotation = Vec3(150,-10,0),
                            position = Vec2(0.4,-0.6))

            def active(self):
                    self.position = Vec2(0.3,-0.5)

            def passive(self):
                    self.position = Vec2(0.4,-0.6)

    for z in range(21):
            for x in range(21):
                    voxel = Voxel(position = (x,0,z))

    player = FirstPersonController()
    sky = Sky()
    hand = Hand()

    app.run()
    k = held_keys['Esc']
    if k == held_keys['Esc']:
        print('\nExiting the program')
        ww 
        
    

elif n==2:
      
    word_list = ['wares','soup','mount','extend','brown','expert','tired','humidity','backpack','crust','dent','market','knock','smite','windy']

    



    def get_word():
        word = random.choice(word_list)
        return word.upper()


    def play(word):
        word_completion = "-" * len(word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6
        print("Let's play Hangman!")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
        while not guessed and tries > 0:
            guess = input("Please guess a letter or word: ").upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You already guessed the letter", guess)
                elif guess not in word:
                    print(guess, "is not in the word.")
                    tries -= 1
                    guessed_letters.append(guess)
                else:
                    print("Good job,", guess, "is in the word!")
                    guessed_letters.append(guess)
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "-" not in word_completion:
                        guessed = True
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print("You already guessed the word", guess)
                elif guess != word:
                    print(guess, "is not the word.")
                    tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = word
            else:
                print("Not a valid guess.")
            print(display_hangman(tries))
            print(word_completion)
            print("\n")
        if guessed:
            print("Congrats, you guessed the word! You win!")
        else:
            print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


    def display_hangman(tries):
        stages = [  # final state: head, torso, both arms, and both legs
                    """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                    """,
                    # head, torso, both arms, and one leg
                    """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / 
                       -
                    """,
                    # head, torso, and both arms
                    """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |      
                       -
                    """,
                    # head, torso, and one arm
                    """
                       --------
                       |      |
                       |      O
                       |     \\|
                       |      |
                       |     
                       -
                    """,
                    # head and torso
                    """
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |     
                       -
                    """,
                    # head
                    """
                       --------
                       |      |
                       |      O
                       |    
                       |      
                       |     
                       -
                    """,
                    # initial empty state
                    """
                       --------
                       |      |
                       |      
                       |    
                       |      
                       |     
                       -
                    """
        ]
        return stages[tries]


    def main():
        word = get_word()
        play(word)
        while input("Play Again? (Y/N) ").upper() == "Y":
            word = get_word()
            play(word)


    if __name__ == "__main__":
        main()

else:
    print("Game not yet added")

