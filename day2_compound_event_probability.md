# Day 2: Compound Event Probability

There are **3** urns labeled **X**, **Y**, and **Z**.

- Urn **X** contains **4** red balls and **3** black balls.
- Urn **Y** contains **5** red balls and **4** black balls.
- Urn **Z** contains **4** red balls and **4** black balls.

One ball is drawn from each of the **3** urns. What is the probability that, of the **3** balls drawn, **2** are red and **1** is black?

### Solution

**Experiment:** Draw 3 balls

**Sample Space:**

​	**X**:
$$
n(S)=7\newline
P(red)=\frac{n(red)}{n(S)}=\frac{4}{7}\newline
P(black)=\frac{n(black)}{n(S)}=\frac{3}{7}
$$


​	**Y**:
$$
n(S)=9\newline
P(red)=\frac{n(red)}{n(S)}=\frac{5}{9}\newline
P(black)=\frac{n(black)}{n(S)}=\frac{4}{9}
$$


​	**Z**:
$$
n(S)=8\newline
P(red)=\frac{n(red)}{n(S)}=\frac{4}{8}\newline
P(black)=\frac{n(black)}{n(S)}=\frac{4}{8}
$$
**Event**:
$$
E=\{(x,y,z)|x\sub X,y\sub Y,z\sub Z\}
$$

$$
P((red, red, black)\text{ or }(red,black,red)\text{ or }(black,red,red)) =\newline
P((red, red, black)) + P((red,black,red)) + P((black,red,red)) =\newline
P(red)\times P(red)\times P(black)+P(red)\times P(black)\times P(red)+P(black)\times P(red)\times P(red)=\newline
\frac{4}{7}\times\frac{5}{9}\times\frac{4}{8}+\frac{4}{7}\times\frac{4}{9}\times\frac{4}{8}+\frac{3}{7}\times\frac{5}{9}\times\frac{4}{8}=\newline
\frac{80}{504}+\frac{64}{504}+\frac{60}{504}=\newline
\frac{80 + 64 + 60}{504}=\frac{204}{504}=\frac{102}{252}=\frac{51}{126}=\newline
\frac{17}{42}
$$

