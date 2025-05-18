def format_bytes(size: int) -> dict[str : str | float | int]:
    """
    Nicely format a file size in bytes with an appropriate suffix. Takes an int and returns a dict
    with the value and suffix.
    """
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0: "", 1: "k", 2: "m", 3: "g", 4: "t"}

    while size > power:
        size /= power
        n += 1

    return {
        "value": size,
        "suffix": power_labels[n] + "b",
    }
