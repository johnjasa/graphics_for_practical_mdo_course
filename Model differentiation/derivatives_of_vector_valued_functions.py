from manim import *
import numpy as np
from manim_helper_functions import *


# class TitleSlide(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"

#         title = r"Derivatives of vector valued functions"
#         contents_list = [
#             "What are vector valued functions?",
#             "Brief math theory of derivative arrays (Jacobians)",
#             "Example case in OpenMDAO",
#             "Sparsity in the Jacobian can be exploited",
#             "Derivative coloring can also help",
#             ]
#         intro_message = "Derivatives of a scalar with respect to a scalar might be relatively straightforward. Derivatives of vector valued functions are not impossibly difficult."
#         outro_message = "Obtaining derivatives of vector valued functions requires thought, planning, and a purposeful implementation. You can use intelligent matrix and array operations to facilitate the process."

#         make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["diff"])

class ArrowsBox(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        textbox = VGroup() # create a VGroup
        box = Rectangle(  # create a box
            height=5, width=3, fill_color=WHITE, 
            fill_opacity=0.5, stroke_color=WHITE
        )
        text = Tex("Model", font_size=60).move_to(box.get_center()) # create text
        textbox.add(box, text)
        self.play(FadeIn(textbox))

        arrow1 = Arrow([-4, 0, 0], textbox.get_edge_center(LEFT))
        text1 = Tex(r"Inputs\\$n_x=1$").move_to(arrow1.get_edge_center(UP)).shift(3*UP)
        self.play(Create(arrow1), Write(text1))

        arrow2 = Arrow(textbox.get_edge_center(RIGHT), [4, 0, 0])
        text2 = Tex(r"Outputs\\$n_f=1$").move_to(arrow2.get_edge_center(UP)).shift(3*UP)
        self.play(Create(arrow2), Write(text2))
        self.wait()

        left_arrows = VGroup()
        for i in range(6):
            left_arrows.add(Arrow([-4, i-2.5, 0], [textbox.get_edge_center(LEFT)[0], i-2.5, 0]))
        new_text1 = Tex(r"Inputs\\$n_x=6$").move_to(text1.get_center())
        self.play(Transform(arrow1, left_arrows), Transform(text1, new_text1))
        self.wait()

        right_arrows = VGroup()
        for i in range(4):
            right_arrows.add(Arrow([textbox.get_edge_center(RIGHT)[0], i-1.5, 0], [4, i-1.5, 0]))
        new_text2 = Tex(r"Outputs\\$n_f=4$").move_to(text2.get_center())
        self.play(Transform(arrow2, right_arrows), Transform(text2, new_text2))
        self.wait()

        left_arrows = VGroup()
        for i in range(2):
            left_arrows.add(Arrow([-4, i, 0], [textbox.get_edge_center(LEFT)[0], i, 0]))
        new_text1 = Tex(r"Inputs\\$n_x=2$").move_to(text1.get_center())
        self.play(Transform(arrow1, left_arrows), Transform(text1, new_text1))
        self.wait()

        self.clear()
        
        

# class MakeAngle(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"

#         text = r"""
# \begin{align*}
#   {\bf a} &= \begin{bmatrix}
#           a_{x} \\
#           a_{y} \\
#           a_{z} \\
#         \end{bmatrix}
# \end{align*}
# """
#         text2 = r"""
# \begin{align*}
#   {\bf b} &= \begin{bmatrix}
#           b_{x} \\
#           b_{y} \\
#           b_{z} \\
#         \end{bmatrix}
# \end{align*}"""

#         a = Arrow(buff=0)
#         b = Arrow([-1., 0., 0], [2., 3., 0.], buff=0)

#         self.play(Create(a), Create(b), Create(Tex(text).move_to(a.get_edge_center(RIGHT)).shift(1.5*RIGHT)), Create(Tex(text2).move_to(b.get_edge_center(RIGHT)).shift(1.5*RIGHT).shift(1.5*UP)))
#         self.wait()

#         ang = Angle(a, b)
#         label = MathTex(r"\theta").move_to(ang.get_edge_center(RIGHT)).shift(0.25*RIGHT, 0.2*UP)
#         self.play(Create(ang), Create(label))
#         self.wait()

#         eqn = MathTex(r"\theta=\cos^{-1} \biggl( \frac{\bf{a} \cdot \bf{b}} {|\bf{a}| |\bf{b}|} \biggr)").shift(3*LEFT, DOWN)
#         self.play(Write(eqn))
#         self.wait()

#         text3 = Tex("6 inputs, 1 output").shift(3*DOWN)
#         self.play(Create(text3))
#         self.wait()


# class TennisBall(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"

#         text = r"""
# \begin{align*}
#   {\bf v}&=\begin{bmatrix}
#           v \cos(\theta) \\
#           v \sin(\theta) \\
#         \end{bmatrix}
# \end{align*}"""

#         image = ImageMobject('tennis_ball_launcher.png').set_width(8).shift(2.5*LEFT, 0.5*UP)
#         self.play(FadeIn(image))

#         self.play(Create(Tex(text).shift(4*RIGHT)))
#         self.wait()

#         text3 = Tex("2 inputs, 2 outputs").shift(3.5*DOWN)
#         self.play(Create(text3))
#         self.wait()

class Math(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        math = r"""
        J_f=\frac{\partial f}{\partial x}=\left[\begin{array}{c}
\nabla f_1^\intercal \\
\vdots \\
\nabla f_{n_f}^\intercal
\end{array}\right]=\underbrace{\left[\begin{array}{ccc}
\frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_{n_{x}}} \\
\vdots & \ddots & \vdots \\
\frac{\partial f_{n_f}}{\partial x_1} & \cdots & \frac{\partial f_{n_f}}{\partial x_{n_{x}}}
\end{array}\right]}_{\left(n_f \times n_{x}\right)}"""

        math_tex = MathTex(math)
        self.play(Write(math_tex))
        self.wait()
        
        self.play(math_tex.animate.move_to((-3, 0, 0)).scale(0.6))
        self.wait()

        textbox = VGroup() # create a VGroup
        box = Rectangle(  # create a box
            height=3, width=2, fill_color=WHITE, 
            fill_opacity=0.5, stroke_color=WHITE
        )
        text = Tex("Model", font_size=44).move_to(box.get_center()) # create text
        textbox.add(box, text)
        textbox.shift(3.5*RIGHT)
        self.play(FadeIn(textbox))

        
        left_arrows = VGroup()
        for i in range(4):
            left_arrows.add(Arrow([0.5, i-1.5, 0], [textbox.get_edge_center(LEFT)[0], i-1.5, 0]))
        self.play(Create(left_arrows))
        self.wait()

        right_arrows = VGroup()
        for i in range(2):
            right_arrows.add(Arrow([textbox.get_edge_center(RIGHT)[0], i-0.5, 0], [6.5, i-0.5, 0]))
        self.play(Create(right_arrows))
        self.wait()

        new_math = r"""
        J_f=\frac{\partial f}{\partial x}=\left[\begin{array}{c}
\nabla f_1^\intercal \\
\vdots \\
\nabla f_{n_f}^\intercal
\end{array}\right]=\underbrace{\left[\begin{array}{cccc}
\frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \frac{\partial f_1}{\partial x_3} & \frac{\partial f_1}{\partial x_4} \\ \\
\frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \frac{\partial f_2}{\partial x_3} & \frac{\partial f_2}{\partial x_4} \\
\end{array}\right]}_{\left(n_2 \times n_4\right)}"""

        self.play(Transform(math_tex, MathTex(new_math, font_size=30).shift(3.5*LEFT)))
        self.wait()

        self.clear()