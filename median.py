def my_median(sample):
     n = len(sample)
     index = n // 2
     # Sample with an odd number of observations
     if n % 2:
         return sorted(sample)[index]
     # Sample with an even number of observations
     return sum(sorted(sample)[index - 1:index + 1]) / 2


print(my_median([0, 2, 2, 1, 0, 7, 4]))

