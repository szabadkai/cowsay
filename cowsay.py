import textwrap

class Cow:
    message = """
 ________________________________________
/ %s\\
%s\ %s/
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||"""

    @classmethod
    def say(cls, tosay):
        tmp = textwrap.wrap(tosay, 39)

        if len(tmp) == 1:
            final = tmp[0] + ((40 - len(tmp[0])) * " ")
            mid = ''
            late = 39 * " "
        elif len(tmp) == 2:
            final = tmp[0]
            mid = ''
            late = tmp[1] + ((40 - len(tmp[1])) * " ")

        else:
            final = tmp[0] + ((40 - len(tmp[0])) * " ")
            mid = "| " + " |\n| ".join([i + (39 - len(i)) * " " for i in tmp[1:-1]]) + " |\n"
            late = tmp[-1] + ((40 - len(tmp[-1])) * " ")

        print(cls.message % (final, mid, late))
