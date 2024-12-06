import unittest
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers



class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.first = Runner("Усейн", 10)
        self.second = Runner("Андрей", 9)
        self.third = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            result = '{' + ', '.join(f'{place}: {runner}' for place, runner in i.items()) + '}'
            print(result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        tournament = Tournament(90, self.first, self.third)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        tournament = Tournament(90, self.second, self.third)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        tournament = Tournament(90, self.first, self.second, self.third)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]

if __name__ == '__main__':
    unittest.main()