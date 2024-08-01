from manim import *
import numpy as np
from manim_helper_functions import *
import openmdao.api as om
from pyxdsm.XDSM import XDSM, OPT, SOLVER, FUNC, LEFT as xdsm_left, RIGHT as xdsm_right
import subprocess



# class TitleSlide(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"

#         title = r"Understanding XDSM diagrams"
#         contents_list = [
#             "What is an XDSM?",
#             "XDSMs for analysis",
#             "XDSMs for optimization",
#             "Making XDSMs",
#             "How XDSMs can be used in large projects",
#             "N2 vs XDSM diagrams",
#             ]
#         intro_message = "XDSM diagrams are a good tool for visualizing models, understanding solver loops, and specifying interfaces between models developed by more than one person."
#         outro_message = "You should always create an XDSM diagram of a model you are analyzing or optimizing. It not only helps your understanding, but allows you to easily share and explain the model to others."

#         make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["mda", "opt"])

#         write_caption(self, "XDSM (eXtended Design Structure Matrix) is a tool to visualize MDO processes created by Lambe and Martins, 2012.")

#         write_caption(self, "The DSM idea is not new, but XDSM provides a standardized way to portray complicated design problems.")


# debug = False

# class Aerostructural(MovingCameraScene):
#     def setup(self):
#         self.camera.background_color="#2d3c54"

#         self.filename = "aerostructural"

#         if debug:
#             # Change `use_sfmath` to False to use computer modern
#             x = XDSM(use_sfmath=True)

#             x.add_system("opt", OPT, r"\text{Optimizer}")
#             x.add_system("geom", FUNC, r"\text{Geometry}")
#             x.add_system("solver", SOLVER, r"\text{NLBGS}")
#             x.add_system("aero", FUNC, r"\text{Aerodynamics}")
#             x.add_system("struct", FUNC, r"\text{Structures}")
#             x.add_system("functionals", FUNC, r"\text{Functionals}")
            
#             x.connect('opt', 'geom', r'\text{Twist}')
#             x.connect('opt', 'struct', r'\text{Spar thickness}')
#             x.connect('geom', 'aero', r'\text{Baseline mesh}')
#             x.connect('geom', 'struct', r'\text{Baseline mesh}')
#             x.connect('aero', 'struct', r'\textit{Aerodynamic loads}')
#             x.connect('aero', 'functionals', r'C_L, C_D, \text{etc}')
#             x.connect('struct', 'functionals', r'\text{Weight, etc}')

#             x.connect('struct', 'solver', r'\textit{Displaced mesh}')
#             x.connect('aero', 'solver', r'\textit{Aerodynamic loads}')
#             x.connect('solver', 'functionals', (r'\text{Displaced mesh,}', r'\text{aerodynamic loads}'))
#             # x.connect('solver', 'aero', r'\text{Displaced mesh}')
#             # x.connect('solver', 'struct', r'\text{Aerodynamic loads}')

#             x.connect('struct', 'aero', r'\textit{Displaced mesh}')
#             x.connect('functionals', 'opt', r'\text{Fuel burn}, C_M')
#             x.connect('struct', 'opt', r'\text{Failure}')

#             x.add_output("opt", r'\text{Twist}^*, \text{Spar thickness}^*', side=xdsm_left)
#             x.add_output("functionals", (r"\text{Weight}^*, C_L/C_D^*,", r"\text{fuel burn}^*"), side=xdsm_left)
#             x.write(self.filename)
#             subprocess.run(["pdf2svg", f"{self.filename}.pdf", f"{self.filename}.svg"])

#     if debug:
#         def construct(self):
#             get_xdsm_indices(self, f"{self.filename}.svg")
#     else:
#         def construct(self):
#             image = load_xdsm(f"{self.filename}.svg")

#             self.play(FadeIn(image))
#             self.wait()
#             clear(self)

#             def add_elements(indices):
#                 group = VGroup()
#                 for idx in indices:
#                     subm = image.submobjects[idx]

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


#             mesh_image = SVGMobject("scaneagle_no_tube.svg")
#             mesh_image.height = 2.5
#             mesh_image.move_to([-4., 2, 0.])

#             tube_image = SVGMobject("scaneagle.svg")
#             tube_image.height = 2.5
#             tube_image.move_to([-4., 2, 0.])

#             real_image = ImageMobject('ScanEagle_real.png')
#             real_image.height = 2.5
#             real_image.move_to([-4., -1., 0.])
            
#             self.play(FadeIn(real_image), Write(mesh_image))
            
#             func = lambda pos: 6. * (UP + RIGHT)
#             spacing = 2.0
#             stream_lines = StreamLines(func, stroke_width=0.75, max_anchors_per_line=2, color=GRAY, x_range=[-8, -4, spacing], y_range=[-3, 0., spacing], opacity=0.2, virtual_time=12)
#             stream_lines.set_z_index(-1)
#             self.add(stream_lines)
#             stream_lines.start_animation(warm_up=False, flow_speed=4.)
#             self.wait(10.)
#             self.play(FadeOut(stream_lines))
            
#             add_elements([65, 66, 67])  # add aero
#             add_elements([47, 48, 49, 17])  # add inputs to aero
            
#             list_to_highlight = [
#                 ('pass', [17]),
#             ]
#             for i in range(3):
#                 highlight_xdsm(self, image, list_to_highlight, wait=False)

#             add_elements([68, 69, 70, 71, 4])  # add outputs to aero
#             list_to_highlight = [
#                 ('pass', [4]),
#             ]
#             for i in range(3):
#                 highlight_xdsm(self, image, list_to_highlight, wait=False)

#             self.wait()

#             self.play(Transform(mesh_image, tube_image))

#             add_elements([19, 91, 92, 50, 51, 52, 18])  # add structures and inputs and connections to structures
#             add_elements([87, 88, 89, 90, 10, 25])  # add outputs from structures

#             def homotopy(x, y, z, t):
#                 return (x, y + 0.1 * rate_functions.there_and_back(t) * np.abs(x + 5.)**2, z)
#             self.play(Homotopy(homotopy=homotopy, mobject=mesh_image), run_time=2.5)
#             self.wait()

#             add_elements([53, 54])  # add solver
#             add_elements([8, 61, 62, 63, 64, 7, 83, 84, 85, 86, 22, 23])  # add disciplinary outputs as inputs to solver
#             self.wait()

#             add_elements([55, 56, 57, 58, 59, 60, 9])  # add outputs from solver


#             def homotopy(x, y, z, t):
#                 return (x, y + 0.01 * rate_functions.there_and_back(t) * np.abs(x + 5.)**2, z)
#             self.play(Homotopy(homotopy=homotopy, mobject=mesh_image), run_time=1.2)
#             self.wait()

#             def homotopy(x, y, z, t):
#                 return (x, y + 0.1 * rate_functions.there_and_back(t) * np.abs(x + 5.)**2, z)
#             self.play(Homotopy(homotopy=homotopy, mobject=mesh_image), run_time=1.2)
#             self.wait()

#             def homotopy(x, y, z, t):
#                 return (x, y + 0.02 * rate_functions.ease_in_out_quad(t) * np.abs(x + 5.)**2, z)
#             self.play(Homotopy(homotopy=homotopy, mobject=mesh_image), run_time=1.2)
#             self.wait()

#             list_to_highlight = [
#                 ('ind', [65, 66, 67]),
#                 ('pass', [4, 8]),
#                 ('pass', [18, 19]),
#                 ('ind', [91, 92]),
#                 ('pass', [7, 10, 25]),
#                 ('pass', [22, 23]),
#                 ('ind', [53, 54]),

#                 ('ind', [65, 66, 67]),
#                 ('pass', [4, 8]),
#                 ('pass', [18, 19]),
#                 ('ind', [91, 92]),
#                 ('pass', [7, 10, 25]),
#                 ('pass', [22, 23]),
#                 ('ind', [53, 54]),
#             ]

#             highlight_xdsm(self, image, list_to_highlight)
            
#             self.wait()

#             add_elements([5, 6, 20, 21, 24, 72, 73, 74, 75, 76, 77, 78, 79, 93, 94, 95, 96, 97, 120, 121, 122])  # add inputs to functionals; add functionals


#             self.play(real_image.animate.scale(0.5).shift((-1.6, 1, 0)), mesh_image.animate.scale(0.5).shift((-1.6, -1, 0)))

#             add_elements([113, 114, 115, 116, 117, 118, 119, 80, 81, 82, 11, 12])  # add fuel burn and failure outputs
#             add_elements([45, 46, 2, 3])  # Add geometry block and connections to mesh
#             add_elements([38, 39, 15, 40, 41, 42, 43, 44, 16])  # Add inputs to geometry
#             add_elements([36, 37, 0, 1, 26, 27])  # Add optimizer interface
#             add_elements([28, 13, 14, 29, 30, 31, 32, 33, 34, 35, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112])  # Add optimizer interface

            
#             self.wait()
            
            
#             list_to_highlight = [
#                 ('ind', [36, 37]),
#                 ('pass', [0]),
#                 ('pass', [15]),
#                 ('ind', [45, 46]),
#                 ('pass', [2]),
#                 ('pass', [17]),

#                 ('ind', [65, 66, 67]),
#                 ('pass', [4, 8]),
#                 ('pass', [16, 18, 19]),
#                 ('ind', [91, 92]),
#                 ('pass', [7, 10, 25]),
#                 ('pass', [22, 23]),
#                 ('ind', [53, 54]),

#                 ('ind', [65, 66, 67]),
#                 ('pass', [4, 8]),
#                 ('pass', [16, 18, 19]),
#                 ('ind', [91, 92]),
#                 ('pass', [7, 10, 25]),
#                 ('pass', [22, 23]),
#                 ('ind', [53, 54]),

#                 ('pass', [9, 5, 6]),
#                 ('pass', [20, 21, 24]),
#                 ('ind', [120, 121, 122]),
#                 ('pass', [21, 11]),
#                 ('pass', [26, 27]),
#                 ('ind', [36, 37]),
#             ]

#             highlight_xdsm(self, image, list_to_highlight)
            
#             self.wait()

#             self.clear()

debug = False
class SimpleXDSM(MovingCameraScene):
    def setup(self):
        self.camera.background_color="#2d3c54"

        self.filename = "simple_xdsm"

        if debug:
            x = XDSM(use_sfmath=True)

            x.add_system("opt", OPT, r"\text{Optimizer}")
            x.add_system("func", FUNC, r"y = x^2 + 2 / x")

            x.connect("opt", "func", "x")
            x.connect("func", "opt", "y")

            x.add_output("func", "y", side=xdsm_right)
            x.add_output("opt", r'x^*, y^*', side=xdsm_left)

            x.write(self.filename)
            subprocess.run(["pdf2svg", f"{self.filename}.pdf", f"{self.filename}.svg"])

    if debug:
        def construct(self):
            get_xdsm_indices(self, f"{self.filename}.svg")
    else:
        def construct(self):
            image = load_xdsm(f"{self.filename}.svg")

            def add_elements(indices):
                group = VGroup()
                for idx in indices:
                    subm = image.submobjects[idx]

                    # Hack to make boxes go over gray lines
                    tol = 1.e-2
                    if subm.width > tol and subm.height > tol:
                        subm.set_z_index(1)
                    group.add(subm)

                anims = []
                for obj in group:
                    anims.append(Write(obj))
                self.play(AnimationGroup(*anims))
                self.wait()

            def remove_elements(indices):
                group = VGroup()
                for idx in indices:
                    subm = image.submobjects[idx]
                    group.add(subm)

                anims = []
                for obj in group:
                    anims.append(FadeOut(obj))
                self.play(AnimationGroup(*anims))
                self.wait()

            add_elements([18, 19, 20, 21, 22, 23, 24, 25, 26])  # add func box
            add_elements([14, 15, 4])  # add inputs
            add_elements([27, 28, 3])  # add outputs            
            
            list_to_highlight = [
                ('pass', [4]),
            ]
            for i in range(3):
                highlight_xdsm(self, image, list_to_highlight, wait=False)

            list_to_highlight = [
                ('pass', [3]),
            ]
            for i in range(3):
                highlight_xdsm(self, image, list_to_highlight, wait=False)

            self.wait()

            remove_elements([27, 28, 3])  # remove outputs  

            add_elements([16, 17])
            self.wait()

            add_elements([12, 13])
            add_elements([5, 0, 1])

            list_to_highlight = [
                ('pass', [0]),
                ('pass', [4]),
                ('pass', [1]),
                ('pass', [5]),
            ]
            for i in range(4):
                highlight_xdsm(self, image, list_to_highlight, wait=False)
            add_elements([2, 6, 7, 8, 9, 10, 11])

            list_to_highlight = [
                ('pass', [2]),
                ('ind', [6, 7, 8, 9, 10, 11]),
            ]
            highlight_xdsm(self, image, list_to_highlight, wait=False)
            self.wait()

            self.clear()


# class ScanEagle(MovingCameraScene):
#     def setup(self):
#         self.camera.background_color="#2d3c54"

#         self.filename = "scaneagle_no_tube"

#     def construct(self):
#         get_xdsm_indices(self, f"{self.filename}.svg")