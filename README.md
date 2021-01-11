# partitions
In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers.

For example, the partitions of 5:

```sh
5
4 + 1
3 + 1 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1
2 + 2 + 1
3 + 2
```

## Setup and run

```sh
pip3 install partitions
```

To run on the command-line:

```sh
$ partitions 11
11
10 + 1
9 + 1 + 1
8 + 1 + 1 + 1
7 + 1 + 1 + 1 + 1
...
```

You can also use this in code:

```py
from partitions import partitions
list(partitions(5)) # returns [(5,), (4, 1), (3, 1, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1), (2, 2, 1), (3, 2)]
```
