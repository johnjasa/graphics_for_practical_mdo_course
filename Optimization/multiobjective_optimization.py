from manim import *
import numpy as np
from manim_helper_functions import *
import random
random.seed(314)
from shapely.geometry import Point
from shapely.geometry import Polygon as shapelyPolygon



def generate_random(number, polygon):
    points = []
    minx, miny, maxx, maxy = polygon.bounds
    while len(points) < number:
        pnt = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
        if polygon.contains(pnt):
            points.append(pnt)
    return points


class TrioVenn(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"
        write_caption(self, "Multiobjective optimization seeks to optimize multiple objective functions simultaneously.")
        make_venn(self, types=["opt"])


class TitleSlide(Scene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        title = r"Multiobjective optimization"
        contents_list = [
            "Context for multiobjective optimization",
            "Weighted sum method",
            "Pareto fronts",
            "Epsilon-constraint method",
            ]
        intro_message = "To perform multiobjective optimization you need to use predefined weightings for each objective or constrain other objective values while optimizing a singular one."
        outro_message = "Multiobjective optimization is somewhat a misnomer -- you need to use predefined weightings for each of the objectives or implement them as constraints. A Pareto front is a good way to examine trade-offs between objectives and the epsilon-constraint method is the preferred way to construct the front."

        make_title_slide(self, title, contents_list, intro_message, outro_message)


class Multiobjective(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        objective = MathTex(r"f_{\text{obj}}(x) = g(x)")

        self.play(FadeIn(objective))

        self.wait()

        multiobjective = MathTex(r"f_{\text{obj}}(x) = g(x) + h(x)")

        self.play(Transform(objective, multiobjective))

        self.wait()

        scaled_multiobjective = MathTex(r"f_{\text{obj}}(x) = \alpha \frac{g(x)}{g_0} + \beta \frac{h(x)}{h_0}")

        self.play(Transform(objective, scaled_multiobjective))

        self.wait()

        objective.generate_target()
        objective.target.move_to(2.5*DOWN)
        self.play(MoveToTarget(objective))

        image = ImageMobject("737.jpg")
        image.height = 4
        image.shift(UP)
        image_caption = Text(r"© Aero Icarus, 2011", font_size=12)
        # image_caption.shift(UP)

        self.play(FadeIn(image), FadeIn(image_caption))

        self.wait()

        united_objective = MathTex(r"f_{\text{obj}}(x) = f_{\text{structural weight}(x)} [\text{kg}] + f_{C_D}")
        united_objective.shift(2.5*DOWN)

        self.play(Transform(objective, united_objective))

        self.wait()

        scaled_multiobjective = MathTex(r"f_{\text{obj}}(x) = \alpha \frac{f_{\text{structural weight}(x)} [\text{kg}]}{2700 [\text{kg}]} + \beta \frac{f_{C_D}}{0.025}")
        scaled_multiobjective.shift(2.5*DOWN)
        self.play(Transform(objective, scaled_multiobjective))
        self.wait()

        scaled_multiobjective = MathTex(r"f_{\text{obj}}(x) = 0.9 \frac{f_{\text{structural weight}(x)} [\text{kg}]}{2700 [\text{kg}]} + 0.1 \frac{f_{C_D}}{0.025}")
        scaled_multiobjective.shift(2.5*DOWN)
        self.play(Transform(objective, scaled_multiobjective))
        self.wait()

        scaled_multiobjective = MathTex(r"f_{\text{obj}}(x) = 0.1 \frac{f_{\text{structural weight}(x)} [\text{kg}]}{2700 [\text{kg}]} + 0.9 \frac{f_{C_D}}{0.025}")
        scaled_multiobjective.shift(2.5*DOWN)
        self.play(Transform(objective, scaled_multiobjective))
        self.wait()

        scaled_multiobjective = MathTex(r"f_{\text{obj}}(x) = 0.5 \frac{f_{\text{structural weight}(x)} [\text{kg}]}{2700 [\text{kg}]} + 0.5 \frac{f_{C_D}}{0.025}")
        scaled_multiobjective.shift(2.5*DOWN)
        self.play(Transform(objective, scaled_multiobjective))
        self.wait()


class Pareto(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"
        self.camera.frame.save_state()

        write_caption(self, "Pareto frontiers (or fronts) show the trade-offs between optimal designs for multiple objectives.")
        
        # create the axes and the curve
        ax = Axes(x_range=[190000, 230000, 5000], y_range=[80000, 125000, 5000], axis_config={"include_numbers": True})
        x_data = np.array([192999.4, 196868.1, 200835, 203791.5, 209339.8, 221850.9])
        y_data = np.array([122904.7, 100998.6, 96588.7, 93228.5, 90595.9, 88878])
        plot = ax.plot_line_graph(x_data, y_data, line_color=GREEN, vertex_dot_style={'color' : GREEN})
        labels = ax.get_axis_labels(x_label=r"\text{Zero-fuel weight [kg]}", y_label=r"\text{Fuel burn [kg]}")
        self.camera.frame.scale(1.1)


        caption = Tex("Pareto data from Brooks et al 2020 https://doi.org/10.2514/1.C035699", font_size=20)
        caption.align_to(ax.get_edge_center(DOWN), UP)
        caption.shift(0.2*DOWN)
        self.play(Create(ax), Create(labels))


        full_x_data = np.hstack((x_data, np.array((193.e3, 230.e3, 230.e3))))
        full_y_data = np.hstack((y_data, np.array((125.e3, 125.e3, 88.878e3))))
        
        poly_points = tuple(map(tuple, zip(full_x_data, full_y_data)))
        poly = shapelyPolygon(poly_points)

        points = generate_random(100, poly)

        dots = VGroup()
        for idx, point in enumerate(points):
            dot = Dot(ax.c2p(point.x, point.y))
            dots += dot
        special_dot = Dot(ax.c2p(209.e3, 108.e3))
        all_dots = VGroup(dots, special_dot)
        self.play(LaggedStart(Create(all_dots), lag_ratio=0.1, run_time=2))
        self.wait()


        self.play(Create(plot), Create(caption))

        objective = MathTex(r"f_{\text{obj}} = \beta \text{FB} + (1 - \beta ) \text{ZFW}")
        objective.shift(2*UP, 2*RIGHT)

        self.wait(1)
        self.play(FadeOut(dots))

        self.wait(1)

        horiz_arrow = Arrow(start=ax.c2p(209.e3, 108.e3), end=ax.c2p(205.e3, 108.e3), buff=0.)
        self.play(FadeIn(horiz_arrow))
        self.wait()
        self.play(FadeOut(horiz_arrow))

        vert_arrow = Arrow(start=ax.c2p(209.e3, 108.e3), end=ax.c2p(209.e3, 99.e3), buff=0.)
        self.play(FadeIn(vert_arrow))
        self.wait()
        self.play(FadeOut(vert_arrow))

        self.play(FadeOut(special_dot))

        beta_vals = [0., .35, .5, .65, .8, 1.]
        captions = []
        for idx, dot in enumerate(plot["vertex_dots"]):
            caption = MathTex(r"\beta = " + str(beta_vals[idx]), font_size=30)
            caption.move_to(dot)
            caption.align_to(dot.get_edge_center(RIGHT), LEFT)
            if idx > 0:  # skip the first label for alignment reasons
                caption.align_to(dot.get_edge_center(UP), DOWN)
            captions.append(caption)

        self.play(FadeIn(*captions), FadeIn(objective))

        self.wait(5)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )


class EpsilonConstrained(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"
        self.camera.frame.save_state()

        table = r"""
            Minimize & $f_{\text{obj}}(x)$ \\
        """

        table2 = r"""
            Minimize & $f_{\text{obj}}(x)$ \\
            Subject to: & \\
            Epsilon constraint & $g(x) = g_0 $ \\
        """

        text_list = [table, table2]

        beg_lines = r"""
            \begin{table}[]
            \def\arraystretch{1.0}
            \centering
            \begin{tabular}{rl}"""

        lagged_write(self, text_list, beginning_text=beg_lines, delay=3, final_text=r"""
            \end{tabular}
            \end{table}""")

        self.wait(2)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

        # create the axes and the curve
        ax = Axes(x_range=[190000, 230000, 5000], y_range=[80000, 125000, 5000], axis_config={"include_numbers": True})
        x_data = np.linspace(195.e3, 225.e3, 7, endpoint=True)
        y_data = np.array([121.e3, 101.e3, 97.e3, 94.e3, 92.e3, 91.e3, 90.5e3])

        plots = VGroup()
        for x in x_data:
            plots += ax.get_vertical_line(ax.c2p(x, 125000))

        labels = ax.get_axis_labels(x_label=r"\text{Zero-fuel weight [kg]}", y_label=r"\text{Fuel burn [kg]}")
        self.camera.frame.scale(1.1)

        self.play(Create(ax), Create(labels))
        self.play(Create(plots))

        self.wait()

        dots = VGroup()
        for x, y in zip(x_data, y_data):
            dot = Dot(ax.c2p(x, 125.e3), color=RED)
            dots += dot

        self.play(Create(dots))
        self.wait()

        dots_animations = []
        for idx, dot in enumerate(dots):
            dots_animations.append(dot.animate.move_to(ax.c2p(x_data[idx], y_data[idx])).set_color(GREEN))
        self.play(LaggedStart(*dots_animations, lag_ratio=0.1, run_time=2))
        self.wait()

        plot = ax.plot_line_graph(x_data, y_data, add_vertex_dots=False, line_color=GREEN)
        self.play(FadeOut(plots), FadeIn(plot))

        self.wait(5)
