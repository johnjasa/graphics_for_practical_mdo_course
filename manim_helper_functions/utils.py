from manim import *
from manim_pptx import *
import numpy as np


def lagged_write(scene, text_list, delay=1, beginning_text="", final_text="", fresh_between=False):

    prev_tex_table = Tex(beginning_text + text_list[0] + final_text)
    scene.play(Write(prev_tex_table))
    scene.wait(delay)

    for idx, text in enumerate(text_list[1:]):
        new_tex_table = Tex(beginning_text + text + final_text)

        if fresh_between:
            scene.play(*[FadeOut(mob)for mob in scene.mobjects])
            scene.play(Write(new_tex_table))
        else:
            scene.play(Transform(prev_tex_table, new_tex_table))

        scene.wait(delay)

def write_caption(scene, message, delay=1):
    caption = Tex("\\raggedright{" + message + "}").scale(0.8)
    scene.play(Create(caption))
    scene.wait(delay)
    scene.play(FadeOut(caption))


def make_venn(scene, types=['opt', 'mda', 'diff'], show_center_words=False):
    font_size = 40
    scene.camera.frame.save_state()

    opt_color = "#FAEEDA"
    diff_color = "#F8A38E"
    mda_color = "#7DC6C5"

    Circle.set_default(stroke_width=0.)
    opt = Circle(color=opt_color, fill_opacity=0.3, radius=1.6)
    mda = Circle(color=mda_color, fill_opacity=0.3, radius=1.6)
    diff = Circle(color=diff_color, fill_opacity=0.3, radius=1.6)
    
    opt_mda = VGroup(opt, mda).arrange(RIGHT, buff=-1.6)
    all = VGroup(opt_mda, diff).arrange(DOWN, buff=-1.6)
    all.shift(0.7*DOWN)

    opt_text = Tex("Optimization", font_size=font_size).set_color(opt_color)
    opt_text.next_to(opt.get_corner(UP+LEFT),0.4*1.6*UP)
    opt_text.align_to(opt_mda.get_edge_center(UP), RIGHT)
    opt_group = VGroup(opt, opt_text)

    mda_text = Tex("Modeling", font_size=font_size).set_color(mda_color)
    mda_text.align_to(opt_text, UP)
    mda_text.align_to(mda.get_edge_center(UP), LEFT)
    mda_group = VGroup(mda, mda_text)

    diff_text = Tex("Differentiation", font_size=font_size).set_color(diff_color)
    diff_text.next_to(diff.get_edge_center(DOWN), 0.16*DOWN)
    diff_group = VGroup(diff, diff_text)
    
    if show_center_words:
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
        mdo_text = Tex("MDAO", font_size=font_size).set_color(BLACK).move_to(0.1*UP)

        scene.play(FadeIn(mdo_text))

        scene.wait(2)

    else:
        scene.play(FadeIn(opt, opt_text, mda, mda_text, diff, diff_text))
        scene.wait(1.5)

        list_to_fade_out = []
        if "opt" not in types:
            list_to_fade_out.extend([opt, opt_text])
        if "mda" not in types:
            list_to_fade_out.extend([mda, mda_text])
        if "diff" not in types:
            list_to_fade_out.extend([diff, diff_text])

        scene.play(FadeOut(*list_to_fade_out))
        scene.wait(2)

    scene.play(
        *[FadeOut(mob)for mob in scene.mobjects]
    )


def make_title_slide(scene, title, contents_list, intro_message, outro_message, venn_types=["opt"]):

    main_title = Tex(title)
    main_title.shift(0.5*UP)

    title_short = Title(title)

    scene.play(FadeIn(main_title))

    scene.play(Transform(main_title, title_short))

    write_caption(scene, intro_message)

    scene.wait()

    make_venn(scene, types=venn_types)

    blist = BulletedList(*contents_list)

    scene.play(FadeIn(blist), FadeIn(main_title))
    scene.wait()
    scene.play(FadeOut(blist), FadeOut(main_title))

    for idx, item in enumerate(blist):
        blist.fade_all_but(idx, opacity=0.3)
        blist.update()

        scene.play(FadeIn(blist), FadeIn(title_short))
        scene.wait(0.5)
        scene.play(FadeOut(blist), FadeOut(title_short))

    real_main_message = "\\raggedright{Main takeaway \\newline \\\\ {\large " + outro_message + "}}"
    message_title = Tex(real_main_message).scale(0.8)
    scene.play(FadeIn(message_title))
    scene.wait(0.5)
    scene.play(FadeOut(message_title))