from manim import *
import numpy as np
from manim_helper_functions import *
import openmdao.api as om
from nlopt_driver import NLoptDriver


class TitleSlide(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        title = r"Types of gradient-free optimizers"
        contents_list = [
            "Genetic algorithms",
            "Particle swarm methods",
            "Other methods",
            ]

        intro_message = r"""There are many different types of gradient-free optimizers. The best method to use varies based on your problem formulation and desired outcome."""
        
        outro_message = "There are so many gradient-free methods! If you need to use one, dig into the details to find which is best for you."

        make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["opt"])


class GAOptimization(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        # objective function
        def objective(x, y):
            return 0.1*(x+y) -abs(np.sin(x) * np.cos(y) * np.exp(abs(1 - (x**2 + y**2)**0.5/np.pi)))
        
        image, ax = plot_2d_function(objective, r_min=-10, r_max=10, font_size=48)

        self.play(FadeIn(image, ax))

        self.wait()

        excomp = om.ExecComp('obj = 0.1*(x+y) -abs(sin(x) * cos(y) * exp(abs(1 - (x**2 + y**2)**0.5/pi)))')

        prob = om.Problem()

        prob.model.add_subsystem('excomp', excomp, promotes=['*'])
        pop_size = 20

        prob.driver = om.SimpleGADriver()
        prob.driver.options['bits'] = {'x': 8, 'y': 8}
        prob.driver.options['pop_size'] = pop_size
        prob.driver.options['max_gen'] = 50
        prob.driver._randomstate = 1111

        prob.driver.recording_options['includes'] = ['*']
        recorder = om.SqliteRecorder("new_GA.sql")
        prob.driver.add_recorder(recorder)

        prob.model.add_design_var('x', lower=-10., upper=10.)
        prob.model.add_design_var('y', lower=-10., upper=10.)
        prob.model.add_objective('obj')

        prob.setup()

        prob.set_val('x', 4.)
        prob.set_val('y', 4.)
        

        # run the optimization
        prob.run_driver()
        results = get_results('new_GA.sql')
        draw_GA_results(self, results, ax, pop_size=pop_size)


class PSOOptimization(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        # objective function
        def objective(x, y):
            return 0.1*(x+y) -abs(np.sin(x) * np.cos(y) * np.exp(abs(1 - (x**2 + y**2)**0.5/np.pi)))
        
        image, ax = plot_2d_function(objective, r_min=-10, r_max=10, font_size=48)

        self.play(FadeIn(image, ax))

        self.wait()

        excomp = om.ExecComp('obj = 0.1*(x+y) -abs(sin(x) * cos(y) * exp(abs(1 - (x**2 + y**2)**0.5/pi)))')

        prob = om.Problem()

        prob.model.add_subsystem('excomp', excomp, promotes=['*'])
        pop_size = 20

        prob.driver = om.pyOptSparseDriver(optimizer="ALPSO")

        prob.driver.recording_options['includes'] = ['*']
        recorder = om.SqliteRecorder("PSO.sql")
        prob.driver.add_recorder(recorder)

        prob.model.add_design_var('x', lower=-10., upper=10.)
        prob.model.add_design_var('y', lower=-10., upper=10.)
        prob.model.add_objective('obj')

        prob.setup()

        prob.set_val('x', 4.)
        prob.set_val('y', 4.)
        

        # run the optimization
        prob.run_driver()
        results = get_results('PSO.sql')
        draw_GA_results(self, results, ax, pop_size=pop_size)


class ISRESOptimization(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        # objective function
        def objective(x, y):
            return 0.1*(x+y) -abs(np.sin(x) * np.cos(y) * np.exp(abs(1 - (x**2 + y**2)**0.5/np.pi)))
        
        image, ax = plot_2d_function(objective, r_min=-10, r_max=10, font_size=48)

        self.play(FadeIn(image, ax))

        self.wait()

        excomp = om.ExecComp('obj = 0.1*(x+y) -abs(sin(x) * cos(y) * exp(abs(1 - (x**2 + y**2)**0.5/pi)))')

        prob = om.Problem()

        prob.model.add_subsystem('excomp', excomp, promotes=['*'])
        pop_size = 60

        prob.driver = NLoptDriver()
        prob.driver.options["optimizer"] = "GN_ISRES"
        prob.driver.options["tol"] = 1e-6
        prob.driver.options["maxiter"] = 3000

        prob.driver.recording_options['includes'] = ['*']
        recorder = om.SqliteRecorder("ISRES.sql")
        prob.driver.add_recorder(recorder)

        prob.model.add_design_var('x', lower=-10., upper=10.)
        prob.model.add_design_var('y', lower=-10., upper=10.)
        prob.model.add_objective('obj')

        prob.setup()

        prob.set_val('x', 4.)
        prob.set_val('y', 4.)
        

        # run the optimization
        prob.run_driver()
        results = get_results('ISRES.sql')
        draw_GA_results(self, results, ax, pop_size=pop_size)


class COBYLAOptimization(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        # objective function
        def objective(x, y):
            return 0.1*(x+y) -abs(np.sin(x) * np.cos(y) * np.exp(abs(1 - (x**2 + y**2)**0.5/np.pi)))
        
        image, ax = plot_2d_function(objective, r_min=-10, r_max=10, font_size=48)

        self.play(FadeIn(image, ax))

        self.wait()

        excomp = om.ExecComp('obj = 0.1*(x+y) -abs(sin(x) * cos(y) * exp(abs(1 - (x**2 + y**2)**0.5/pi)))')

        prob = om.Problem()

        prob.model.add_subsystem('excomp', excomp, promotes=['*'])

        prob.driver = NLoptDriver()
        prob.driver.options["optimizer"] = "LN_COBYLA"
        prob.driver.options["tol"] = 1e-6      

        prob.driver.recording_options['includes'] = ['*']
        recorder = om.SqliteRecorder("cobyla.sql")
        prob.driver.add_recorder(recorder)

        prob.model.add_design_var('x', lower=-10., upper=10.)
        prob.model.add_design_var('y', lower=-10., upper=10.)
        prob.model.add_objective('obj')

        prob.setup()

        prob.set_val('x', 4.)
        prob.set_val('y', 4.)
        

        # run the optimization
        prob.run_driver();
        results = get_results('cobyla.sql')
        draw_results(self, results, ax)

