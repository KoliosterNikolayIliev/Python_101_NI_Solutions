def nan_expand(times):
    fragment = 'Not a '
    if times > 0:
        return times * fragment + 'NaN'
    return ''


test = [
    nan_expand(0) == "",
    nan_expand(1) == "Not a NaN",
    nan_expand(2) == "Not a Not a NaN",
    nan_expand(3) == "Not a Not a Not a NaN",
]
[print(x) for x in test]
