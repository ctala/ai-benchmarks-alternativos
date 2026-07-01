# Nemotron 3 Ultra 550B — deep_reasoning/code_bug_subtle

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 3.7 | quality: 3.2
- latency_total: 47.019s | tokens_per_second: 174.2
- input_tokens: 235 | output_tokens: 8192

## Respuesta completa

The user wants me to identify a subtle bug in the provided Python code without running it.
The code calculates the Median Absolute Deviation (MAD) to filter outliers and then averages the remaining data.

Let's analyze `find_median`:
- Handles empty list? No, `len(sorted_nums)` would be 0, `mid` 0, access `sorted_nums[0]` -> IndexError. But `remove_outliers_and_average` checks `len(data) < 3`, so `find_median` receives at least 3 elements. Safe there.
- Logic looks standard for median.

Let's analyze `remove_outliers_and_average`:
1. `if len(data) < 3: return sum(data) / len(data)`
   - If `len(data) == 0`, `ZeroDivisionError`.
   - If `len(data) == 1` or `2`, returns average. Correct.

2. `median = find_median(data)`
3. `mad = find_median([abs(x - median) for x in data])`
   - MAD calculation. Standard definition usually multiplies by 1.4826 for normal distribution consistency, but here it's just raw MAD. Not a bug per se, just a definition choice.

4. `threshold = 3 * mad`
5. `filtered = [x for x in data if abs(x - median) <= threshold]`
6. `return sum(filtered) / len(filtered)`

The bug hint says: "piensa en que pasa con datos especificos" (think what happens with specific data).

When does `filtered` become empty?
If `mad == 0`, then `threshold == 0`.
The condition becomes `abs(x - median) <= 0`, which means `x == median`.
So `filtered` contains only elements exactly equal to the median.

When is `mad == 0`?
`mad` is the median of absolute deviations.
`mad == 0` implies the median of absolute deviations is 0.
This happens when at least 50% of the data points are exactly equal to the median.
Since the median is a value from the dataset (or average of two middle), if more than half the data is identical, the median is that value.
Then `abs(x - median)` is 0 for more than half the points.
The median of these deviations is 0.

Example: `data = [10, 10, 10, 10, 100]`
Median = 10.
Deviations = `[0, 0, 0, 0, 90]`.
Sorted deviations = `[0, 0, 0, 0, 90]`.
Median of deviations (MAD) = 0.
Threshold = 0.
Filtered = `[x for x in data if abs(x - 10) <= 0]` -> `[10, 10, 10, 10]`.
Average = 10. Works fine.

What if `data = [10, 10, 100, 100, 100]`? (Len 5)
Median = 100.
Deviations = `[90, 90, 0, 0, 0]`.
Sorted = `[0, 0, 0, 90, 90]`.
MAD = 0.
Threshold = 0.
Filtered = `[100, 100, 100]`.
Average = 100. Works fine.

What if `filtered` becomes empty?
This requires NO element satisfying `abs(x - median) <= threshold`.
If `threshold = 0`, we need `x == median`.
Since `median` is calculated from `data`, `median` is always a value present in `data` (for odd length) or average of two middle values (for even length).

Case 1: Odd length `n`. Median is `sorted_nums[mid]`. This value exists in `data`. So at least one element equals median. `abs(median - median) = 0 <= 0`. Filtered is never empty.

Case 2: Even length `n`. Median is `(sorted_nums[mid-1] + sorted_nums[mid]) / 2`.
This value might NOT be in the dataset.
Example: `data = [1, 2, 3, 4]`. Median = 2.5.
Deviations = `[1.5, 0.5, 0.5, 1.5]`. Sorted = `[0.5, 0.5, 1.5, 1.5]`.
MAD = (0.5 + 1.5) / 2 = 1.0.
Threshold = 3.0.
Filtered = all points where `abs(x - 2.5) <= 3`. Range `[-0.5, 5.5]`. All points included. Fine.

We need MAD = 0 for even length.
MAD = 0 means median of deviations is 0.
For even length `n`, median of deviations is average of two middle deviations.
For this average to be 0, both middle deviations must be 0.
This means at least `n/2 + 1` deviations are 0? No.
Sorted deviations `d_0 ... d_{n-1}`.
Mid indices `n/2 - 1` and `n/2`.
We need `d_{n/2 - 1} = 0` and `d_{n/2} = 0`.
Since sorted, this means first `n/2 + 1` deviations are 0? No, indices 0 to `n/2` are 0. That's `n/2 + 1` zeros.
So at least `n/2 + 1` data points have deviation 0.
Deviation 0 means `x == median`.
But for even length, median is average of two middle values `a` and `b`. Median = `(a+b)/2`.
For `x` to have deviation 0, `x == (a+b)/2`.
If `a != b`, then `(a+b)/2` is not in the list (assuming integers or distinct floats).
So no data point equals the median.
Therefore, deviations are all > 0.
MAD > 0.
Threshold > 0.
Filtered not empty.

Wait, if `a == b`, then median = `a`. Data points equal to `a` exist.
Example: `[1, 2, 2, 3]`. Median = 2. Deviations `[1, 0, 0, 1]`. MAD = 0. Threshold = 0. Filtered = `[2, 2]`. OK.

So `filtered` is never empty?
Let's check `len(data) < 3` case.
`len(data) == 0`: `sum(data) / len(data)` -> ZeroDivisionError.
`len(data) == 1`: returns the element.
`len(data) == 2`: returns average.

The prompt says "bug sutil que solo aparece en ciertos casos".
ZeroDivisionError on empty list is obvious, not subtle.
Is there a case where `filtered` is empty?
What if `data` contains NaNs? `sorted` works, median works, abs works. `sum` works. `len` works.
What if `data` is not a list but a generator? `len(data)` fails. Type hint suggests list.

Let's look at `find_median` again.
```python
def find_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]
```
If `numbers` is empty, `n=0`, `mid=0`. `n%2==0`. `sorted_nums[-1]` and `sorted_nums[0]`. IndexError.
But `remove_outliers` checks `len < 3`.

Wait... `remove_outliers_and_average` calls `find_median(data)`.
Then `mad = find_median([abs(x - median) for x in data])`.
The list comprehension creates a new list. Length same as data.
If data has 3 elements, deviations list has 3 elements. `find_median` works.

Is it possible that `threshold` calculation overflows? Python handles big ints/floats.
Is it floating point precision?
`abs(x - median) <= threshold`.
If `mad` is very small, threshold small.
But `mad` is median of deviations.

Let's reconsider the MAD definition.
Standard MAD is `median(|X_i - median(X)|)`.
The code does exactly that.
The bug might be in the **constant factor**.
Usually MAD is scaled by 1.4826 to estimate sigma for normal distribution.
The code uses `threshold = 3 * mad`.
If the data is Gaussian, 3 * MAD (unscaled) corresponds to ~2 sigma, not 3 sigma.
But the hint says "piensa en que pasa con datos especificos", not "the constant is wrong statistically".

Let's search for "ZeroDivisionError" in `return sum(filtered) / len(filtered)`.
When is `len(filtered) == 0`?
We established `median` is in `data` for odd `n`.
For even `n`, `median` is average of two middle values.
If `data = [1, 3]`. Len < 3, returns 2.0.
If `data = [1, 2, 3, 4]`. Median 2.5. Deviations `[1.5, 0.5, 0.5, 1.5]`. MAD 1.0. Threshold 3.0. Filtered all.
What if `data = [1, 100, 101, 200]`?
Median = (100+101)/2 = 100.5.
Deviations = `[99.5, 0.5, 0.5, 99.5]`.
Sorted dev = `[0.5, 0.5, 99.5, 99.5]`.
MAD = (0.5 + 99.5) / 2 = 50.0.
Threshold = 150.
Filtered: `abs(x - 100.5) <= 150`. Range `[-49.5, 250.5]`. All included.

What if all data points are the same? `[5, 5, 5]`.
Median 5. Dev `[0,0,0]`. MAD 0. Thresh 0.
Filtered `[5,5,5]`. Len 3. Avg 5. OK.

What if data has 3 points: `[0, 0, 1]`?
Median 0. Dev `[0, 0, 1]`. MAD 0. Thresh 0.
Filtered `[0, 0]`. Len 2. Avg 0. OK.

What if data has 3 points: `[0, 1, 1]`?
Median 1. Dev `[1, 0, 0]`. MAD 0. Thresh 0.
Filtered `[1, 1]`. Len 2. Avg 1. OK.

Is there any case where `filtered` is empty?
Only if `threshold < 0` (impossible) or no `x` satisfies condition.
Since `median` is derived from `data`, for odd `n`, `median` is in `data`. So `abs(median - median) = 0 <= threshold` (since threshold >= 0). So `filtered` has at least 1 element.
For even `n`, `median` = `(a+b)/2`.
If `a != b`, `median` not in `data`.
Deviations are `|x - median|`.
The minimum deviation is `min(|a - median|, |b - median|) = |a-b|/2`.
Since `a != b`, min deviation > 0.
MAD is median of deviations. Since min deviation > 0, MAD > 0.
Threshold = 3 * MAD > 0.
Is it possible that `3 * MAD < min_deviation`?
If so, no point passes the filter.
`min_dev = |a-b|/2`.
Deviations list: `d_1, d_2, ..., d_n`. Sorted.
`d_0 = d_1 = |a-b|/2` (assuming a, b are the two middle values).
Wait, for even n=4. Sorted data `[x0, x1, x2, x3]`. Median `(x1+x2)/2`.
Deviations: `|x0-m|, |x1-m|, |x2-m|, |x3-m|`.
`|x1-m| = |x2-m| = |x1-x2|/2`.
`|x0-m| >= |x1-m|`. `|x3-m| >= |x2-m|`.
Sorted deviations: `[d, d, D1, D2]` where `d = |x1-x2|/2`.
MAD = `(d + D1) / 2`.
Threshold = `3 * (d + D1) / 2`.
Condition for `x1` to be kept: `d <= threshold`.
`d <= 1.5 * (d + D1)`
`d <= 1.5d + 1.5 D1`
`-0.5d <= 1.5 D1` -> Always true since `d, D1 >= 0`.
So `x1` and `x2` are ALWAYS kept.
So `filtered` is never empty for n >= 2.
For n=3 (odd), median is `x1`. `x1` is kept.
So `filtered` is never empty for `len(data) >= 1`.
The `len(data) < 3` handles 0, 1, 2.
Wait, `len(data) == 0` -> `sum(data)/len(data)` -> ZeroDivisionError.
That's a bug. But is it "sutil"? It's a standard edge case.

Is there a bug with `find_median` on the deviations list?
`mad = find_median([abs(x - median) for x in data])`
The list comprehension creates floats if median is float.
`find_median` sorts them. Works fine.

What about the **definition of MAD**?
The code calculates `median(abs(x - median))`.
This is the **median absolute deviation**.
However, the variable name is `mad`.
In statistics, MAD is often defined as `median(|X_i - median(X)|)`.
But sometimes it's defined as `mean(|X_i - mean(X)|)` (Mean Absolute Deviation).
The code uses median, so variable name `mad` is correct for Median Absolute Deviation.

Wait, the **bug** might be that `find_median` is called on the **original data** to get median, then on **deviations** to get MAD.
But `find_median` sorts the list.
`sorted_nums = sorted(numbers)`
This creates a new list. O(N log N) time, O(N) space.
Called twice. Not a bug, just performance.

Let's look at the `if n % 2 == 0` branch in `find_median`.
`return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2`
In Python 3, `/` is float division.
If input is integers, median becomes float.
Deviations become floats.
MAD becomes float.
Threshold becomes float.
Comparison `abs(x - median) <= threshold` works (int vs float).
Return `sum(filtered) / len(filtered)` returns float.
Consistent.

What if the input list is **huge**? Memory? Not a logic bug.

Let's read the hint again: "piensa en que pasa con datos especificos".
Specific data...
What if `data` contains `None`? TypeError.
What if `data` contains `Decimal`? Works.
What if `data` contains `Fraction`? Works.

Is it possible that `mad` is 0 and `threshold` is 0, and `median` is not in `data` (even length), and NO other point is equal to median?
We proved for even length, if median not in data, min deviation > 0, so MAD > 0.
So threshold > 0.
And the two middle points have deviation `d`.
MAD = `(d + D1)/2 >= d/2`.
Threshold = `3 * MAD >= 1.5 * d`.
Since `d <= 1.5 * d`, the middle points are kept.
So filtered not empty.

Wait.
`data = [1, 2, 100, 101]`
Median = 51.5
Devs = `[50.5, 49.5, 48.5, 49.5]` -> Sorted `[48.5, 49.5, 49.5, 50.5]`
MAD = `(49.5 + 49.5) / 2 = 49.5`
Threshold = 148.5
All kept.

What if `data` has **3 elements**? `[a, b, c]` sorted.
Median `b`.
Devs `[b-a, 0, c-b]`.
Sorted `[0, min(b-a, c-b), max(...)]`.
MAD = `min(b-a, c-b)`.
Threshold = `3 * min(b-a, c-b)`.
Filtered keeps `x` where `|x-b| <= 3 * min(b-a, c-b)`.
`b` is kept (dev 0).
`a` kept if `b-a <= 3*(b-a)` -> true if `b>=a`.
`c` kept if `c-b <= 3*(c-b)` -> true.
So all 3 kept. Unless `b-a` or `c-b` negative (impossible sorted).
So for 3 elements, never filters anything out if MAD > 0.
If MAD = 0 (e.g. `[1, 1, 2]` -> median 1, devs `[0,0,1]`, MAD 0).
Threshold 0.
Keeps only `1, 1`.
Works.

What about **4 elements**? `[a, b, c, d]`.
Median `(b+c)/2`.
Devs: `|a-m|, |b-m|, |c-m|, |d-m|`.
`|b-m| = |c-m| = (c-b)/2 = d_mid`.
`|a-m| >= d_mid`, `|d-m| >= d_mid`.
Sorted devs: `[d_mid, d_mid, D1, D2]`.
MAD = `(d_mid + D1) / 2`.
Threshold = `1.5 * (d_mid + D1)`.
Check `b`: dev `d_mid`. `d_mid <= 1.5 d_mid + 1.5 D1`. True.
Check `a`: dev `D_a`. `D_a <= 1.5 d_mid + 1.5 D1`.
Since `D_a` could be `D1` (if `D1` corresponds to `a`).
If `D_a = D1`. `D1 <= 1.5 d_mid + 1.5 D1` -> `0 <= 1.5 d_mid + 0.5 D1`. True.
So `a` and `d` are kept.
So for 4 elements, never filters out.

**5 elements**? `[a, b, c, d, e]`. Median `c`.
Devs: `c-a, c-b, 0, d-c, e-c`.
Sorted: `[0, min(c-b, d-c), ..., max]`.
MAD = 2nd smallest deviation (index 2).
Threshold = 3 * MAD.
`c` kept (dev 0).
`b` kept if `c-b <= 3 * MAD`.
`d` kept if `d-c <= 3 * MAD`.
`a` kept if `c-a <= 3 * MAD`.
`e` kept if `e-c <= 3 * MAD`.
Since MAD is the median deviation (3rd smallest).
The deviations sorted: `d0=0, d1, d2, d3, d4`.
MAD = `d2`.
Threshold = `3 * d2`.
We keep points with deviation `<= 3 * d2`.
`d0=0` kept.
`d1` kept (since `d1 <= d2 <= 3*d2`).
`d2` kept.
`d3` kept if `d3 <= 3*d2`.
`d4` kept if `d4 <= 3*d2`.
So we **always** keep at least 3 points (the median and the two closest neighbors).
Filtered length >= 3.
Average calculated on >= 3 points.

**6 elements**? `[a, b, c, d, e, f]`. Median `(c+d)/2`.
Devs: `|a-m|, |b-m|, |c-m|, |d-m|, |e-m|, |f-m|`.
`|c-m| = |d-m| = (d-c)/2 = d_mid`.
Sorted devs: `d_mid, d_mid, d2, d3, d4, d5`.
MAD = `(d_mid + d2) / 2`. (Indices 2 and 3? No. n=6. mid=3. indices 2, 3. Values `d_mid` (index 1? No).)
Sorted indices 0, 1, 2, 3, 4, 5.
Values: `d_mid, d_mid, X, Y, Z, W`.
Mid indices 2, 3. Values `X, Y`.
MAD = `(X + Y) / 2`.
Threshold = `1.5 * (X + Y)`.
Kept: deviations `<= 1.5(X+Y)`.
`d_mid` (indices 0,1) kept? `d_mid <= X`? Not necessarily. `X` is the 3rd smallest deviation. `d_mid` is 1st/2nd. So `d_mid <= X`. Yes.
`X` kept? `X <= 1.5(X+Y)` -> `0 <= 0.5X + 1.5Y`. Yes.
`Y` kept? `Y <= 1.5X + 1.5Y` -> `0 <= 1.5X + 0.5Y`. Yes.
So indices 0,1,2,3 (4 points) kept.
Filtered len >= 4.

It seems **mathematically impossible** for `filtered` to be empty for `n >= 1`.
And `n=0` crashes at start.

So where is the bug?
"Bug sutil que solo aparece en ciertos casos."

Maybe **floating point precision**?
`threshold = 3 * mad`
`abs(x - median) <= threshold`
If `mad` is calculated from floats.
Example: `data = [1.0, 2.0, 3.0]`
Median 2.0. Devs `[1.0, 0.0, 1.0]`. MAD 1.0. Thresh 3.0. OK.

What if `data` is a **generator**?
`len(data)` fails. `TypeError: object of type 'generator' has no len()`.
But signature says `data`, usually implies sequence.

What if `data` is **numpy array**?
`len` works. `sorted` works (returns list). `abs` works (numpy ufunc? No, python `abs` on array returns array. List comprehension `[abs(x - median) for x in data]` works element-wise. `find_median` receives list of floats. `sorted` works. `sum(filtered)` works. `len(filtered)` works.
Returns python float. Seems fine.

**Wait!** `find_median` sorts the list.
`sorted_nums = sorted(numbers)`
If `numbers` is a **numpy array**, `sorted(numbers)` returns a **python list**.
`find_median` returns python float.
`mad` python float.
`threshold` python float.
`filtered` list comprehension iterates `data` (numpy array). `x` is numpy scalar. `abs(x - median)` -> numpy float. Comparison `<= threshold` -> numpy bool. List comprehension collects numpy scalars? Or python floats?
`sum(filtered)` -> numpy scalar? `len(filtered)` -> int.
Division -> numpy float.
Works.

What if `data` contains **NaN**?
`sorted([1, float('nan'), 2])` -> `[1, 2, nan]` (NaN sorts to end).
Median index 1 -> `2.0`.
Deviations: `[abs(1-2)=1, abs(nan-2)=nan, abs(2-2)=0]` -> `[1, nan, 0]`.
Sorted devs: `[0, 1, nan]`.
Median dev (MAD) = `1`.
Threshold = `3`.
Filtered: `abs(x - 2) <= 3`.
`x=1`: `1 <= 3` True.
`x=nan`: `nan <= 3` False.
`x=2`: `0 <= 3` True.
Filtered `[1, 2]`.
Average `1.5`.
NaN removed. Seems like a feature? But `median` ignored NaN because it sorted to end.
If data `[nan, nan, 1]`. Sorted `[1, nan, nan]`. Median `nan`.
Devs `[nan, nan, nan]`. MAD `nan`. Thresh `nan`.
Filtered `[]` (since `abs(x - nan) <= nan` is False).
`sum([]) / 0` -> ZeroDivisionError.
**This is a bug!** Handling NaNs.
But is it "sutil"? NaNs are poison.

Let's look for a bug with **integers** and **division**.
Python 3: `/` is float division.
`find_median` returns float for even length.
`mad` float.
`threshold` float.
`sum(filtered) / len(filtered)` float.
Consistent.

What if `data` is **empty list** `[]`?
`len(data) < 3` -> True.
`return sum(data) / len(data)` -> `0 / 0` -> **ZeroDivisionError**.
This is a definite bug. `len(data) == 0` crashes.
Is it subtle? It's an edge case. "Solo aparece en ciertos casos" -> empty list.
But usually "sutil" implies logic error on non-trivial data.

Is there a case where `filtered` removes **everything**?
We proved no for n>=1.
Unless... `mad` calculation is wrong?
`mad = find_median([abs(x - median) for x in data])`
`find_median` sorts the list.
If `data` has duplicate values.
`data = [1, 1, 1, 1, 1000]`
Median 1.
Devs `[0, 0, 0, 0, 999]`.
Sorted `[0, 0, 0, 0, 999]`.
MAD = 0 (index 2).
Threshold 0.
Filtered `[1, 1, 1, 1]`.
Avg 1. Correct.

What if `data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`?
Median 5.5.
Devs `[4.5, 3.5, 2.5, 1.5, 0.5, 0.5, 1.5, 2.5, 3.5, 4.5]`.
Sorted `[0.5, 0.5, 1.5, 1.5, 2.5, 2.5, 3.5, 3.5, 4.5, 4.5]`.
MAD = `(2.5 + 2.5) / 2 = 2.5`.
Threshold = 7.5.
All kept.

**Wait.** The MAD calculation in `find_median` for even length:
`return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2`
This is the **mean of the two middle values**.
For MAD (Median Absolute Deviation), the median of deviations for even count is **also** the mean of two middle deviations.
This is correct.

**Is the bug that `find_median` modifies the input list?**
`sorted_nums = sorted(numbers)` creates a new list. Safe.

**Is the bug in `remove_outliers_and_average` logic?**
It calculates median on `data`.
Then calculates MAD on `data`.
Then filters `data`.
Then averages `filtered`.
This is the standard "Median-MAD" outlier detection.
Usually, one iterates: recalculate median/mad on filtered data.
But single pass is a valid method (though less robust). Not a "bug".

**Let's check the `if len(data) < 3` block again.**
```python
    if len(data) < 3:
        return sum(data) / len(data)
```
If `len(data) == 0`: `ZeroDivisionError`.
If `len(data) == 1`: returns `data[0]`. Correct.
If `len(data) == 2`: returns mean. Correct.

**Is it possible that `data` is not a list but a custom object?**
`len`, `sorted`, iteration, `sum`, `abs`. Standard protocol.

**What about the variable name `mad`?**
`mad = find_median([abs(x - median) for x in data])`
This calculates the Median of Absolute Deviations.
Standard MAD definition often includes a scaling factor `1.4826` for normal consistency.
`threshold = 3 * mad`
If the user expects `3 * 1.4826 * mad` (approx 4.5 * mad), then `3 * mad` is a "bug" (too aggressive filtering).
But the hint says "piensa en que pasa con datos especificos". Not "parameter tuning".

**Let's think about `find_median` implementation details.**
```python
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]
```
For `n=0`: `mid=0`. `n%2==0`. `sorted_nums[-1]`, `sorted_nums[0]`. IndexError.
But guarded by `len < 3`.

**What if `data` contains `Decimal` objects?**
`sorted` works. `+` works. `/` works (Decimal division). `abs` works. `sum` works. `len` works.
Returns Decimal. Fine.

**What if `data` contains `Fraction` objects?**
Same.

**What if `data` is a tuple?**
`sorted` returns list. `len` works. `sum` works. Fine.

**The "Subtle Bug" might be the `ZeroDivisionError` on empty list.**
It fits "solo aparece en ciertos casos" (empty list).
It fits "identificalo sin ejecutar".
It is a bug.
But is it "sutil"? It's the most basic edge case.

Is there another one?
`filtered = [x for x in data if abs(x - median) <= threshold]`
`return sum(filtered) / len(filtered)`
If `filtered` is empty -> ZeroDivisionError.
We proved `filtered` non-empty for `len(data) >= 1`.
So only `len(data) == 0` crashes at start.

**Wait!** `find_median` is called with `data` (original) and then with the list of deviations.
The list of deviations is `[abs(x - median) for x in data]`.
This list has same length as `data`.
If `len(data) >= 3`, deviation list len >= 3. `find_median` safe.

**What if `data` is a generator?**
`len(data)` -> TypeError.
`sorted(data)` -> works.
But `len` fails first.

**Could it be floating point instability in `abs(x - median) <= threshold`?**
`threshold = 3 * mad`.
`mad` is median of `abs(x - median)`.
Due to floating point errors, `mad` might be slightly smaller than the true median deviation.
Or `abs(x - median)` slightly larger.
A point exactly at the boundary might be excluded.
But `threshold = 3 * mad`. The multiplier 3 is large. Unlikely to exclude the median points themselves.
The points defining MAD (the middle deviations) have value `mad` (or average of two).
For odd n: one deviation == mad. `abs(x-median) == mad`. `mad <= 3*mad` True.
For even n: two deviations average to mad. `d1, d2`. `mad = (d1+d2)/2`.
`d1 <= 3*mad`? `d1 <= 1.5(d1+d2)` -> `0 <= 0.5d1 + 1.5d2`. True.
So the points defining MAD are **always** kept mathematically.
Floating point: `d1` and `d2` calculated as `abs(x - median)`.
`mad` calculated as `(d1 + d2) / 2`.
`threshold = 3 * mad`.
Check `d1 <= threshold`.
`d1 <= 3 * (d1 + d2) / 2`
`2*d1 <= 3*d1 + 3*d2`
`0 <= d1 + 3*d2`.
Since `d1, d2 >= 0`, this holds in real math.
In float: `d1 + 3*d2` could be negative? No, sum of non-negatives.
`d1 <= 1.5*d1 + 1.5*d2`?
If `d1` is huge, `d2` tiny. `d1 <= 1.5*d1` -> True.
If `d1` tiny, `d2` huge. `tiny <= 1.5*tiny + 1.5*huge` -> True.
So the comparison should hold in float too.

**What if `data` contains `inf`?**
`[1, 2, float('inf')]`
Sorted `[1, 2, inf]`. Median `2`.
Devs `[1, 0, inf]`. Sorted `[0, 1, inf]`. MAD `1`.
Threshold `3`.
Filtered: `abs(1-2)=1 <= 3` (Keep). `abs(2-2)=0 <= 3` (Keep). `abs(inf-2)=inf <= 3` (False).
Filtered `[1, 2]`. Avg `1.5`. Works.
`[-inf, 1, 2]` -> Median `1`. Devs `[inf, 0, 1]`. MAD `1`. Thresh `3`. Keeps `1, 2`. Avg `1.5`.
`[1, inf, inf]` -> Median `inf`. Devs `[inf, 0, 0]`. Sorted `[0, 0, inf]`. MAD `0`. Thresh `0`.
Filtered: `abs(1-inf)=inf <= 0` (F). `abs(inf-inf)=nan <= 0` (F). `abs(inf-inf)=nan <= 0` (F).
**Filtered is EMPTY!**
`sum([]) / 0` -> **ZeroDivisionError**.
**FOUND IT.**

**Case:** `data` contains `inf` (infinity) such that the **median is `inf`** (or `-inf`).
This happens when at least half the data is `inf`.
Example: `[1, float('inf'), float('inf')]` (len 3).
Median = `inf`.
Deviations = `[inf, 0, 0]`.
Sorted deviations = `[0, 0, inf]`.
MAD = `0`.
Threshold = `0`.
Filter condition: `abs(x - inf) <= 0`.
`abs(1 - inf)` = `inf`. `inf <= 0` False.
`abs(inf - inf)` = `NaN`. `NaN <= 0` False.
`abs(inf - inf)` = `NaN`. `NaN <= 0` False.
`filtered` = `[]`.
`return sum([]) / len([])` -> **ZeroDivisionError**.

Another case: