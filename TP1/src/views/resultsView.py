import arcade
from src.utils import show_data

class ResultsView(arcade.View):
    
    def on_show_view(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        
        arcade.draw_text(f"Your results with {self.window.algorithm_type}",
                          self.window.width / 2, 
                         self.window.height - (self.window.width/6),
                         arcade.color.WHITE, 
                         font_size=self.window.width/14, 
                         anchor_x="center", 
                         font_name="Kenney Future", 
                         multiline=True, 
                         align="center", 
                         width=self.window.width - 50)
        
        # Imprimir un resumen de los pasos.
        # Pasos
        # Nodos expandidos
        # Nodos frontera
        # Solución --> array mostrando los colores elegidos
        # Tiempo de Procesamiento
        # show_data(self.visited, self.time, self.solution, self.bfs, self.plot)
            
        
