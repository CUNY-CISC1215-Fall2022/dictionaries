# The code in this file shows how to reverse a
# dictionary so that its keys are now values,
# and its values are now keys.

def reverse_dictionary(d):
    out = {}
    for key in d:
        value = d[key]
        out[value] = key
    
    return out

# This dictionary reverses cleanly, because all values
# are unique.
a = {8: "A", 1: "B", 9: "C", 27: "D"}
print(reverse_dictionary(a))

# This dictionary does not reverse cleanly: the value
# "B" ocurs twice. How does that affect the output of 
# this function?
b = {8: "A", 1: "B", 9: "C", 27: "D", 7: "B"}
print(reverse_dictionary(b))