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

My better version of the instructions:
If floor is equal to or above f, eggs are broken upon throw.
If floor is less than f, eggs are not broken upon drop.
Find a way make eggs broken minimized by solving for f.
Let n represent all the amount floors of the building.

A binary search needs to be done so we minimize the amount of needed testing and breaking of eggs. Solution in words:

Take n and divide it in half. Drop an egg at that number. 

If egg breaks we are above f and we can know all floors at and above our value will also surely break our egg and can eliminate these floors from being our f value.

Else egg doesn't break we can assume all floors below our value are safe and we've either found f or some floor below it. Eliminate all floors below this value from being f. We must continue our research for now just to be sure.

Next we take our values that aren't eliminated from being f and half them then drop an egg at that value. Repeat the if and else above. And keep repeating this process until we have only one value left which we can be sure then is f.
