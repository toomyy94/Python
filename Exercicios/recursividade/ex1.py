def replace_rec(old_ch, new_ch, astring):
    # Base case: if the string is empty, return an empty string
    if not astring:
        return ""

    # Check if the first character of the string is equal to old_ch
    if astring[0] == old_ch:
        # If it is, replace it with new_ch and recurse on the rest of the string
        return new_ch + replace_rec(old_ch, new_ch, astring[1:])
    else:
        # If it's not, keep the current character and recurse on the rest of the string
        return astring[0] + replace_rec(old_ch, new_ch, astring[1:])

# Example usage:
print(replace_rec("e", "_", "these are the best days"))  # Output: "th_se ar_ th_ b_st days"
print(replace_rec(",", ".", "1,2,3,4,5,6,7,8,9"))      # Output: "1.2.3.4.5.6.7.8.9"
print(replace_rec("M", "#", "NY^T&^MM#M%f*zv#u"))     # Output: "NY^T&^####%f*zv#u"
print(replace_rec("s", "@", "CaseSensitiveTest"))      # Output: "Ca@eSen@itiveTe@t"
