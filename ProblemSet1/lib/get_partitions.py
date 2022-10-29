"""GetPartitions."""

from .partitions import partitions


def get_partitions(set_):
    """Return partitions."""
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]
