import argparse
from select_problems import select_problems
from mashup import create_mashup

if __name__ == '__main__':
    with open('handle.txt', 'r') as f:
        login_handle, login_password = f.read().strip().split()

    parser = argparse.ArgumentParser(description=
                                     "A script to automatically choose problems in a given rating range and create a mashup contest",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--handle', action='append', default = [login_handle], help = 'Codeforces handle')
    parser.add_argument('--name', default = 'Practice Mashup', help = 'Name of mashup contest')
    parser.add_argument('-d', '--duration', default = '120', type = int, help = 'Duration of contest (minutes)')
    parser.add_argument('--min_contest_id', default = '650', type = int, help = 'Minimum contest id (useful for filtering out old problems)')
    parser.add_argument("min_rating", type = int, help = "Min rating of problem")
    parser.add_argument("max_rating", type = int, help = "Max rating of problem")
    parser.add_argument("problem_count", type = int, help = "Number of problems")

    args = parser.parse_args()
    config = vars(args)
    print(config)
    (handles, mashup_name, duration, min_contest_id, min_rating, max_rating, problem_count) = (args.handle, args.name, args.duration, args.min_contest_id, args.min_rating, args.max_rating, args.problem_count)
    problems = select_problems(handles, min_rating, max_rating, problem_count, min_contest_id)
    # print("Problems selected: ", problems)
    create_mashup(problems, mashup_name, duration, login_handle, login_password)