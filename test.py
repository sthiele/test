
from clingo import Control, ast, symbol, Function, Number, String
from clingo.ast import Location, Position

def test1():

    pos = Position('', 0, 0)
    loc = Location(pos, pos)

    sym1 = Number(42)
    print(sym1)
    sym2 = String("test")
    print(sym2)

    symbols = [sym1, sym2];
    sym3 = Function("fun1", symbols, True)
    print(sym3)

    term1 = ast.SymbolicTerm(loc, sym1)
    print(term1)
    term2 = ast.SymbolicTerm(loc, sym2)
    print(term2)
    term3 = ast.SymbolicTerm(loc, sym3)
    print(term3)

    bc = ast.BooleanConstant(True)
    lit = ast.Literal(loc, ast.Sign.NoSign, bc)
    print(lit)
    satm = ast.SymbolicAtom(term1)
    lit = ast.Literal(loc, ast.Sign.NoSign, satm)
    print(lit)
    
    gt = ast.ComparisonOperator.GreaterThan
    guard = ast.Guard(gt, term2)
    print(guard)
    comp = ast.Comparison(term3, [guard])
    print(comp)
    lit = ast.Literal(loc, ast.Sign.NoSign, comp)
    result = str(lit)
    assert result == "fun1(42,\"test\") > \"test\""

test1()
