import rich

class Idea:
    def __init__(self, s):
        self.s = s

    def __str__(self):
        return f"Idea {{ {self.s} }}"

def parse_ideas(s):
    s_ideas = eval(str(s))
    ideas = []
    for e in s_ideas:
        ideas.append(Idea(e['name']))
    return ideas



