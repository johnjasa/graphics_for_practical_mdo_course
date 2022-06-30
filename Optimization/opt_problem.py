from manim import *
from manim_helper_functions import lagged_write


class Table1(Scene):
    def construct(self):
        table = r"""
            Minimize & $f_{obj}(x,t,u,d)$ \\
        """

        table2 = r"""
            Minimize & $f_{obj}(x,t,u,d)$ \\
            With respect to: & \\
            State dynamics & $\dot x = f_{ODE}(x,t,u,d)$ \\
            Time & $t_{lb} \leq t \leq t_{ub}$ \\
            State variables & $x_{lb} \leq x \leq x_{ub}$ \\
            Dynamics controls & $u_{lb} \leq u \leq u_{ub}$ \\
            Design parameters & $d_{lb} \leq d \leq d_{ub}$ \\
        """

        table3 = r"""
            Minimize & $f_{obj}(x,t,u,d)$ \\
            With respect to: & \\
            State dynamics & $\dot x = f_{ODE}(x,t,u,d)$ \\
            Time & $t_{lb} \leq t \leq t_{ub}$ \\
            State variables & $x_{lb} \leq x \leq x_{ub}$ \\
            Dynamics controls & $u_{lb} \leq u \leq u_{ub}$ \\
            Design parameters & $d_{lb} \leq d \leq d_{ub}$ \\
            Subject to: & \\
            Boundary constraints & $g_{lb} \leq p(x,t,u,d) \leq g_{ub} $ \\
            Path constraints & $p_{lb} \leq p(x,t,u,d) \leq p_{ub} $ \\
        """

        text_list = [table, table2, table3]

        beg_lines = r"""
            \begin{table}[]
            \def\arraystretch{1.0}
            \centering
            \begin{tabular}{rl}"""

        lagged_write(self, text_list, beginning_text=beg_lines, final_text=r"""
            \end{tabular}
            \end{table}""")