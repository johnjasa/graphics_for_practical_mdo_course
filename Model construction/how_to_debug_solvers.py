from manim import *
import numpy as np
from manim_helper_functions import *


# class TitleSlide(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"

#         title = r"How to debug solvers"
#         contents_list = [
#             "What types of solvers are you using?",
#             "Should you expect convergence?",
#             "Checklist for solver debugging (in OpenMDAO)",
#             ]
#         intro_message = "Optimizers often push systems to their limits of multidisciplinary analysis, so sometimes solvers don't converge. You can follow a series of debugging steps to determine why this is and implement a solution."
#         outro_message = "Solver convergence is sometimes tricky business. Follow this checklist to help put some order to the madness."

#         make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["mda"])

# class MiddlePoint(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"
#         myTemplate = TexTemplate()
#         myTemplate.add_to_preamble(r"\usepackage{amsmath}")
        
#         resids = Tex(r"""\begin{align*}
# \begin{bmatrix}
# x_{1} \\
# x_{2} \\
# \vdots \\
# x_{m-1} \\
# x_{m}
# \end{bmatrix}
# \end{align*}
# """)
#         initial_state_vector = Tex("Initial state vector", font_size=48, color=WHITE).move_to(resids.get_edge_center(UP) + np.array([0., 0.5, 0.]))
#         self.play(Write(resids), Write(initial_state_vector))
#         self.wait()

#         resids_0 = Tex(r"""\begin{align*}
# \begin{bmatrix}
# 0 \\
# 0 \\
# \vdots \\
# 0 \\
# 0
# \end{bmatrix}
# \end{align*}
# """)
#         self.play(Transform(resids, resids_0))
#         self.play(resids.animate.move_to((-4., 0., 0.)), initial_state_vector.animate.shift(4*LEFT))

#         textbox = VGroup() # create a VGroup
#         box = Rectangle(  # create a box
#             height=1, width=3, fill_color=WHITE, 
#             fill_opacity=0.5, stroke_color=WHITE
#         )
#         text = Tex("Solver", font_size=60, color=WHITE).move_to(box.get_center()) # create text
#         textbox.add(box, text)

#         arrow = Arrow(start=resids.get_edge_center(RIGHT), end=textbox.get_edge_center(LEFT))
#         self.play(Write(arrow), Write(textbox))        
#         self.wait()

#         resids_final = Tex(r"""\begin{align*}
# \begin{bmatrix}
# 23,945 \\
# 789 \\
# \vdots \\
# 4662 \\
# 14,822
# \end{bmatrix}
# \end{align*}
# """).move_to((4, 0., 0.))
#         final_state_vector = Tex("Converged state vector", font_size=48, color=WHITE).move_to(resids_final.get_edge_center(UP) + np.array([0., 0.5, 0.]))

#         arrow2 = Arrow(start=textbox.get_edge_center(RIGHT), end=resids_final.get_edge_center(LEFT))
#         self.play(Write(arrow2), Write(resids_final), Write(final_state_vector))        
#         self.wait()
#         self.play(arrow2.animate.set_opacity(0.2), resids_final.animate.set_opacity(0.2), final_state_vector.animate.set_opacity(0.2))
#         self.wait()

#         resids_better = Tex(r"""\begin{align*}
# \begin{bmatrix}
# 10,000 \\
# 1000 \\
# \vdots \\
# 1000 \\
# 10,000
# \end{bmatrix}
# \end{align*}
# """).move_to((-4.6, 0., 0.))
#         self.play(Transform(resids, resids_better), arrow2.animate.set_opacity(1.0), resids_final.animate.set_opacity(1.0), final_state_vector.animate.set_opacity(1.0), initial_state_vector.animate.shift(0.3*LEFT))
#         self.wait()

#         clear(self)


# class BendyWing(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"

#         image = SVGMobject("crm_fig.svg").move_to((-3, 0, 0))
#         image.height = 6
#         self.play(Write(image))
#         self.wait()

#         arrows = VGroup()
#         arrows.add(Arrow(start=(-4.75, -3.5, 0), end=(-4.75, -1., 0)))
#         arrows.add(Arrow(start=(-2.8, -0.5, 0), end=(-2.8, 2., 0)))
#         arrows.set_z_index(99999.)
#         self.play(Create(arrows))
#         self.wait()

#         code = '''==================
# AS_point_0.coupled
# ==================
# NL: NLBGS 1 ; 544210.77 1
# NL: NLBGS 2 ; 1084801.38 1.99334788
# NL: NLBGS 3 ; 580774.24 1.06718623
# NL: NLBGS 4 ; 708902.246 1.30262443
# NL: NLBGS 5 ; 1095934.34 2.01380495
# NL: NLBGS 6 ; 2936158.74 5.39526027
# NL: NLBGS 7 ; 2714050.96 4.98713203
# NL: NLBGS 8 ; 2944253.25 5.41013411
# NL: NLBGS 9 ; 2.33911213e+10 42981.7317
# NL: NLBGS 10 ; 5.97112757e+11 1097208.64
# NL: NLBGS 11 ; 5.96746988e+13 109653653
# NL: NLBGS 12 ; 5.40054817e+18 9.92363339e+12
# NL: NLBGS 13 ; 9.93389021e+42 1.82537553e+37
#         '''
#         rendered_code = Code(code=code, tab_width=4, background="window",
#                             language="Python", font="Monospace", font_size=16,
#                             insert_line_no=False, line_spacing=0.4)
#         self.play(Write(rendered_code.move_to([3., -1., 0.])))
#         self.wait()

#         clear(self)


# class SolverTypes(MovingCameraScene):
#     def setup(self):
#         self.camera.background_color="#2d3c54"
#         self.filename = "solver_types"

#     def construct(self):
#         image = load_xdsm(f"{self.filename}.svg", filter_small_lines=False)
#         caption = Tex("Fig. 3.13 from Engineering Design Optimization by Martins and Ning").scale(0.8).move_to((0, -3.5, 0))

#         self.play(FadeIn(caption), FadeIn(image))
#         self.wait(2)
#         self.clear()


class SolverChecklistNew(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{setspace}")
        
        checklist = r"""\setstretch{1.2}
\raggedright{
0. Try using more solver iterations\\
1. Use solver debug printing in OpenMDAO\\
2. Check your data connections within your model\\
3. Improve your initial guess for the states\\
4. Try checking the bounds on the state values in your model\\
5. For fixed-point iteration methods, use Aitken relaxation\\
6. For Newton methods, follow the detailed debugging doc page\\
7. Reorganize your model to minimize subsystem size within a solver\\
8. Try using a nested solver hierarchy or a different solver setup\\
9. Remove (or "fix") some states within the solver loop\\
}"""
        self.play(Write(Tex(checklist).scale(0.85)))
        self.wait(2)
        self.clear()

        checklist = [
            "0. Try using more solver iterations",
            "1. Use solver debug printing in OpenMDAO",
            "2. Check your data connections within your model",
            "3. Improve your initial guess for the states",
            "4. Try checking the bounds on the state values in your model",
            "5. For fixed-point iteration methods, use Aitken relaxation",
            "6. For Newton methods, follow the detailed debugging doc page",
            "7. Reorganize your model to minimize subsystem size within a solver",
            "8. Try using a nested solver hierarchy or a different solver setup",
            '9. Remove (or "fix") some states within the solver loop',
        ]

        for message in checklist:
            write_caption(self, message, scale=0.85)


        