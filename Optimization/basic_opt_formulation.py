from manim import *
import numpy as np
from manim_helper_functions import *
import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image
import openmdao.api as om


class TitleSlide(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        title = r"Basic optimization problem formulation"
        contents_list = [
            "Objective function",
            "Design variables",
            "Constraints",
            "Example 2D optimization",
            ]
        intro_message = "One of the most important steps in optimization is formulating well-posed and meaningful problems that you can interpret accurately."
        outro_message = "Formulating a well-posed and reasonable optimization problem is important. You should start with the most simple optimization problem possible and build up complexity slowly, solving each problem along the way."

        make_title_slide(self, title, contents_list, intro_message, outro_message)


class BasicOptFormulation(Scene):
    def construct(self):
        self.camera.background_color="#2d3c54"
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{physics}")
        text_list = []

        # Objective discussion
        text_list.append(r"""
            Minimize & $f_{\text{obj}}(x)$ \\
        """)
        text_list.append(r"""
            Minimize & $f_{\text{cost}}(x)$ \\
        """)
        text_list.append(r"""
            Maximize & $f_{\text{performance}}(x)$ \\
        """)
        text_list.append(r"""
            Minimize & $-f_{\text{performance}}(x)$ \\
        """)
        text_list.append(r"""
            Minimize & $f_{\text{obj}}(x) = g(x) + h(x)$ \\
        """)
        text_list.append(r"""
            Minimize & $f_{\text{obj}}(x)$ \\
        """)

        # Design variables
        text_list.append(r"""
            Minimize & $f_{\text{obj}}(x)$ \\ \\
            With respect to: & \\
            Design variables & $x$ \\
        """)
        text_list.append(r"""
            Minimize & $f_{\text{obj}}(\vb*{\va{x}})$ \\ \\
            With respect to: & \\
            Design variables & $\vb*{\va{x}}$ \\
        """)
        text_list.append(r"""
            Minimize & $f_{\text{Aircraft weight}}(\vb*{\va{x}})$ \\ \\
            With respect to: & \\
            Design variables & $\vb*{\va{x}}_{\text{Wing structure thickness}}$ \\
                             & $\vb*{\va{x}}_{\text{Wing aerodynamic shape}}$ \\
        """)

        # Constraints
        text_list.append(r"""
            Minimize & $f_{\text{obj}}(\vb*{\va{x}})$ \\ \\
            With respect to: & \\
            Design variables & $\vb*{\va{x}}$ \\ \\
            Subject to: & \\
            Constraints & $g_{\text{lb}} \leq g(\vb*{\va{x}}) \leq g_{\text{ub}} $ \\
        """)

        text_list.append(r"""
            Minimize & $f_{\text{obj}}(\vb*{\va{x}})$ \\ \\
            With respect to: & \\
            Design variables & $\vb*{\va{x}}$ \\ \\
            Subject to: & \\
            Constraints & $g_{\text{lb}} \leq g(\vb*{\va{x}}) \leq g_{\text{ub}} $ \\
                        & $h(\vb*{\va{x}}) = h_{\text{eq}} $ \\
        """)

        beg_lines = r"""
            \begin{table}[]
            \def\arraystretch{1.0}
            \centering
            \begin{tabular}{rl}"""

        lagged_write(self, text_list, beginning_text=beg_lines, final_text=r"""
            \end{tabular}
            \end{table}""")


        self.wait()

        self.play(*[FadeOut(mob)for mob in self.mobjects])


class SequenceForExample(Scene):
    def construct(self):
        self.camera.background_color="#2d3c54"
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{physics}")
        text_list = []

        # Objective discussion
        text_list.append(r"""
            Minimize & $f_{\text{obj}}(x, y) = (x^2 + y - 11)^2 + (x+y^2 -7)^2$\\
        """)
        text_list.append(r"""
            Minimize & $f_{\text{obj}}(x, y) = (x^2 + y - 11)^2 + (x+y^2 -7)^2$\\ \\
            With respect to: & \\
            Design variables & $x, y$ \\
        """)
        text_list.append(r"""
            Minimize & $f_{\text{obj}}(x, y) = (x^2 + y - 11)^2 + (x+y^2 -7)^2$\\ \\
            With respect to: & \\
            Design variables & $x, y$ \\ \\
            Subject to: & \\
            Constraints & $x^2 + y^2 \leq 4 $ \\
        """)
        text_list.append(r"""
            Minimize & $f_{\text{obj}}(x, y) = (x^2 + y - 11)^2 + (x+y^2 -7)^2$\\ \\
            With respect to: & \\
            Design variables & $x, y$ \\ \\
            Subject to: & \\
            Constraints & $x^2 + y^2 \leq 4 $ \\
                        & $x + y = 1$ \\
        """)

        beg_lines = r"""
            \begin{table}[]
            \def\arraystretch{1.0}
            \centering
            \begin{tabular}{rl}"""

        lagged_write(self, text_list, beginning_text=beg_lines, final_text=r"""
            \end{tabular}
            \end{table}""",
            fresh_between=True)


        self.wait()

        self.play(*[FadeOut(mob)for mob in self.mobjects])


class SampleOptimization(Scene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        # objective function
        def objective(x, y):
            return (x**2 + y - 11)**2 + (x + y**2 -7)**2
        
        # define range for input
        r_min, r_max = -4., 4.
        # sample input range uniformly at 0.1 increments
        xaxis = np.arange(r_min, r_max, 0.01)
        yaxis = np.arange(r_min, r_max, 0.01)
        # create a mesh from the axis
        x, y = np.meshgrid(xaxis, yaxis)
        # compute targets
        results = objective(x, y)

        cm_hot = mpl.cm.get_cmap('viridis')
        im = np.array(results / np.max(results))
        im = cm_hot(im)
        im = np.uint8(im * 255)

        plt.figure(figsize=(10, 8))
        contours = plt.contour(x, y, results, 15, colors='black')
        plt.clabel(contours, inline=True, fontsize=12)
        plt.imshow(results, extent=[r_min, r_max, r_min, r_max], origin='lower', cmap='RdGy', alpha=0.5)
        ax = plt.gca()
        ax.axis('off')
        plt.savefig('out.png', transparent=True, bbox_inches="tight", dpi=300)

        im = Image.open("out.png")
        im2 = im.crop(im.getbbox())
        im2.save("out.png")

        image = ImageMobject('out.png').scale(0.55)

        ax = Axes(
            x_range=(r_min, r_max, 1),
            y_range=(r_min, r_max, 1),
            x_length=r_max - r_min,
            y_length=r_max - r_min,
            tips=False,
            axis_config={"include_numbers": True, "numbers_to_exclude": [r_min, r_max]},
        ).scale_to_fit_height(image.height)

        self.play(FadeIn(image, ax))

        self.wait()


        # Plot the minima and maxima
        minima = [
            [3., 2.],
            [-2.805118, 3.131312],
            [-3.779310, -3.283186],
            [3.584428, -1.848126],
        ]

        maxima = [[-.270845, -.923039]]

        def plot_dots(points):
            dots = VGroup()
            for idx, point in enumerate(points):
                dot = Dot(color=WHITE, stroke_width=.02, radius=0.06, stroke_color=BLACK).move_to(ax.c2p(point[0], point[1]))
                dots.add(dot)
            self.play(FadeIn(dots))
            anims = []
            for dot in dots:
                anims.append(Flash(dot, color=WHITE))
            self.play(LaggedStart(*anims, lag_ratio=0.25))
            self.wait()
            self.play(FadeOut(dots))
        
        plot_dots(maxima)
        plot_dots(minima)



        excomp = om.ExecComp('obj=(x**2 + y - 11)**2 + (x + y**2 -7)**2')

        prob = om.Problem()

        prob.model.add_subsystem('excomp', excomp, promotes=['*'])

        # setup the optimization
        prob.driver = om.ScipyOptimizeDriver()
        prob.driver.options['optimizer'] = 'SLSQP'
        prob.driver.options['tol'] = 1.e-9

        prob.driver.recording_options['includes'] = ['*']
        recorder = om.SqliteRecorder("unconstrained.sql")
        prob.driver.add_recorder(recorder)

        prob.model.add_design_var('x', lower=-4., upper=4.)
        prob.model.add_design_var('y', lower=-4., upper=4.)
        prob.model.add_objective('obj')

        prob.setup()

        # run the optimization
        prob.run_driver();

        def get_results(filename):
            cr = om.CaseReader(filename)
            cases = cr.get_cases()

            results = {}
            for case in cases:
                for key in case.outputs.keys():
                    if key not in results.keys():
                        results[key] = []
                    results[key].append(case.outputs[key])

            for key in case.outputs.keys():
                results[key] = np.array(results[key])

            return results

        results = get_results('unconstrained.sql')



        x_point = ValueTracker(1.0)
        y_point = ValueTracker(1.0)

        def draw_tangent_line_on_curve(x_value, y_value):
            dot = always_redraw(
                lambda: Dot(color=WHITE, stroke_width=.02, radius=0.06, stroke_color=BLACK).move_to(
                    ax.c2p(x_value.get_value(), y_value.get_value()))
                )
            return dot

        dot = draw_tangent_line_on_curve(x_point, y_point)

        def draw_results(results):
            x_prev = 1
            y_prev = 1
            self.play(FadeIn(dot))
            lines = VGroup()
            for idx, (x, y) in enumerate(zip(results['x'], results['y'])):
                line = Line(ax.c2p(x_prev, y_prev), ax.c2p(x, y))
                line.set_stroke(opacity=0.5)
                self.play(Create(line), x_point.animate.set_value(x), y_point.animate.set_value(y), run_time=.5, rate_func=linear)
                self.wait(0.1)
                lines.add(line)
                x_prev = x
                y_prev = y
            self.wait()
            
            self.play(FadeOut(dot), FadeOut(lines))

        draw_results(results)

        


        excomp = om.ExecComp('obj=(x**2 + y - 11)**2 + (x + y**2 -7)**2')
        constraint_comp = om.ExecComp('con=x**2 + y**2')

        prob = om.Problem()

        prob.model.add_subsystem('excomp', excomp, promotes=['*'])
        prob.model.add_subsystem('constraint_comp', constraint_comp, promotes=['*'])

        # setup the optimization
        prob.driver = om.ScipyOptimizeDriver()
        prob.driver.options['optimizer'] = 'SLSQP'
        prob.driver.options['tol'] = 1.e-9

        prob.driver.recording_options['includes'] = ['*']
        recorder = om.SqliteRecorder("constrained.sql")
        prob.driver.add_recorder(recorder)

        prob.model.add_design_var('x', lower=-4., upper=4.)
        prob.model.add_design_var('y', lower=-4., upper=4.)
        prob.model.add_constraint('con', upper=4)

        prob.model.add_objective('obj')

        prob.setup()

        # run the optimization
        prob.run_driver();

        results = get_results('constrained.sql')

        circle = Circle(radius=np.linalg.norm(ax.c2p(2., 0.)), color=RED)
        square = Square(side_length=np.linalg.norm(ax.c2p(8., 0.)))
        un = Difference(
            square, circle, stroke_width=0., color=RED, fill_opacity=0.25)
        self.play(FadeIn(circle), FadeIn(un))
        self.wait()
        
        x_point.set_value(1.0)
        y_point.set_value(1.0)

        dot = draw_tangent_line_on_curve(x_point, y_point)
        
        draw_results(results)



        


        excomp = om.ExecComp('obj=(x**2 + y - 11)**2 + (x + y**2 -7)**2')
        constraint_comp = om.ExecComp('con=x**2 + y**2')
        constraint_comp2 = om.ExecComp('con2=y+x')

        prob = om.Problem()

        prob.model.add_subsystem('excomp', excomp, promotes=['*'])
        prob.model.add_subsystem('constraint_comp', constraint_comp, promotes=['*'])
        prob.model.add_subsystem('constraint_comp2', constraint_comp2, promotes=['*'])

        # setup the optimization
        prob.driver = om.ScipyOptimizeDriver()
        prob.driver.options['optimizer'] = 'SLSQP'
        prob.driver.options['tol'] = 1.e-9

        prob.driver.recording_options['includes'] = ['*']
        recorder = om.SqliteRecorder("more_constrained.sql")
        prob.driver.add_recorder(recorder)

        prob.model.add_design_var('x', lower=-4., upper=4.)
        prob.model.add_design_var('y', lower=-4., upper=4.)
        prob.model.add_constraint('con', upper=4)
        prob.model.add_constraint('con2', equals=1)

        prob.model.add_objective('obj')

        prob.setup()

        # run the optimization
        prob.run_driver();

        results = get_results('more_constrained.sql')

        line = Line(ax.c2p(-3, 4), ax.c2p(4, -3), color=GREEN)
        self.play(Create(line))
        self.wait()
        
        x_point.set_value(1.0)
        y_point.set_value(1.0)

        dot = draw_tangent_line_on_curve(x_point, y_point)
        
        draw_results(results)
        
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )