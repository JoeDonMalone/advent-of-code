# Day 1

## Part 1:

### Understandings:

- Initially, there will be no previous scan or 'measurements'
- I consider measurements to mean, reads-per-measurement. It seems like this is what they are saying. I will be given the input of a single measurement consisting of n reads.
- I will need to determine if each read is positive(deeper) or negative(more shallow) and count the total number or positive reads before the next measurement(step 2?)

### Observations:

- There will be at least two variables to keep track of:
  - previous 'read' value (to compare to current 'read' value)
  - count of positive(deeper) 'reads'
- <b>Every</b> 'read' deeper than the previous 'read' counts as a depth increase, and counts towards the total score (Doesn't have to be the deepest depth reached so far to count)

## Part 2:

### Understandings:

- The game is now a three sum sliding window
- The 'prev_read' will now consist of a sum of three consecutive reads
- Score increase when consecutive sum is larger than prev consecutive sums

### Observations:

- Seems that the solution will require:
  - prev_read
  - depth_increase_score
  - variables for left and right side of windows. (Not sure how I want to handle that yet, I'm thinking While loop)

### Ambiguities:

- The way that the problem is phrased could make you think that the goal is to count increases inside of the sliding window, when the example shows that the solution should only compare the sums of the windows themselves. We'll see...
