def get_full_name(first, middle, last):
    """Return a full name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()

# test for fail and refactor code using this
# def get_full_name(first, last, middle=''):
#     """Return a full name."""
#     if middle:
#         full_name = f"{first} {middle} {last}"
#     else:
#         full_name = f"{first} {last}"
#
#     return full_name.title()
