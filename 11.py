""" 11_A """


class Dice:
    def __init__(self, init_state: list) -> None:
        self.state = {
            "top": init_state[0],
            "bottom": init_state[5],
            "left": init_state[3],
            "right": init_state[2],
            "front": init_state[1],
            "back": init_state[4],
        }
        return

    def __repr__(self) -> str:
        return f"[dice] {self.state}"

    def rot(self, order: str) -> None:
        """サイコロをoの方向に一回転がす"""
        prev = Dice(self.state)
        if order == "N":
            self.state["top"] = prev.state["back"]
            self.state["bottom"] = prev.state["front"]
            self.state["front"] = prev.state["top"]
            self.state["back"] = prev.state["bottom"]
        elif order == "S":
            self.state["top"] = prev.state["front"]
            self.state["bottom"] = prev.state["back"]
            self.state["front"] = prev.state["bottom"]
            self.state["back"] = prev.state["top"]
        elif order == "E":
            self.state["top"] = prev.state["right"]
            self.state["bottom"] = prev.state["left"]
            self.state["left"] = prev.state["top"]
            self.state["right"] = prev.state["bottom"]
        elif order == "W":
            self.state["top"] = prev.state["back"]
            self.state["bottom"] = prev.state["front"]
            self.state["left"] = prev.state["top"]
            self.state["right"] = prev.state["bottom"]
        return

    def get_top_number(self) -> int:
        """サイコロの上面の整数を返すゲッター"""
        return self.state["top"]


if __name__ == '__main__':
    dice = Dice()
    print("init:", dice)
    order = input()
    for o in order:
        dice.rot(o)
        print("now:", dice)
    print(dice.get_top_number())


""" 11_B """


""" 11_C """


""" 11_D """
