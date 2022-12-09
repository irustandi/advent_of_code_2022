class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self):
        return (self.x, self.y)


def is_touching(head, tail):
    return abs(tail.x - head.x) <= 1 and abs(tail.y - head.y) <= 1


def move(pos, dir):
    if dir == "R":
        pos.x += 1
    elif dir == "L":
        pos.x -= 1
    elif dir == "U":
        pos.y += 1
    elif dir == "D":
        pos.y -= 1
    
    return pos


def move_tail(head, tail):
    x_diff = tail.x - head.x
    y_diff = tail.y - head.y

    if abs(y_diff) > 1:
        if y_diff < -1:
            tail.y += 1
        elif y_diff > 1:
            tail.y -= 1
        if x_diff < 0:
            tail.x += 1
        elif x_diff > 0:
            tail.x -= 1

        return tail

    if abs(x_diff) > 1:
        if x_diff < -1:
            tail.x += 1
        elif x_diff > 1:
            tail.x -= 1

        if y_diff < 0:
            tail.y += 1
        elif y_diff > 0:
            tail.y -= 1

    return tail


def main():
    with open("input") as f:
        input = f.readlines()

    pos_list = [
        Position(0, 0),
        Position(0, 0),
        Position(0, 0),
        Position(0, 0),
        Position(0, 0),
        Position(0, 0),
        Position(0, 0),
        Position(0, 0),
        Position(0, 0),
        Position(0, 0),
    ]
    visited = set([(0, 0)])

    for elem in input:
        elems = elem.strip().split(" ")
        dir = elems[0]
        num = int(elems[1])
        print(elems)

        for idx in range(num):
            #print(idx)
            pos_list[0] = move(pos_list[0], dir)
            #print(f"head is at {pos_list[0].get_coord()}")

            for pos_idx in range(1, len(pos_list)):
                if not is_touching(pos_list[pos_idx-1], pos_list[pos_idx]):
                    pos_list[pos_idx] = move_tail(pos_list[pos_idx-1], pos_list[pos_idx])
                    #print(f"moving {pos_idx} to {pos_list[pos_idx].get_coord()}")

                    if pos_idx == 9:
                        visited.add(pos_list[pos_idx].get_coord())

    print(visited)
    print(len(visited))


if __name__ == '__main__':
    main()
