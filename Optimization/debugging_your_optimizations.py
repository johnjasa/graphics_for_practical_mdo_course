from manim import *
import numpy as np
from manim_helper_functions import *


class TitleSlide(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        title = r"Debugging your optimizations"
        contents_list = [
            "Context",
            "Checklist",
            ]
        intro_message = r"""Optimization of complicated multidisciplinary systems is not easy. By following this systematic debugging procedure you can maximize your chances of success."""
        outro_message = "An inordinate amount of my time has been spent debugging optimizations. I hope this checklist helps save you some time!"

        make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["mda", "diff", "opt"])


class Sweeps(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        image = ImageMobject("sweep_2.png").scale(0.75).shift(0.25*UP)
        image_caption = Tex(r"Figures from Jasa dissertation, 2020", font_size=36).shift(3.5*DOWN)
        self.play(FadeIn(image), FadeIn(image_caption))
        self.wait()

        arrow = Arrow(start=ORIGIN, end=UP, color=GREEN, max_stroke_width_to_length_ratio=20, stroke_width=20, max_tip_length_to_length_ratio=0.5)
        arrow.move_to((-2., 0.4, 0))
        self.play(Create(arrow))
        self.wait()
        
        self.play(arrow.animate.move_to((0.4, 0.4, 0)), run_time=3)
        self.wait()

        self.play(arrow.animate.move_to((-1.14, 2.05, 0)))
        self.wait()

        self.play(FadeOut(image), FadeOut(arrow))
        image = ImageMobject("sweep_3.png").scale(0.6).shift(0.5*UP)
        self.play(FadeIn(image))
        self.wait()

        clear(self)


class OptChecklist(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{setspace}")
        
        checklist = r"""\setstretch{1.2}
\raggedright{
0. Understand your model inside and out\\
1. Exhaustively check your derivatives\\
2. Check your optimization problem formulation\\
3. Try a simpler optimization problem\\
4. Start from a feasible point in the design space\\
5. Use driver debug printing\\
6. Plot variable history vs optimizer iterations\\
7. Set solver tolerances smaller than optimization tolerances\\
8. Scale your problem\\
9. Manually investigate and visualize the design space\\
10. Try a different optimizer\\
}"""
        self.play(Write(Tex(checklist).scale(0.85)))
        self.wait(2)
        self.clear()

        checklist = [
            "0. Understand your model inside and out",
            "1. Exhaustively check your derivatives",
            "2. Check your optimization problem formulation",
            "3. Try a simpler optimization problem",
            "4. Start from a feasible point in the design space",
            "5. Use driver debug printing",
            "6. Plot variable history vs optimizer iterations",
            "7. Set solver tolerances smaller than optimization tolerances",
            "8. Scale your problem",
            '9. Manually investigate and visualize the design space',
            '10. Try a different optimizer',
        ]

        for message in checklist:
            write_caption(self, message, scale=0.85)


        