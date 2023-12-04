from stadeo.cff.cff_strategies import CFFStrategies
from miasm.expression.expression import ExprId, ExprInt

print("======= Testing CFFStrategies")
cs = CFFStrategies(64)
cs.solve_loop(0x1800158B0,
    0x18008D000,
    context={ExprId("R9", 64): ExprInt(0x567c, 64)},
    ip='127.0.0.1')

print("==== done")

# 11:12:35 [cod] stadeo_samples > sha1sum *
# 791ad58d9bb66ea08465aad4ea968656c81d0b8e  DEMO1.dll
# e0087a763929dee998deebbcfa707273380f05ca  DEMO2.dll
# e575f01d3df0b38fc9dc7549e6e762936b9cc3c3  DEMO3