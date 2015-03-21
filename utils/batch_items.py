import fileinput

def main():
    batch = []

    for line in fileinput.input():
        item = line.strip()

        if item:
            batch.append(item)

        if len(batch) >= 10:
            print('gif:{}'.format(','.join(batch)))
            batch = []

    print('gif:{}'.format(','.join(batch)))


if __name__ == '__main__':
    main()
