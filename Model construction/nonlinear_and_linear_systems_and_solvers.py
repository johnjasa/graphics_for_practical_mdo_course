from manim import *
import numpy as np
from manim_helper_functions import *


# class TitleSlide(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"

#         title = r"Nonlinear and linear systems and solvers"
#         contents_list = [
#             "What are nonlinear and linear systems?",
#             "Differences between nonlinear and linear solvers",
#             ]
#         intro_message = r"""1. In OpenMDAO terms, your nonlinear system is your model or governing system of equations. Your linear system is a behind-the-scenes linearization of your model.
#         ~\\
#         2. You need to use a nonlinear solver when there's backwards coupling or implicit systems; need to use linear solver when using derivatives for Newton solvers or optimizers."""
#         outro_message = "Think of your model as a nonlinear system in the most general sense and the corresponding linearized version of your model as a linear system. You must use the appropriate solvers to resolve coupling and compute derivatives accurately. "

#         make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["mda"])

# class Context(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"

#         write_caption(self, "In the most general case, you need both nonlinear and linear systems for coupled multidisciplinary models.")

#         message = 'Nonlinear system = your "physical" model'
#         caption = Tex("\\raggedright{" + message + "}").shift(UP)
#         self.play(Create(caption))
#         self.wait()

#         message = 'Linear system = a linearized approximation of your model'
#         caption2 = Tex("\\raggedright{" + message + "}").shift(DOWN)
#         self.play(Create(caption2))
#         self.wait()

#         clear(self)


class SystemGraph(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"
        self.camera.frame.save_state()

        fontsize = 36

        # create the axes and the curve
        ax = Axes(x_range=[0, 10], y_range=[0, 10])
        plot = ax.plot(lambda x: np.sin(x) - 0.05*x**2 + x + 4)
        plot2 = ax.plot(lambda x: 5.)
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")
        label = Tex("Nonlinear system", font_size=fontsize).shift(0.5*UP).shift(2*RIGHT)

        text1 = MathTex(r"y = \sin(x) - \frac{x^2}{20} + x + 4", font_size=36).move_to(ax.c2p(4., 8., 0))
        text2 = MathTex(r"y = 5", font_size=36) .move_to(ax.c2p(4., 4.5, 0))

        self.play(Create(ax), Create(labels))
        self.play(Create(plot), Create(plot2), Create(label), Create(text1), Create(text2))

        self.wait()

        x_point = ValueTracker(2)

        def draw_tangent_line_on_curve(input_plot, x):
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
        moving_slope2, dot2 = draw_tangent_line_on_curve(plot2, x_point)

        label2 = Tex("Linearization", color=RED, font_size=fontsize).move_to(ax.c2p(1.5, 7.4, 0.))

        self.play(Create(moving_slope), Create(dot1), Create(moving_slope2), Create(dot2))
        self.play(Create(label2))
        self.wait()

        self.play(FadeOut(plot, label, label2, moving_slope, dot1))
        self.wait()
        
        plot = ax.plot(lambda x: 2 + 0.5*x)
        moving_slope, dot1 = draw_tangent_line_on_curve(plot, x_point)
        
        label.move_to(ax.c2p(5., 5.6, 0.))
        self.play(Create(plot), Create(label))

        label2 = Tex("Linearization", color=RED, font_size=fontsize).move_to(ax.c2p(1.5, 3.75, 0.))

        self.play(Create(moving_slope), Create(dot1))
        self.play(Create(label2))
        self.wait()

        clear(self)

        text = write_caption(self, r"""
        Examples of systems that are called nonlinear systems in OpenMDAO:\\
        Finite element analysis (FEA)\\
        Vortex lattice methods (VLM)\\
        Computational fluid dynamics (CFD)\\
        Economics and cost models\\
        ~\\
        All of these also have corresponding linear systems that are used to compute gradient information.
        """,
        run_time=5)

        clear(self)


# class NewtonGraph(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"
#         self.camera.frame.save_state()

#         ax = Axes(x_range=[0, 3], y_range=[0, 5], tips=False, x_length=5.5, axis_config={"include_numbers": True}).shift(3.5*LEFT).shift(0.5*UP)
#         plot1 = ax.plot(lambda x: 1. / x, x_range=[0.2, 3])
#         plot2 = ax.plot(lambda x: np.sqrt(x), x_range=[0.2, 3])
#         labels = ax.get_axis_labels(x_label="x", y_label="y")
#         labels.submobjects[1].shift(0.1*UP)
#         labels.submobjects[0].shift(0.2*DOWN)

#         text1 = MathTex("y = 1/x", font_size=36).move_to(ax.c2p(2.5, .75, 0))
#         text2 = MathTex("x = y^2", font_size=36) .move_to(ax.c2p(2.5, 1.95, 0))

#         caption = Tex("Adapted from Ex. 3.8 Engineering Design Optimization by Martins and Ning").scale(0.65).move_to((0, -3.75, 0))

#         self.play(Create(ax), Create(labels))
#         self.play(Create(plot1), Create(plot2), Create(caption))
#         self.play(Create(text1), Create(text2))
#         self.wait()


#         ax2 = Axes(x_range=[0, 6], y_range=[-12, 3, 3], tips=False, x_length=5.5, y_axis_config={"scaling": LogBase(custom_labels=True)}, axis_config={"include_numbers": True}).shift(3.75*RIGHT).shift(0.5*UP)
#         labels2 = ax2.get_axis_labels(x_label="k", y_label="||r||")
#         labels2.submobjects[1].shift(0.5*DOWN).shift(LEFT)

#         self.play(Create(ax2), Create(labels2))
#         self.wait()

#         text3 = Tex("Using a Newton solver").move_to(ax.c2p(2, 4, 0))
#         self.play(Create(text3))
#         self.wait()

#         xs = [2., .485281, .760064, .952668, .998289, .999998, 1.]
#         ys = [3., .87868, .893846, .982278, .999417, .999999, 1.]
#         rs = [2.96, 1.2, 4.22e-1, 6.77e-2, 2.31e-3, 2.95e-6, 4.87e-12]

#         plot = ax.plot_line_graph(xs, ys, line_color=RED, vertex_dot_style={'color' : RED})
#         plot2 = ax2.plot_line_graph(np.arange(len(rs)), rs, line_color=BLUE, vertex_dot_style={'color' : BLUE})

#         for idx, dot1 in enumerate(plot["vertex_dots"]):
#             dot2 = plot2["vertex_dots"][idx]
#             self.play(Create(dot1), Create(dot2))

#             if idx < (len(rs) - 1):
#                 line1 = Line(dot1.get_center(), plot["vertex_dots"][idx+1].get_center(), color=RED)
#                 line2 = Line(dot2.get_center(), plot2["vertex_dots"][idx+1].get_center(), color=BLUE)
#                 self.play(Create(line1), Create(line2))
            
#         self.wait()



# class LinearGraph(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"
#         myTemplate = TexTemplate()
#         myTemplate.add_to_preamble(r"\usepackage{physics}")
#         myTemplate.add_to_preamble(r"\usepackage{bm}")
#         myTemplate.add_to_preamble(r"\usepackage{amsmath}")

#         # Show linear system
#         linear_system = MathTex(r"[\vb*A] \vb*{\va{x}} = \vb*{\va{b}}")
#         self.play(Write(linear_system))
#         self.wait()
#         clear(self)

#         self.camera.frame.save_state()

#         ax = Axes(x_range=[0, 3], y_range=[0, 5], tips=False, x_length=5.5, axis_config={"include_numbers": True}).shift(3.5*LEFT).shift(0.5*UP)
#         plot1 = ax.plot(lambda x: 0.5 * x + 1.5, x_range=[0.2, 3])
#         plot2 = ax.plot(lambda x: -.75*x + 4, x_range=[0.2, 3])
#         labels = ax.get_axis_labels(x_label="x", y_label="y")
#         labels.submobjects[1].shift(0.1*UP)
#         labels.submobjects[0].shift(0.2*DOWN)

#         self.play(Create(ax), Create(labels))
#         self.play(Create(plot1), Create(plot2))
#         self.wait()


#         ax2 = Axes(x_range=[0, 6], y_range=[-12, 3, 3], tips=False, x_length=5.5, y_axis_config={"scaling": LogBase(custom_labels=True)}, axis_config={"include_numbers": True}).shift(3.75*RIGHT).shift(0.5*UP)
#         labels2 = ax2.get_axis_labels(x_label="k", y_label="||r||")
#         labels2.submobjects[1].shift(0.5*DOWN).shift(LEFT)

#         self.play(Create(ax2), Create(labels2))
#         self.wait()

#         xs = [1., 2.]
#         ys = [4., 2.5]
#         rs = [3.816, 1.e-12]

#         plot = ax.plot_line_graph(xs, ys, line_color=RED, vertex_dot_style={'color' : RED})
#         plot2 = ax2.plot_line_graph(np.arange(len(rs)), rs, line_color=BLUE, vertex_dot_style={'color' : BLUE})

#         for idx, dot1 in enumerate(plot["vertex_dots"]):
#             dot2 = plot2["vertex_dots"][idx]
#             self.play(Create(dot1), Create(dot2))

#             if idx < (len(rs) - 1):
#                 line1 = Line(dot1.get_center(), plot["vertex_dots"][idx+1].get_center(), color=RED)
#                 line2 = Line(dot2.get_center(), plot2["vertex_dots"][idx+1].get_center(), color=BLUE)
#                 self.play(Create(line1), Create(line2))
            
#         self.wait()

#         clear(self)

#         # Show linear system
#         linear_system = MathTex(r"[\vb*A] \vb*{\va{x}} = \vb*{\va{b}}")
#         self.play(Write(linear_system))
#         self.wait()
#         clear(self)

#         caption = Tex("Direct methods are the standard way to solve linear systems").shift(3*UP)
#         image = ImageMobject("LU.png").scale(0.6)
#         self.play(FadeIn(image), FadeIn(caption))
#         self.wait()

#         clear(self)

class NonlinearAndLinearSystems(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        nonlinear = ImageMobject("nonlinear_system_from_venn.png").scale(0.4)
        linear = ImageMobject("linear_system_from_venn.png").scale(0.4)
        
        self.add(nonlinear.shift(3.5*LEFT), linear.shift(3.5*RIGHT))