from manim import *
import numpy as np
from manim_helper_functions import *
from pyxdsm.XDSM import XDSM, OPT, SOLVER, FUNC, LEFT as xdsm_left, RIGHT as xdsm_right
import subprocess


# class TitleSlide(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"

#         title = r"Solving coupled systems"
#         contents_list = [
#             "How to recognize when you need a solver",
#             "Solving a simple system by hand",
#             "Notes specific for OpenMDAO",            
#             ]
#         intro_message = "When you have a coupled or implicit system, you must use a solver to converge that system. Take time to recognize those systems within your models and identify the best way to solve them."
#         outro_message = "Determine if your system is coupled or implicit and if it is, make sure to use solvers to correctly account for those relationships."

#         make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["mda"])


# class SimpleSystem(MovingCameraScene):
#     def setup(self):
#         self.camera.background_color="#2d3c54"
#         myTemplate = TexTemplate()
#         myTemplate.add_to_preamble(r"\usepackage{physics}")
#         myTemplate.add_to_preamble(r"\usepackage{bm}")
#         myTemplate.add_to_preamble(r"\usepackage{amsmath}")

#         # Show residual calc
#         self.play(Write(MathTex(r"R(\vb*{\va{x}}) = \vb*0")))
#         self.wait()
#         clear(self)
#         self.wait()

#         # Show linear system
#         linear_system = MathTex(r"[\vb*A] \vb*{\va{x}} = \vb*{\va{b}}")
#         self.play(Write(linear_system))
#         self.wait()

#         linear_system_string = r"""
#             \[
#             \begin{bmatrix}
#             a_{11} & a_{12} & a_{13} & \dots & a_{1n} \\
#             a_{21} & a_{22} & a_{23} & \dots & a_{2n} \\
#             \dots  & \dots  & \dots  & \dots & \dots  \\
#             a_{n1} & a_{n2} & a_{n3} & \dots & a_{nn} 
#             \end{bmatrix}
#             \begin{bmatrix}
#             x_1 \\ x_2 \\ \dots \\ x_n 
#             \end{bmatrix}
#             =
#             \begin{bmatrix}
#             b_{1} \\ b_{2} \\ \dots \\ b_{n}
#             \end{bmatrix}
#             \]"""
#         self.play(Transform(linear_system, Tex(linear_system_string)))
#         self.wait()

#         self.play(Transform(linear_system, MathTex(r"[\vb*A] \vb*{\va{x}} = \vb*{\va{b}}")))
#         self.wait()

#         self.play(Transform(linear_system, MathTex(r"[\vb*A] \vb*{\va{x}} - \vb*{\va{b}} = \vb*0")))
#         self.wait()
        
#         self.play(Transform(linear_system, MathTex(r"[\vb*A] \vb*{\va{x}} - \vb*{\va{b}} = \vb*0 = R(\vb*{\va{x}})")))
#         self.wait()

#         # Show nonlinear system
#         nonlinear_system_string = r"""
#             \begin{alignat*}{4}
#             9x^2 + y^2 = 9 \\
#             y - 3 = 3x^2
#             \end{alignat*}"""
#         self.play(Transform(linear_system, Tex(nonlinear_system_string)))
#         self.wait()

#         nonlinear_system_string = r"""
#             \begin{alignat*}{4}
#             9x^2 + y^2 = 9 \\
#             y = 3x^2 + 3
#             \end{alignat*}"""
#         self.play(Transform(linear_system, Tex(nonlinear_system_string)))
#         self.wait()

#         nonlinear_system_string = r"""
#             \begin{alignat*}{4}
#             9x^2 + (3x^2 + 3)^2 = 9
#             \end{alignat*}"""
#         self.play(Transform(linear_system, Tex(nonlinear_system_string)))
#         self.wait()

#         nonlinear_system_string = r"""
#             \begin{alignat*}{4}
#             9x^2 + 9x^4+18x^2+9 = 9
#             \end{alignat*}"""
#         self.play(Transform(linear_system, Tex(nonlinear_system_string)))
#         self.wait()

#         nonlinear_system_string = r"""
#             \begin{alignat*}{4}
#             x^2 + x^4 + 2x^2 = 0
#             \end{alignat*}"""
#         self.play(Transform(linear_system, Tex(nonlinear_system_string)))
#         self.wait()

#         nonlinear_system_string = r"""
#             \begin{alignat*}{4}
#             x = 0
#             \end{alignat*}"""
#         self.play(Transform(linear_system, Tex(nonlinear_system_string)))
#         self.wait()

#         nonlinear_system_string = r"""
#             \begin{alignat*}{4}
#             x = 0 \\
#             y - 3 = 3x^2
#             \end{alignat*}"""
#         self.play(Transform(linear_system, Tex(nonlinear_system_string)))
#         self.wait()

#         nonlinear_system_string = r"""
#             \begin{alignat*}{4}
#             x = 0 \\
#             y = 3
#             \end{alignat*}"""
#         self.play(Transform(linear_system, Tex(nonlinear_system_string)))
#         self.wait(2)
        
#         # Show nonlinear system
#         nonlinear_system_string = r"""
#             \begin{alignat*}{4}
#             2x^2 & {}+{} &  xy & {}+{} & 3z^3 & {}={} & 10 \\
#                 x & {}+{} &  y & {}+{} &  \sqrt{z} & {}={} &  6 \\
#                 x^3 & {}+{} & 3yz & {}+{} & 2z & {}={} & 13
#             \end{alignat*}"""
#         self.play(Transform(linear_system, Tex(nonlinear_system_string)))
#         self.wait()

#         self.play(Transform(linear_system, MathTex(r"R(\vb*{\va{x}}) = \vb*0")))

#         clear(self)

#         image = ImageMobject("esav.png")
#         image.height = 5.
#         image_caption = Tex(r"Pressure contours on the ESAV aircraft, Jasa 2020", font_size=36).shift(3*DOWN)
#         self.play(FadeIn(image), FadeIn(image_caption))
#         self.wait(2)
#         clear(self)
        

# debug = False
# class SimpleXDSM(MovingCameraScene):
#     def setup(self):
#         self.camera.background_color="#2d3c54"

#         self.filename = "xdsm_for_solving_systems"

#     if debug:
#         def construct(self):
#             get_xdsm_indices(self, f"{self.filename}.svg", filter_small_lines=False)
#     else:
#         def construct(self):
#             dsm = load_xdsm(f"dsm", filter_small_lines=False)
#             directed_graph = load_xdsm(f"directed_graph", filter_small_lines=False)
#             xdsm = load_xdsm(f"xdsm_for_solving_systems", filter_small_lines=False)

#             def add_elements(asset, indices):
#                 group = VGroup()
#                 for idx in indices:
#                     subm = asset.submobjects[idx]

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

#             def remove_elements(asset, indices):
#                 group = VGroup()
#                 for idx in indices:
#                     subm = asset.submobjects[idx]
#                     group.add(subm)

#                 anims = []
#                 for obj in group:
#                     anims.append(FadeOut(obj))
#                 self.play(AnimationGroup(*anims))
#                 self.wait()

#             caption = Tex("Adapted from Fig. 13.10 and 13.11 from Engineering Design Optimization by Martins and Ning").scale(0.6).move_to((0, -3.5, 0))
#             self.play(FadeIn(caption))

#             dsm.scale(0.5).move_to((-4.5, 0, 0))
#             idxs = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13]
#             add_elements(dsm, idxs)

#             directed_graph.scale(0.5).move_to((0, 0, 0))
#             idxs = list(np.arange(len(directed_graph.submobjects)))
#             [idxs.pop(idx) for idx in [18, 17]]
#             add_elements(directed_graph, idxs)

#             xdsm.scale(0.5).move_to((4.5, 0, 0))
#             idxs = list(np.arange(len(xdsm.submobjects)))
#             xdsm_indices = [8, 26, 27, 28, 29, 3]
#             [idxs.pop(idx) for idx in reversed(sorted(xdsm_indices))]
#             add_elements(xdsm, idxs)

#             caption2 = Tex("Three different depictions of the same feed-forward system").scale(0.8).move_to((0, 3., 0))
#             caption3 = Tex("The system now has backwards feedback and you need a solver!").scale(0.8).move_to((0, 3., 0))
#             self.play(Write(caption2))

#             self.wait()

#             group = VGroup()
#             group.add(dsm.submobjects[7])
#             group.add(directed_graph.submobjects[17])
#             group.add(directed_graph.submobjects[18])
#             for idx in xdsm_indices:
#                 subm = xdsm.submobjects[idx]
#                 group.add(subm)
#             anims = []
#             for obj in group:
#                 anims.append(Write(obj))
#             self.play(AnimationGroup(*anims), Transform(caption2, caption3))

#             self.wait()
#             self.clear()


debug = False
class GraphReordering(MovingCameraScene):
    def setup(self):
        self.camera.background_color="#2d3c54"

        self.filename = "component_reordering"

    if debug:
        def construct(self):
            get_xdsm_indices(self, f"{self.filename}.svg", filter_small_lines=False)
    else:
        def construct(self):
            xdsm = load_xdsm(f"{self.filename}.svg", filter_small_lines=False)

            def add_elements(asset, indices):
                group = VGroup()
                for idx in indices:
                    subm = asset.submobjects[idx]

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

            def remove_elements(asset, indices):
                group = VGroup()
                for idx in indices:
                    subm = asset.submobjects[idx]
                    group.add(subm)

                anims = []
                for obj in group:
                    anims.append(FadeOut(obj))
                self.play(AnimationGroup(*anims))
                self.wait()

            caption = Tex("Fig. 13.14 from Engineering Design Optimization by Martins and Ning").scale(0.6).move_to((0, -3.5, 0))
            self.play(FadeIn(caption))

            idxs = list(np.arange(35))
            add_elements(xdsm, idxs)
            self.wait()

            unordered = Tex("Unordered system").move_to((-3.5, 3.5, 0))
            self.play(FadeIn(unordered))
            self.wait()

            
            idxs = list(np.arange(35, 71))
            add_elements(xdsm, idxs)
            self.wait()

            ordered = Tex("The same system reordered").move_to((3.5, 3.5, 0))
            self.play(FadeIn(ordered))
            self.wait()

            clear(self)