"""Partitions."""


# pylint: disable=C0103
def partitions(set_):
    """Yield partitions."""
    if not set_:
        yield []
        return

    for i in range(2**len(set_) // 2):
        parts = [set(), set()]
        for item in set_:
            parts[i & 1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]] + b
