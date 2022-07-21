from manim import *
import numpy as np
from manim_helper_functions import *
import openmdao.api as om
from pyxdsm.XDSM import XDSM, OPT, SOLVER, FUNC, LEFT
import subprocess




debug = False

class NLBGS(MovingCameraScene):
    def setup(self):
        self.camera.background_color="#2d3c54"

        self.filename = "nlbgs"

        # Change `use_sfmath` to False to use computer modern
        x = XDSM(use_sfmath=True)

        x.add_system("opt", OPT, r"\text{Optimizer}")
        x.add_system("solver", SOLVER, r"\text{NLBGS}")
        x.add_system("D1", FUNC, "D_1")
        x.add_system("D2", FUNC, "D_2")
        x.add_system("Funcs", FUNC, "Funcs")

        x.connect("opt", "D1", "x, z")
        x.connect("opt", "D2", "z")
        x.connect("opt", "Funcs", "x, z")
        x.connect("solver", "D1", "y_2")
        x.connect("D1", "D2", "y_1")
        x.connect("D1", "solver", "y_1")
        x.connect("D2", "solver", "y_2")
        x.connect("solver", "Funcs", "y_1, y_2")

        x.connect("Funcs", "opt", "f, g")

        x.add_output("opt", "x^*, z^*", side=LEFT)
        x.add_output("D1", "y_1^*", side=LEFT)
        x.add_output("D2", "y_2^*", side=LEFT)
        x.add_output("Funcs", "f^*, g^*", side=LEFT)
        x.write(self.filename)
        subprocess.run(["pdf2svg", f"{self.filename}.pdf", f"{self.filename}.svg"])

    if debug:
        def construct(self):
            get_xdsm_indices(self, f"{self.filename}.svg")
    else:
        def construct(self):

            image = load_xdsm(f"{self.filename}.svg")

            self.play(Create(image))

            # TODO: need to fix this XDSM to actually be NLBGS
            list_to_highlight = [
                ('ind', [28, 29]),
                ('pass', [0]),
                # ('ind', [30, 31, 32, 33, 42, 43, 44]),
                ('pass', [13, 16]),

                # begin loop
                ('ind', [58, 59, 60]),
                ('pass', [4]),
                # ('ind', [61, 62, 63]),
                ('pass', [17]),
                ('ind', [71, 72, 73]),
                ('pass', [6]),
                # ('ind', [68, 69, 70, 55, 56, 57]),
                ('pass', [18, 19]),
                ('ind', [40, 41]),
                ('pass', [3]),
                # ('ind', [42, 43, 44]),
                ('pass', [13, 16]),

                ('ind', [58, 59, 60]),
                ('pass', [4]),
                # ('ind', [61, 62, 63]),
                ('pass', [17]),
                ('ind', [71, 72, 73]),
                ('pass', [6]),
                # ('ind', [68, 69, 70, 55, 56, 57]),
                ('pass', [18, 19]),
                ('ind', [40, 41]),
                ('pass', [3]),
                # ('ind', [42, 43, 44]),
                ('pass', [13, 16]),

                ('ind', [58, 59, 60]),
                ('pass', [4]),
                # ('ind', [61, 62, 63]),
                ('pass', [17]),
                ('ind', [71, 72, 73]),
                ('pass', [6]),
                # ('ind', [68, 69, 70, 55, 56, 57]),
                ('pass', [18, 19]),
                ('ind', [40, 41]),
                # ('pass', [3]),
                # ('ind', [42, 43, 44]),
                ('pass', [7]),

                # functionals
                # ('ind', [36, 37, 38, 39, 45, 46, 47, 48, 49, 50]),
                ('pass', [15, 20]),
                # ('ind', [84, 85, 86]),
                ('pass', [8]),
                # ('ind', [80, 81, 82, 83]),
                ('pass', [21]),

                ('ind', [28, 29]),
                ('pass', [9, 10, 11, 12]),

                ('ind', [22, 23, 24, 25, 26, 27, 51, 52, 53, 54, 64, 65, 66, 67, 74, 75, 76, 77, 78, 79]),
            ]

            highlight_xdsm(self, image, list_to_highlight)


# class TitleSlide(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"

#         title = r"Basic optimization problem formulation"
#         contents_list = [
#             "Objective function",
#             "Design variables",
#             "Constraints",
#             "Example 2D optimization",
#             ]
#         intro_message = "One of the most important steps in optimization is formulating well-posed and meaningful problems that you can interpret accurately."
#         outro_message = "Formulating a well-posed and reasonable optimization problem is important. You should start with the most simple optimization problem possible and build up complexity slowly, solving each problem along the way."

#         make_title_slide(self, title, contents_list, intro_message, outro_message)


# class BasicOptFormulation(Scene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"
#         myTemplate = TexTemplate()
#         myTemplate.add_to_preamble(r"\usepackage{physics}")
#         text_list = []

#         # Objective discussion
#         text_list.append(r"""
#             Minimize & $f_{\text{obj}}(x)$ \\
#         """)
#         text_list.append(r"""
#             Minimize & $f_{\text{cost}}(x)$ \\
#         """)
#         text_list.append(r"""
#             Maximize & $f_{\text{performance}}(x)$ \\
#         """)
#         text_list.append(r"""
#             Minimize & $-f_{\text{performance}}(x)$ \\
#         """)
#         text_list.append(r"""
#             Minimize & $f_{\text{obj}}(x) = g(x) + h(x)$ \\
#         """)
#         text_list.append(r"""
#             Minimize & $f_{\text{obj}}(x)$ \\
#         """)

#         # Design variables
#         text_list.append(r"""
#             Minimize & $f_{\text{obj}}(x)$ \\ \\
#             With respect to: & \\
#             Design variables & $x$ \\
#         """)
#         text_list.append(r"""
#             Minimize & $f_{\text{obj}}(\vb*{\va{x}})$ \\ \\
#             With respect to: & \\
#             Design variables & $\vb*{\va{x}}$ \\
#         """)
#         text_list.append(r"""
#             Minimize & $f_{\text{Aircraft weight}}(\vb*{\va{x}})$ \\ \\
#             With respect to: & \\
#             Design variables & $\vb*{\va{x}}_{\text{Wing structure thickness}}$ \\
#                              & $\vb*{\va{x}}_{\text{Wing aerodynamic shape}}$ \\
#         """)

#         # Constraints
#         text_list.append(r"""
#             Minimize & $f_{\text{obj}}(\vb*{\va{x}})$ \\ \\
#             With respect to: & \\
#             Design variables & $\vb*{\va{x}}$ \\ \\
#             Subject to: & \\
#             Constraints & $g_{\text{lb}} \leq g(\vb*{\va{x}}) \leq g_{\text{ub}} $ \\
#         """)

#         text_list.append(r"""
#             Minimize & $f_{\text{obj}}(\vb*{\va{x}})$ \\ \\
#             With respect to: & \\
#             Design variables & $\vb*{\va{x}}$ \\ \\
#             Subject to: & \\
#             Constraints & $g_{\text{lb}} \leq g(\vb*{\va{x}}) \leq g_{\text{ub}} $ \\
#                         & $h(\vb*{\va{x}}) = h_{\text{eq}} $ \\
#         """)

#         beg_lines = r"""
#             \begin{table}[]
#             \def\arraystretch{1.0}
#             \centering
#             \begin{tabular}{rl}"""

#         lagged_write(self, text_list, beginning_text=beg_lines, final_text=r"""
#             \end{tabular}
#             \end{table}""")


#         self.wait()

#         self.play(*[FadeOut(mob)for mob in self.mobjects])