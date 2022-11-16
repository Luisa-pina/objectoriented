import arcade
import random

class Comp151Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width,height,"Demo Window")
        self.player =None
        self.targets = arcade.SpriteList()
        self.score = 0
        self.sound = None
        self.player_dx = 0

#setting up the function
    def setup(self):
        self.sound = arcade.load_sound("elec_lightning.wav")
        self.player = arcade.Sprite(f"f1-ship1-6.png")
        for number in range(5): # to add more Rock
            rock = arcade.Sprite(":resources:images/space_shooter/meteorGrey_med1.png")
            self.targets.append(rock)
            rock.center_x= random.randint(16,666)
            rock.center_y = random.randint(16,657)
        self.player.center_x = 500
        self.player.center_y = 400

#two other methods
    def on_update(self, delta_time): #the lastest update
        self.player.center_x += self.player_dx
        if self.player.center_x > 985:
            self.player.center_x = 0
            arcade.play_sound(self.sound)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.targets.draw()
        arcade.finish_render()

#using the Keybord input
def on_key_press(self, symbol, modifiers):
    if symbol == arcade.key.RIGHT:
        self.player_dx = 3
    elif symbol == arcade.key.LEFT:
        self.player_dx = -3
    elif symbol == arcade.key.UP:
        self.player_dx = 3

def on_key_release(self, symbol, modifiers):
    if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
        self.player_dx = 0
    elif symbol == arcade.key.UP:
        self.player_dx = 0

