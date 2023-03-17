import arcade
from src.fillZoneView import FillZone

class InstructionView(arcade.View):
    """ View to show instructions """

    def on_show_view(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        arcade.draw_text("Fill Zone", self.window.width / 2, self.window.height - (self.window.width/6),
                         arcade.color.WHITE, font_size=self.window.width/12, anchor_x="center", font_name="Kenney Future")
        arcade.draw_text("Instructions Screen", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=self.window.width/15, anchor_x="center")
        arcade.draw_text("Press 'R' to reset the game", self.window.width / 2, (self.window.height/2) - (self.window.width/12),
                         arcade.color.WHITE, font_size=self.window.width/24, anchor_x="center")
        arcade.draw_text("Click to advance", self.window.width / 2, (self.window.height/2) - (self.window.width/3),
                         arcade.color.WHITE, font_size=self.window.width/20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = FillZone()
        game_view.setup()
        self.window.show_view(game_view)