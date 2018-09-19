import hLotto


def CmdHelp():
    print()
    print("- Usage ----------------------")
    print('"Help": show usage')
    print('"Get" : get won number')
    print('"Exit": exit to shell')
    print("------------------------------")


hoyaLotto = hLotto.CLotto()
CmdHelp()

while (True):
    print("Input command: ", end="")
    cmd = input().lower()

    if cmd == "help":
        CmdHelp()
    elif cmd == "get":
        print("Input index: ", end="")
        idx = int(input())
        list = hoyaLotto.GetWonNumber(idx)
        print(list)
    elif cmd == "exit":
        exit()
    else:
        print("[Err] Wrong command!")
