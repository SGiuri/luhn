class Luhn:
    def __init__(self, card_num):
        self.card_num = "".join(card_num.split(" "))
        print(self.card_num)

    def valid(self):
        if len(self.card_num) < 2:
            return False
        try:
            int(self.card_num)
        except:
            return False
        sum = 0
        for index in range(len(self.card_num)):
            if index % 2 == 0:
                sum += int(self.card_num[::-1][index])
            else:
                to_sum = int(self.card_num[::-1][index]) * 2
                if to_sum > 9:
                    to_sum -= 9
                sum += to_sum
        if sum % 10 == 0:
            return True
        return False
