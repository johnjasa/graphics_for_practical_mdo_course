from manim import *
import numpy as np
from manim_helper_functions import make_venn


class trio_venn(MovingCameraScene):
    def construct(self):
        make_venn(self, show_center_words=True)