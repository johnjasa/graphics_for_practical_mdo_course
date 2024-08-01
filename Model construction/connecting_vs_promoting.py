from manim import *
import numpy as np
from manim_helper_functions import *


class TitleSlide(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        title = r"Connecting variables vs. promoting them"
        contents_list = [
            "What does connecting mean?",
            "What does promoting mean?",
            "Absolute vs. promoted names",
            "When should you do what?",
            ]
        intro_message = "You should promote variables up a level if they are generally useful at that level or used in many components, whereas you should connect variables if you need more precise control of where the data is being passed."
        outro_message = "Depending on your model and needs, it might be better to connect or promote certain variables. It's worth thinking critically about it to avoid future confusion."

        make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["mda"])

# def make_textbox(color, string, height=1.5, width=2.):
#     result = VGroup() # Write a VGroup
#     box = Rectangle(  # Write a box
#         height=height, width=width, fill_color=color, 
#         fill_opacity=0.5, stroke_color=color
#     )
#     if height < 0.9:
#         text = Tex(string).move_to(box.get_center()) # Write text
#     else:
#         text = Tex(string).move_to(box.get_top() - np.array([0., 0.5, 0.])) # Write text
#     result.add(box, text) # add both objects to the VGroup
#     return result


# def make_box_and_line(string, object, loc, width=2.5, height=0.75, color=ORANGE):
#     objects = VGroup()
#     item = make_textbox(color=color, string=string, width=width, height=height)
#     item = item.move_to(loc)
#     item_line = Line(object.get_bottom(), item.get_top())
#     objects.add(item)
#     objects.add(item_line)
#     return objects


# class ShowConnections(MovingCameraScene):
#     def setup(self):
#         self.camera.background_color="#2d3c54"
#         self.camera.frame.save_state()

#         # make model block
#         model = make_textbox(color=GREEN, string="Model", height=1.)
#         self.play(Write(model))
#         self.play(model.animate.move_to([0., 3., 0.]))
#         self.wait()

#         # make comp_1 block and connect it
#         aero = make_textbox(color=GREEN, string="Weights", width=3.5, height=1.)
#         aero = aero.move_to([-3.5, 1, 0])
#         line_model_c1 = Line(model.get_bottom(), aero.get_top())
#         self.play(Write(aero), Write(line_model_c1))
#         self.wait()

#         # make comp_2 block and connect it
#         struct = make_textbox(color=GREEN, string="Costs", width=3.5, height=1.)
#         struct = struct.move_to([3., 1., 0])
#         line_model_c2 = Line(model.get_bottom(), struct.get_top())
#         self.play(Write(struct), Write(line_model_c2))
#         self.wait()

#         inputs = make_textbox(color=PURPLE, string="Inputs", width=2.0, height=0.75).move_to([-5., 3.25, 0.])
#         outputs = make_textbox(color=ORANGE, string="Outputs", width=2.0, height=0.75).move_to([-5., 2.4, 0.])
#         self.play(Write(inputs), Write(outputs))
#         self.wait()

#         geom = make_box_and_line("aircraft\_size", aero, [-5., -1., 0], color=PURPLE, width=3.)
#         self.play(Write(geom))
#         self.wait()

#         forces = make_box_and_line("max\_takeoff\_weight", aero, [-3., -2., 0], width=4.5)
#         self.play(Write(forces))
#         self.wait()

#         struct_forces = make_box_and_line("max\_takeoff\_weight", struct, [1.75, -1., 0], color=PURPLE, width=4.5)
#         self.play(Write(struct_forces))
#         self.wait()

#         struct_disp = make_box_and_line("aircraft\_cost", struct, [4.5, -2., 0], width=3.)
#         self.play(Write(struct_disp))
#         self.wait()

#         self.play(self.camera.frame.animate.move_to([0, -1.75, 0]))

#         code = '''prob = om.Problem(model=om.Group())
# prob.model.add_subsystem('weights', Weights())
# prob.model.add_subsystem('costs', Costs())
#     '''

#         rendered_code = Code(code=code, tab_width=4, background="window",
#                             language="Python", font="Monospace", font_size=16,
#                             insert_line_no=False, line_spacing=0.4)
#         self.play(Write(rendered_code.move_to([-1.5, -3.75, 0.])))
#         self.wait()

#         unconnected_image = ImageMobject("unconnected_n2.png").move_to([0., -8, 0.])
#         unconnected_image.height = 6

#         self.play(self.camera.auto_zoom([unconnected_image, rendered_code, geom, struct_disp]))
#         self.play(FadeIn(unconnected_image))
#         self.wait()

#         self.play(self.camera.auto_zoom([unconnected_image]))
#         self.wait()

#         dot = Dot(color=RED).shift(unconnected_image.get_center()).shift(2.5*RIGHT)
#         self.add(dot)
#         self.play(Flash(dot, color=RED))
#         self.remove(dot)
#         self.wait()

#         self.play(self.camera.auto_zoom([unconnected_image, rendered_code, geom, struct_disp]))
#         self.play(FadeOut(unconnected_image))
#         self.wait()


#         line = Arrow(forces[0].get_right(), struct_forces[0].get_left(), buff=0., stroke_width=4)

#         connected_image = ImageMobject("connect_n2.png").move_to([0., -8, 0.])
#         connected_image.height = 6

#         new_code = '''prob = om.Problem(model=om.Group())
# prob.model.add_subsystem('weights', Weights())
# prob.model.add_subsystem('costs', Costs())
# prob.model.connect('weights.max_takeoff_weight', 'costs.max_takeoff_weight')
#     '''

#         new_rendered_code = Code(code=new_code, tab_width=4, background="window",
#                             language="Python", font="Monospace", font_size=16,
#                             insert_line_no=False, line_spacing=0.4).move_to([0.5, -3.75, 0.])
#         self.play(Transform(rendered_code, new_rendered_code), FadeIn(connected_image), Write(line))
#         self.wait()

#         self.play(Indicate(rendered_code.code.chars[2], scale_factor=1.1))
#         self.wait()


#         self.play(self.camera.auto_zoom([connected_image]))
#         self.wait()

#         dot = Dot(color=RED).shift(connected_image.get_center()).shift(2.3*RIGHT)
#         self.add(dot)
#         self.play(Flash(dot, color=RED))
#         self.remove(dot)
#         self.wait()

#         self.play(self.camera.auto_zoom([rendered_code, geom, struct_disp, aero, struct], margin=0.1))
#         self.wait()

#         list_to_highlight = [
#             ('rev_pass', geom[1]),
#             ('pass', forces[1]),
#             ('pass', line),
#             ('rev_pass', struct_forces[1]),
#             ('pass', struct_disp[1]),
#         ]

#         def highlight_objects(list_to_highlight):
#             for data_tuple in list_to_highlight:
#                 type_of_animation = data_tuple[0]
#                 obj = data_tuple[1]
                
#                 if 'ind' in type_of_animation:
#                     anim = Indicate(obj, color=WHITE)
#                 elif 'pass' in type_of_animation:
#                     if 'rev' in type_of_animation:
#                         new_obj = obj.copy()
#                         new_obj.points = new_obj.points[::-1]
#                         anim = ShowPassingFlash(new_obj.set_color(RED), time_width=0.5)
#                     else:
#                         anim = ShowPassingFlash(obj.copy().set_color(RED), time_width=0.5)
#                 self.play(anim)

#         highlight_objects(list_to_highlight)
#         self.wait()

#         dot = Dot(color=RED).shift(connected_image.get_center()).shift(1.25*LEFT).shift(DOWN)
#         self.add(dot)
#         self.play(Flash(dot, color=RED))
#         self.remove(dot)
#         self.wait()

#         self.play(FadeOut(line), FadeOut(connected_image))

#         promote_code = '''prob = om.Problem(model=om.Group())
# prob.model.add_subsystem('weights', Weights(), promotes=['max_takeoff_weight'])
# prob.model.add_subsystem('costs', Costs(), promotes=['max_takeoff_weight'])
#     '''

#         new_rendered_code = Code(code=promote_code, tab_width=4, background="window",
#                             language="Python", font="Monospace", font_size=16,
#                             insert_line_no=False, line_spacing=0.4).move_to([0., -3.75, 0.])
#         self.play(Transform(rendered_code, new_rendered_code))
#         self.wait()

#         self.play(Indicate(rendered_code.code.chars[1:3], scale_factor=1.1))
#         self.wait()

#         self.play(self.camera.auto_zoom([rendered_code, geom, struct_disp, aero, struct, model], margin=0.1))
#         self.wait()

#         new_forces = forces[0].copy()
#         new_struct_forces = struct_forces[0].copy()
#         self.play(forces.animate.set_opacity(0.2), struct_forces.animate.set_opacity(0.2), new_forces.animate.move_to([0., 2.0, 0]), new_struct_forces.animate.move_to([0., 2.0, 0]))
#         new_line = Line(model.get_bottom(), new_forces.get_top())
#         self.play(Create(new_line))
#         self.wait()

#         promoted_image = ImageMobject("group_n2.png").move_to([0., -8, 0.])
#         promoted_image.height = 6
#         self.play(self.camera.auto_zoom([promoted_image, rendered_code, geom, struct_disp]))
#         self.play(FadeIn(promoted_image))
#         self.wait()


#         self.play(self.camera.auto_zoom([promoted_image], margin=0.1))
#         self.wait()

#         dot = Dot(color=RED).shift(promoted_image.get_center()).shift(2.45*RIGHT)
#         self.add(dot)
#         self.play(Flash(dot, color=RED))
#         self.remove(dot)
#         self.wait()


#         dot = Dot(color=RED).shift(promoted_image.get_center()).shift(1.*LEFT).shift(DOWN)
#         self.add(dot)
#         self.play(Flash(dot, color=RED))
#         self.remove(dot)
#         self.wait()

#         self.play(self.camera.auto_zoom([model, promoted_image, rendered_code, geom, struct_disp, aero, struct], margin=0.5))
#         self.wait()

#         clear(self)