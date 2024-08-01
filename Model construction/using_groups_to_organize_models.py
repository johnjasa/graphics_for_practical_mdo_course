from manim import *
import numpy as np
from manim_helper_functions import *
import openmdao.api as om
from pyxdsm.XDSM import XDSM, OPT, SOLVER, FUNC, LEFT
import subprocess


class TitleSlide(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        title = r"Using groups to organize models"
        contents_list = [
            "Basics of groups in OpenMDAO",
            "What is the best size for groups?",
            "Usually top-level groups are physical systems or disciplines",
            "You should make reusable groups",
            ]
        intro_message = "You should intelligently group components and subgroups in an intuitive way that makes computational or physical sense."
        outro_message = "Purposefully formulating groups to be reusable, understandable, and reasonably sized makes it easier to write large and complicated MDO problems."

        make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["mda"])

class GroupSize(MovingCameraScene):
    def setup(self):
        self.camera.background_color="#2d3c54"
        self.camera.frame.save_state()

        long_string = """\\raggedright{
        Groups should probably have 2-10 subgroups or components. \\newline
        Components should have 5-30 variables. \\newline
        ~ \\newline
        ~ \\newline
        This will help you obtain derivatives more easily. \\newline
        Also, others can more easily understand your model. \\newline
        }
        """
        text = Tex(long_string).shift(1.5*UP)

        self.play(Write(text))

def make_textbox(color, string, height=1.5, width=2.):
    result = VGroup() # Write a VGroup
    box = Rectangle(  # Write a box
        height=height, width=width, fill_color=color, 
        fill_opacity=0.5, stroke_color=color
    )
    if height < 0.9:
        text = Tex(string).move_to(box.get_center()) # Write text
    else:
        text = Tex(string).move_to(box.get_top() - np.array([0., 0.5, 0.])) # Write text
    result.add(box, text) # add both objects to the VGroup
    return result

class ReuseGroups(MovingCameraScene):
    def setup(self):
        self.camera.background_color="#2d3c54"

        # make model block
        model = make_textbox(color=GREEN, string="Model", height=1.)
        self.play(Write(model))
        self.play(model.animate.move_to([0.5, 2., 0.]))
        self.wait()

        # make comp_1 block and connect it
        comp_1 = make_textbox(color=GREEN, string="Aerodynamics", width=3.5, height=1.)
        comp_1 = comp_1.move_to([-3.5, 0, 0])
        line_model_c1 = Line(model.get_bottom(), comp_1.get_top())
        self.play(Write(comp_1), Write(line_model_c1))
        self.wait()

        # make comp_2 block and connect it
        comp_2 = make_textbox(color=GREEN, string="Structures", width=3.5, height=1.)
        comp_2 = comp_2.move_to([0.5, 0., 0])
        line_model_c2 = Line(model.get_bottom(), comp_2.get_top())
        self.play(Write(comp_2), Write(line_model_c2))
        self.wait()

        # make comp_3 block and connect it
        comp_3 = make_textbox(color=GREEN, string="Propulsion", width=3.5, height=1.)
        comp_3 = comp_3.move_to([4.5, 0., 0])
        line_model_c3 = Line(model.get_bottom(), comp_3.get_top())
        self.play(Write(comp_3), Write(line_model_c3))
        self.wait()

        objects = VGroup()
        for i in range(5):
            if i < 3:
                item = make_textbox(color=BLUE, string="C", width=0.5, height=0.5)
            else:
                item = make_textbox(color=GREEN, string="G", width=0.5, height=0.5)
            item = item.move_to([-1.5+4*float(i)/5, -2., 0])
            line = Line(comp_2.get_bottom(), item.get_top())
            objects.add(item)
            objects.add(line)

        self.play(Write(objects))
        self.wait()

        self.play(FadeOut(comp_1), FadeOut(comp_3), FadeOut(line_model_c1), FadeOut(line_model_c3))
        self.wait()

        comp_4 = make_textbox(color=GREEN, string="Weights", width=4., height=1.)
        comp_4 = comp_4.move_to([4.5, 0., 0])
        line_model_c4 = Line(model.get_bottom(), comp_4.get_top())
        self.play(Write(comp_4), Write(line_model_c4))
        self.wait()

        next_objects = VGroup()
        for i in range(3):
            if i < 2:
                small_item = make_textbox(color=BLUE, string="C", width=0.5, height=0.5)
            else:
                small_item = make_textbox(color=GREEN, string="G", width=0.5, height=0.5)
            small_item = small_item.move_to([3.5+4*(float(i)+1)/5, -2., 0])
            line = Line(comp_4.get_bottom(), small_item.get_top())
            next_objects.add(small_item)
            next_objects.add(line)

        new_item = item.copy()
        self.play(new_item.animate.move_to([3.5, -2., 0]))
        small_line = Line(comp_4.get_bottom(), new_item.get_top())
        self.play(Create(small_line))
        self.wait()
        self.play(Create(next_objects))
        self.wait()

        clear(self)


        

# class ModelTree(MovingCameraScene):
#     def setup(self):
#         self.camera.background_color="#2d3c54"

#         code = '''prob = om.Problem(model=om.Group())
# prob.model.add_subsystem('Comp1', Comp1())
# prob.model.add_subsystem('Comp2', Comp2())
# prob.model.add_subsystem('Comp3', Comp3())
#         '''
        
#         rendered_code = Code(code=code, tab_width=4, background="window",
#                             language="Python", font="Monospace", font_size=16,
#                             insert_line_no=False, line_spacing=0.4)
#         self.play(Write(rendered_code.move_to([-3.5, 3., 0.])))

#         self.wait()

#         # make model block
#         model = make_textbox(color=GREEN, string="Model")
#         self.play(Write(model), Indicate(rendered_code.code.chars[0], scale_factor=1.1))
#         self.play(model.animate.move_to([1.5, 2., 0.]))
#         self.wait()

#         # make comp_1 block and connect it
#         comp_1 = make_textbox(color=BLUE, string="Comp1")
#         comp_1 = comp_1.move_to([-1., -1, 0])
#         line_model_c1 = Line(model.get_bottom(), comp_1.get_top())
#         self.play(Write(comp_1), Write(line_model_c1), Indicate(rendered_code.code.chars[1], scale_factor=1.1))
#         self.wait()

#         # make comp_2 block and connect it
#         comp_2 = make_textbox(color=BLUE, string="Comp2")
#         comp_2 = comp_2.move_to([1.5, -1., 0])
#         line_model_c2 = Line(model.get_bottom(), comp_2.get_top())
#         self.play(Write(comp_2), Write(line_model_c2), Indicate(rendered_code.code.chars[2], scale_factor=1.1))
#         self.wait()

#         # make comp_3 block and connect it
#         comp_3 = make_textbox(color=BLUE, string="Comp3")
#         comp_3 = comp_3.move_to([4., -1., 0])
#         line_model_c3 = Line(model.get_bottom(), comp_3.get_top())
#         self.play(Write(comp_3), Write(line_model_c3), Indicate(rendered_code.code.chars[3], scale_factor=1.1))
#         self.wait()

#         # erase comp_1 and comp_2
#         clear(self)
#         self.wait()


#         code = '''prob = om.Problem(model=om.Group())
# g1 = prob.model.add_subsystem('Group1', om.Group())
# g1.add_subsystem('Comp1', Comp1())
# g1.add_subsystem('Comp2', Comp2())
# prob.model.add_subsystem('Comp3', Comp3())
#         '''
        
#         rendered_code = Code(code=code, tab_width=4, background="window",
#                             language="Python", font="Monospace", font_size=14,
#                             insert_line_no=False, line_spacing=0.4)
#         self.play(Write(rendered_code.move_to([-3.5, 3., 0.])))
#         self.wait()

#         # make model block
#         model = make_textbox(color=GREEN, string="Model")
#         self.play(Write(model), Indicate(rendered_code.code.chars[0], scale_factor=1.1))
#         self.play(model.animate.move_to([1.5, 2., 0.]))
#         self.wait()

#         # make a group
#         group1 = make_textbox(color=GREEN, string="Group1")
#         group1.move_to([-1., -0.5, 0.])
#         line_model_group = Line(model.get_bottom(), group1.get_top())
#         self.play(Write(group1), Write(line_model_group), Indicate(rendered_code.code.chars[1], scale_factor=1.1))
#         self.wait()

#         # put c1 and c2 in a group
#         comp_1 = make_textbox(color=BLUE, string="Comp1")
#         comp_1 = comp_1.move_to([-2, -3., 0])
#         line_model_c1 = Line(group1.get_bottom(), comp_1.get_top())
#         self.play(Write(comp_1), Write(line_model_c1), Indicate(rendered_code.code.chars[2], scale_factor=1.1))
#         self.wait()

#         # make comp_2 block and connect it
#         comp_2 = make_textbox(color=BLUE, string="Comp2")
#         comp_2 = comp_2.move_to([1, -3., 0])
#         line_model_c2 = Line(group1.get_bottom(), comp_2.get_top())
#         self.play(Write(comp_2), Write(line_model_c2), Indicate(rendered_code.code.chars[3], scale_factor=1.1))
#         self.wait()

#         comp_3 = make_textbox(color=BLUE, string="Comp3")
#         comp_3 = comp_3.move_to([4, -1., 0])
#         line_model_c3 = Line(model.get_bottom(), comp_3.get_top())
#         self.play(Write(comp_3), Write(line_model_c3), Indicate(rendered_code.code.chars[4], scale_factor=1.1))
#         self.wait()

#         # some people think of groups and models as a tree, others as russian nesting dolls
#         self.play(FadeOut(line_model_c1, line_model_c2, line_model_c3, line_model_group))

#         # show a model
#         model_big = make_textbox(color=GREEN, string="Model", height=5.5, width=7.5).move_to([2.5, -1., 0.])
#         self.play(Transform(model, model_big),
#             group1.animate.move_to([-5.5, 0.5, 0.]),
#             comp_1.animate.move_to([-5.5, -1.5, 0.]),
#             comp_2.animate.move_to([-3., 0.5, 0.]),
#             comp_3.animate.move_to([-3., -1.5, 0.]),
#             )
#         self.wait()

#         # fill in the model with groups
#         group1_big = make_textbox(color=GREEN, string="Group1", height=3.5, width=4.75).move_to([1.25, -1.5, 0.])
#         self.play(Transform(group1, group1_big))
#         self.wait()

#         # g1, g2, g2 contains c1 and c2
#         self.play(
#             comp_1.animate.move_to([0., -2., 0.]),
#             comp_2.animate.move_to([2.5, -2., 0.]),
#         )
#         self.wait()

#         self.play(
#             comp_3.animate.move_to([5., -1.5, 0.]),
#         )

#         # reinforce that anything can be hetereogenuous
#         self.wait()
#         clear(self)

#         image = ImageMobject('simple_n2.png').scale(0.4)
#         self.play(FadeIn(image))
#         self.wait()

# class DiscussWindTurbine(MovingCameraScene):
#     def setup(self):
#         self.camera.background_color="#2d3c54"

#         # new idea from my run based on what Jennifer and Justin said
#         # two main examples; wind turbine and aircraft

#         # 1 ===========
#         # show a wind turbine
#         # say we're doing performance estimation, where we're trying to get the amount of power produced by the turbine and the cost
#         # we'd need to care about the wind, cost of materials, how strong they are, the power produced
#         # really dive into the variables and what's represented
#         # we'd also need to care about these physical systems the blade and rotor performance, the tower, generator, tower, foundation
#         # how should we architect this code?

#         # show a box and containing box examples
#         # start with a wind turbine
#         # think wind first
#         # wind hits the turbine
#         # based on the airfoil performance, aeroelastic performance, and other things, it will impart a force
#         # this force then turns a gear or generator
#         # this produces electricity
#         # imagine a tower undergoing loads
#         # if we make the turbine bigger then the tower needs to be stronger
#         # can the tower FEA beam element be the same as the blades?
        
#         # we can discuss how to organize these things
#         # all things that get hit by wind? all electricity? all metal that's manufactured?
#         # 
#         # okay so we have an example now and can show the N2 accordingly
#         # then we'll discuss how it basically follows the physical system at the higher group levels
#         # however, within some of those levels there would be groups focused on the computational side of things

#         # 2 ==========
#         # show an electric aircraft
#         # okay what do we do here? is it markedly different than the wind turbine case? let's find out
#         # what do we care about. wind again but this time the aircraft is making it. so airspeed, weight, battery states, controller positions
#         # should we start with the wings cause they produce lift or the battery cause it gives the power to the aircraft?
#         # well no we should start with the wing and the tail and the fuselage all together because we'll need them all together for the lift and weights to make sure it makes sense
#         # okay maybe I'll put all the electrical systems together; but the controller is different than propulsion different than AV but they're related right
#         # we haven't even talked about the aerodynamics with the motor rotors
        
#         # what if we have multiple flight conditions that we care about? would we have multiple planes? or can we put everything together
#         # heck we could have multiple aircraft


#         # 3 ==============
#         # all right, let's put all this together
#         # show a wind turbine and aircraft
#         # is there anything we can re-use between these two cases?
#         # yes, airfoils, maybe rotors, maybe electrical wiring, even structural considerations
#         # this is actually possible and Andrew Ning is a great example of it with CCBlade and a few other things
