from manim import *
import numpy as np
from manim_helper_functions import *
from pyxdsm.XDSM import XDSM, OPT, SOLVER, FUNC, LEFT as xdsm_left, RIGHT as xdsm_right
import subprocess


class TitleSlide(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        title = r"Total vs partial derivatives"
        contents_list = [
            "What are partial derivatives?",
            "What are total derivatives?",
            "Totals can be computed from a mix of partials",
            ]
        intro_message = "Partial derivatives involve only individual components. Total derivatives are the derivatives of an objective or constraint with respect to design variables."
        outro_message = "Total derivatives are computed through a combination of partial derivatives. You need to supply or compute the partials; OpenMDAO handles the totals."

        make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["diff"])

def make_textbox(color, string, height=1.5, width=2.):
    result = VGroup() # Write a VGroup
    box = Rectangle(  # Write a box
        height=height, width=width, fill_color=color, 
        fill_opacity=0.5, stroke_color=color
    )
    text = Tex(string).move_to(box.get_center()) # Write text
    result.add(box, text) # add both objects to the VGroup
    return result


# debug = False
# class PartialsDiscussion(MovingCameraScene):
#     def setup(self):
#         self.camera.background_color="#2d3c54"

#         self.filename = "simple_xdsm"

#         if debug:
#             x = XDSM(use_sfmath=True)

#             x.add_system("func", FUNC, r"y = x^2 + 2x")
#             x.add_system("func2", FUNC, r"z = y^2 - 3x")
#             x.connect("func", "func2", r"y")

#             x.add_input("func", r"x")
#             x.add_input("func2", r"x")
            
#             x.add_output("func", r"y", side=xdsm_right)
#             x.add_output("func2", r"z", side=xdsm_right)

#             x.write(self.filename)
#             subprocess.run(["pdf2svg", f"{self.filename}.pdf", f"{self.filename}.svg"])

#     if debug:
#         def construct(self):
#             get_xdsm_indices(self, f"{self.filename}.svg")
#     else:
#         def construct(self):
#             xdsm = load_xdsm(f"{self.filename}.svg", scale=0.6).shift(2.5*RIGHT)

#             self.camera.background_color="#2d3c54"

#             partial = MathTex(r"\frac{\partial f}{\partial x}", font_size=180).shift(3*LEFT)
#             total = MathTex(r"\frac{d f}{d x}", font_size=180).shift(3*RIGHT)
#             func = MathTex(r"f(x,y)", font_size=180).shift(2.5*DOWN)
#             implicit_func = MathTex(r"f(x,y(x))", font_size=180).shift(2.5*DOWN)
#             unequal = MathTex(r"\neq", font_size=180)

#             self.play(Write(partial))
#             self.wait()

#             self.play(Write(total))
#             self.wait()

#             self.play(Write(unequal))
#             self.wait()

#             self.play(FadeOut(unequal), partial.animate.shift(1.25*UP, 1.25*LEFT), total.animate.shift(1.25*UP, 1.25*RIGHT))

#             self.play(Write(func))
#             self.wait()

#             self.play(Transform(func, implicit_func))
#             self.wait()


#             self.play(FadeOut(func), FadeOut(total), partial.animate.scale(0.8))
#             self.wait()
            
#             total.move_to(partial.get_center()).scale(0.8)

#             def add_elements(indices):
#                 group = VGroup()
#                 for idx in indices:
#                     subm = xdsm.submobjects[idx]

#                     # Hack to make boxes go over gray lines
#                     tol = 1.e-2
#                     if subm.width > tol and subm.height > tol:
#                         subm.set_z_index(1)
#                     group.add(subm)

#                 anims = []
#                 for obj in group:
#                     anims.append(Write(obj))
#                 self.play(AnimationGroup(*anims))
#                 self.wait()

#             add_elements([10, 11, 12, 13, 14, 15, 16, 17])
#             add_elements([6, 7, 4, 0, 18, 19])
#             self.wait()

#             self.play(Transform(partial, total))
#             self.wait()

#             y_total = MathTex(r"\frac{d y}{d x}", font_size=180).move_to(total.get_center()).scale(0.8)

#             self.play(Transform(partial, y_total))
#             self.wait()
            
#             add_elements([22, 23, 24, 25, 26, 27, 28, 29, 8, 9, 5, 3, 2, 30, 31])
#             self.wait()

#             z_total = MathTex(r"\frac{d z}{d x}", font_size=180).move_to(total.get_center()).scale(0.8)
#             self.play(Transform(partial, z_total))
#             self.wait()

#             z_total_more = MathTex(r"\frac{d z}{d x} = \frac{\partial z}{\partial x}", font_size=120).move_to(partial.get_center()).shift(2*DOWN)
#             self.play(Transform(partial, z_total_more))
#             self.wait()

#             z_total_even_more = MathTex(r"\frac{d z}{d x} = \frac{\partial Z}{\partial x} + \frac{\partial Z}{\partial y} \frac{d y}{d x}", font_size=80).move_to(partial.get_center()).shift(1.5*DOWN, 1.5*RIGHT)
#             self.play(Transform(partial, z_total_even_more))
#             self.wait()
            

class TradeOffer(MovingCameraScene):
    def setup(self):
        self.camera.background_color="#2d3c54"

        text = Tex(r"""Trade offer:""", font_size=60).shift(2.75*UP)
        self.play(Write(text))
        self.wait()

        text = Tex(r"""\raggedright{
You provide:\\
Partial derivatives for each component\\
How to solve for the totals}""", font_size=44).shift(2.8*LEFT, UP)
        self.play(Write(text))
        self.wait()

        text2 = Tex(r"""\raggedright{
OpenMDAO computes:\\
Total derivatives}""", font_size=44).shift(4.2*RIGHT, UP).align_to(text, UP)
        self.play(Write(text2))
        self.wait()

        
# debug = False
# class ExampleSetup(MovingCameraScene):
#     def setup(self):
#         self.camera.background_color="#2d3c54"

#         self.filename = "aerostructural"

#         if debug:
#             x = XDSM(use_sfmath=True)

#             x.add_system("geom", FUNC, (r"\text{Geometry}", r"\text{(finite-differenced)}"))
#             x.add_system("aero", FUNC, (r"\text{Aerodynamics}", r"\text{(automatic differentiated)}"))
#             x.add_system("struct", FUNC, (r"\text{Structures}", r"\text{(analytic)}"))
#             x.add_system("functionals", FUNC, (r"\text{Performance}", r"\text{(analytic)}"))
            
#             x.connect("geom", "aero", r"\text{Wing geometry}")
#             x.connect("aero", "struct", r"\text{Wing loads}")
#             x.connect("struct", "aero", r"\text{Mesh displacements}")
#             x.connect("struct", "functionals", r"\text{Struct performance}")
#             x.connect("aero", "functionals", r"\text{Aero performance}")

#             x.write(self.filename)
#             subprocess.run(["pdf2svg", f"{self.filename}.pdf", f"{self.filename}.svg"])

#     if debug:
#         def construct(self):
#             get_xdsm_indices(self, f"{self.filename}.svg")
#     else:
#         def construct(self):
#             xdsm = load_xdsm(f"{self.filename}.svg")

#             self.play(Write(xdsm))
#             self.wait()