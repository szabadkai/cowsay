class Cow:
    message = """
 ________________________________________
/ %s \\
%s\ %s /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||"""

    @classmethod
    def chunk_string(cls, string, length):
        return (string[0 + i:length + i] for i in range(0, len(string), length))

    @classmethod
    def say(cls, tosay):
        tmp = []
        final = ''
        for line in cls.chunk_string(tosay, 40):
            tmp.append(line)

        if len(tmp) == 1:
            final = tmp[0] + ((39 - len(tmp[0])) * " ")
            mid = ''
            late = 39 * " "
        elif len(tmp) == 2:
            final = tmp[0]
            mid = ''
            late = tmp[1] + ((40 - len(tmp[1])) * " ")

        else:
            final = tmp[0]
            mid = "| " + " |\n| ".join(tmp[1:-1]) + " |\n"
            late = tmp[1] + ((40 - len(tmp[1])) * " ")

        print(cls.message % (final, mid, late))
