from pyxdsm.XDSM import XDSM, OPT, SOLVER, FUNC, LEFT

# Change `use_sfmath` to False to use computer modern
x = XDSM(use_sfmath=True)

x.add_system("opt", OPT, r"\text{Optimizer}")
x.add_system("interp", FUNC, r"\text{Interpolation}")

x.connect("opt", "interp", "x")

x.connect("interp", "opt", "y")

x.write("xdsm_differentiable")