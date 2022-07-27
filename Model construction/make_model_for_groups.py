import openmdao.api as om

prob = om.Problem(model=om.Group())
g1 = prob.model.add_subsystem('Group1', om.Group())
g1.add_subsystem('Comp1', om.ExplicitComponent())
g1.add_subsystem('Comp2', om.ExplicitComponent())
prob.model.add_subsystem('Comp3', om.ExplicitComponent())

prob.setup()

om.n2(prob)