def slices(series, length):
    s_length = len(series)
    if length < 1 or length > s_length:
        message = f"Cannot get slice of length {length} from string of length {s_length}"
        raise ValueError(message)
    else:
        start_indices = range(s_length-length+1)
        return [series[start:start+length] for start in start_indices]
