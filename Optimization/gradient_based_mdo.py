from manim import *
import numpy as np
from manim_helper_functions import *
import openmdao.api as om
from pyxdsm.XDSM import XDSM, OPT, SOLVER, FUNC, LEFT as xdsm_left, RIGHT as xdsm_right
import subprocess



# class TitleSlide(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"

#         title = r"Gradient-based multidisciplinary optimization"
#         contents_list = [
#             "What is gradient-based MDO?",
#             "Gradient-based MDO allows you to solve tough problems",
#             "Why is gradient-based MDO hard?",
#             "OpenMDAO helps you do gradient-based MDO",
#             ]
#         intro_message = "Gradient-based multidisciplinary optimization is the bee's knees. The cat's pajamas. The ultimate goal of this short course is for you to be able to formulate and solve complicated optimization problems using gradient-based methods in an efficient manner."
#         outro_message = "Gradient-based MDO is powerful yet challenging. OpenMDAO helps you solve tough multidisciplinary problems."

#         make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["mda", "opt", "diff"])

# debug = False

# class BizarroSystem(MovingCameraScene):
#     def setup(self):
#         self.camera.background_color="#2d3c54"

#         self.filename = "nonlinear"
#         self.filename_lin = "linear"

#         if debug:
#             # Change `use_sfmath` to False to use computer modern
#             x = XDSM(use_sfmath=True)

#             x.add_system("geom", FUNC, r"\text{Geometry}")
#             x.add_system("solver", SOLVER, r"\text{NLBGS}")
#             x.add_system("aero", FUNC, r"\text{Aerodynamics}")
#             x.add_system("struct", FUNC, r"\text{Structures}")
#             x.add_system("functionals", FUNC, r"\text{Functionals}")
            
#             x.connect('geom', 'aero', r'\text{Baseline mesh}')
#             x.connect('geom', 'struct', r'\text{Baseline mesh}')
#             x.connect('aero', 'struct', r'\textit{Aerodynamic loads}')
#             x.connect('aero', 'functionals', r'C_L, C_D, \text{etc}')
#             x.connect('struct', 'functionals', r'\text{Weight, etc}')

#             x.connect('struct', 'solver', r'\textit{Displaced mesh}')
#             x.connect('aero', 'solver', r'\textit{Aerodynamic loads}')
#             x.connect('solver', 'functionals', (r'\text{Displaced mesh,}', r'\text{aerodynamic loads}'))

#             x.connect('struct', 'aero', r'\textit{Displaced mesh}')

#             x.add_input("geom", r'\text{Twist}')
#             x.add_input("struct", r'\text{Spar thickness}')
            
#             x.add_output("functionals", (r"\text{Weight}, C_L/C_D,", r"\text{fuel burn}"), side=xdsm_right)
#             x.add_output("struct", (r"\text{Structural failure}"), side=xdsm_right)

#             x.write(self.filename)
#             subprocess.run(["pdf2svg", f"{self.filename}.pdf", f"{self.filename}.svg"])

            
#             # Change `use_sfmath` to False to use computer modern
#             x = XDSM(use_sfmath=True)

#             x.add_system("geom", FUNC, r"\text{Geometry}")
#             x.add_system("solver", SOLVER, r"\text{LNBGS}")
#             x.add_system("aero", FUNC, r"\text{Aerodynamics}")
#             x.add_system("struct", FUNC, r"\text{Structures}")
#             x.add_system("functionals", FUNC, r"\text{Functionals}")
            
#             x.connect('geom', 'aero', r'\text{Baseline mesh}')
#             x.connect('geom', 'struct', r'\text{Baseline mesh}')
#             x.connect('aero', 'struct', r'\textit{Aerodynamic loads}')
#             x.connect('aero', 'functionals', r'C_L, C_D, \text{etc}')
#             x.connect('struct', 'functionals', r'\text{Weight, etc}')

#             x.connect('struct', 'solver', r'\textit{Displaced mesh}')
#             x.connect('aero', 'solver', r'\textit{Aerodynamic loads}')
#             x.connect('solver', 'functionals', (r'\text{Displaced mesh,}', r'\text{aerodynamic loads}'))

#             x.connect('struct', 'aero', r'\textit{Displaced mesh}')

#             x.add_input("geom", r'\text{Twist}')
#             x.add_input("struct", r'\text{Spar thickness}')
            
#             x.add_output("functionals", (r"\text{Weight}, C_L/C_D,", r"\text{fuel burn}"), side=xdsm_right)
#             x.add_output("struct", (r"\text{Structural failure}"), side=xdsm_right)

#             x.write(self.filename_lin)
#             subprocess.run(["pdf2svg", f"{self.filename_lin}.pdf", f"{self.filename_lin}.svg"])

#     if debug:
#         def construct(self):
#             get_xdsm_indices(self, f"{self.filename}.svg")
#             get_xdsm_indices(self, f"{self.filename_lin}.svg")
#     else:
#         def construct(self):
#             image = load_xdsm(f"{self.filename}.svg")
#             system_text = Tex("System model", font_size=60).move_to(image.get_edge_center(UP)).shift(0.5*UP)
#             self.play(Write(image), FadeIn(system_text))
#             self.wait()

#             self.play(FadeOut(system_text), image.animate.scale(0.50).move_to((-3.5, 0, 0)))
#             self.wait()

#             nonlinear_text = Tex("Nonlinear system model").move_to(image.get_edge_center(UP)).shift(0.5*UP)
#             self.play(FadeIn(nonlinear_text))
#             self.wait()

#             image_lin = load_xdsm(f"{self.filename}.svg")
#             self.add(image_lin.scale(0.50).move_to((-3.5, 0, 0)))
#             self.play(image_lin.animate.move_to((3.5, 0, 0)), run_time=1.5)
#             self.wait()

#             image_lin_new = load_xdsm(f"{self.filename_lin}.svg").scale(0.50).move_to((3.5, 0, 0))
#             linear_text = Tex("Linear system model").move_to(image_lin.get_edge_center(UP)).shift(0.5*UP)
#             self.play(FadeIn(linear_text))
#             self.play(Transform(image_lin, image_lin_new))

#             list_to_highlight = [('ind', [36, 37])]

#             highlight_xdsm(self, image_lin, list_to_highlight)
#             self.wait()

#             model_text = Tex(r"""Used for analysis\\(compute and run\_model)""", font_size=28).move_to(image.get_edge_center(DOWN)).shift(0.5*DOWN)
#             total_text = Tex(r"""Used for derivatives\\(compute\_partials and compute\_totals)""", font_size=28).move_to(image_lin.get_edge_center(DOWN)).shift(0.5*DOWN)
#             self.play(FadeIn(model_text), FadeIn(total_text))
#             self.wait()

#             anims = []
#             opt_text = Tex("Both used for optimization").move_to((0., -3., 0))
#             line1 = Line(model_text.get_edge_center(DOWN), opt_text.get_edge_center(UP), color=WHITE)
#             line2 = Line(total_text.get_edge_center(DOWN), opt_text.get_edge_center(UP), color=WHITE)

#             anims.append(Write(line1))            
#             anims.append(Write(line2))
#             anims.append(FadeIn(opt_text))

#             self.play(LaggedStart(*anims, lag_ratio=0.25))
#             self.wait()

#             self.play(FadeOut(linear_text), FadeOut(nonlinear_text), FadeOut(opt_text), FadeOut(line1), FadeOut(line2), FadeOut(model_text), FadeOut(total_text))

#             self.play(image.animate.move_to((0., 0., 0.)), image_lin.animate.move_to((0., 0., 0)))
#             self.play(FadeOut(image_lin))
#             self.play(image.animate.scale(2.), FadeIn(system_text))

#             self.wait()


# class GradientBasedMDO(MovingCameraScene):
#     def setup(self):
#         self.camera.background_color="#2d3c54"

#     def construct(self):
#         myTemplate = TexTemplate()
#         myTemplate.add_to_preamble(r"\usepackage{physics}")
#         text = Tex("Gradient-based multidisciplinary design optimization")
#         self.play(Write(text))
#         self.wait()
        
#         rect = Rectangle(height=1, width=3.4).shift(4.15*LEFT)
#         self.play(Create(rect))
#         self.wait()

#         # image = ImageMobject("gradient_2d_diff.png").scale(.25).move_to((-4.5, 2.2, 0))
#         # self.play(FadeIn(image))
#         # self.wait()

#         grad_text = MathTex(r"\frac{\mathrm{d} f}{\mathrm{~d} x}=\frac{\partial F}{\partial x}+\frac{\partial F}{\partial y} \frac{\mathrm{d} y}{\mathrm{~d} x}")
#         grad_text.move_to((-4.5, 2.2, 0))
#         self.play(FadeIn(grad_text))
#         self.wait()

#         rect1 = Rectangle(height=1, width=3.75).shift(0.45*LEFT)
#         self.play(Transform(rect, rect1), FadeOut(grad_text))
#         self.wait()

#         multid = load_xdsm("nonlinear", scale=0.5, filter_small_lines=False).move_to((-3, -2.25, 0))
#         self.play(FadeIn(multid))
#         self.wait()


#         rect1 = Rectangle(height=1, width=1.5).shift(2.2*RIGHT)
#         self.play(Transform(rect, rect1), FadeOut(multid))
#         self.wait()

#         # x = XDSM(use_sfmath=True)

#         # x.add_system("analysis", FUNC, r"\text{Analysis}")
        
#         # x.add_input("analysis", r'\text{Design variables}')
#         # x.add_output("analysis", r"\text{Performance metrics}", side=xdsm_right)

#         # filename = "design"
#         # x.write(filename)
#         # subprocess.run(["pdf2svg", f"{filename}.pdf", f"{filename}.svg"])

#         design = load_xdsm("design", scale=0.4).move_to((2.5, 2.5, 0))
#         self.play(FadeIn(design))
#         self.wait()

#         list_to_highlight = [
#             ('ind', [2, 3, 4, 5, 6]),
#             ('rev_pass', [1]),
#             ('ind', [7, 8]),
#             ('pass', [0]),
#             ('ind', [9, 10, 11, 12, 13]),
#         ]
#         highlight_xdsm(self, design, list_to_highlight)


#         rect1 = Rectangle(height=1, width=2.9).shift(4.45*RIGHT)
#         self.play(Transform(rect, rect1), FadeOut(design))
#         self.wait()

#         opt = r"""
#             \begin{table}[]
#             \def\arraystretch{1.0}
#             \centering
#             \begin{tabular}{rl}
#             Minimize & $f_{\text{obj}}(\vb*{\va{x}})$ \\ \\
#             With respect to: & \\
#             Design variables & $\vb*{\va{x}}$ \\ \\
#             Subject to: & \\
#             Constraints & $g_{\text{lb}} \leq g(\vb*{\va{x}}) \leq g_{\text{ub}} $ \\
#                         & $h(\vb*{\va{x}}) = h_{\text{eq}} $ \\
#             \end{tabular}
#             \end{table}
#         """
#         opt_text = Tex(opt, font_size=28).move_to((3.5, -2.25, 0))
#         self.play(FadeIn(opt_text))
#         self.wait()

#         self.play(FadeOut(rect), FadeOut(opt_text))


#         self.wait()
#         self.play(FadeIn(grad_text), FadeIn(design), FadeIn(opt_text), FadeIn(multid))
#         self.wait()

#         clear(self)


# class GradientFreeVSBased(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"
#         self.camera.frame.save_state()

#         image = SVGMobject("gbased_vs_gfree", unpack_groups=False, stroke_width=3)
#         image.scale(3.)
#         caption = Tex("Fig. 1.23 from Engineering Design Optimization by Martins and Ning").scale(0.7).move_to((0, -3.75, 0))
#         self.play(Write(image), Write(caption))
#         self.wait(2)

#         def add_elements(asset, indices):
#             group = VGroup()
#             for idx in indices:
#                 subm = asset.submobjects[idx]

#                 # Hack to make boxes go over gray lines
#                 tol = 1.e-2
#                 if subm.width > tol and subm.height > tol:
#                     subm.set_z_index(1)
#                 group.add(subm)

#             anims = []
#             for obj in group:
#                 anims.append(Write(obj))
#             self.play(AnimationGroup(*anims))
#             self.wait()

#         def remove_elements(asset, indices):
#             group = VGroup()
#             for idx in indices:
#                 subm = asset.submobjects[idx]
#                 group.add(subm)

#             anims = []
#             for obj in group:
#                 anims.append(FadeOut(obj))
#             self.play(AnimationGroup(*anims))
#             self.wait()

#         self.play(self.camera.frame.animate.scale(0.1).move_to((2.8, -1.8, 0)))
#         self.wait()

#         remove_elements(image, [34])
#         self.wait()

#         add_elements(image, [34])
#         self.wait()

#         self.play(Restore(self.camera.frame))
#         self.wait()

#         clear(self)

class SeqVsMDO(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        image = ImageMobject("seq_mdo_white.png").scale(.5).move_to((-2.5, 0., 0))
        caption = Tex("Fig. 13.34 from Engineering Design Optimization by Martins and Ning").scale(0.7).move_to((-1., -3.75, 0))
        caption2 = Tex(r"""\raggedright{Contour lines show the objective, fuel burn.\\
            Better values are lower on the plot.}""", font_size=26).align_to(image.get_edge_center(RIGHT), LEFT).shift(0.2*RIGHT)
        self.play(FadeIn(image), FadeIn(caption), FadeIn(caption2))
        self.wait(2)

        clear(self)

