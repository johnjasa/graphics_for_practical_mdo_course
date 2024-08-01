from manim import *
import numpy as np
from manim_helper_functions import *


# class TitleSlide(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"

#         title = r"Common ways to compute derivatives"
#         contents_list = [
#             "Finite difference",
#             "Complex step",
#             "Analytically or by hand",
#             "Algorithmic differentiation",
#             ]
#         intro_message = "There are many ways to compute partial derivatives: finite-differencing, complex-step, analytically by hand, or through algorithmic differentiation. The best method depends on your problem formulation, but the best implementation usually involves an intelligent mix of these methods."
#         outro_message = "We blazed through an overview of the few main ways to compute derivative information. The appropriate method to use for your model greatly depends on your use case, computational cost, and developer time available."

#         make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["diff"])

# class FDExplanation(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"
#         self.camera.frame.save_state()

#         fd = MathTex(r"\frac{\partial f}{\partial x} = \frac{f(x+h) - f(x)}{h}")
#         self.play(Write(fd))
#         self.wait()

#         self.play(Transform(fd, MathTex(r"\frac{\partial f}{\partial x} = \frac{f(3.5 + 10^{-9}) - f(3.5)}{10^{-9}}")))
#         self.wait()

#         self.play(Transform(fd, MathTex(r"\frac{\partial f}{\partial x} = \frac{f(3.5 + 10^{-16}) - f(3.5)}{10^{-16}}")))
#         self.wait()

#         self.play(Transform(fd, MathTex(r"\frac{\partial f}{\partial x} = \frac{5.875 - 5.875}{10^{-16}}")))
#         self.wait()

#         self.play(Transform(fd, MathTex(r"\frac{\partial f}{\partial x} = \frac{0.}{10^{-16}} = 0.")))
#         self.wait()

#         clear(self)


# class FDAdvantages(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"
#         self.camera.frame.save_state()

#         text1 = Tex(r"""\raggedright{
#             \textbf{Advantages of FD:}\\
#             Simple and versatile\\
#             Useful for blackbox functions
#         }""")
#         text2 = Tex(r"""\raggedright{
#             \textbf{Disadvantages:}\\
#             Inaccurate\\
#             Computationally expensive\\
#         }""")

#         self.play(Write(text1.shift(2*UP)))
#         self.wait()

#         self.play(Write(text2.align_to(text1, LEFT).shift(DOWN)))
#         self.wait()

#         clear(self)


# class FDPlot(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"
#         self.camera.frame.save_state()

#         # create the axes and the curve
#         ax = Axes(x_range=[0, 10], y_range=[0, 10])
#         plot = ax.plot(lambda x: 0.5*x**2 - 1.5*x + 5)
#         labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

#         self.play(Create(ax), Create(labels))
#         self.play(Create(plot))

#         self.wait()
#         x_point = ValueTracker(2)
#         dx_point = ValueTracker(1)

#         def draw_tangent_line_on_curve(input_plot, x, dx):
#             moving_slope = always_redraw(
#                 lambda: ax.get_secant_slope_group(
#                     x=x.get_value(),
#                     graph=input_plot,
#                     dx=dx.get_value(),
#                     dx_line_color=WHITE,
#                     dx_label=Tex(f"dx = {dx.get_value():.2f}", font_size=32),
#                     dy_label=Tex(f"dy = {input_plot.underlying_function(x.get_value() + dx.get_value()) - input_plot.underlying_function(x.get_value()):.2f}", font_size=32),
#                     secant_line_length=1 + np.sqrt(dx.get_value()**2 + (input_plot.underlying_function(x.get_value() + dx.get_value()) - input_plot.underlying_function(x.get_value()))**2),
#                     secant_line_color=RED,
#                 )
#             )

#             dot2 = always_redraw(
#                 lambda: Dot(color=WHITE, radius=0.05).move_to(
#                     ax.c2p(x.get_value() + dx.get_value(), input_plot.underlying_function(x.get_value() + dx.get_value()))
#                 )
#             )

#             dot1 = always_redraw(
#                 lambda: Dot(color=RED, z_index=999, radius=0.05).move_to(
#                     ax.c2p(x.get_value(), input_plot.underlying_function(x.get_value()))
#                 )
#             )

#             label = always_redraw(
#                 lambda: MathTex(r"\frac{dy}{dx}" + f" = {(input_plot.underlying_function(x.get_value() + dx.get_value()) - input_plot.underlying_function(x.get_value())) / dx.get_value():.8f}").move_to(
#                     ax.c2p(6., 6.), aligned_edge=LEFT,
#                 )
#             )

#             label2 = always_redraw(
#                 lambda: MathTex(f"dx = {dx.get_value():.4f}").move_to(
#                     ax.c2p(6., 9.)
#                 ).align_to(label, LEFT)
#             )

#             return moving_slope, dot1, dot2, label, label2

#         moving_slope, dot1, dot2, label, label2 = draw_tangent_line_on_curve(plot, x_point, dx_point)

#         self.play(FadeIn(moving_slope), FadeIn(dot1), FadeIn(dot2), FadeIn(label), FadeIn(label2))
#         self.play(x_point.animate.set_value(3.5), run_time=3.0, rate_func=linear)
#         self.wait()

#         self.play(dx_point.animate.set_value(1.e-9), run_time=3.0, rate_func=linear)
        
#         new_label = MathTex(r"dx = 10^{-9}").move_to(ax.c2p(8., 9.)).align_to(label, LEFT)
#         self.remove(label2)
#         self.add(new_label)
#         self.wait()

#         clear(self)




class CSExplanation(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"
        self.camera.frame.save_state()

        cs = MathTex(r"\frac{\partial f}{\partial x} = \frac{\text{Im}(f(x + ih))}{h}")
        self.play(Write(cs))
        self.wait()

        clear(self)

        rect = Rectangle(height=8., width=1, z_index=999, fill_color="#2d3c54", color="#2d3c54", fill_opacity=1).move_to((4.1935, 1., 0))
        self.add(rect)

        image = SVGMobject("cs_stepsize", unpack_groups=False, stroke_width=3)
        image.scale(3.5)
        caption = Tex("Fig. 6.9 from Engineering Design Optimization by Martins and Ning").scale(0.7).move_to((0, -3.75, 0))
        self.play(Write(image), Write(caption))
        self.wait(2)

        self.play(FadeOut(image, caption))


# class CSAdvantages(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"
#         self.camera.frame.save_state()

#         text1 = Tex(r"""\raggedright{
#             \textbf{Advantages of CS:}\\
#             As accurate as your model\\
#         }""")
#         text2 = Tex(r"""\raggedright{
#             \textbf{Disadvantages:}\\
#             Computationally expensive\\
#             Requires source-code modification\\
#             Model must be complex-safe\\
#         }""")

#         self.play(Write(text1.shift(2*UP)))
#         self.wait()

#         self.play(Write(text2.align_to(text1, LEFT).shift(DOWN)))
#         self.wait()

#         clear(self)


# class AnalyticDerivs(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"
#         self.camera.frame.save_state()

#         cs = MathTex(r"f(x) = 0.5x^2 - 1.5x + 5")
#         self.play(Write(cs))
#         self.wait()

#         self.play(Transform(cs, MathTex(r"\frac{\partial f}{\partial x} = \frac{\partial (0.5x^2 - 1.5x + 5)}{\partial x}")))
#         self.wait()

#         self.play(Transform(cs, MathTex(r"\frac{\partial f}{\partial x} = x - 1.5")))
#         self.wait()

#         heat = MathTex(r"""
#         \frac{dT}{dt} = \frac{\dot Q_{\text{env}} + \dot m_{\text{flow}} q_{\text{pump}} + \left[ 1 - \frac{\dot m_{\text{burned}}}{\dot m_{\text{flow}}} \right] \dot Q_{\text{sink}} - (\dot m_{\text{flow}} - \dot m_{\text{burned}}) q_{\text{out}}}{m c_v}""").scale(0.8)
#         self.play(Transform(cs, heat))
#         self.wait()

#         ns = MathTex(r"""
#         \frac{ \partial \overline{u_{i}} }{\partial t} +
# \overline{u_{j}} \frac{ \partial \overline{u_{i}} }{ \partial x_{j} } =
# - \frac{1}{\rho} \frac{\partial \overline{p} }{ \partial x_{i} }
#    + \frac{1}{\rho} \frac{\partial}{\partial x_{j}} 
# \left( \mu \frac{\partial \overline{u_{i}}}{\partial x_{j}} -
#               \rho \overline{u_i^\prime u_j^\prime } \right)
#         """)
#         self.play(Transform(cs, ns))
#         self.wait()

# class AnalyticAdvantages(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"
#         self.camera.frame.save_state()

#         text1 = Tex(r"""\raggedright{
#             \textbf{Advantages of analytic:}\\
#             Accurate\\
#             Potentially efficient\\
#         }""")
#         text2 = Tex(r"""\raggedright{
#             \textbf{Disadvantages:}\\
#             Often large developer cost\\
#             Closed form solutions don't exist for some equations\\
#         }""")

#         self.play(Write(text1.shift(2*UP).shift(3*LEFT)))
#         self.wait()

#         self.play(Write(text2.align_to(text1, LEFT).shift(DOWN)))
#         self.wait()

#         clear(self)


# class ADAdvantages(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"
#         self.camera.frame.save_state()

#         text1 = Tex(r"""\raggedright{
#             \textbf{Advantages of AD:}\\
#             Accurate\\
#             Efficient (depending on implementation)\\
#             Potentially less developer cost
#         }""")
#         text2 = Tex(r"""\raggedright{
#             \textbf{Disadvantages:}\\
#             Requires some code reworking\\
#             Might be computationally intensive or inefficient\\
#         }""")

#         self.play(Write(text1.shift(2*UP).shift(LEFT)))
#         self.wait()

#         self.play(Write(text2.align_to(text1, LEFT).shift(DOWN)))
#         self.wait()

#         clear(self)


# class ADBasics(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"
#         self.camera.frame.save_state()

#         v_text = r"""v_i=v_i(v_1, v_2, ..., v_{i-1})"""
#         caption = Tex("Fig. 6.13-14 from Engineering Design Optimization by Martins and Ning").scale(0.8).move_to((0, -3.5, 0))
#         image0 = SVGMobject("ad_variables", unpack_groups=False, stroke_width=3)
#         image0.scale(2.5).shift(4*RIGHT)
#         self.play(Write(MathTex(v_text).shift(3*UP).shift(2*LEFT)), Write(image0), Write(caption))
#         self.wait()

#         image = SVGMobject("unrolled_AD_loop", unpack_groups=False, stroke_width=3)
#         image.scale(2.).shift(2*LEFT)
#         self.play(Write(image))
#         self.wait()
#         self.play(FadeOut(image))

#         text = r"""
#             \begin{aligned}
#             \dot{v}_{1} &=1 \\
#             \dot{v}_{2} &=\frac{\partial v_{2}}{\partial v_{1}} \dot{v}_{1} \\
#             \dot{v}_{3} &=\frac{\partial v_{3}}{\partial v_{1}} \dot{v}_{1}+\frac{\partial v_{3}}{\partial v_{2}} \dot{v}_{2} \\
#             \dot{v}_{4} &=\frac{\partial v_{4}}{\partial v_{1}} \dot{v}_{1}+\frac{\partial v_{4}}{\partial v_{2}} \dot{v}_{2}+\frac{\partial v_{4}}{\partial v_{3}} \dot{v}_{3} \equiv \frac{\mathrm{d} f}{\mathrm{~d} x}
#             \end{aligned}"""
#         self.play(Write(MathTex(text).shift(2*LEFT)))
#         self.wait()

#         clear(self)