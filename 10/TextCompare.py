import sys



def main(ip1, ip2):
    text1 = open(ip1)
    text2 = open(ip2)
    c = 0
    if text1.read() != text2.read():
        return print(f'ERROR:===>\n{ip1}\n{ip2}')
    else:
        return print("WE CANNT TELL THE DIFFERENCE!!!")
    

if __name__ == "__main__":
    arguments = sys.argv[1:]
    # print(arguments)
    if len(arguments) != 2:
        print("PLS GIVE 2 FILES TO COMPARE!!!!!")
    main(arguments[0], arguments[1])