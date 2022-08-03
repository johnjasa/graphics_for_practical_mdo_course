from manim import *
import numpy as np
from manim_helper_functions import *


class TitleSlide(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        title = r"Types of solvers and when to use them"
        contents_list = [
            "Brief introduction to solver types",
            "Solvers within OpenMDAO",
            ]
        intro_message = "For nonlinear and linear systems there are various solvers that can converge your system. The best solver to use is highly problem dependent but the goal of this lecture is to be able to recognize a reasonable staring configuration for your systems."
        outro_message = "Solvers are needed to resolve coupling or compute gradient information for multidisciplinary systems. The best solver setup is highly problem dependent."

        make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["mda"])


class ShowSolverConvergence(MovingCameraScene):
    def setup(self):
        self.camera.background_color="#2d3c54"
        self.camera.frame.save_state()

        # Show graphical convergence for NLBGS
        nlbgs = [50.5247285,
            3.91711889,
            0.0758730639,
            0.00150052731,
            2.96633139e-5,
            5.86406806e-7,
            1.15925306e-8,
            2.29166181e-10,
        ]

        # Aitken
        nlbgs_aitken = [50.5247285,
            3.91711889,
            0.0744313595,
            2.9722743e-5,
            1.16801147e-8,
            2.21703753e-10,
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
        newton_ls = [12.25451411,
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
        tol_label = Tex("Tolerance", font_size=30).move_to(line.get_corner(UR)).shift(-4, -0.2, 0)
        self.play(Create(line), Create(tol_label))
        self.wait()
        
        solvers = [nlbgs, nlbgs_aitken, newton_no_solve_subsystems, newton, newton_ls]
        solver_labels = ['NLBGS', 'NLBGS w/ Aitken', 'Newton w/o solve\_subsystems', 'Newton', 'Newton w/ LS']
        colors = [ORANGE, BLUE, RED, GREEN, PURPLE]
        coords = [
            [5., 1.e-4, 0],
            [5., 2.e-11, 0],
            [11., 1.e-3, 0],
            [1.5, 5.e-3, 0],
            [1.6, 4.e-9, 0],
        ]

        for idx, solver in enumerate(solvers):
            x_data = np.arange(len(solver))
            plot = ax.plot_line_graph(x_data, solver, line_color=colors[idx], vertex_dot_style=dict(fill_color=colors[idx]))
            label = Tex(solver_labels[idx], color=colors[idx], font_size=36)
            label.move_to(np.array(ax.c2p(*coords[idx])))

            self.play(Write(plot), Write(label), run_time=2)
            self.wait()

debug = False

class SolverTypes(MovingCameraScene):
    def setup(self):
        self.camera.background_color="#2d3c54"
        self.filename = "solver_types"

    if debug:
        def construct(self):
            get_xdsm_indices(self, f"{self.filename}.svg", filter_small_lines=False)
    else:
        def construct(self):
            image = load_xdsm(f"{self.filename}.svg", filter_small_lines=False)
            caption = Tex("Fig. 3.13 from Engineering Design Optimization by Martins and Ning").scale(0.8).move_to((0, -3.5, 0))

            self.play(FadeIn(caption))

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

            add_elements([0, 1, 2, 3, 4]) # Solver
            add_elements([7, 5, 6, 65, 66, 67, 68]) # linear and nonlinear
            add_elements([10, 8, 9]) # direct
            add_elements([11, 12, 18, 19, 20, 21, 26, 13, 14, 15, 16, 17, 31, 27, 28, 29, 30, 25, 22, 23, 24]) # LU, QR, Cholesky
            add_elements([32, 36, 33, 34, 35]) # Iterative
            add_elements([37, 42, 38, 39, 40, 41]) # Fixed point
            add_elements([45, 43, 44, 45, 46, 47, 48, 49, 50, 51]) # Jacobi, GS, SOR
            add_elements([58, 52, 53, 54, 55, 56, 57, 61, 64, 59, 60, 62, 63]) # CG, GMRES

            self.wait()

            add_elements([69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 94, 95]) # Newton
            add_elements([80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90])
            add_elements([91, 92, 93])
            

            
            