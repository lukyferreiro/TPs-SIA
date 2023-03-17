import arcade
from src.instructionView import InstructionView
from src.utils import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE

def main():

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()