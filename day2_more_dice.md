# Day 2: More Dice

In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that the values rolled by each die will be *different* and the two dice have a sum of **6**.

------

### Solution

**Experiment:** Toss 2 six-sided dice. 

**Sample Space:**

​	Sample Space of 1 event (one dice rolled):
$$
D = \{1, 2, 3, 4 ,5 , 6\}
$$
Sample Space of 2 events (two dice rolled):
$$
S = \{D \times D\}\newline 
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
 **Events **(A) and (B):

​	The event **E** is a event compoused of events A and B:
$$
E =A\cap B \newline
A=\{(x,y)|x\neq y\text{ and }x,y\subset D\text{ and }(x,y)\subset S\}\newline
B=\{(x,y)|x+y=6\text{ and }x,y\subset D\text{ and }(x,y)\subset S\}
$$

$$
A = \{
(1,2),(1,3),(1,4),(1,5),(1,6),\newline
(2,1),(2,3),(2,4),(2,5),(2,6),\newline
(3,1),(3,2),(3,4),(3,5),(3,6),\newline
(4,1),(4,2),(4,3),(4,5),(4,6),\newline
(5,1),(5,2),(5,3),(5,4),(5,6),\newline
(6,1),(6,2),(6,3),(6,4),(6,5)
\}\newline
B={(1,5),(2,4),(3,3),(4,2),(5,1)}
$$

$$
P(E)=P(A\cap B)=\frac{P(A|B)}{P(B)}=\frac{\frac{4}{5}}{}
$$
