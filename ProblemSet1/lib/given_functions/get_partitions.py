def get_partitions(set_):
    from ProblemSet1 import partitions
    
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]