def main():
    with open("input") as f:
        input = f.readlines()

    nums = []
    num = 0
    for elem in input:
        try:
            num_elem = int(elem)
            num += num_elem
        except:
            nums.append(num)
            num = 0

    if num > 0:
        nums.append(num)

    nums.sort(reverse=True)
    print(sum(nums[:3]))
    

if __name__ == '__main__':
    main()