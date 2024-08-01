from manim import *
from manim_helper_functions import *


class TitleSlide(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        title = r"Why to use gradient-based optimizers"
        contents_list = [
            "Gradient-based optimizers are quite efficient",
            "Mathematically, gradients are helpful for optimization",
            "Considerations",
            ]
        intro_message = r"Gradient-based optimizers are the most efficient way to explore highly dimensional design spaces and find optimal designs."
        outro_message = r"I highly suggest using gradient-based optimizers as they are the most effective way to explore complex design spaces."
        make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["opt"])
