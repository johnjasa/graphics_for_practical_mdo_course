from manim import *
from manim_helper_functions import *


class TitleSlide(MovingCameraScene):
    def construct(self):
        self.camera.background_color="#2d3c54"

        title = r"Computing derivatives of implicit functions"
        contents_list = [
            "We need derivatives of the residual functions",
            "Explained example of getting derivatives",
            ]
        intro_message = r"Computing derivatives of implicit functions can seem quite confusing at first, but it is not markedly harder than computing derivatives of explicit functions. Instead of getting $d_{\text{outputs}}/d_{\text{inputs}}$, you simply need to get $d_{\text{residuals}}/d_{\text{inputs}}$ and $d_{\text{residuals}}/d_{\text{outputs}}$."
        outro_message = r"For implicit functions, you need to compute the derivatives of the residual functions wrt the inputs and outputs."
        make_title_slide(self, title, contents_list, intro_message, outro_message, venn_types=["diff"])


# class ExplicitVsImplicitDiff(MovingCameraScene):
#     def setup(self):
#         self.camera.background_color="#2d3c54"
#         myTemplate = TexTemplate()
#         myTemplate.add_to_preamble(r"\usepackage{physics}")
#         myTemplate.add_to_preamble(r"\usepackage{bm}")
#         myTemplate.add_to_preamble(r"\usepackage{amsmath}")

#         text = Tex(r"""\raggedright{
# {\Large For explicit functions:}\\
# Derivs of outputs wrt inputs}""", font_size=40).shift(2*UP, 2*LEFT)
#         self.play(Write(text))
#         self.wait()

#         text2 = Tex(r"""\raggedright{
# {\Large For implicit functions:}\\
# Derivs of residuals wrt inputs\\
# Derivs of residuals wrt outputs}""", font_size=40).shift(DOWN, 2*LEFT).align_to(text, LEFT)
#         self.play(Write(text2))
#         self.wait()

#         clear(self)

#         # Show residual calc
#         self.play(Write(MathTex(r"R(u) = 0", font_size=96)))
#         self.wait()
#         clear(self)
#         self.wait()

#         text = MathTex(r"R(a, b, c, x) = ax^2 + bx + c", font_size=72)
#         self.play(Write(text))
#         self.wait()

#         text2 = MathTex(r"R(a, b, c, x) = ax^2 + bx + c = 0", font_size=72)
#         self.play(Transform(text, text2))
#         self.wait()
        