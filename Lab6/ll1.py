from Lab5.grammar import Grammar

grammar_filename = "C:\\Users\\Ionut\\PycharmProjects\\Formal-Languages-and-Compiler-Design\\Lab5\\grammar1.txt"
grammar = Grammar(grammar_filename)
# grammar.print_grammar()

"""
If x is a terminal, then FIRST(x) = { ‘x’ }
If x-> Є, is a production rule, then add Є to FIRST(x).
If X->Y1 Y2 Y3….Yn is a production, 
    FIRST(X) = FIRST(Y1)
    If FIRST(Y1) contains Є then FIRST(X) = { FIRST(Y1) – Є } U { FIRST(Y2) }
    If FIRST (Yi) contains Є for all i = 1 to n, then add Є to FIRST(X).
"""

def reunit(list1, list2):
    result = []
    for elem in list1:
        if elem not in result:
            result.append(elem)
    for elem in list2:
        if elem not in result:
            result.append(elem)
    return result

"""
def first1(grammar, symbol):
    result = []
    if symbol in grammar.terminals:
        return symbol
    if symbol == 'e':
        return symbol
    for production in grammar.productions[symbol]:
        result = reunit(result, first(grammar, production[0]))
    return result
"""

def first(grammar, rule):
    if len(rule) != 0 and (rule is not None):
        if rule[0] in grammar.terminals:
            return rule[0]
        elif rule[0] == 'e':
            return 'e'
    if len(rule) != 0:
        if rule[0] in list(grammar.productions.keys()):
            temp_result = []
            rhs_rules = grammar.productions[rule[0]]
            for itr in rhs_rules:
                indivRes = first(grammar, itr)
                if type(indivRes) is list:
                    temp_result = reunit(temp_result, indivRes)
                else:
                    temp_result = reunit(temp_result, [indivRes])

            # if no epsilon in result received return temp_result
            if 'e' not in temp_result:
                return temp_result
            else:
                # apply epsilon rule => f(ABC)=f(A)-{e} U f(BC)
                newList = []
                temp_result.remove('e')
                if len(rule) > 1:
                    ansNew = first(grammar, rule[1:])
                    if ansNew != None:
                        if type(ansNew) is list:
                            newList = reunit(temp_result, ansNew)
                        else:
                            newList = reunit(temp_result, [ansNew])
                    else:
                        newList = temp_result
                    return newList
                # if eplison still persists keep it in result of first
                temp_result = reunit(temp_result, ['e'])
                return temp_result


def follow(grammar, nonterminal):
    #global start_symbol, rules, nonterm_userdef, \
    #    term_userdef, diction, firsts, follows

    solution = set()
    if nonterminal == grammar.starting_symbol:
        solution.add('$')

    # check all occurrences
    # solution - is result of computed 'follow' so far

    # For input, check in all rules
    for currentNonterm in grammar.productions:
        rhs = grammar.productions[currentNonterm]
        # go for all productions of NT
        for subrule in rhs:
            if nonterminal in subrule:
                # call for all occurrences on - non-terminal in subrule
                while nonterminal in subrule:
                    index_nt = subrule.index(nonterminal)
                    subrule = subrule[index_nt + 1:]
                    # empty condition - call follow on LHS
                    if len(subrule) != 0:
                        # compute first if symbols on
                        # - RHS of target Non-Terminal exists
                        res = first(grammar, subrule)
                        # if epsilon in result apply rule
                        # - (A->aBX)- follow of -
                        # - follow(B)=(first(X)-{ep}) U follow(A)
                        if 'e' in res:
                            newList = []
                            res.remove('e')
                            ansNew = follow(grammar, currentNonterm)
                            if ansNew != None:
                                if type(ansNew) is list:
                                    newList = res + ansNew
                                else:
                                    newList = res + [ansNew]
                            else:
                                newList = res
                            res = newList
                    else:
                        # when nothing in RHS, go circular
                        # - and take follow of LHS
                        # only if (NT in LHS)!=curNT
                        if nonterminal != currentNonterm:
                            res = follow(grammar, currentNonterm)

                    # add follow result in set form
                    if res is not None:
                        if type(res) is list:
                            for g in res:
                                solution.add(g)
                        else:
                            solution.add(res)
    return list(solution)


print("First: ")
for symbol in grammar.non_terminals:
    print(symbol, " -> ", first(grammar, symbol))

print("Follow: ")
for symbol in grammar.non_terminals:
    print(symbol, " -> ", follow(grammar, symbol))