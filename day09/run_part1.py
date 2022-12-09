def is_touching(head_x, head_y, tail_x, tail_y):
    return abs(tail_x - head_x) <= 1 and abs(tail_y - head_y) <= 1


def move(x, y, dir):
    if dir == "R":
        x += 1
    elif dir == "L":
        x -= 1
    elif dir == "U":
        y += 1
    elif dir == "D":
        y -= 1
    
    return x, y


def move_tail(head_x, head_y, tail_x, tail_y, dir):
    if dir == "R":
        tail_y = head_y
        tail_x += 1
    elif dir == "L":
        tail_y = head_y
        tail_x -= 1
    elif dir == "U":
        tail_y += 1
        tail_x = head_x
    elif dir == "D":
        tail_y -= 1
        tail_x = head_x
    
    return tail_x, tail_y


def main():
    with open("input") as f:
        input = f.readlines()

    head_pos = (0, 0)
    tail_pos = (0, 0)
    visited = set([tail_pos])

    for elem in input:
        elems = elem.strip().split(" ")
        dir = elems[0]
        num = int(elems[1])

        for _ in range(num):
            head_pos = move(head_pos[0], head_pos[1], dir)
            if not is_touching(head_pos[0], head_pos[1], tail_pos[0], tail_pos[1]):
                tail_pos = move_tail(head_pos[0], head_pos[1], tail_pos[0], tail_pos[1], dir)
                visited.add(tail_pos)

    print(len(visited))


if __name__ == '__main__':
    main()
