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
            "What is the best size for groups?",
            "Usually top-level groups are physical systems or disciplines",
            "How many groups are too many?",
            "Make reusable groups",
            ]
        intro_message = "You should intelligently group components and subgroups in an intuitive way that makes computational or physical sense."
        outro_message = "Purposefully formulating groups to be reusable, understandable, and reasonably sized makes it easier to write large and complicated MDO problems."

        make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["mda"])

# def make_textbox(color, string, height=1.5, width=2.):
#     result = VGroup() # Write a VGroup
#     box = Rectangle(  # Write a box
#         height=height, width=width, fill_color=color, 
#         fill_opacity=0.5, stroke_color=color
#     )
#     text = Tex(string).move_to(box.get_top() - np.array([0., 0.5, 0.])) # Write text
#     result.add(box, text) # add both objects to the VGroup
#     return result

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

