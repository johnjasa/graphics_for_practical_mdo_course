from manim import *
import numpy as np
from manim_helper_functions import *
import openmdao.api as om
import subprocess


class TitleSlide(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        title = r"Practical MDO: Course introduction"
        contents_list = [
            "Hello and welcome!",
            "Main goals for this course",
            "Prerequisite knowledge",
            "Course format",
            "Related resources",
            ]
        intro_message = "This course is focused on empowering you to understand and perform efficient gradient-based design optimization for practical problems."
        outro_message = "The lectures, notebooks, and other resources presented in this course should serve as a set of rapid onboarding tools for systems engineers." 

        make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["mda", "opt", "diff"])



class FoundationalBlockBuilding(MovingCameraScene):  
    def construct(self):
        self.camera.background_color="#2d3c54"
        self.camera.frame.scale(0.9).move_to(3*UP)

        def create_textbox(string, landing_left_coords, width=6, height=1, color=BLUE):
            textbox = VGroup() # create a VGroup
            box = Rectangle(  # create a box
                height=height, width=width, fill_color=color, 
                fill_opacity=0.5, stroke_color=color
            )
            text = Tex(string, font_size=44).move_to(box.get_center()) # create text
            textbox.add(box, text).move_to(np.array([landing_left_coords[0], 5.25, 0])) # add both objects to the VGroup

            self.play(FadeIn(textbox))

            # move text box around
            self.play(textbox.animate.move_to(landing_left_coords), run_time=0.5 + 0.5*((5.25 - landing_left_coords[1]) / 5.25), rate_func=rate_functions.ease_out_bounce)
            self.wait()
            return textbox

        self.wait()

        self.play(Create(Line(start=[-8., 0., 0], end=[8., 0., 0.])))

        create_textbox("Python", [-4, 0.5, 0.], width=4)
        create_textbox("Calculus", [0, 0.5, 0.], width=4, color=RED)
        create_textbox("Numerical methods", [4, 0.5, 0.], width=4, color=GREEN)
        create_textbox("OpenMDAO", [0, 1.75, 0.], width=12, height=1.5, color=ORANGE)
        create_textbox("Practical MDO course", [0, 3.25, 0.], width=12, height=1.5, color=PURPLE)
        
        self.wait()
        textbox = create_textbox("Small project", [0, 4.5, 0.], width=4, height=1., color=WHITE)
        self.play(FadeOut(textbox))
        textbox = create_textbox("Next-generation systems engineering project", [0, 5., 0.], width=12, height=2., color=WHITE)
        self.wait()

        self.clear()



class Timeline(MovingCameraScene):  
    def construct(self):
        self.camera.background_color="#2d3c54"
        self.camera.frame.scale(0.9).move_to(2*UP)

        # draw line
        self.play(Create(DoubleArrow([-6, 0, 0], [6, 0, 0])))

        # show theoretical side with books and papers
        book_image = ImageMobject('mdo_book.png').scale(0.18).move_to([-5, 3, 0])
        papers_image = ImageMobject('om_paper.png').scale(0.25).move_to([-4, 2, 0])
        self.play(FadeIn(Tex("Theoretical", font_size=56).move_to([-4, -0.5, 0])))
        self.play(FadeIn(book_image))
        self.play(FadeIn(papers_image))
        
        # show implementation focused side on the right
        doc_image = ImageMobject('om_docs.png').scale(0.2).move_to([4, 2, 0])
        self.play(FadeIn(Tex("Implementation", font_size=56).move_to([4, -0.5, 0])))
        self.play(FadeIn(doc_image))

        # show practical MDO in the middle but overlapping
        textbox = VGroup() # create a VGroup
        box = Ellipse(  # create a box
            height=2.5, width=8, fill_color=BLUE, 
            fill_opacity=0.5, stroke_color=BLUE
        )
        text = Tex("Practical MDO (this course)", font_size=44).move_to(box.get_center()) # create text
        textbox.add(box, text).move_to([0, 0.5, 0]) # add both objects to the VGroup

        self.play(FadeIn(textbox))

        self.wait(2)

        self.clear()
