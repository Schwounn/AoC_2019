

class Comp:

    def __init__(self, prog):
        self.prog = prog
        self.pc = 0


    def _addition(self):
        a_i = self.prog[self.pc + 1]
        b_i = self.prog[self.pc + 2]
        c_i = self.prog[self.pc + 3]
        self.prog[c_i] = self.prog[a_i] + self.prog[b_i]
        self.pc += 4


    def _multiplication(self):
        a_i = self.prog[self.pc + 1]
        b_i = self.prog[self.pc + 2]
        c_i = self.prog[self.pc + 3]
        self.prog[c_i] = self.prog[a_i] * self.prog[b_i]
        self.pc += 4


    def execute(self):

        while True:
            if self.prog[self.pc] == 99:
                break
            elif self.prog[self.pc] == 1:
                self._addition()
            elif self.prog[self.pc] == 2:
                self._multiplication()
        return self.prog
