from manim import *


def lagged_write(scene, text_list, delay=1, final_text_lines=""):

    prev_tex_table = Tex(text_list[0] + final_text_lines)
    scene.play(Write(prev_tex_table))
    scene.wait(delay)

    for idx, text in enumerate(text_list[1:]):
        new_tex_table = Tex(text + final_text_lines)

        scene.play(Transform(prev_tex_table, new_tex_table))

        scene.wait(delay)