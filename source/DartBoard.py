import random


class DartBoard:
    """
    Class representing a standard dartboard.
    """
    def __init__(self):
        # not sure if i need these
        self.board_diameter = 340.0
        self.double_bull_diameter = 12.7
        self.outer_bull_diameter = 31.8
        self.multiscore_width = 10.0
        self.inner_single = 80.0
        self.outer_single = 52.5

        # tuple = (number, # to the clockwise direction, # to the counterclockwise direction)
        self.numbers = {20: [1, 5, 'bull'], 1: [18, 20, 'bull'], 18: [1, 4, 'bull'], 4: [18, 13, 'bull'],
                        13: [4, 6, 'bull'], 6: [10, 13, 'bull'], 10: [6, 15, 'bull'], 15: [2, 10, 'bull'],
                        2: [17, 15, 'bull'], 17: [2, 3, 'bull'], 3: [17, 19, 'bull'], 19: [3, 7, 'bull'],
                        7: [16, 19, 'bull'], 16: [8, 7, 'bull'], 8: [16, 11, 'bull'], 11: [9, 14, 'bull'],
                        14: [9, 12, 'bull'], 9: [12, 14, 'bull'], 12: [9, 5, 'bull'], 5: [20, 12, 'bull'],
                        'bull': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 'double_bull'],
                        'double_bull': ['bull']}

        self.edges = []
        for node in self.numbers:
            for neighbor in self.numbers[node]:
                self.edges.append({node, neighbor})

    def find_hit(self, target, distance):
        """
        Find a hit based on the target and distance from the target
        :param target: The number that was aimed at
        :param distance: How far away the hit was
        :return: The number hit
        """
        graph = self.numbers
        hit = None
        if distance == 0:
            return target
        elif distance < 0:
            while distance < 0:
                if target == 'bull':
                    hit = random.choices(graph[target], cum_weights=(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110,
                                                                     120, 130, 140, 150, 160, 170, 180, 190, 200, 201),
                                         k=1)[0]
                    target = hit
                    distance += 1
                elif target == 'double_bull':
                    hit = 'bull'
                    target = hit
                    distance += 1
                # if the target is still a number, continue
                elif target:
                    # TODO make weights adjustable?
                    hit = random.choices([graph[target][1], graph[target][2], None],
                                         cum_weights=(100, 105, 125), k=1)[0]
                    target = hit
                    distance += 1
                # if target is now None, then break and return None, a miss
                else:
                    return None
        elif distance > 0:
            while distance > 0:
                if target == 'bull':
                    hit = random.choices(graph[target], cum_weights=(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110,
                                                                     120, 130, 140, 150, 160, 170, 180, 190, 200, 201),
                                         k=1)[0]
                    target = hit
                    distance -= 1
                elif target == 'double_bull':
                    hit = 'bull'
                    target = hit
                    distance -= 1
                elif target:
                    hit = random.choices([graph[target][1], graph[target][2], None],
                                         cum_weights=(100, 105, 125), k=1)[0]
                    target = hit
                    distance -= 1
                else:
                    return None
        # small chance of a miss still
        if distance:
            weight = 1 - abs(distance)
            possible_miss = random.choice(graph[target])
            hit = random.choices([target, possible_miss], weights=(1, weight), k=1)[0]
        return hit


if __name__ == '__main__':
    db = DartBoard()
    for i in range(100):
        print(db.find_hit(20, 2))





