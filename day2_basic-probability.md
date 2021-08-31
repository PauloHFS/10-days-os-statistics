#   Day 2: Basic Probability

In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that their sum will be *at most* **9**.

### Solution

**Experiment**: toss 2 six-sided dice

**Sample Space:**

​	Sample Space of 1 event (one dice rolled):
$$
A = \{1, 2, 3, 4 ,5 , 6\}
$$
​	Sample Space of 2 events (two dice rolled):
$$
S = \{A \times A\}\newline 
S = \{\{1,2,3,4,5,6\}\times\{1,2,3,4,5,6\}\}\newline
S = \{
(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),\newline
(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),\newline
(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),\newline
(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),\newline
(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),\newline
(6,1),(6,2),(6,3),(6,4),(6,5),(6,6)
\}
$$
 **Event** (E):

​	The sum of two dices are at most **9**.
$$
E=\{(x,y)|x+y\leq9\text{ and }(x,y)\subset S\}
$$
