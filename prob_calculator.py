import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **balls) -> None:
        # dict with all the colors and amount of balls
        self.hat = dict()
        self.contents = []
        for key, value in balls.items():
            self.hat[key] = value
            for item in range(value):
                self.contents.append(key)

    def draw(self, number):
        balls_drawn = []

        if number > len(self.contents):
            balls_drawn = self.contents.copy()
            self.contents = []
        else:
            for i in range(number):
                ball_rm = random.choice(self.contents)
                balls_drawn.append(ball_rm)
                self.contents.remove(ball_rm)

        return balls_drawn

    def get_contents(self):
        return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
    count_luck = 0
  
    for i in range(num_experiments):
      
        expected_balls_t_f = []
        hat_use = copy.deepcopy(hat)
        draw = hat_use.draw(num_balls_drawn)
      
        for key, value in expected_balls.items():
            tmp = draw.count(key)
            if tmp >= value:
                expected_balls_t_f.append(True)
            else:
                expected_balls_t_f.append(False)
        #all the values match the expected
        if all(expected_balls_t_f):
            count_luck += 1

    prob = count_luck / num_experiments

    return prob