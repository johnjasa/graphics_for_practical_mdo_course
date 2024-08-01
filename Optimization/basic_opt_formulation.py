from manim import *
import numpy as np
from manim_helper_functions import *
import openmdao.api as om


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


# class SequenceForExample(Scene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"
#         myTemplate = TexTemplate()
#         myTemplate.add_to_preamble(r"\usepackage{physics}")
#         text_list = []

#         # Objective discussion
#         text_list.append(r"""
#             Minimize & $f_{\text{obj}}(x, y) = (x^2 + y - 11)^2 + (x+y^2 -7)^2$\\
#         """)
#         text_list.append(r"""
#             Minimize & $f_{\text{obj}}(x, y) = (x^2 + y - 11)^2 + (x+y^2 -7)^2$\\ \\
#             With respect to: & \\
#             Design variables & $x, y$ \\
#         """)
#         text_list.append(r"""
#             Minimize & $f_{\text{obj}}(x, y) = (x^2 + y - 11)^2 + (x+y^2 -7)^2$\\ \\
#             With respect to: & \\
#             Design variables & $x, y$ \\ \\
#             Subject to: & \\
#             Constraints & $x^2 + y^2 \leq 4 $ \\
#         """)
#         text_list.append(r"""
#             Minimize & $f_{\text{obj}}(x, y) = (x^2 + y - 11)^2 + (x+y^2 -7)^2$\\ \\
#             With respect to: & \\
#             Design variables & $x, y$ \\ \\
#             Subject to: & \\
#             Constraints & $x^2 + y^2 \leq 4 $ \\
#                         & $x + y = 1$ \\
#         """)

#         beg_lines = r"""
#             \begin{table}[]
#             \def\arraystretch{1.0}
#             \centering
#             \begin{tabular}{rl}"""

#         lagged_write(self, text_list, beginning_text=beg_lines, final_text=r"""
#             \end{tabular}
#             \end{table}""",
#             fresh_between=True)


#         self.wait()

#         self.play(*[FadeOut(mob)for mob in self.mobjects])


# class SampleOptimization(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"

#         # objective function
#         def objective(x, y):
#             return (x**2 + y - 11)**2 + (x + y**2 -7)**2
        
#         image, ax = plot_2d_function(objective)

#         self.play(FadeIn(image, ax))

#         self.wait()

#         # Plot the minima and maxima
#         minima = [
#             [3., 2.],
#             [-2.805118, 3.131312],
#             [-3.779310, -3.283186],
#             [3.584428, -1.848126],
#         ]

#         maxima = [[-.270845, -.923039]]

#         plot_dots(self, maxima, ax)
#         plot_dots(self, minima, ax)


#         excomp = om.ExecComp('obj=(x**2 + y - 11)**2 + (x + y**2 -7)**2')

#         prob = om.Problem()

#         prob.model.add_subsystem('excomp', excomp, promotes=['*'])

#         # setup the optimization
#         prob.driver = om.ScipyOptimizeDriver()
#         prob.driver.options['optimizer'] = 'SLSQP'
#         prob.driver.options['tol'] = 1.e-9

#         prob.driver.recording_options['includes'] = ['*']
#         recorder = om.SqliteRecorder("unconstrained.sql")
#         prob.driver.add_recorder(recorder)

#         prob.model.add_design_var('x', lower=-4., upper=4.)
#         prob.model.add_design_var('y', lower=-4., upper=4.)
#         prob.model.add_objective('obj')

#         prob.setup()

#         # run the optimization
#         prob.run_driver();
#         results = get_results('unconstrained.sql')
#         draw_results(self, results, ax)

        
#         excomp = om.ExecComp('obj=(x**2 + y - 11)**2 + (x + y**2 -7)**2')
#         constraint_comp = om.ExecComp('con=x**2 + y**2')

#         prob = om.Problem()

#         prob.model.add_subsystem('excomp', excomp, promotes=['*'])
#         prob.model.add_subsystem('constraint_comp', constraint_comp, promotes=['*'])

#         # setup the optimization
#         prob.driver = om.ScipyOptimizeDriver()
#         prob.driver.options['optimizer'] = 'SLSQP'
#         prob.driver.options['tol'] = 1.e-9

#         prob.driver.recording_options['includes'] = ['*']
#         recorder = om.SqliteRecorder("constrained.sql")
#         prob.driver.add_recorder(recorder)

#         prob.model.add_design_var('x', lower=-4., upper=4.)
#         prob.model.add_design_var('y', lower=-4., upper=4.)
#         prob.model.add_constraint('con', upper=4)

#         prob.model.add_objective('obj')

#         prob.setup()

#         # run the optimization
#         prob.run_driver();

#         results = get_results('constrained.sql')

#         circle = Circle(radius=np.linalg.norm(ax.c2p(2., 0.)), color=RED)
#         square = Square(side_length=np.linalg.norm(ax.c2p(8., 0.)))
#         un = Difference(
#             square, circle, stroke_width=0., color=RED, fill_opacity=0.25)
#         self.play(FadeIn(circle), FadeIn(un))
#         self.wait()
        
#         draw_results(self, results, ax)


#         excomp = om.ExecComp('obj=(x**2 + y - 11)**2 + (x + y**2 -7)**2')
#         constraint_comp = om.ExecComp('con=x**2 + y**2')
#         constraint_comp2 = om.ExecComp('con2=y+x')

#         prob = om.Problem()

#         prob.model.add_subsystem('excomp', excomp, promotes=['*'])
#         prob.model.add_subsystem('constraint_comp', constraint_comp, promotes=['*'])
#         prob.model.add_subsystem('constraint_comp2', constraint_comp2, promotes=['*'])

#         # setup the optimization
#         prob.driver = om.ScipyOptimizeDriver()
#         prob.driver.options['optimizer'] = 'SLSQP'
#         prob.driver.options['tol'] = 1.e-9

#         prob.driver.recording_options['includes'] = ['*']
#         recorder = om.SqliteRecorder("more_constrained.sql")
#         prob.driver.add_recorder(recorder)

#         prob.model.add_design_var('x', lower=-4., upper=4.)
#         prob.model.add_design_var('y', lower=-4., upper=4.)
#         prob.model.add_constraint('con', upper=4)
#         prob.model.add_constraint('con2', equals=1)

#         prob.model.add_objective('obj')

#         prob.setup()

#         # run the optimization
#         prob.run_driver();

#         results = get_results('more_constrained.sql')

#         line = Line(ax.c2p(-3, 4), ax.c2p(4, -3), color=GREEN)
#         self.play(Create(line))
#         self.wait()
        
#         draw_results(self, results, ax)
        
#         clear(self)


# class PoorlyPosed(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"

#         # objective function
#         def objective(x, y):
#             return (x**2 + y**2 - 1)**2.
        
#         image, ax = plot_2d_function(objective, r_min=-2, r_max=2, font_size=18)
#         self.play(FadeIn(image, ax))
#         self.wait()

#         unit_conversion = np.linalg.norm(ax.c2p(1., 0.))
#         radius = unit_conversion
#         circle = Circle(radius, color=WHITE)
#         self.play(Create(circle))
#         self.play(Flash(
#             circle, line_length=1,
#             num_lines=30, color=WHITE,
#             flash_radius=radius+SMALL_BUFF,
#             time_width=0.3, run_time=1,
#             rate_func = rush_from
#         ))
#         self.wait()
#         self.play(circle.animate.set_stroke(opacity=0.3))


#         excomp = om.ExecComp('obj=(x**2 + y**2 - 1)**2.')

#         prob = om.Problem()

#         prob.model.add_subsystem('excomp', excomp, promotes=['*'])

#         # setup the optimization
#         prob.driver = om.ScipyOptimizeDriver()
#         prob.driver.options['optimizer'] = 'SLSQP'
#         prob.driver.options['tol'] = 1.e-9

#         prob.driver.recording_options['includes'] = ['*']
#         recorder = om.SqliteRecorder("poorly_posed.sql")
#         prob.driver.add_recorder(recorder)

#         prob.model.add_design_var('x', lower=-4., upper=4.)
#         prob.model.add_design_var('y', lower=-4., upper=4.)
#         prob.model.add_objective('obj')

#         prob.setup()

#         prob.set_val('x', 0.5)
#         prob.set_val('y', 1.5)

#         # run the optimization
#         prob.run_driver();
#         results = get_results('poorly_posed.sql')
#         draw_results(self, results, ax)

#         prob.set_val('x', -0.25)
#         prob.set_val('y', -.5)

#         # run the optimization
#         prob.run_driver();
#         results = get_results('poorly_posed.sql')
#         draw_results(self, results, ax)
        
#         clear(self)

# class WellPosed(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"

#         # objective function
#         def objective(x, y):
#             return ((x-0.5)**2 + 0.5*(y-1.0)**2 + x*y - 0.5)
        
#         image, ax = plot_2d_function(objective, r_min=-2, r_max=2, font_size=18)
#         self.play(FadeIn(image, ax))
#         self.wait()

#         excomp = om.ExecComp('obj=(x-0.5)**2 + 0.5*(y-1.0)**2 + x*y - 0.5')

#         prob = om.Problem()

#         prob.model.add_subsystem('excomp', excomp, promotes=['*'])

#         # setup the optimization
#         prob.driver = om.ScipyOptimizeDriver()
#         prob.driver.options['optimizer'] = 'SLSQP'
#         prob.driver.options['tol'] = 1.e-9

#         prob.driver.recording_options['includes'] = ['*']
#         recorder = om.SqliteRecorder("wellposed.sql")
#         prob.driver.add_recorder(recorder)

#         prob.model.add_design_var('x', lower=-4., upper=4.)
#         prob.model.add_design_var('y', lower=-4., upper=4.)
#         prob.model.add_objective('obj')

#         prob.setup()

#         prob.set_val('x', 0.5)
#         prob.set_val('y', 1.5)

#         # run the optimization
#         prob.run_driver();
#         results = get_results('wellposed.sql')
#         draw_results(self, results, ax)


class PoorlyPosedWords(Scene):
    def construct(self):
        self.camera.background_color="#2d3c54"
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{physics}")

        write_caption(self, r"""
            Possible causes of ill-posed problems: \\
            ~\\
            Conflicting constraints \\
            Discontinuities in the design space \\
            Multiple local minima and maxima \\
            Flat design space near the optimum \\
        """, scale=1.0)

        self.wait()

        self.play(*[FadeOut(mob)for mob in self.mobjects])