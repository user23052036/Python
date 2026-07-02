Exactly. That's one of the differences between Python and C++.

### Python

Dictionary keys **must be hashable**.

A mutable object like a `list` is **not hashable**, so it cannot be a key.

```python
d = {}

d[[1,2,3]] = 10
```

Output:

```text
TypeError: unhashable type: 'list'
```

The reason is that if the list changed after being inserted, its hash would change, breaking the dictionary's internal structure.

However, immutable objects like tuples are hashable (provided all their elements are hashable):

```python
d = {}

d[(1,2,3)] = 10

print(d[(1,2,3)])   # 10
```

---

### C++

C++ doesn't have the concept of "mutable keys must be hashable" in the same way.

An `unordered_map` only requires:

1. A hash function.
2. An equality function.

So if you provide a hash for `vector<int>`, it can be used as a key:

```cpp
unordered_map<vector<int>, int, VectorHash> mp;
```

Even though `vector` is mutable.

---

### But there's an important rule

Once a vector is used as a key, **you must not modify that key while it is inside the map**.

For example, conceptually:

```cpp
vector<int> v = {1,2,3};
mp[v] = 10;

// If you somehow modified the stored key,
// the hash would no longer match its bucket.
```

In practice, `unordered_map` stores its own copy of the key, and its keys are treated as `const`, so you cannot modify them through the map:

```cpp
for (auto& p : mp) {
    // p.first.push_back(4);   // ❌ Compilation error
}
```

This design prevents exactly the kind of problem that Python avoids by requiring immutable keys.

### Summary

| Feature                        | Python `dict`    | C++ `unordered_map`          |
| ------------------------------ | ---------------- | ---------------------------- |
| Mutable `list`/`vector` as key | ❌ Not allowed    | ✅ Allowed with a custom hash |
| Immutable `tuple` as key       | ✅ Yes            | N/A                          |
| Keys modifiable inside the map | ❌ Not applicable | ❌ No (`first` is `const`)    |
| Requires hash function         | Built-in         | Built-in or user-provided    |

So Python enforces immutability as a requirement for hashability, whereas C++ allows mutable types as keys but prevents modification of the stored keys and relies on you to provide a correct hash function.
