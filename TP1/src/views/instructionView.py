import arcade
from src.views.algorithmsView import AlgorithmsView

""" View to show instructions """
class InstructionView(arcade.View):
    
    def on_show_view(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        arcade.draw_text("Fill Zone",
                         self.window.width / 2, 
                         self.window.height - (self.window.width/6),
                         arcade.color.WHITE, 
                         font_size=self.window.width/12, 
                         anchor_x="center", 
                         font_name="Kenney Future")
        arcade.draw_text("Instructions Screen", 
                         self.window.width / 2, 
                         self.window.height / 2,
                         arcade.color.WHITE, 
                         font_size=self.window.width/15, 
                         anchor_x="center")
        arcade.draw_text("When finish selecting option,\n"
                          "press ENTER to view results", 
                         self.window.width / 2, 
                         self.window.height / 2.5,
                         arcade.color.WHITE, 
                         font_size=self.window.width/25, 
                         multiline=True, 
                         anchor_x="center",
                         align="center",
                         width=self.window.width - 50)
        arcade.draw_text("Click to advance", 
                         self.window.width / 2, 
                         (self.window.height/2) - (self.window.width/3),
                         arcade.color.WHITE, 
                         font_size=self.window.width/20, 
                         anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        algorithm_view = AlgorithmsView()
        self.window.show_view(algorithm_view)