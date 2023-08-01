import time
import requests
import random
from dataclasses import dataclass

@dataclass
class Problem:
    contest: int
    index: str
    rating: int
    tags: list

    def getId(self):
        return f'{self.contest}{self.index}'

def get_submissions(handle):
    my_submissions = requests.get(f'https://codeforces.com/api/user.status?handle={handle}')
    return my_submissions.json()['result']

def get_solved_problems(submissions):
    solved_problems = set()
    for submission in submissions:
        if submission['verdict'] == 'OK':
            try:
                problemName = str(submission['problem']['contestId']) + submission['problem']['index']
                solved_problems.add(problemName)
            except:
                pass
    return solved_problems


def get_all_problems():
    problems = requests.get('https://codeforces.com/api/problemset.problems')
    return problems.json()['result']['problems']

def get_unsolved_problems(all_problems, solved_problems):
    problem_list = []
    for problem in all_problems:
        if all(key in problem for key in ['contestId', 'index', 'rating', 'tags']):
            contest = problem['contestId']
            index = problem['index']
            rating = problem['rating']
            tags = problem['tags']
            prob = Problem(contest, index, rating, tags)
            if prob.getId() not in solved_problems:
                problem_list.append(prob)
    return problem_list

def get_all_unsolved(handle):
    solved_problems = get_solved_problems(get_submissions(handle))
    time.sleep(2) # Avoid API rate limiting
    unsolved_problems = get_unsolved_problems(get_all_problems(), solved_problems)
    return unsolved_problems

def select_problems(handle, min_rating, max_rating, count, min_contest_id):
    problems = list(filter(
        lambda p: min_rating <= p.rating <= max_rating and p.contest >= min_contest_id,
        get_all_unsolved(handle)))
    return [p.getId() for p in random.sample(problems, count)]
    

# print(select_problems('silxi', min_rating = 2100, max_rating = 2500, count = 4))
