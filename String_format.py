class Command:
    def __init__(self, name, num, score, time):
        self.name = name
        self.num = num
        self.score = score
        self.time = time

Team1 = Command('Мастера кода', 5, 42, 13015.2)
Team2 = Command('Волшебники данных', 6, 45, 13015.2)
if Team1.score > Team2.score or Team1.score == Team2.score and Team1.time < Team2.time:
    result = f'Победа команды {Team1.name}!'
elif Team1.score < Team2.score or Team1.score == Team2.score and Team1.time > Team2.time:
    result = f'Победа команды {Team2.name}!'
else:
    result = 'Ничья!'

# Использование %
print('В команде %s участников: %s' % (Team1.name, Team1.num))
print('Итого сегодня в команде %s участников: %s, в команде %s участников: %s' % (Team1.name,
                                                                                  Team1.num, Team2.name, Team2.num))

# Использование format()
print('Команда {} решила задач: {}'.format(Team2.name, Team2.score))
print('{} решили задачи за {} с'.format(Team2.name, Team2.time))

# Использование f-строк
print(f'Команды решили {Team1.score} и {Team2.score} задач')
print(f'Результат битвы: {result}')
print(f'Сегодня было решено {Team1.score + Team2.score} задач, '
      f'в среднем {(Team1.time + Team2.time)/(Team1.score + Team2.score)} секунды на задачу!')



