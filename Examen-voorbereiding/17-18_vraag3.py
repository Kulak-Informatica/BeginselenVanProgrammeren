def mo(a, b):
    # De te berekenen variabelen: sum (s), product (p), quadratic(?) (q)
    s = p = q = 0

    # help variable for p (and q)
    sum_of_a = 0

    # Origineel: for va in a: for vb in b:
    #     s += va - vb
    #     p += va * vb
    #     q += (va + vb)**2
    #
    # s kan herschreven worden naar s += va voor elke va, en dezelfde va wordt voor elke vb opgeteld, dus:
    # for va in a: s += va * len(b)
    # op een gelijkaardige manier moet s -= vb voor elke vb, voor elke va:
    # for vb in b: s -= vb * len(a)
    #
    # p kan herschreven worden als p += va * (vb1 + vb2 + vb3 + vb4 + ...) voor elke va (of omgekeerd voor elke vb)
    # dus berekenen we eerst de som sum_of_a voor alle va in a, dan doen we
    # for vb in b: p += vb * sum_of_a
    #
    # q kan herschreven worden als q += (va**2) + (2*va*vb) + (vb**2) voor elke va in a, voor elke vb in b.
    # Het dubbel product is gelijkaardig aan p, want, na elke va en vb, is de som van al die termen gelijk aan
    # 2 * p. Dan hoeven we enkel, op een gelijkaardige manier als s, nog de termen va**2 en vb**2 toe te voegen. Dus:
    # for va in a: q += (va**2) * len(b)
    # for vb in b: q += (vb**2) * len(a)
    # q += 2 * p
    #
    # Op die manier lopen we 1 keer door de a-lijst en 1 keer door de b-lijst, ipv voor elke va door de b-lijst te gaan.
    for va in a:
        s += va * len(b)
        sum_of_a += va
        q += (va**2) * len(b)

    for vb in b:
        s -= vb * len(a)
        p += vb * sum_of_a
        q += (vb**2) * len(a)

    q += 2 * p  # dubbel product bij q nog op tellen

    return s, p, q


print("s= {:5d}, p= {:5d}, q= {:5d}".format(*mo([1, 2, 3], [4, 5, 6])))
