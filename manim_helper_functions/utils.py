from manim import *
from manim_pptx import *
import numpy as np


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


def make_venn(scene, types=['opt', 'mda', 'diff'], show_center_words=False):
    scene.camera.background_color="#2d3c54"
    font_size = 24
    scene.camera.frame.scale(0.6)
    scene.camera.frame.save_state()

    opt_color = "#FAEEDA"
    diff_color = "#F8A38E"
    mda_color = "#7DC6C5"

    Circle.set_default(stroke_width=0.)
    opt = Circle(color=opt_color, fill_opacity=0.3)
    mda = Circle(color=mda_color, fill_opacity=0.3)
    diff = Circle(color=diff_color, fill_opacity=0.3)
    
    opt_mda = VGroup(opt, mda).arrange(RIGHT, buff=-1.)
    all = VGroup(opt_mda, diff).arrange(DOWN, buff=-1.)

    # TODO: tweak alignment of labels
    Text.set_default(font_size=font_size, font="Noto sans")

    opt_text = Text("Optimization").set_color(opt_color)
    opt_text.next_to(opt.get_corner(UP+LEFT),0.4*UP)
    opt_text.align_to(opt_mda.get_edge_center(UP), RIGHT)
    opt_group = VGroup(opt, opt_text)

    mda_text = Text("Modeling").set_color(mda_color)
    mda_text.align_to(opt_text, UP)
    mda_text.align_to(mda.get_edge_center(UP), LEFT)
    mda_group = VGroup(mda, mda_text)

    diff_text = Text("Differentiation").set_color(diff_color)
    diff_text.next_to(diff.get_edge_center(DOWN), 0.1*DOWN)
    diff_group = VGroup(diff, diff_text)
    
    scene.play(FadeIn(opt), FadeIn(opt_text))
    scene.play(FadeIn(mda), FadeIn(mda_text))
    scene.play(FadeIn(diff), FadeIn(diff_text))

    scene.play(scene.camera.frame.animate.scale(0.55).move_to(opt_group))
    scene.wait(0.5)
    
    scene.play(scene.camera.frame.animate.move_to(mda_group))
    scene.wait(0.5)
    
    scene.play(scene.camera.frame.animate.move_to(diff_group))
    scene.wait(0.5)
    
    scene.play(Restore(scene.camera.frame))
    scene.wait(1)

    if show_center_words:
        mdo_text = Text("MDAO").set_color(BLACK).move_to(0.1*UP)

        scene.play(FadeIn(mdo_text))

        scene.wait(2)
