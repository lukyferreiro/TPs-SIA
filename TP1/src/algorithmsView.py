import arcade
from src.fillZoneView import FillZone

class AlgorithmsView(arcade.View):
    
    def on_show_view(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        
        arcade.draw_text("Choose the "
                         "algorithm", self.window.width / 2, 
                         self.window.height - (self.window.width/6),
                         arcade.color.WHITE, 
                         font_size=self.window.width/14, 
                         anchor_x="center", 
                         font_name="Kenney Future", 
                         multiline=True, 
                         align="center", 
                         width=self.window.width - 50)
        
        arcade.draw_text("press the number to select the option", 
                         self.window.width / 2, 
                         self.window.height / 2+(self.window.width/12),
                         arcade.color.WHITE, 
                         font_size=self.window.width/20, 
                         anchor_x="center",
                         multiline=True, 
                         align="center", 
                         width=self.window.width - 50)
        
        arcade.draw_text("1- BFS\n"
                         "2- DFS\n"
                         "3- GREEDY\n"
                         "4- A*\n",
                         self.window.width / 2, 
                         (self.window.height / 2+(self.window.width/12))-self.window.width/6,
                         arcade.color.WHITE, 
                         font_size=self.window.width/24, 
                         anchor_x="center",
                         multiline=True, 
                         align="center", 
                         width=self.window.width - 50)
        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.KEY_1:
            self.window.algorithm_type = 'BFS'
            game_view = FillZone()
            game_view.setup()
            self.window.show_view(game_view)

        elif key == arcade.key.KEY_2:
            self.window.algorithm_type = 'DFS'
            game_view = FillZone()
            game_view.setup()
            self.window.show_view(game_view)