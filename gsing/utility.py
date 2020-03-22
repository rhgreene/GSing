def linear_map(in_value, in_lower, in_upper, out_lower, out_upper):
    return (
            (out_upper - out_lower) * (in_value - in_lower) /
            (in_upper - in_lower)
        ) + out_lower
