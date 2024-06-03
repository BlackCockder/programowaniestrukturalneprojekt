class Player:
    def __init__(self, name):
        self.name = name
        self.money = 1000
        self.units = 10
        self.isLeftFlankControlled = True
        self.isRightFlankControlled = True
        self.rightFlankUnits = 0
        self.leftFlankUnits = 0
        self.mainUnits = 0
        self.unitsLevel = 1
        self.industryLevel = 1
        self.leftFlankDefenceBonus = 1.5
        self.rightFlankDefenceBonus = 1.5
        self.mainDefenceBonus = 3
        self.actions = {

        }

    def passiveMoneyGeneration(self):
        self.money = self.money + 100 * self.industryLevel
        return

    def improveIndustry(self):
        self.industryLevel = self.industryLevel + 1
        return


humanPlayer = Player(input("Welcome to 1v1 game simulator, enter your name: "))
AIPlayer = Player("AI")


def fightingInstance(where, attackers):
    areas_map = {
        "Right flank": "rightFlankUnits",
        "Left flank": "leftFlankUnits",
        "Center": "mainUnits"
    }
    defence_bonus_map = {
        "rightFlankUnits": "rightFlankDefenceBonus",
        "leftFlankUnits": "leftFlankDefenceBonus",
        "mainUnits": "mainDefenceBonus"
    }
    message_map = {
        humanPlayer: humanPlayer.name,
        AIPlayer: "enemy"
    }

    attack_direction = areas_map[where]

    if attackers is None:
        return

    if attackers[0] is not None:
        if len(attackers) == 2:
            if (getattr(attackers[0], attack_direction) > getattr(attackers[1], attack_direction)):
                return "{} and {} are both attacking the same line. Defence bonuses nullified.\n{} won the attack.".format(
                    message_map[attackers[0]], message_map[attackers[1]], message_map[attackers[0]])
            elif (getattr(attackers[0], attack_direction) == getattr(attackers[1], attack_direction)):
                return "{} and {} are both attacking the same line. Defence bonuses nullified.\nTie. Both sides lost all units.".format(
                    message_map[attackers[0]], message_map[attackers[1]])
            else:
                return "{} and {} are both attacking the same line. Defence bonuses nullified.\n{} won the attack.".format(
                    message_map[attackers[0]], message_map[attackers[1]], message_map[attackers[1]])
        else:
            if attackers[0] == humanPlayer:
                defender = AIPlayer
            else:
                defender = humanPlayer

            if (getattr(attackers[0], attack_direction) > getattr(defender, attack_direction) * getattr(defender,
                                                                                                        defence_bonus_map[
                                                                                                            attack_direction])):
                return "{} is attacking {} with {} units on the {}.\nAttack on {} by {} was succesful.".format(
                    message_map[attackers[0]],
                    message_map[defender],
                    getattr(attackers[0], attack_direction),
                    where,
                    where,
                    message_map[attackers[0]])
            elif (getattr(attackers[0], attack_direction) == getattr(defender, attack_direction) * getattr(defender,
                                                                                                           defence_bonus_map[
                                                                                                               attack_direction])):
                return "{} is attacking {} with {} units on the {}.\nTie. Both sides lost all units.".format(
                    message_map[attackers[0]],
                    message_map[defender],
                    getattr(attackers[0], attack_direction),
                    where)
            else:
                return "{} is attacking {} with {} units on the {}.\nAttack was repelled by {}.".format(
                    message_map[attackers[0]],
                    message_map[defender],
                    getattr(attackers[0], attack_direction),
                    where,
                    message_map[defender])
    return


def fightStage(attackers1, attackers2, attackers3):
    if fightingInstance("Left flank", attackers1) is not None:
        print(fightingInstance("Left flank", attackers1))
    if fightingInstance("Right flank", attackers2) is not None:
        print(fightingInstance("Right flank", attackers2))
    if fightingInstance("Center", attackers3) is not None:
        print(fightingInstance("Center", attackers3))
    return


def asignUnits(where, howMuch, humanExec):
    if humanExec:
        if where == "Left flank":
            humanPlayer.leftFlankUnits = howMuch
        elif where == "Right flank":
            humanPlayer.rightFlankUnits = howMuch
        elif where == "Center":
            humanPlayer.mainUnits = howMuch
    else:
        if where == "Left flank":
            AIPlayer.leftFlankUnits = howMuch
        elif where == "Right flank":
            AIPlayer.rightFlankUnits = howMuch
        elif where == "Center":
            AIPlayer.mainUnits = howMuch
    return


# gameGoingOn = True


# This is main
# while gameGoingOn:
# humanPlayer.passiveMoneyGeneration()
# AIPlayer.passiveMoneyGeneration()

asignUnits("Left flank", 5, True)
asignUnits("Left flank", 7, False)
fightStage([AIPlayer], None, None)
