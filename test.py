
from clingo import Control, ast, symbol, Function, Number, String
from clingo.ast import Location, Position

def test1():

    pos = Position('', 0, 0)
    loc = Location(pos, pos)

    symbols = [];
    sym = Function("test", symbols, True)
    print(sym)

    term = ast.SymbolicTerm(loc, sym)
    print(term)

    terms = [term];
    th_seq_set = ast.TheorySequence(loc, ast.TheorySequenceType.Set, terms)
    print(th_seq_set)
    
    result = str(th_seq_set)
    assert result == "{test}"

def test2():

    pos = Position('', 0, 0)
    loc = Location(pos, pos)

    symbols = [];
    sym = Function("test", symbols, True)
    print(sym)

    term = ast.SymbolicTerm(loc, sym)
    print(term)

    terms = [term];
    th_seq_list = ast.TheorySequence(loc, ast.TheorySequenceType.List, terms)
    print(th_seq_list)
    
    result = str(th_seq_list)
    assert result == "[test]"

test1()
test2()