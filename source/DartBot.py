class DartBot:
    """
    A bot that will attempt to play you in a game of darts.
    """
    def __init__(self, skill_level: int = 1):
        """
        Basic parameters for the dartbot
        :param skill_level: A skill level. Affects the sampling parameters.
        """
        self.skill_level = skill_level

    def __str__(self):
        """
        print string
        :return: string with the dartbot description
        """
        return f'dartbot skill = {self.skill_level}'

    def __repr__(self):
        """
        repr string
        :return: string with dartbot description
        """
        return self.__str__()

    def shoot_dart(self, target):
        """
        Dartbot makes an attempt to throw a dart at a specified target
        :param target: The number the dartbot is attempting to shoot
        :return: Actual result
        """
        # TODO add a probabilistic attempt, based on radius from the target in a 2D plane representing
        # the dartboard.
        pass
