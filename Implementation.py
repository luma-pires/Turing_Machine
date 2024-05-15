from TuringMachineClass import TuringMachine

possible_states = {'0.1': [0, 1, 1, 0, 'R'],
                   '0.0': [0, 0, 0, 0, 'R'],
                   '0.': [0, '', '', 1, 'L'],
                   '1.0': [1, 0, 'X', 2, 'L'],
                   '2.0': [2, 0, 'X', 3, 'L'],
                   '3.0': [3, 0, 'X', 3, 'L'],
                   '3.1': [3, 1, 'X', 3, 'L'],
                   '3.': [3, '', '', 4, 'R'],
                   '1.': [1, '', '', 4, 'R']}

start_tape = [0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0]
final_states = [4]

M1 = TuringMachine(start_tape, possible_states, final_states)
accepted = M1.follow_states()
