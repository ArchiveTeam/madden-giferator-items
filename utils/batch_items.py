import fileinput

def main():
    batch = []

    for line in fileinput.input():
        batch.append(line.strip())
        
        if len(batch) > 10:
            print('gif:{}'.format(','.join(batch)))
            batch = []

    print('gif:{}'.format(','.join(batch)))


if __name__ == '__main__':
    main()
