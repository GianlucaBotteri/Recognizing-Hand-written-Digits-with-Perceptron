

def main():
    openFile("train.0.txt")


def openFile(name):
    #f = open(name, "r")
    s = []
    #for str in f:
     #   f.readline()
      #  print(len(str))
       # s.append([str])
    #print(s)

    with open(name, 'r') as file:
        for line in file:
            text = line.sp
            s.append(text)
    print(s)


if __name__ == '__main__':
    main()
