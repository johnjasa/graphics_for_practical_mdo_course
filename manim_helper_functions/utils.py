from manim import *
from manim_pptx import *


def lagged_write(scene, text_list, delay=1, beginning_text="", final_text=""):

    prev_tex_table = Tex(beginning_text + text_list[0] + final_text)
    scene.play(Write(prev_tex_table))
    scene.wait(delay)

    for idx, text in enumerate(text_list[1:]):
        new_tex_table = Tex(beginning_text + text + final_text)

        scene.play(Transform(prev_tex_table, new_tex_table))

        scene.wait(delay)


def make_title_slide(scene, title, contents_list, main_message):

    main_title = Tex(title)
    main_title.shift(0.5*UP)

    title_short = Title(title)

    scene.play(FadeIn(main_title))

    scene.play(Transform(main_title, title_short))

    real_main_message = "\\raggedright{\larger{Main takeaway:} \\\\" + main_message + "}"
    message_title = Tex(real_main_message).scale(0.8)
    scene.play(FadeIn(message_title))
    scene.wait(0.5)
    scene.play(FadeOut(message_title))

    blist = BulletedList(*contents_list)

    scene.play(FadeIn(blist))
    scene.wait()
    scene.play(FadeOut(blist), FadeOut(main_title))

    for idx, item in enumerate(blist):
        blist.fade_all_but(idx, opacity=0.3)
        blist.update()

        scene.play(FadeIn(blist), FadeIn(title_short))
        scene.wait(0.5)
        scene.play(FadeOut(blist), FadeOut(title_short))
