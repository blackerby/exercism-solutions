def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("strands must have same length")
    return sum(base_a != base_b for base_a, base_b in zip(strand_a, strand_b))
