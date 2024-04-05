from my_stack import Stack

my_stack_ = Stack(6)
my_set_in = set(["{", "(", "["])
my_set_ou = set(["}", ")", "]"])

while True:
    word = str(input("Write a value here : "))
    if word in my_set_in:
        my_stack_.push(word)
    elif word in my_set_ou:
        cond1 = my_stack_.ver_topo() == "(" and word == ")"
        cond2 = my_stack_.ver_topo() == "[" and word == "]"
        cond3 = my_stack_.ver_topo() == "{" and word == "}"
        if cond1 == True or cond2 == True or cond3 == True:
            my_stack_.pop()
    if word == "q":
        break

if my_stack_.isEmpty():
    print(" Its empty")
else:
    print(" Its not empty")