from manim import *
import numpy as np
from manim_helper_functions import *


class TitleSlide(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        title = r"Why to use gradient-based optimizers"
        contents_list = [
            "Gradient-based optimizers are quite efficient",
            "Mathematically, gradients are helpful for optimization",
            "Further considerations",
            ]
        intro_message = "Gradient-based optimizers are the most efficient way to explore highly dimensional design spaces and find optimal designs."
        outro_message = ""
        make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["diff"])

class Mathy(MovingCameraScene):
    def setup(self):
        self.camera.background_color="#2d3c54"

        text = Tex(r"""\raggedright{
Gradient-based optimization provides:\\
Mathematically provable convergence to an optimum\\
Debuggable optimization paths}""", font_size=60).shift(2*UP)
        self.play(Write(text))
        self.wait()
        clear(self)


class Considerations(MovingCameraScene):
    def setup(self):
        self.camera.background_color="#2d3c54"

        text = Tex(r"""\raggedright{
Gradient-based optimization methods benefit from:\\
Efficient derivatives\\
A (reasonably) smooth model and design space\\
Multiple initial design points}""", font_size=60).shift(2*UP)
        self.play(Write(text))
        self.wait()
        clear(self)



