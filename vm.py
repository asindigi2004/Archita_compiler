# vm_switch.py - VM with match-case instead of if/elif

class VM:
    def __init__(self, instructions):
        self.instructions = instructions
        self.stack = []
        self.env = {}
        self.labels = self._find_labels()
        self.pc = 0

    def _find_labels(self):
        labels = {}
        for i, instr in enumerate(self.instructions):
            if instr[0] == "LABEL":
                labels[instr[1]] = i
        return labels

    def run(self):
        while self.pc < len(self.instructions):
            instr = self.instructions[self.pc]

            match instr[0]:
                # --- stack & variables ---
                case "PUSH":
                    _, val = instr
                    self.stack.append(val)

                case "LOAD":
                    _, name = instr
                    self.stack.append(self.env.get(name, 0))

                case "STORE":
                    _, name = instr
                    val = self.stack.pop()
                    self.env[name] = val

                # --- arithmetic ---
                case "ADD":
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(a + b)

                case "SUB":
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(a - b)

                case "MUL":
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(a * b)

                case "DIV":
                    b, a = self.stack.pop(), self.stack.pop()
                    if b == 0:
                        raise ZeroDivisionError("Division by zero in VM")
                    self.stack.append(a // b)

                # --- comparisons ---
                case "EQ":
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(1 if a == b else 0)
                case "NEQ":
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(1 if a != b else 0)
                case "LT":
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(1 if a < b else 0)
                case "GT":
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(1 if a > b else 0)
                case "LE":
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(1 if a <= b else 0)
                case "GE":
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(1 if a >= b else 0)

                # --- IO ---
                case "PRINT":
                    val = self.stack.pop()
                    print(val)

                # --- control flow ---
                case "JUMP":
                    _, label = instr
                    self.pc = self.labels[label]
                    continue

                case "JUMP_IF_FALSE":
                    _, label = instr
                    cond = self.stack.pop()
                    if cond == 0:
                        self.pc = self.labels[label]
                        continue

                case "LABEL":
                    pass  # no-op

                # --- default case ---
                case _:
                    raise RuntimeError(f"Unknown instruction: {instr}")

            self.pc += 1
