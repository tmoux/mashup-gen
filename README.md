# Mashup Generator

I enjoy using mashups as a method of practicing Codeforces problems, but (a) it can be tedious to set up mashups and (b) it can be difficult to find problems and create mashups without spoiling the problems by viewing the problem rating and/or tags.

This script addresses these issues by automating the process of selecting problem and creating mashup contests.
Specifically, given a list of unsolved problems, the script will open a web browser, login with your credentials, and automatically create the mashup.

The script also chooses problems in a certain rating range from a random sample of unsolved problems using the Codeforces API.

## Dependencies

Install dependencies with `pip install -r requirements.txt`.

By default, the script uses Firefox and [GeckoDriver](https://github.com/mozilla/geckodriver).
You can change the browser in the `mashup.py` file.

## Usage

Create a file `handle.txt` to store your Codeforces login in the format `[username] [password]`.
To run the script, run `python3 create_mashup.py [args]`.

Most information can be found by running `python3 create_mashup.py -h`:
```
usage: create_mashup.py [-h] [-n HANDLE] [--name NAME] [-d DURATION] [--min_contest_id MIN_CONTEST_ID]
                        min_rating max_rating problem_count

A script to automatically choose problems in a given rating range and create a mashup contest

positional arguments:
  min_rating            Min rating of problem
  max_rating            Max rating of problem
  problem_count         Number of problems

options:
  -h, --help            show this help message and exit
  -n HANDLE, --handle HANDLE
                        Codeforces handle (default: [default-handle])
  --name NAME           Name of mashup contest (default: Practice Mashup)
  -d DURATION, --duration DURATION
                        Duration of contest (minutes) (default: 120)
  --min_contest_id MIN_CONTEST_ID
                        Minimum contest id (useful for filtering out old problems) (default: 500)