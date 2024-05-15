
class TuringMachine:

    def __init__(self, tape_start, possible_states, final_states):
        """
        :param tape_start: list containing the start tape (!!! blank spaces should not be considered !!!)
        :param possible_states: dictionary with the possible states following this structure: {str(current_state) + '.' + str(current_symbol): [current_state, current_symbol, new_symbol, new_state, direction ('L' or 'R')]}
        :param final_states: list containing the possible final states
        """
        self.tape_start = tape_start
        self.states = possible_states
        self.current_state = 0
        self.current_symbol = None
        self.current_index = 0
        self.final_states = final_states

    def follow_states(self, show_process=True):

        n = 0
        current_tape = self.tape_start
        self.current_symbol = current_tape[1]
        possible_config = [[i[0], i[1]] for i in self.states.values()]

        while [self.current_state, self.current_symbol] in possible_config:

            n += 1

            if show_process:
                print('\n', f'<><><><><><><><><><> Step {n} <><><><><><><><><><>', '\n')

                print('Old tape:')
                self.mark_current_index(current_tape)
                print(f'--- current state: {self.current_state}')

            if self.current_index == len(current_tape) - 1:
                current_tape.append('')

            instructions = self.states[str(self.current_state) + '.' + str(self.current_symbol)]
            if show_process:
                print('\n', f'Instructions: {instructions}', '\n')

            new_value = instructions[2]
            new_state = instructions[3]
            direction = instructions[4]

            current_tape[self.current_index] = new_value

            if direction == 'R':
                self.current_index = self.current_index + 1
            elif direction == 'L':
                self.current_index = self.current_index - 1
            else:
                print(f'Please set a valid direction for {instructions}')
                return

            if self.current_index == -1:
                current_tape.insert(0, '')
                self.current_index = 0
            elif self.current_index > len(current_tape):
                current_tape.append('')

            self.current_state = new_state
            self.current_symbol = current_tape[self.current_index]

            if self.current_state in self.final_states:
                if show_process:
                    print(f'Tape accepted:')
                    self.mark_current_index(current_tape)
                    print(f' --- current state: {self.current_state}')
                else:
                    print(f'Tape accepted')
                return True

            while current_tape[-2] == '' and current_tape[-1] == '':
                current_tape.pop()

            if show_process:
                print('New tape:')
                self.mark_current_index(current_tape)
                print(f' ---  current state: {self.current_state}')

        print('Tape was not accepted!')
        return False

    def mark_current_index(self, tape):

        for i, item in enumerate(tape):

            if i == self.current_index:
                print("\033[91m" + str(item) + "\033[0m", end=" ")
            else:
                print(item, end=" ")
                
