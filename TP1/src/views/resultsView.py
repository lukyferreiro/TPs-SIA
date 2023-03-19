import arcade
from src.utils import get_dimensions, get_solution_steps, get_frontier_nodes

class ResultsView(arcade.View):
    
    def __init__(self, visited, solution, time, bfs):
        """ Set up the application. """
        super().__init__()
        self.visited = visited
        self.solution = solution
        self.time = time
        self.bfs = bfs

    def on_show_view(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        
        ALGORITHM = self.window.algorithm_type
        HEURISITC = self.window.heuristic_type

        if ALGORITHM == 'GREEDY' or ALGORITHM == 'A*':
            arcade.draw_text(f"Results with {ALGORITHM} and heuristic '{HEURISITC}'",
                            self.window.width / 2, 
                            self.window.height - (self.window.width/6),
                            arcade.color.WHITE, 
                            font_size=self.window.width/22, 
                            anchor_x="center", 
                            font_name="Kenney Future", 
                            multiline=True, 
                            align="center", 
                            width=self.window.width - 50)
        else: 
            arcade.draw_text(f"Your results with {ALGORITHM}",
                            self.window.width / 2, 
                            self.window.height - (self.window.width/6),
                            arcade.color.WHITE, 
                            font_size=self.window.width/22, 
                            anchor_x="center", 
                            font_name="Kenney Future", 
                            multiline=True, 
                            align="center", 
                            width=self.window.width - 50)
        
        if self.bfs:
            solution_cost = len(self.solution)
            solution_steps = get_solution_steps(self.solution)
        else:
            solution_cost = len(self.visited)
            solution_steps = get_solution_steps(self.visited)

        arcade.draw_text(f"Board dimension: {get_dimensions(self.visited)}\n"
                         f"Solution cost: {solution_cost} turns\n"
                         f"Frontier nodes: {get_frontier_nodes(self.visited)} nodes\n"
                         f"Expanded nodes: {len(self.visited)} nodes\n"
                         f"Processing time: {self.time} ms\n"
                         f"Solution steps: {solution_steps}\n",
                         self.window.width / 2, 
                         (self.window.height / 2+(self.window.width/15))-self.window.width/5,
                         arcade.color.WHITE, 
                         font_size=self.window.width/26, 
                         anchor_x="center",
                         multiline=True, 
                         align="left", 
                         width=self.window.width - 50)