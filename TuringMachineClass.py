
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

        current_tape = self.tape_start
        self.current_symbol = current_tape[1]
        possible_config = [[i[0], i[1]] for i in self.states.values()]

        while [self.current_state, self.current_symbol] in possible_config:

            if show_process:
                print(' Old tape:', '\n', current_tape)
                print((1 + (3 * self.current_index)) * " ", '|', '\n',
                      (3 * self.current_index) * " ", self.current_state, '\n')

            if self.current_index == len(current_tape) - 1:
                current_tape.append('')

            instructions = self.states[str(self.current_state) + '.' + str(self.current_symbol)]
            if show_process:
                print(f'Instructions: {instructions}', '\n')

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
                    print(f'Tape accepted: {current_tape}')
                else:
                    print(f'Tape accepted')
                return True

            while current_tape[-2] == '' and current_tape[-1] == '':
                current_tape.pop()

            if show_process:
                print(' New tape:', '\n', current_tape)
                print((1 + (3 * self.current_index)) * " ", '|', '\n',
                      (3 * self.current_index) * " ", self.current_state, '\n')

            print('<><><><><><><><><><><><><><><><><><><><><>')

        print('Tape was not accepted!')
        return False
      
