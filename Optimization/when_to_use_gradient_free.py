from manim import *
import numpy as np
from manim_helper_functions import *
import openmdao.api as om


# class TitleSlide(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"

#         title = r"When to use gradient-free optimizers"
#         contents_list = [
#             "You should probably use gradient-based methods",
#             "Noisy and discontinuous design spaces",
#             "Multimodal problems",
#             "Very cheap models",
#             "When you can't compute derivatives",
#             ]
#         intro_message = " "

#         intro_message = r"""Use gradient-free optimizers when:
#         ~\\
#         ~\\
#         - the design space is noisy or discontinuous
#         ~\\
#         - there are multiple optima
#         ~\\
#         - the model is computationally inexpensive
#         ~\\
#         - when you cannot efficiently compute derivatives"""
        
#         outro_message = "There are a few situations when you should use gradient-free methods, though I would suggest approaching problems aiming to use gradient-based ones."

#         make_title_slide(self, title, contents_list, intro_message, outro_message)


# class GAOptimization(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"

#         # objective function
#         def objective(x, y):
#             return 0.1*(x+y) -abs(np.sin(x) * np.cos(y) * np.exp(abs(1 - (x**2 + y**2)**0.5/np.pi)))
        
#         image, ax = plot_2d_function(objective, r_min=-10, r_max=10, font_size=48)

#         self.play(FadeIn(image, ax))

#         self.wait()


#         excomp = om.ExecComp('obj = 0.1*(x+y) -abs(sin(x) * cos(y) * exp(abs(1 - (x**2 + y**2)**0.5/pi)))')

#         prob = om.Problem()

#         prob.model.add_subsystem('excomp', excomp, promotes=['*'])
#         pop_size = 20

#         prob.driver = om.SimpleGADriver()
#         prob.driver.options['bits'] = {'x': 8, 'y': 8}
#         prob.driver.options['pop_size'] = pop_size
#         prob.driver.options['max_gen'] = 50
#         prob.driver._randomstate = 1111

#         # prob.driver = om.pyOptSparseDriver(optimizer='ALPSO')
#         # prob.driver.opt_settings['SwarmSize'] = pop_size
#         # prob.driver.opt_settings['maxOuterIter'] = 50
#         # prob.driver.opt_settings['seed'] = 314
        

#         prob.driver.recording_options['includes'] = ['*']
#         recorder = om.SqliteRecorder("new_GA.sql")
#         prob.driver.add_recorder(recorder)

#         prob.model.add_design_var('x', lower=-10., upper=10.)
#         prob.model.add_design_var('y', lower=-10., upper=10.)
#         prob.model.add_objective('obj')

#         prob.setup()

#         prob.set_val('x', 4.)
#         prob.set_val('y', 4.)
        

#         # run the optimization
#         prob.run_driver();
#         results = get_results('new_GA.sql')
#         draw_GA_results(self, results, ax, pop_size=pop_size)


# class SampleOptimization(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"

#         # objective function
#         def objective(x, y):
#             return 0.1*(x+y) -abs(np.sin(x) * np.cos(y) * np.exp(abs(1 - (x**2 + y**2)**0.5/np.pi)))
        
#         image, ax = plot_2d_function(objective, r_min=-10, r_max=10, font_size=48)

#         self.play(FadeIn(image, ax))

#         self.wait()


#         excomp = om.ExecComp('obj = 0.1*(x+y) -abs(sin(x) * cos(y) * exp(abs(1 - (x**2 + y**2)**0.5/pi)))')

#         prob = om.Problem()

#         prob.model.add_subsystem('excomp', excomp, promotes=['*'])

#         # setup the optimization
#         prob.driver = om.ScipyOptimizeDriver()
#         prob.driver.options['optimizer'] = 'SLSQP'
#         prob.driver.options['tol'] = 1.e-9

#         prob.driver.recording_options['includes'] = ['*']
#         recorder = om.SqliteRecorder("unconstrained.sql")
#         prob.driver.add_recorder(recorder)

#         prob.model.add_design_var('x', lower=-10., upper=10.)
#         prob.model.add_design_var('y', lower=-10., upper=10.)
#         prob.model.add_objective('obj')

#         prob.setup()

#         np.random.seed(314)
#         for idx in range(4):
#             prob.set_val('x', np.random.random()*20-10)
#             prob.set_val('y', np.random.random()*20-10)
            
#             # run the optimization
#             prob.run_driver();
#             results = get_results('unconstrained.sql')
#             draw_results(self, results, ax)

#         clear(self)

# class C0discontinuity(MovingCameraScene):
#     def construct(self):
#         self.camera.background_color="#2d3c54"
#         self.camera.frame.save_state()

#         # create the axes and the curve
#         ax = Axes(x_range=[0, 10], y_range=[0, 10])
#         plot = VGroup()
#         x_data = [1., 3.]
#         y_data = [4., 2.]
#         plot1 = ax.plot_line_graph(x_data, y_data, add_vertex_dots=False, line_color=WHITE)
#         plot.add(plot1)
#         x_data = [3., 4.]
#         y_data = [5., 5.5]
#         plot2 = ax.plot_line_graph(x_data, y_data, add_vertex_dots=False, line_color=WHITE)
#         plot.add(plot2)
#         x_data = np.linspace(4., 8.5, 101)
#         y_data = (x_data-6)**2 + 0.5
#         plot3 = ax.plot_line_graph(x_data, y_data, add_vertex_dots=False, line_color=WHITE)
#         plot.add(plot3)
#         labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

#         self.play(Create(ax), Create(labels))
#         self.play(Create(plot))

#         self.wait(1)

#         text = Tex("C0 discontinuities", font_size=60).move_to((-2, 2, 0))
#         self.play(Create(text))
#         text2 = Tex("C1 discontinuities", font_size=60).move_to((-2, 2, 0))
#         self.wait()

#         x_data = [1., 3.]
#         y_data = [6., 5.]
#         plot4 = ax.plot_line_graph(x_data, y_data, add_vertex_dots=False, line_color=WHITE)
#         x_data = np.linspace(4., 8.5, 101)
#         y_data = (x_data-6)**2 + 1.5
#         plot5 = ax.plot_line_graph(x_data, y_data, add_vertex_dots=False, line_color=WHITE)
#         self.play(Transform(plot1, plot4), Transform(plot3, plot5), Transform(text, text2))

#         self.wait()


class Noisy(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"
        self.camera.frame.save_state()

        np.random.seed(314)

        x = np.linspace(0., 10., 201)
        y = 0.4*(x-4)**2 + np.sin(x) + np.random.random_sample(201)*2

        # create the axes and the curve
        ax = Axes(x_range=[0, 10], y_range=[0, 10])
        plot = ax.plot_line_graph(x, y, add_vertex_dots=True, line_color=WHITE)
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        dots = plot["vertex_dots"]
        list_to_create = [167, 166, 168, 120, 20, 40, 80, 60, 65, 69]

        self.play(Create(ax), Create(labels))
        self.wait()

        for idx_dot in list_to_create:
            self.play(Create(dots[idx_dot]))
            self.wait()

        new_dots = VGroup()
        for i in range(201):
            if i not in list_to_create:
                new_dots.add(dots[i])

        self.play(Create(new_dots))

        self.wait()