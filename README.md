# aoc_2024
[Advent of Code - 2024](https://adventofcode.com/2024)

## Notes
- Suggeestion: Use pen-paper to outline before jumping to code
- Tea and water sips are included in the timings, long breaks excluded
- No other tool is used except the python documentation
    - exception:
    1. day 13: scipy's linalg.solve
- No templates
- First simple solution - could be refactored


```
_______________________
|   Day | Time(HH:MM) |(comments)
|-------+-------------|
|   1   | 00:39       |
|-------+-------------|
|   2   | 00:55       |(part2 couldn't solve)
|-------+-------------|
|   3   | 02:15       |
|-------+-------------|
|   4   | 03:30       |
|-------+-------------|
|   5   | 01:48       |
|-------+-------------|
|   6   | 06:00       |(multidimensional list name referencing, set-reset logic for loop condition, bad execution time)
|-------+-------------|
|   7   | 03:30       |(needed itertools.product function to get arrangements)
|-------+-------------|
|   8   | 02:05       |(the wording is too funny after one solves it otherwise: 'how to write english to confuse')
|-------+-------------|
|   9   | 03:25       |(missed conditions: language bit me; given example not sufficient to get correct algo; use names from problem statement: helps in debugging)
|-------+-------------|
|   10  | 2:55        |(debugging missed conditions; recursion and state of recording variable)
|-------+-------------|
|   11  | 02:20       |(exponential sized array with naive approach; hashing solves: many to one)
|-------+-------------|
|   12  | 06:00       |(bad logic to crawler logic for part1, could not solve part2 on same day: still not an elegant solution)
|-------+-------------|
|   13  | 01:35       |(kind of a cheat: used scipy linalg.solve for solving pair of equations)
|-------+-------------|
|   14  | 01:23       |(part2 meaning of tree picture not understable, even no symmetric shape)
|-------+-------------|
|   15  | 06:20       |(part2 took too long)
|-------+-------------|
|   16  | 00:00       |(could not solve)
|-------+-------------|
|   17  | 03:00       |(part1: one statement misunderstood caused long time; part two: could not solve)
|-------+-------------|
|   18  | full day    |(read about graphs from Skiena, Steven S and solve on next day; then first part was easier and second part also worked is direct approach)
|-------+-------------|
|   19  |             |(didnt attempt due to backlog of day18)
|-------+-------------|
|   20  |             |()
|-------+-------------|

```