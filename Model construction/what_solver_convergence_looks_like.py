from manim import *
import numpy as np
from manim_helper_functions import *
import openmdao.api as om
from pyxdsm.XDSM import XDSM, OPT, SOLVER, FUNC, LEFT
import subprocess


class TitleSlide(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        title = r"What solver convergence looks like"
        contents_list = [
            "The basic idea of convergence",
            "How to tell when a system is converged",
            "Convergence in the terminal",
            ]
        intro_message = "A system is converged when the residuals are close to 0 within a tolerance. How this is achieved depends on what solver you use, but generally you want your residuals to decrease as computationally quickly as possible."
        outro_message = 'Converging a system means that all coupling and implicit interactions have been resolved. The best solver settings and what "good" solver convergence means are highly problem dependent.'

        make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["mda"])


class ResidualCalc(MovingCameraScene):
    def setup(self):
        self.camera.background_color="#2d3c54"
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{physics}")
        myTemplate.add_to_preamble(r"\usepackage{bm}")
        myTemplate.add_to_preamble(r"\usepackage{amsmath}")

        # Show residual calc
        self.play(Write(MathTex(r"R(\vb*{\va{x}}) = \vb*0")))
        self.wait()
        clear(self)
        self.wait()

        # Show linear system
        linear_system = MathTex(r"[\vb*A] \vb*{\va{x}} = \vb*{\va{b}}")
        self.play(Write(linear_system))
        self.wait()

        linear_system_string = r"""
            \[
            \begin{bmatrix}
            a_{11} & a_{12} & a_{13} & \dots & a_{1n} \\
            a_{21} & a_{22} & a_{23} & \dots & a_{2n} \\
            \dots  & \dots  & \dots  & \dots & \dots  \\
            a_{n1} & a_{n2} & a_{n3} & \dots & a_{nn} 
            \end{bmatrix}
            \begin{bmatrix}
            x_1 \\ x_2 \\ \dots \\ x_n 
            \end{bmatrix}
            =
            \begin{bmatrix}
            b_{1} \\ b_{2} \\ \dots \\ b_{n}
            \end{bmatrix}
            \]"""
        self.play(Transform(linear_system, Tex(linear_system_string)))
        self.wait()

        # Show nonlinear system
        nonlinear_system_string = r"""
            \begin{alignat*}{4}
            2x^2 & {}+{} &  xy & {}+{} & 3z^3 & {}={} & 10 \\
                x & {}+{} &  y & {}+{} &  \sqrt{z} & {}={} &  6 \\
                x^3 & {}+{} & 3yz & {}+{} & 2z & {}={} & 13
            \end{alignat*}"""
        self.play(Transform(linear_system, Tex(nonlinear_system_string)))
        self.wait()

        self.play(Transform(linear_system, MathTex(r"[\vb*A] \vb*{\va{x}} = \vb*{\va{b}}")))
        self.wait()

        self.play(Transform(linear_system, MathTex(r"[\vb*A] \vb*{\va{x}} - \vb*{\va{b}} = \vb*0")))
        self.wait()
        
        self.play(Transform(linear_system, MathTex(r"[\vb*A] \vb*{\va{x}} - \vb*{\va{b}} = \vb*0 = R(\vb*{\va{x}})")))
        self.wait()

        self.play(Transform(linear_system, MathTex(r"R(\vb*{\va{x}}) = \vb*0")))
        self.wait()

        clear(self)



class ShowSolverConvergence(MovingCameraScene):
    def setup(self):
        self.camera.background_color="#2d3c54"
        self.camera.frame.save_state()
        self.camera.frame.scale(1.05)

        # Hit the bounds
        newton_bounded = [2.25451411,
            5.8309261e-03,
            1.8309261e-03,
            8.2309261e-04,
            6.2309261e-04,
            6.2309261e-04,
            6.2309261e-04,
            6.2309261e-04,
            6.2309261e-04,
            6.2309261e-04,
            6.2309261e-04,
            6.2309261e-04,
            6.2309261e-04,
            6.2309261e-04,
            6.2309261e-04,
            6.2309261e-04,
        ]

        newton_explode = [2.25451411,
            5.8309261e-02,
            1.8309261e-01,
            8.2309261e-00,
            8.2309261e1,
            8.2309261e4,            
        ]

        # Show graphical convergence for Newton
        newton = [2.25451411,
            5.8309261e-05,
            0.000862032337,
            1.6727336e-05,
            1.27465221e-08,
            6.78410217e-09,
            1.2648016e-10,
        ]

        # Newton with LS
        newton_ls = [2.25451411,
            5.8309261e-05,
            1.02607101e-06,
            2.025957e-08,
            4.00021349e-10,
        ]

        newton_no_solve_subsystems = [
            36.8229305,
            12.2837727,
            6.0606187,
            2.14967189,
            0.227624537,
            0.0642920936,
            0.00611849532,
            0.0015263487,
            0.00018041202,
            3.73164117e-05,
            5.04139962e-06,
            9.37031206e-07,
            1.36709744e-07,
            2.3929104e-08,
            3.64867603e-09,
            6.17305318e-10,
        ]
        # create the axes and the curve
        ax = Axes(
            x_range=[0.0001, 15.0001, 1],
            y_range=[-12, 2, 2],
            tips=False,
            axis_config={"include_numbers": True, "exclude_origin_tick": False},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
        )
        labels = ax.get_axis_labels(x_label=r"\text{Solver iteration}", y_label="R(x)")
        self.play(Create(ax), Create(labels))
        self.wait()
        line = DashedLine(ax.c2p(0., 1.e-9), ax.c2p(15., 1.e-9))
        tol_label = Tex("Tolerance", font_size=36).move_to(ax.c2p(12, 3.e-9, 0))
        self.play(Write(line), Write(tol_label))
        self.wait()
        
        solvers = [newton_explode, newton_bounded, newton_no_solve_subsystems, newton, newton_ls]
        solver_labels = ['Newton (bad guess)', 'Newton (bounded)', 'Newton w/o solve\_subsystems', 'Newton', 'Newton w/ LS']
        colors = [RED, ORANGE, BLUE, GREEN, PURPLE]
        coords = [
            [6.5, 3.e1, 0],
            [11., 3.e-3, 0],
            [12.6, 5.e-5, 0],
            [4., 5.e-5, 0],
            [1.65, 3.5e-9, 0],
        ]

        for idx, solver in enumerate(solvers):
            x_data = np.arange(len(solver))
            plot = ax.plot_line_graph(x_data, solver, line_color=colors[idx], vertex_dot_style=dict(fill_color=colors[idx]))
            label = Tex(solver_labels[idx], color=colors[idx], font_size=36)
            label.move_to(np.array(ax.c2p(*coords[idx])))

            self.play(Write(plot), Write(label), run_time=3)
            self.wait()

        