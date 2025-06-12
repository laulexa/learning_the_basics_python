squared = [x**2 for x in range(1,11)]
print("squares: ", squared)

cubed = [x**3 for x in range(1,11)]
print("cubed: ", cubed)

celsius = [0, 10, 20, 40]
fahrenheit = [(temp *9/5) * 32 for temp in celsius] #F =(9/5 *C) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# even numbers
evens = [x for x in range(1,21) if x % 2 == 0]
print("even numbers: ", evens)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(len(matrix[0]))
print(matrix)
print(transposed)

#another way to do it
transposed_2 = []

for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed_2.append(transposed_row)
print(transposed)

'''```python
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
```

This line **transposes a matrix** — meaning it converts rows into columns and columns into rows.

---

### Example Matrix:
Let's say `matrix` is:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
```

This is a **2x3 matrix** (2 rows, 3 columns). After transposition, it becomes a **3x2 matrix**:

```python
[
    [1, 4],
    [2, 5],
    [3, 6]
]
```

---

### Step-by-Step Breakdown:

#### 1. **Outer list comprehension**
```python
for i in range(len(matrix[0]))
```

- `matrix[0]` is the first row: `[1, 2, 3]`
- `len(matrix[0])` is `3`, which is the number of **columns**
- So `i` will loop over: `0, 1, 2`

Each value of `i` corresponds to a column index in the original matrix.

---

#### 2. **Inner list comprehension**
```python
[row[i] for row in matrix]
```

- This loops over **each row** in `matrix`
- For a given `i`, it picks the **i-th element from each row**

Let's walk through one loop of the outer list comprehension:

##### For `i = 0`:
```python
[row[0] for row in matrix] 
→ [1, 4]   # first elements from each row
```

##### For `i = 1`:
```python
[row[1] for row in matrix] 
→ [2, 5]   # second elements from each row
```

##### For `i = 2`:
```python
[row[2] for row in matrix] 
→ [3, 6]   # third elements from each row
```

---

### Final Result:
Putting it all together:

```python
transposed = [
    [1, 4],  # i = 0
    [2, 5],  # i = 1
    [3, 6]   # i = 2
]'''