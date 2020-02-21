#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
this problem above is linear. I input 1 for n then solved seeing the loop run just once. I input 2 and the loop ran twice. Then I solved for 3 and the loop ran 3 times. O(n)


b)

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
First column for n, second how many loops ran for each iteration. Included the for loop running once for each in my 2nd columns count
1 * 1
2 * 2
3 * 3
4 * 3
5 * 4

From the relationship of these numbers it looks to me as though it is a relationship of O(log(n))


c)

c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

This looks like O(1) it gets no more complicated for each number input. No extra work is done for it I put 10 vs 10,000

## Exercise II


