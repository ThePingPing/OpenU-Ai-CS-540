import numpy as np
import pandas as pd

def bellman_equation_entropy():
    gama = 0.99
    remainder_value = -1
    around_np = 6
    direction_select = 0.8
    no_select = (1 - direction_select) / 2
    const_ten = 10
    const_epsilon = 10 ** (-7)
    vector_r = [-100, -3, 0, 3]
    value_x = []
    value_x_next = []
    value_sub = []

    for r0 in vector_r:
        remainder_r0 = r0
        x2 = x4 = x5 = x6 = x7 = x8 = x9 = 0
        global flag_for
        flag_for = True
        print("Current r0 = ", r0, "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        direction_dict = {"UP": [0, 0, 0, 0, 0, 0, 0, 0], "DOWN": [0, 0, 0, 0, 0, 0, 0, 0],
                          "RIGHT": [0, 0, 0, 0, 0, 0, 0, 0], "LEFT": [0, 0, 0, 0, 0, 0, 0, 0]}
        # Choice Order UP, DOWN, RIght, Left

        while flag_for:
            direction = {"UP": 0, "DOWN": 0, "RIGHT": 0, "LEFT": 0}
            i = 0
            while i < 1000 and flag_for:

                value_x.clear()
                value_x_next.clear()

                # ***** r0
                max_value = max(((direction_select * r0) + (no_select * r0) + (no_select * x2),"UP"),
                      ((direction_select * x4) + (no_select * r0) + (no_select * x2),"DOWN"),
                      ((direction_select * x2) + (no_select * r0) + (no_select * x4),"RIGHT"),
                      ((direction_select * r0) + (no_select * r0) + (no_select * x4),"LEFT")
                )
                r0_next = np.around(remainder_r0 + gama * max_value[0], around_np)
                # direction[max_value[1]] += 1
                direction_dict[max_value[1]][0] += 1

                # ***** x2
                max_value = max(
                    ((direction_select * x2) + (no_select * r0) + (no_select * const_ten),"UP"),
                    ((direction_select * x5) + (no_select * r0) + (no_select * const_ten),"DOWN"),
                    ((direction_select * const_ten) + (no_select * x2) + (no_select * x5),"RIGHT"),
                    ((direction_select * r0) + (no_select * x2) + (no_select * x5),"LEFT")
                )
                x2_next = np.around(remainder_value + gama * max_value[0], around_np)
                direction[max_value[1]] += 1
                direction_dict[max_value[1]][1] += 1

                # x2_next = np.around(

                # ***** x4
                max_value = max(
                    ((direction_select * r0) + (no_select * x5) + (no_select * x4),"UP"),
                    ((direction_select * x7) + (no_select * x5) + (no_select * x4),"DOWN"),
                    ((direction_select * x5) + (no_select * r0) + (no_select * x7),"RIGHT"),
                    ((direction_select * x4) + (no_select * r0) + (no_select * x7), "LEFT")
                )
                x4_next = np.around(remainder_value + gama * max_value[0], around_np)
                direction[max_value[1]] += 1
                direction_dict[max_value[1]][2] += 1



                # **** *x5
                max_value = max(
                    ((direction_select * x2) + (no_select * x6) + (no_select * x4),"UP"),
                    ((direction_select * x8) + (no_select * x6) + (no_select * x4),"DOWN"),
                    ((direction_select * x6) + (no_select * x2) + (no_select * x8),"RIGHT"),
                    ((direction_select * x4) + (no_select * x2) + (no_select * x8),"LEFT")
                )
                x5_next = np.around(remainder_value + gama * max_value[0], around_np)
                direction_dict[max_value[1]][3] += 1


                # ***** x6
                max_value = max(
                    ((direction_select * const_ten) + (no_select * x6) + (no_select * x5),"UP"),
                    ( (direction_select * x9) + (no_select * x5) + (no_select * x6),"DOWN"),
                    ( (direction_select * x6) + (no_select * const_ten) + (no_select * x9),"RIGHT"),
                    ( (direction_select * x5) + (no_select * const_ten) + (no_select * x9),"LEFT"),
                )
                x6_next = np.around(remainder_value + gama * max_value[0], around_np)
                direction_dict[max_value[1]][4] += 1
                # x6_next = np.around(


                # ***** x7
                max_value = max(
                    ((direction_select * x4) + (no_select * x7) + (no_select * x8),"UP"),
                    ( (direction_select * x7) + (no_select * x7) + (no_select * x8),"DOWN"),
                    ( (direction_select * x8) + (no_select * x4) + (no_select * x7),"RIGHT"),
                    ((direction_select * x7) + (no_select * x7) + (no_select * x4), "LEFT")
                )
                x7_next = np.around(remainder_value + gama * max_value[0], around_np)
                direction_dict[max_value[1]][5] += 1


                # **** x8
                max_value = max(
                    ((direction_select * x5) + (no_select * x9) + (no_select * x7),"UP"),
                    ( (direction_select * x8) + (no_select * x9) + (no_select * x7),"DOWN"),
                    ((direction_select * x9) + (no_select * x5) + (no_select * x8),"RIGHT"),
                    ((direction_select * x7) + (no_select * x5) + (no_select * x8),"LEFT")
                )
                x8_next = np.around(remainder_value + gama * max_value[0], around_np)
                direction_dict[max_value[1]][6] += 1


                # ***** x9
                max_value = max(
                    ((direction_select * x6) + (no_select * x8) + (no_select * x9),"UP"),
                    ( (direction_select * x9) + (no_select * x9) + (no_select * x8),"DOWN"),
                    ((direction_select * x9) + (no_select * x6) + (no_select * x9),"RIGHT"),
                    ((direction_select * x8) + (no_select * x6) + (no_select * x9),"LEFT")
                )
                x9_next = np.around(remainder_value + gama * max_value[0], around_np)
                direction_dict[max_value[1]][7] += 1


                value_x.extend([r0, x2, x4, x5, x6, x7, x8, x9])
                value_x_next.extend([r0_next, x2_next, x4_next, x5_next, x6_next, x7_next, x8_next, x9_next])

                value_sub = np.subtract(value_x, value_x_next)
                all_smaller = True
                for value in value_sub:

                    if abs(value) > const_epsilon:
                        all_smaller = False
                        r0 = r0_next
                        x2 = x2_next
                        x4 = x4_next
                        x5 = x5_next
                        x6 = x6_next
                        x7 = x7_next
                        x8 = x8_next
                        x9 = x9_next
                        break

                if all_smaller:
                    flag_for = False

                i = i + 1
            # print(direction)
            #flag_for = False


        df_policy = pd.DataFrame(direction_dict, index=["r0", "x2", "x4", "x5", "x6", "x7", "x8", "x9"])
        print(df_policy)
        print(" value_x = ", value_x, '\n', "value_x_next = ", value_x_next, '\n', "value_sub = ", value_sub)
    print()




if __name__ == '__main__':
    bellman_equation_entropy()
