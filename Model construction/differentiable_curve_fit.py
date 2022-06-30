from manim import *
import numpy as np
from openmdao.components.interp_util.interp import InterpND
from manim_helper_functions import make_title_slide

class TitleSlide(Scene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        title = r"Adding curve fits in a differentiable way"
        contents_list = ["Intro and motivation", "Simple (wrong) approach", "Correct approach", "Further notes and recommendations"]
        main_message = "You must fit a curve to data in a differentiable way if you're using gradient-based optimizers or a Newton solver."

        make_title_slide(self, title, contents_list, main_message)


class LinearInterpPlot(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"
        self.camera.frame.save_state()

        # create the axes and the curve
        ax = Axes(x_range=[0, 10], y_range=[0, 10])
        x_data = np.arange(11)
        y_data = np.array([3., 2.5, 2.3, 2., 5.6, 4.5, 6.7, 4.2, 3.1, 2.2, 2.1])
        plot = ax.plot_line_graph(x_data, y_data)
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        self.play(Create(ax), Create(labels))
        self.play(Create(plot["vertex_dots"]))

        self.wait(1)

        
        interp = InterpND(method='slinear', points=x_data, values=y_data)
        linear_plot = ax.plot(interp.interpolate, x_range=[0., 10.0, 0.01])
        self.play(Create(linear_plot), rate_func=linear)

        self.wait(1)

        self.play(self.camera.frame.animate.scale(0.25).move_to(plot["vertex_dots"][3]))

        self.wait(1)

        x_point = ValueTracker(2.5)

        def draw_tangent_line_on_curve(input_plot, tracked_value):
            moving_slope = always_redraw(
                lambda: ax.get_secant_slope_group(
                    x=tracked_value.get_value(),
                    graph=input_plot,
                    dx=0.00001,
                    secant_line_length=0.75,
                    secant_line_color=RED,
                )
            )

            dot = always_redraw(
                lambda: Dot(color=RED, radius=0.05).move_to(
                    ax.c2p(tracked_value.get_value(), input_plot.underlying_function(tracked_value.get_value()))
                )
            )

            return moving_slope, dot

        moving_slope, dot = draw_tangent_line_on_curve(linear_plot, x_point)

        self.play(FadeIn(moving_slope), FadeIn(dot))
        self.play(x_point.animate.set_value(3.5), run_time=3, rate_func=linear)
        self.wait()

        self.play(FadeOut(linear_plot), FadeOut(dot), FadeOut(moving_slope), Restore(self.camera.frame))

        x_point.set_value(2.5)


        interp = InterpND(method='akima', points=x_data, values=y_data, delta_x=0.1)
        akima_plot = ax.plot(interp.interpolate, x_range=[0., 10.0, 0.01])
        self.play(Create(akima_plot))
        
        self.play(self.camera.frame.animate.scale(0.25).move_to(plot["vertex_dots"][3]))

        moving_slope, dot = draw_tangent_line_on_curve(akima_plot, x_point)

        self.play(FadeIn(moving_slope), FadeIn(dot))
        self.play(x_point.animate.set_value(3.5), run_time=2, rate_func=linear)
        self.wait()

