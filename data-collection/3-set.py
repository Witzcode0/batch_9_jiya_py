"""
Docstring for data-collection.3-set

Set | mutable/immutable | unordered | not allowed duplicate


syntax: 

set_name = {}
set_name = set()


Example :
set_name = {ele1, ele2,..., elen}
"""

# nums = {}

# print(type(nums)) # <class 'dict'>

# nums = {1,2,3,4,5,1,1,1,2,3,4,1,2,4,45,1}
# print(type(nums)) # <class 'set'>

# print(len(nums))

nums = {1,2,3,4,5}

# nums.add(11)
# print(nums)
# print(dir(nums))


s = {1, 2, 3}
s.clear()
print(s)   # set()


s1 = {1, 2, 3}
s2 = s1.copy()
print(s2)  # {1, 2, 3}


# | **Method**                      | **Description**                   | **Example Code**                                           | **Output**   |
# | ------------------------------- | --------------------------------- | ---------------------------------------------------------- | ------------ |
# | `add()`                         | Add one element to set            | `s={1,2}; s.add(3)`                                        | `{1,2,3}`    |
# | `clear()`                       | Remove all elements               | `s={1,2}; s.clear()`                                       | `set()`      |
# | `copy()`                        | Create copy of set                | `s={1,2}; s2=s.copy()`                                     | `{1,2}`      |
# | `difference()`                  | Elements in A not in B            | `A={1,2,3}; B={3,4}`<br>`A.difference(B)`                  | `{1,2}`      |
# | `difference_update()`           | Remove common elements from A     | `A={1,2,3}; B={3,4}`<br>`A.difference_update(B)`           | `{1,2}`      |
# | `discard()`                     | Remove element (no error)         | `s={1,2,3}; s.discard(4)`                                  | `{1,2,3}`    |
# | `intersection()`                | Common elements                   | `A={1,2,3}; B={2,3,4}`<br>`A.intersection(B)`              | `{2,3}`      |
# | `intersection_update()`         | Keep only common elements         | `A={1,2,3}; B={2,3,4}`<br>`A.intersection_update(B)`       | `{2,3}`      |
# | `isdisjoint()`                  | No common elements?               | `A={1,2}; B={3,4}`<br>`A.isdisjoint(B)`                    | `True`       |
# | `issubset()`                    | A ⊆ B                             | `A={1,2}; B={1,2,3}`<br>`A.issubset(B)`                    | `True`       |
# | `issuperset()`                  | A ⊇ B                             | `A={1,2,3}; B={1,2}`<br>`A.issuperset(B)`                  | `True`       |
# | `pop()`                         | Remove random element             | `s={1,2,3}; s.pop()`                                       | random value |
# | `remove()`                      | Remove element (error if missing) | `s={1,2,3}; s.remove(2)`                                   | `{1,3}`      |
# | `symmetric_difference()`        | Non-common elements               | `A={1,2,3}; B={3,4}`<br>`A.symmetric_difference(B)`        | `{1,2,4}`    |
# | `symmetric_difference_update()` | Update with non-common            | `A={1,2,3}; B={3,4}`<br>`A.symmetric_difference_update(B)` | `{1,2,4}`    |
# | `union()`                       | All unique elements               | `A={1,2}; B={3,4}`<br>`A.union(B)`                         | `{1,2,3,4}`  |
# | `update()`                      | Add elements from another set     | `A={1,2}; B={3,4}`<br>`A.update(B)`                        | `{1,2,3,4}`  |
