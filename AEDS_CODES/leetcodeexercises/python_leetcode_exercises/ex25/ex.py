def reverseString(s : list[str] ):
        s = "".join(s)
        reverse_string = ""
        for i in range(len(s)):
            reverse_string = reverse_string + "," + s[len(s) - 1 - i]
        reverse_string = reverse_string.split(",")

        reverse_string = reverse_string[1 : ]
        return reverse_string

print(reverseString(["H","a","n","n","a","h"]))
