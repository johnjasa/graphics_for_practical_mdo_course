from manim import *
import numpy as np
from manim_helper_functions import *
import openmdao.api as om



class TitleSlide(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        title = r"Using the N2 viewer"
        contents_list = [
            "How to read the N2 diagram",
            "How to create an N2 using OpenMDAO",
            "Debugging connections using N2",
            "Debugging groupings using N2",
            ]
        intro_message = "The N2 diagram is a fantastic interactive tool to understand and debug your OpenMDAO models. If you're wondering how systems are organized, connected, or solved, an N2 is for you."
        outro_message = "OpenMDAO easily creates N2 diagrams which are an extremely helpful tool in understanding and debugging multidisciplinary models."

        make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["mda"])
