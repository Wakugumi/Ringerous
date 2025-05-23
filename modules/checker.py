def check_associativity(ring, op_name):
    op = ring.add if op_name == 'add' else ring.mul
    for a in ring.elements:
        for b in ring.elements:
            for c in ring.elements:
                if op(op(a, b), c) != op(a, op(b, c)):
                    return False, (a, b, c)
    return True, None

def check_identity(ring, op_name):
    op = ring.add if op_name == 'add' else ring.mul
    for e in ring.elements:
        if all(op(e, x) == x and op(x, e) == x for x in ring.elements):
            return True, e
    return False, None

def check_inverse(ring):
    for a in ring.elements:
        if not any(ring.add(a, b) == ring.elements[0] for b in ring.elements):  # assuming 0 is first
            return False, a
    return True, None

def check_distributivity(ring):
    for a in ring.elements:
        for b in ring.elements:
            for c in ring.elements:
                if ring.mul(a, ring.add(b, c)) != ring.add(ring.mul(a, b), ring.mul(a, c)):
                    return False, (a, b, c)
    return True, None

def check_all_properties(ring):
    results = {}

    res, ex = check_associativity(ring, 'add')
    results['Additive Associativity'] = {"result": res, "counterexample": ex}

    res, ex = check_associativity(ring, 'mul')
    results['Multiplicative Associativity'] = {"result": res, "counterexample": ex}

    res, id_add = check_identity(ring, 'add')
    results['Additive Identity'] = {"result": res, "counterexample": None if res else 'Missing'}

    res, fail = check_inverse(ring)
    results['Additive Inverse'] = {"result": res, "counterexample": fail}

    res, id_mul = check_identity(ring, 'mul')
    results['Multiplicative Identity'] = {"result": res, "counterexample": None if res else 'Missing'}

    res, ex = check_distributivity(ring)
    results['Distributivity'] = {"result": res, "counterexample": ex}

    return results