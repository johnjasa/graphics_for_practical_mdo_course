from manim import *
from manim_helper_functions import *


class TitleSlide(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        title = r"Examples of groupings for systems engineering problems"
        contents_list = [
            "Simple beam problem",
            "Wing design with OpenAeroStruct",
            "Wind turbine design with WISDEM",
            "Engine design with PyCycle",
            ]
        intro_message = "Here we show some real-world examples of groupings for systems engineering problems from a few different applications."
        outro_message = "Choosing how to set up your groups is pretty subjective, but hopefully some of these examples can give you inspiration for your models."

        make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["mda"])
