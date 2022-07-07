from manim import *
import numpy as np
from openmdao.components.interp_util.interp import InterpND
from manim_helper_functions import *
import openmdao.api as om


x_training = np.arange(11)
y_training = np.array([3., 2.5, 2.3, 2., 5.6, 4.5, 6.7, 4.2, 3.1, 2.2, 2.1])

def run_interp_opt(method):
    # Create regular grid interpolator instance
    interp = om.MetaModelStructuredComp(method=method)

    # set up inputs and outputs
    interp.add_input('x', 4.0, training_data=x_training, units=None)
    interp.add_output('y', 1.0, training_data=y_training, units=None)

    prob = om.Problem()

    prob.model.add_subsystem('interps', interp, promotes=['*'])

    # setup the optimization
    prob.driver = om.ScipyOptimizeDriver()
    prob.driver.options['optimizer'] = 'SLSQP'
    prob.driver.options['tol'] = 1.e-9

    prob.driver.recording_options['includes'] = ['*']
    recorder = om.SqliteRecorder(f"{method}_cases.sql")
    prob.driver.add_recorder(recorder)

    prob.model.add_design_var('x', lower=0., upper=10.)
    prob.model.add_objective('y')

    prob.setup()

    # run the optimization
    prob.run_driver();

run_interp_opt('slinear')
run_interp_opt('akima')

cr = om.CaseReader('slinear_cases.sql')
cases = cr.get_cases()
x_slinear = []
y_slinear = []
for case in cases:
    x_slinear.append(case.outputs['x'])
    y_slinear.append(case.outputs['y'])

x_slinear = np.array(x_slinear)
y_slinear = np.array(y_slinear)


cr = om.CaseReader('akima_cases.sql')
cases = cr.get_cases()
x_akima = []
y_akima = []
for case in cases:
    x_akima.append(case.outputs['x'])
    y_akima.append(case.outputs['y'])

x_akima = np.array(x_akima)
y_akima = np.array(y_akima)



class TrioVenn(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"
        make_venn(self, types=["mda"])


class TitleSlide(Scene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        title = r"Adding curve fits in a differentiable way"
        contents_list = ["Intro and motivation", "Simple (wrong) approach", "Correct approach", "Further notes and recommendations"]
        intro_message = "Using a smooth and continuous curve fit for data will help gradient-based optimizers and Newton solvers converge accurately and quickly."
        outro_message = "You must fit a curve to data in a differentiable way if you're using gradient-based optimizers or a Newton solver."

        make_title_slide(self, title, contents_list, intro_message, outro_message)


class InterpPlot(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"
        self.camera.frame.save_state()

        # create the axes and the curve
        ax = Axes(x_range=[0, 10], y_range=[0, 10])
        x_data = np.arange(11)
        y_data = np.array([3., 2.5, 2.3, 2., 5.6, 4.5, 6.7, 4.2, 3.1, 2.2, 2.1])
        plot = ax.plot_line_graph(x_data, y_data)
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        self.play(Create(ax), Create(labels))
        self.play(Create(plot["vertex_dots"]))

        self.wait(1)

        
        interp = InterpND(method='slinear', points=x_data, values=y_data)
        linear_plot = ax.plot(interp.interpolate, x_range=[0., 10.0, 0.01])
        self.play(Create(linear_plot), rate_func=linear)

        self.wait(1)

        self.play(self.camera.frame.animate.scale(0.25).move_to(plot["vertex_dots"][3]))

        self.wait(1)

        x_point = ValueTracker(2.5)

        def draw_tangent_line_on_curve(input_plot, tracked_value):
            moving_slope = always_redraw(
                lambda: ax.get_secant_slope_group(
                    x=tracked_value.get_value(),
                    graph=input_plot,
                    dx=0.00001,
                    secant_line_length=0.75,
                    secant_line_color=RED,
                )
            )

            dot = always_redraw(
                lambda: Dot(color=RED, radius=0.05).move_to(
                    ax.c2p(tracked_value.get_value(), input_plot.underlying_function(tracked_value.get_value()))
                )
            )

            return moving_slope, dot

        moving_slope, dot = draw_tangent_line_on_curve(linear_plot, x_point)

        self.play(FadeIn(moving_slope), FadeIn(dot))
        self.play(x_point.animate.set_value(3.5), run_time=3, rate_func=linear)
        self.wait()

        self.play(FadeOut(linear_plot), FadeOut(dot), FadeOut(moving_slope), Restore(self.camera.frame))

        x_point.set_value(2.5)


        interp = InterpND(method='akima', points=x_data, values=y_data, delta_x=0.1)
        akima_plot = ax.plot(interp.interpolate, x_range=[0., 10.0, 0.01])
        self.play(Create(akima_plot))
        
        self.play(self.camera.frame.animate.scale(0.25).move_to(plot["vertex_dots"][3]))

        moving_slope, dot = draw_tangent_line_on_curve(akima_plot, x_point)

        self.play(FadeIn(moving_slope), FadeIn(dot))
        self.play(x_point.animate.set_value(3.5), run_time=2, rate_func=linear)
        self.wait()


        self.play(FadeOut(akima_plot), FadeOut(dot), FadeOut(moving_slope), Restore(self.camera.frame))

        x_point.set_value(4.0)

        moving_slope, dot = draw_tangent_line_on_curve(linear_plot, x_point)

        self.play(FadeIn(linear_plot))
        self.play(FadeIn(moving_slope), FadeIn(dot))

        for idx, x in enumerate(x_slinear):
            if x >= 9.99:
                x = 9.99
            if idx > 10:
                self.remove(five_x)
                five_x = Text(f'Iteration {idx} (5x speed)', font_size=24).move_to(ax.c2p(2., 6.))
                self.add(five_x)
                self.play(x_point.animate.set_value(x), run_time=.1, rate_func=linear)
            else:
                try:
                    self.remove(five_x)
                except:
                    pass
                five_x = Text(f'Iteration {idx}', font_size=24).move_to(ax.c2p(2., 6.))
                self.add(five_x)
                self.play(x_point.animate.set_value(x), run_time=.5, rate_func=linear)

        self.wait()
        self.play(FadeOut(linear_plot), FadeOut(dot), FadeOut(moving_slope), FadeOut(five_x), FadeOut(five_x), Restore(self.camera.frame))

        x_point.set_value(4.0)

        moving_slope, dot = draw_tangent_line_on_curve(akima_plot, x_point)

        self.play(FadeIn(akima_plot))
        self.play(FadeIn(moving_slope), FadeIn(dot))

        for idx, x in enumerate(x_akima):
            try:
                self.remove(five_x)
            except:
                pass
            five_x = Text(f'Iteration {idx}', font_size=24).move_to(ax.c2p(2., 6.))
            self.add(five_x)
            self.play(x_point.animate.set_value(x), run_time=.5, rate_func=linear)
        self.wait()
        
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )


class XDSM_comparison(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        image = SVGMobject("xdsm_differentiable.svg")
        image.height = 3
        self.play(FadeIn(image))
        self.wait()
        image2 = SVGMobject("overall_XDSM.svg")
        image2.height = 7.5
        self.play(Transform(image, image2))
        self.wait()

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )