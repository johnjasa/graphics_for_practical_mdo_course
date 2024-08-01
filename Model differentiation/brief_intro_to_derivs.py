from manim import *
import numpy as np
from manim_helper_functions import *


class TitleSlide(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        title = r"Brief intro to derivatives"
        contents_list = [
            "What is a derivative?",
            "Types of derivatives (partials and totals)",
            "Benefits and costs of using derivatives",
            ]
        intro_message = "Derivatives are necessary to effectively guide gradient-based optimizers and Newton solvers to the correct answers."
        outro_message = "A basic understanding of derivatives will make your journey using gradient-based optimizers much easier."
        make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["diff"])

class DerivativeBasics(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"
        self.camera.frame.save_state()

        fd = MathTex(r"\frac{\partial f}{\partial x} = \text{the change of $f$ per unit change in $x$")
        self.play(Write(fd))
        self.wait()
        self.play(FadeOut(fd))
        self.wait()

        ax = Axes(x_range=[0, 10], y_range=[0, 10])
        plot = ax.plot(lambda x: np.sin(x) - 0.05*x**2 + x + 2)
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")
        text1 = MathTex(r"y = \sin(x) - \frac{x^2}{20} + x + 2", font_size=36).move_to(ax.c2p(4., 6., 0))

        self.play(Create(ax), Create(labels))
        self.play(Create(plot), Create(text1))

        self.wait()

        x_point = ValueTracker(1.)

        def draw_tangent_line_on_curve(input_plot, x, ax=ax):
            moving_slope = always_redraw(
                lambda: ax.get_secant_slope_group(
                    x=x.get_value(),
                    graph=input_plot,
                    dx=1.e-6,
                    dx_line_color=WHITE,
                    secant_line_length=2,
                    secant_line_color=RED,
                )
            )

            dot1 = always_redraw(
                lambda: Dot(color=RED, z_index=999, radius=0.05).move_to(
                    ax.c2p(x.get_value(), input_plot.underlying_function(x.get_value()))
                )
            )

            return moving_slope, dot1

        moving_slope, dot1 = draw_tangent_line_on_curve(plot, x_point)

        self.play(Create(moving_slope), Create(dot1))
        self.wait()
        self.play(x_point.animate.set_value(5.), run_time=3, rate_func=linear)
        self.wait()

        self.play(FadeOut(moving_slope, dot1))
        self.wait()

        ax2 = Axes(x_range=[0, 10], y_range=[0, 10]).shift(6.5*DOWN)
        self.play(self.camera.frame.animate.move_to(ax2), Create(ax2))
        self.wait()

        plot2 = ax2.plot(lambda x: np.cos(x) - 0.1*x + 1)
        labels2 = ax2.get_axis_labels(x_label="x", y_label="").shift(6*DOWN)
        text2 = MathTex(r"\frac{\partial y}{\partial x} = \cos(x) - \frac{x}{10} + 1", font_size=36).move_to(ax2.c2p(3., 2., 0))
        self.play(Create(labels2), Create(plot2), Create(text2))
        self.wait()

        self.play(self.camera.frame.animate.scale(1.8).move_to([3., -3.5, 0.]))
        self.wait()

        x_point.set_value(1.)
        x2_point = ValueTracker(1.)

        slope2, dot2 = draw_tangent_line_on_curve(plot2, x2_point, ax2)
        self.play(Create(moving_slope), Create(dot1), Create(dot2))
        self.wait()

        self.play(x_point.animate.set_value(8.05022), x2_point.animate.set_value(8.05022), run_time=8, rate_func=linear)
        self.wait()

        self.play(Create(slope2))
        self.wait()




class PartialsTotals(MovingCameraScene):
    def setup(self):
        self.camera.background_color="#2d3c54"

        text = Tex(r"""Two main types of derivatives:""", font_size=60).shift(2.75*UP)
        self.play(Write(text))
        self.wait()

        text = Tex(r"""\raggedright{
{\Large Partial derivatives:}\\
Sensitivities of outputs wrt inputs for components\\
These do not consider any implicit coupling\\
Just a piece of the puzzle}""", font_size=40).shift(UP)
        self.play(Write(text))
        self.wait()

        text2 = Tex(r"""\raggedright{
{\Large Total derivatives:}\\
Sensitivities of systems' outputs wrt inputs\\
Essentially the objectives/constraints wrt design variables\\
The full puzzle put together}""", font_size=40).shift(2*DOWN).align_to(text, LEFT)
        self.play(Write(text2))
        self.wait()


class DerivSyn(MovingCameraScene):
    def setup(self):
        self.camera.background_color="#2d3c54"

        text = Tex(r"""\raggedright{
{\large These are all (essentially) synonyms:}\\
~\\
Derivatives\\
Gradients\\
Sensitivities\\
    }""", font_size=54)
        self.play(Write(text))
        self.wait()


class DerivativeCosts(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"
        self.camera.frame.save_state()

        ax = Axes(x_range=[1, 10], y_range=[0, 1], axis_config={"include_ticks" : False})
        plot = ax.plot(lambda x: 1 / x, stroke_width=4)
        labels = ax.get_axis_labels(x_label=r"\text{Implementation cost (developer time)}", y_label=r"\text{Computational cost}")
        labels[0].shift(DOWN+LEFT)

        self.play(Create(ax), Create(labels))
        self.play(Create(plot))

        self.wait()

        data = [
            [1.5, r"Finite difference"],
            [3., r"Complex step"],
            [5.5, r"Algorithmic differentiation"],
            [8.5, r"Analytic"],
        ]

        for (x_val, lab) in data:
            y_val = plot.underlying_function(x_val)
            dot = Dot(color=RED, z_index=999, radius=0.15).move_to(ax.c2p(x_val, y_val))
            if "differentiation" in lab:
                label = Tex(lab, font_size=48).align_to(dot, LEFT).align_to(dot, UP).shift(0.2*LEFT+0.6*UP)
            else:
                label = Tex(lab, font_size=48).align_to(dot, LEFT).align_to(dot, UP).shift(0.4*RIGHT+0.4*UP)
            self.play(Create(dot), Create(label))
            self.wait()

