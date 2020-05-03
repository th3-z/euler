
def mult35range(start, stop):
    out = []
    for i in range(start, stop):
        if i%5 == 0 or i%3 == 0:
            out.append(i)

    return out

if __name__ == "__main__":
    print(sum(mult35range(0, 1000)))
