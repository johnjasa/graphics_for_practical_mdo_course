from manim import *
import numpy as np
from manim_helper_functions import *
import openmdao.api as om


class TitleSlide(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        title = r"Why optimization convergence is important"
        contents_list = [
            "What do we mean by convergence?",
            "Convergence means that the constraints are valid",
            "Converged results allow you to compare design points",
            ]

        intro_message = r"""Getting a converged optimization result is important so you are comparing and understanding designs that are optimal. This gives you an apples-to-apples comparison."""

        outro_message = "For designs resulting from optimizations to be meaningful, your optimization runs must be converged."

        make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["opt"])


class GBOptimization(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#2d3c54"

        # objective function
        def objective(x, y):
            return (x - 1) ** 2 + 20 * (y - x ** 2) ** 2

        excomp = om.ExecComp("obj = (x-1)**2 + 20*(y-x**2)**2")

        prob = om.Problem()
        prob.model.add_subsystem("excomp", excomp, promotes=["*"])
        prob.driver = om.pyOptSparseDriver(optimizer="SLSQP")

        prob.driver.recording_options["includes"] = ["*"]
        recorder = om.SqliteRecorder("slsqp_opt_converge.sql")
        prob.driver.add_recorder(recorder)

        prob.model.add_design_var("x", lower=-3.0, upper=3.0)
        prob.model.add_design_var("y", lower=-3.0, upper=3.0)
        prob.model.add_objective("obj")

        prob.setup()

        prob.set_val("x", 2.0)
        prob.set_val("y", 2.0)

        # # run the optimization
        # prob.run_driver()

        results = get_results("slsqp_opt_converge.sql")

        print(results)

        image, ax = plot_2d_function(objective, r_min=-3, r_max=3, font_size=24)
        self.play(FadeIn(image, ax))
        self.wait()
        draw_results(self, results, ax)
        self.wait()
        clear(self)

        # create the axes and the curve
        x = results["x"]
        y = results["y"]
        obj = results["obj"]
        range = np.arange(len(x))


        ax = Axes(
            x_range=[0, len(x)],
            y_range=[np.min(obj), np.max(obj), 1.0e2],
            axis_config={"include_numbers": True},
            x_axis_config={"numbers_to_include": np.arange(0, len(x), 2)},
        )
        labels = ax.get_axis_labels(
            x_label=r"\text{Iterations}", y_label=r"\text{Objective}"
        )
        self.play(Create(ax), Create(labels))
        plot = ax.plot_line_graph(range, obj, line_color=WHITE, add_vertex_dots=False)
        self.play(Create(plot), run_time=6, rate_func=rate_functions.linear)
        self.wait()

        dot = Dot(color=RED).shift(ax.coords_to_point(12, 0, 0.))
        self.add(dot)
        self.play(Flash(dot, color=RED), run_time=2)
        self.wait()
        self.remove(dot)
        self.wait()

        clear(self)

        

        ax2 = Axes(
            x_range=[0, len(x)],
            y_range=[-6, 3, 3],
            axis_config={"include_numbers": True},
            x_axis_config={"numbers_to_include": np.arange(0, len(x), 2)},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
        )
        labels2 = ax.get_axis_labels(
            x_label=r"\text{Iterations}", y_label=r"\text{log(Objective)}"
        )
        plot = ax2.plot_line_graph(range, obj, line_color=WHITE, add_vertex_dots=False)
        self.play(Create(ax2), Create(labels2))
        self.wait()
        self.play(Create(plot), run_time=6, rate_func=rate_functions.linear)
        self.wait()
        clear(self)



        ax = Axes(
            x_range=[0, len(x)],
            y_range=[min(np.min(x), np.min(y)), max(np.max(x), np.max(y))],
            axis_config={"include_numbers": True},
            x_axis_config={"numbers_to_include": np.arange(0, len(x), 2)},
        )
        plot = ax.plot_line_graph(range, x, line_color=WHITE, add_vertex_dots=False)
        plot2 = ax.plot_line_graph(range, y, line_color=WHITE, add_vertex_dots=False)
        labels = ax.get_axis_labels(
            x_label=r"\text{Iterations}", y_label=r"\text{DV values}"
        )

        self.play(Create(ax), Create(labels))
        self.play(
            Create(plot), Create(plot2), run_time=6, rate_func=rate_functions.linear
        )
        self.wait()

        clear(self)
        self.wait()
