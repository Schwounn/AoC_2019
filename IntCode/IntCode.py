import re

class Comp:

    def __init__(self, prog):
        self.prog = prog
        self.pc = 0
        self.out_buffer = []
        self.op_map = {int(attribute[3:]) : getattr(self, attribute) for attribute in dir(self)
                       if callable(getattr(self, attribute)) and attribute[:3] == '_op'}

    def get_param_modes(self, pad=None):
        value = self.prog[self.pc] // 100
        modes = []
        while value:
            modes.append(value % 10)
            value //= 10
        if pad is not None:
            modes = (modes + pad * [0])[:pad]
        return modes

    def get_value(self, mode, param_addr):
        if mode == 0:
            return self.prog[self.prog[param_addr]]
        elif mode == 1:
            return self.prog[param_addr]

    def get_values(self, modes):
        ret = []
        offset = 1
        for mode in modes:
            ret.append(self.get_value(mode, self.pc + offset))
            offset += 1
        return ret

    def _op1(self):
        a_i, b_i = self.get_values(self.get_param_modes(pad=2))
        c_i = self.prog[self.pc + 3]
        self.prog[c_i] = a_i + b_i
        self.pc += 4

    def _op2(self):
        a_i, b_i = self.get_values(self.get_param_modes(pad=2))
        c_i = self.prog[self.pc + 3]
        self.prog[c_i] = a_i * b_i
        self.pc += 4

    def _op3(self):
        user_data = int(input("> "))
        a_i = self.prog[self.pc + 1]
        self.prog[a_i] = user_data
        self.pc += 2

    def _op4(self):
        a_i, = self.get_values(self.get_param_modes(pad=1))
        print(f'* {a_i}')
        self.out_buffer.append(a_i)
        self.pc += 2

    def _op5(self):
        a_i, b_i = self.get_values(self.get_param_modes(pad=2))
        if a_i != 0:
            self.pc = b_i
        else:
            self.pc += 3

    def _op6(self):
        a_i, b_i = self.get_values(self.get_param_modes(pad=2))
        if a_i == 0:
            self.pc = b_i
        else:
            self.pc += 3

    def _op7(self):
        a_i, b_i = self.get_values(self.get_param_modes(pad=2))
        c_i = self.prog[self.pc + 3]
        self.prog[c_i] = 1 if a_i < b_i else 0
        self.pc += 4

    def _op8(self):
        a_i, b_i = self.get_values(self.get_param_modes(pad=2))
        c_i = self.prog[self.pc + 3]
        self.prog[c_i] = 1 if a_i == b_i else 0
        self.pc += 4

    def execute(self):
        while True:
            opcode = self.prog[self.pc] % 100
            if opcode == 99:
                break
            else:
                self.op_map[opcode]()
        return self.prog
