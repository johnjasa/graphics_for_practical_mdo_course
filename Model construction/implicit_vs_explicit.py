from manim import *
import numpy as np
from manim_helper_functions import *
from pyxdsm.XDSM import XDSM, OPT, SOLVER, FUNC, LEFT as xdsm_left, RIGHT as xdsm_right
import subprocess


# class TitleSlide(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"

#         title = r"Explicit vs implicit systems"
#         contents_list = [
#             "Implicit vs explicit functions",
#             "When to make an implicit system",
#             "An implicit component and equivalent explicit system",
#             "How to use implicit models correctly",
#             ]
#         intro_message = "Explicit systems have outputs defined only by the inputs, whereas implicit systems can have outputs that are defined as a function of both inputs and outputs."
#         outro_message = "You can formulate subsystems as explicit or implicit systems. Explicit systems are generally easier to understand and solve but implicit systems are necessary and helpful to correctly model physical phenomena."

#         make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["mda"])

# class ImplicitVsExplicit(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"
#         self.camera.frame.save_state()

#         font_size = 144
#         explicit = MathTex(r"y = 5x - 2", font_size=font_size).shift(2*UP)
#         implicit = MathTex(r"y - 5x + 2 = 0", font_size=font_size).shift(2*DOWN)

#         self.play(Write(explicit))
#         self.wait()
#         self.play(Write(implicit))
#         self.wait()

#         clear(self)

#         implicit = MathTex(r"y^4 + y = 0", font_size=font_size)
#         self.play(Write(implicit))
#         self.wait()

#         clear(self)


debug = False
class ExplicitVsImplicitXDSM(MovingCameraScene):
    def setup(self):
        self.camera.background_color="#2d3c54"

        self.filename = "implicit_system_xdsm"

        if debug:
            x = XDSM(use_sfmath=True)

            x.add_system("func1", FUNC, r"A")
            x.add_system("func2", FUNC, r"B")
            x.add_system("func3", FUNC, r"C")

            x.connect("func1", "func2", "x")
            x.connect("func3", "func1", "y")

            x.write(self.filename)
            subprocess.run(["pdf2svg", f"{self.filename}.pdf", f"{self.filename}.svg"])

        self.filename2 = "explicit_system"

        if debug:
            x = XDSM(use_sfmath=True)

            x.add_system("func3", FUNC, r"C")
            x.add_system("func1", FUNC, r"A")
            x.add_system("func2", FUNC, r"B")

            x.connect("func1", "func2", "x")
            x.connect("func3", "func1", "y")

            x.write(self.filename2)
            subprocess.run(["pdf2svg", f"{self.filename2}.pdf", f"{self.filename2}.svg"])

    if debug:
        def construct(self):
            get_xdsm_indices(self, f"{self.filename}.svg")
    else:
        def construct(self):
            xdsm = load_xdsm(f"{self.filename}.svg").scale(0.85)
            text = Tex(r"Implicit system").move_to(xdsm.get_edge_center(DOWN)).shift(0.25*DOWN)
            self.play(Create(xdsm), Write(text))
            self.wait()
            self.play(xdsm.animate.shift(3*LEFT), text.animate.shift(3*LEFT))

            xdsm2 = load_xdsm(f"{self.filename2}.svg").shift(3*RIGHT).scale(0.85)
            text2 = Tex(r"Explicit system").move_to(xdsm2.get_edge_center(DOWN)).shift(0.25*DOWN)
            self.play(Create(xdsm2), Write(text2))
            self.wait()

            self.clear()




# debug = False
# class CouplingComparisons(MovingCameraScene):
#     def setup(self):
#         self.camera.background_color="#2d3c54"

#         self.filename = "implicit_system"

#         if debug:
#             x = XDSM(use_sfmath=True)

#             x.add_system("func1", FUNC, r"y=x^2")
#             x.add_system("func2", FUNC, r"x=3y")

#             x.connect("func1", "func2", "y")
#             x.connect("func2", "func1", "x")

#             x.write(self.filename)
#             subprocess.run(["pdf2svg", f"{self.filename}.pdf", f"{self.filename}.svg"])

#         self.filename2 = "implicit_system2"

#         if debug:
#             x = XDSM(use_sfmath=True)

#             x.add_system("func1", FUNC, (r"y=9y^2", r"x=3x^2"))

#             x.write(self.filename2)
#             subprocess.run(["pdf2svg", f"{self.filename2}.pdf", f"{self.filename2}.svg"])

#         self.filename3 = "implicit_system3"

#         if debug:
#             x = XDSM(use_sfmath=True)

#             x.add_system("func1", FUNC, (r"9y^2-y=0", r"3x^2-x=0"))

#             x.write(self.filename3)
#             subprocess.run(["pdf2svg", f"{self.filename3}.pdf", f"{self.filename3}.svg"])

#     if debug:
#         def construct(self):
#             get_xdsm_indices(self, f"{self.filename}.svg")
#     else:
#         def construct(self):
#             xdsm2 = load_xdsm(f"{self.filename}.svg").scale(0.6)
#             text2 = Tex(r"An implicit system").move_to(xdsm2.get_edge_center(DOWN)).shift(0.5*DOWN)
#             self.play(Create(xdsm2), Write(text2))
#             self.wait()
#             self.play(xdsm2.animate.shift(3.5*LEFT), text2.animate.shift(3.5*LEFT))

#             xdsm = load_xdsm(f"{self.filename2}.svg").scale(0.3).shift(3.5*RIGHT)
#             text = Tex(r"An equivalent implicit system").move_to(xdsm.get_edge_center(DOWN)).shift(0.5*DOWN)
#             self.play(Create(xdsm), Write(text))
#             self.wait()


#             xdsm3 = load_xdsm(f"{self.filename3}.svg").scale(0.3).shift(3.5*RIGHT)
#             self.play(Transform(xdsm, xdsm3))
#             self.wait()

#             self.clear()