from manim import *
from manim_pptx import *
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import openmdao.api as om
from pyxdsm.XDSM import XDSM, OPT, SOLVER, FUNC, LEFT


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


def plot_2d_function(function_to_plot, r_min=-4., r_max=4., font_size=24):
    # objective function
    def objective(x, y):
        return (x**2 + y - 11)**2 + (x + y**2 -7)**2
    
    # sample input range uniformly at 0.1 increments
    xaxis = np.arange(r_min, r_max, 0.01)
    yaxis = np.arange(r_min, r_max, 0.01)
    # create a mesh from the axis
    x, y = np.meshgrid(xaxis, yaxis)
    # compute targets
    results = function_to_plot(x, y)

    plt.figure(figsize=(10, 8))
    contours = plt.contour(x, y, results, 15, colors='black')
    plt.clabel(contours, inline=True, fontsize=12)
    plt.imshow(results, extent=[r_min, r_max, r_min, r_max], origin='lower', cmap='RdGy', alpha=0.5)
    ax = plt.gca()
    ax.axis('off')
    plt.savefig('out.png', transparent=True, bbox_inches="tight", dpi=300)

    im = Image.open("out.png")
    im2 = im.crop(im.getbbox())
    im2.save("out.png")

    image = ImageMobject('out.png').scale(0.55)

    ax = Axes(
        x_range=(r_min, r_max, 1),
        y_range=(r_min, r_max, 1),
        x_length=r_max - r_min,
        y_length=r_max - r_min,
        tips=False,
        axis_config={"include_numbers": True, "numbers_to_exclude": [r_min, r_max], "font_size": font_size},
    ).scale_to_fit_height(image.height)

    return image, ax

def get_results(filename):
    cr = om.CaseReader(filename)
    cases = cr.get_cases()

    results = {}
    for case in cases:
        for key in case.outputs.keys():
            if key not in results.keys():
                results[key] = []
            results[key].append(case.outputs[key])

    for key in case.outputs.keys():
        results[key] = np.array(results[key])

    return results

def plot_dots(scene, points, ax):
    dots = VGroup()
    for idx, point in enumerate(points):
        dot = Dot(color=WHITE, stroke_width=.02, radius=0.06, stroke_color=BLACK).move_to(ax.c2p(point[0], point[1]))
        dots.add(dot)
    scene.play(FadeIn(dots))
    anims = []
    for dot in dots:
        anims.append(Flash(dot, color=WHITE))
    scene.play(LaggedStart(*anims, lag_ratio=0.25))
    scene.wait()
    scene.play(FadeOut(dots))


def plot_point_animation(x_value, y_value, ax):
    dot = always_redraw(
        lambda: Dot(color=WHITE, stroke_width=.02, radius=0.06, stroke_color=BLACK).move_to(
            ax.c2p(x_value.get_value(), y_value.get_value()))
        )
    return dot


def draw_results(scene, results, ax):
    x_point = ValueTracker(results['x'][0])
    y_point = ValueTracker(results['y'][0])
    x_prev = x_point.get_value()
    y_prev = y_point.get_value()
    dot = plot_point_animation(x_point, y_point, ax)
    scene.play(FadeIn(dot))
    lines = VGroup()
    for idx, (x, y) in enumerate(zip(results['x'], results['y'])):
        line = Line(ax.c2p(x_prev, y_prev), ax.c2p(x, y))
        line.set_stroke(opacity=0.5)
        scene.play(Create(line), x_point.animate.set_value(x), y_point.animate.set_value(y), run_time=.5, rate_func=linear)
        scene.wait(0.1)
        lines.add(line)
        x_prev = x
        y_prev = y
    scene.wait()
    
    scene.play(FadeOut(dot), FadeOut(lines))

def clear(scene):
    scene.play(
        *[FadeOut(mob)for mob in scene.mobjects]
    )

def add_all(scene):
    scene.play(
        *[FadeIn(mob)for mob in scene.mobjects]
    )

def make_xdsm(scene):

    # Change `use_sfmath` to False to use computer modern
    x = XDSM(use_sfmath=True)

    x.add_system("opt", OPT, r"\text{Optimizer}")
    x.add_system("solver", SOLVER, r"\text{Newton}")
    x.add_system("D1", FUNC, "D_1")
    x.add_system("D2", FUNC, "D_2")
    x.add_system("F", FUNC, "F")
    x.add_system("G", FUNC, "G")

    x.connect("opt", "D1", "x, z")
    x.connect("opt", "D2", "z")
    x.connect("opt", "F", "x, z")
    x.connect("solver", "D1", "y_2")
    x.connect("solver", "D2", "y_1")
    x.connect("D1", "solver", r"\mathcal{R}(y_1)")
    x.connect("solver", "F", "y_1, y_2")
    x.connect("D2", "solver", r"\mathcal{R}(y_2)")
    x.connect("solver", "G", "y_1, y_2")

    x.connect("F", "opt", "f")
    x.connect("G", "opt", "g")

    x.add_output("opt", "x^*, z^*", side=LEFT)
    x.add_output("D1", "y_1^*", side=LEFT)
    x.add_output("D2", "y_2^*", side=LEFT)
    x.add_output("F", "f^*", side=LEFT)
    x.add_output("G", "g^*", side=LEFT)
    x.write("mdf")