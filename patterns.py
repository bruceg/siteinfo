import re

class PATTERNS:
    def __init__(self, patterns):
        self.patterns = list(patterns)
        self.compile()
        self.attempts = []
    def compile(self):
        for i in range(len(self.patterns)):
            self.patterns[i] = (re.compile(self.patterns[i][0]),
                                self.patterns[i][1])
    def match(self, string):
        self.attempts.append(string)
        for pattern in self.patterns:
            m = pattern[0].search(string)
            if m:
                g = m.groups()
                if len(g) > 0:
                    return pattern[1] + " " + m.group(1)
                else:
                    return pattern[1]
        return None
