def main():
    with open("input") as f:
        input = f.readlines()

    stacks = [
        ["B", "P", "N", "Q", "H", "D", "R", "T"],
        ["W", "G", "B", "J", "T", "V"],
        ["N", "R", "H", "D", "S", "V", "M", "Q"],
        ["P", "Z", "N", "M", "C"],
        ["D", "Z", "B"],
        ["V", "C", "W", "Z"],
        ["G", "Z", "N", "C", "V", "Q", "L", "S"],
        ["L", "G", "J", "M", "D", "N", "V"],
        ["T", "P", "M", "F", "Z", "C", "G"],
    ]

    move_inputs = input[10:]

    for inst in move_inputs:
        inst_elems = inst.split(" ")
        num_to_move = int(inst_elems[1])
        src = int(inst_elems[3]) - 1
        dst = int(inst_elems[5]) - 1

        elems_moved = []

        for _ in range(num_to_move):
            elem = stacks[src].pop()
            elems_moved.append(elem)

        elems_moved.reverse()
        for elem in elems_moved:
            stacks[dst].append(elem)

    top_list = []
    for stack in stacks:
        top_list.append(stack[-1])

    print(top_list)

if __name__ == '__main__':
    main()
