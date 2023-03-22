import arcade
from src.views.fillZoneView import FillZone

class HeuristicsView(arcade.View):

    def on_show_view(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        
        arcade.draw_text("Choose the "
                         "heuristics", self.window.width / 2, 
                         self.window.height - (self.window.width/6),
                         arcade.color.WHITE, 
                         font_size=self.window.width/14, 
                         anchor_x="center", 
                         font_name="Kenney Future", 
                         multiline=True, 
                         align="center", 
                         width=self.window.width - 50)
        
        arcade.draw_text("Press the number to select the option", 
                         self.window.width / 2, 
                         self.window.height / 2+(self.window.width/12),
                         arcade.color.WHITE, 
                         font_size=self.window.width/20, 
                         anchor_x="center",
                         multiline=True, 
                         align="center", 
                         width=self.window.width - 50)
        
        arcade.draw_text("1. Remaining colors\n"
                         "2. Most neighbors\n"
                         "3. Dijkstra distance\n",
                         self.window.width / 2, 
                         (self.window.height / 2+(self.window.width/12))-self.window.width/4,
                         arcade.color.WHITE, 
                         font_size=self.window.width/28, 
                         anchor_x="center",
                         multiline=True, 
                         align="left", 
                         width=self.window.width - 50)
        
    def on_key_press(self, key, modifiers):
        match key:
            case arcade.key.KEY_1:
                self.window.heuristic_type = 'Remaining colors'
                game_view = FillZone()
                game_view.setup()
                self.window.show_view(game_view)

            case arcade.key.KEY_2:
                self.window.heuristic_type = 'Most neighbors'
                game_view = FillZone()
                game_view.setup()
                self.window.show_view(game_view)

            case arcade.key.KEY_3:
                self.window.heuristic_type = 'Dijkstra distance'
                game_view = FillZone()
                game_view.setup()
                self.window.show_view(game_view)