import itertools


class Dice:
    def __init__(self, init_state: list) -> None:
        self.__state = {
            "top": init_state[0],
            "front": init_state[1],
            "right": init_state[2],
            "left": init_state[3],
            "back": init_state[4],
            "bottom": init_state[5],
        }
        return

    def __eq__(self, other: object) -> bool:
        """
        - 回転させて同じになるものも同じとみなす．
        - 全探索して一致判定するので計算量はO(6*4) = O(1)
        """
        for pos in ["top", "front", "right", "left", "back", "bottom"]:
            copy_dice = self.get_copy_dice()
            copy_dice.set_state(pos)
            for order in ["H", "H", "H", "H", "H"]:
                if copy_dice.get_state() == other.get_state():
                    return True
                copy_dice.rot(order)
        return False

    def get_copy_dice(self) -> object:
        return Dice(list(self.get_state().values()))

    def get_state(self) -> dict:
        return self.__state

    def rot(self, order: str) -> None:
        """ orderの向きに回転させる """
        prev = self.get_copy_dice()
        if order == "N":  # North
            self.__state["top"] = prev.__state["front"]
            self.__state["bottom"] = prev.__state["back"]
            self.__state["front"] = prev.__state["bottom"]
            self.__state["back"] = prev.__state["top"]
        elif order == "S":  # South
            self.__state["top"] = prev.__state["back"]
            self.__state["bottom"] = prev.__state["front"]
            self.__state["front"] = prev.__state["top"]
            self.__state["back"] = prev.__state["bottom"]
        elif order == "E":  # East
            self.__state["top"] = prev.__state["left"]
            self.__state["bottom"] = prev.__state["right"]
            self.__state["left"] = prev.__state["bottom"]
            self.__state["right"] = prev.__state["top"]
        elif order == "W":  # West
            self.__state["top"] = prev.__state["right"]
            self.__state["bottom"] = prev.__state["left"]
            self.__state["left"] = prev.__state["top"]
            self.__state["right"] = prev.__state["bottom"]
        elif order == "H":  # Horizontal
            self.__state["front"] = prev.__state["right"]
            self.__state["back"] = prev.__state["left"]
            self.__state["left"] = prev.__state["front"]
            self.__state["right"] = prev.__state["back"]
        else:
            print(f"\n[Error] @Dice/rot() -> argument error. arg:{order}\n")
        return

    def set_state(self, pos: str) -> None:
        """ posの位置がtopとなるように回転させる """
        if pos == "top":
            pass
        elif pos == "front":
            self.rot("N")
        elif pos == "right":
            self.rot("W")
        elif pos == "left":
            self.rot("E")
        elif pos == "back":
            self.rot("S")
        elif pos == "bottom":
            self.rot("N")
            self.rot("N")
        else:
            print(f"\n[Error] @Dice/set_state() -> argument error. arg:{pos}\n")
        return


def main() -> None:
    """ A """
    # dice = Dice(list(map(int, input().split())))
    # for order in input():
    #     dice.rot(order)
    # print(dice.get_state()["top"])

    """ B """
    # dice = Dice(list(map(int, input().split())))
    # q = int(input())
    # for _ in range(q):
    #     top, front = map(int, input().split())
    #     copy_dice = dice.get_copy_dice()
    #     for k, v in copy_dice.get_state().items():
    #         # state[k]=v=topとなるkを探す
    #         if v == top:
    #             copy_dice.set_state(k)
    #             break
    #     for order in ["H", "H", "H", "H"]:
    #         # topを固定して水平回転させる
    #         copy_dice.rot(order)
    #         state = copy_dice.get_state()
    #         if state["front"] == front:
    #             print(state["right"])
    #             break

    """ C """
    # a = Dice(list(map(int, input().split())))
    # b = Dice(list(map(int, input().split())))
    # print(["No", "Yes"][a == b])

    """ D """
    n = int(input())
    dices = [list(map(int, input().split())) for _ in range(n)]
    index_pairs = list(itertools.combinations([i for i in range(n)], 2))
    for i, j in index_pairs:  # O(n^2)
        if Dice(dices[i]) == Dice(dices[j]):
            print("No")
            return
    print("Yes")

    return


if __name__ == '__main__':
    main()
