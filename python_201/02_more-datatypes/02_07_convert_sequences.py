# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string_ = "codingnomads"
tuple_ = tuple(string_)
list_ = list(tuple_)
list_.remove("c")
list_.insert(0, "k")
tuple_ = tuple(list_)
print(tuple_)