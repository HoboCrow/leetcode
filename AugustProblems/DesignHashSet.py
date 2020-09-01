import unittest


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [None for i in range(10)]
        self.load = 0

    def rebuild(self):
        # print("rebuild")
        old_table = self.table
        self.load = 0
        self.table = [None for i in range(len(old_table)*2)]
        for key in old_table:
            if key is not None:
                self.add(key)

    def hash(self, value):
        h = 7 + value * 31
        return h % len(self.table)

    def add(self, key: int) -> None:
        h = self.hash(key)
        if self.table[h] is not None and self.table[h] != key:
            self.rebuild()
            self.add(key)
        else:
            self.table[h] = key
            self.load += 1

    def remove(self, key: int) -> None:
        h = self.hash(key)
        if self.table[h] == key:
            self.table[h] = None
            self.load -= 1

    def contains(self, key: int) -> bool:
        """
        Returns True if this set contains the specified element
        """
        return self.table[self.hash(key)] == key

    def get_load(self):
        return (self.load/len(self.table), self.load, len(self.table))

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


class Tests(unittest.TestCase):
    def test_add(self):
        mhs = MyHashSet()
        self.assertFalse(mhs.contains(0))
        mhs.add(0)
        self.assertTrue(mhs.contains(0))

    def test_remove(self):
        mhs = MyHashSet()
        mhs.add(0)
        self.assertTrue(mhs.contains(0))
        mhs.remove(0)
        self.assertFalse(mhs.contains(0))

    def leetcode_format(self, mhs, ops, ins, outs):
        result = [None]
        notes = []
        for op, inp, out in zip(ops[1:], ins[1:], outs[1:]):
            inp = inp[0]
            if op == "contains":
                r = mhs.contains(inp)
                result.append(r)
                if r != out:
                    notes.append(f"Contains {inp} - got {r} expected {out}")
            if op == "remove":
                mhs.remove(inp)
                result.append(None)
            if op == "add":
                mhs.add(inp)
                result.append(None)
            # print(f"{op} {inp} {mhs.contains(40)}")
        return result, notes

    def test_full(self):
        ops = ["MyHashSet", "contains", "remove", "add", "add", "contains", "remove", "contains", "contains", "add", "add", "add", "add", "remove", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "contains", "add", "contains", "add", "add", "contains", "add", "add", "remove", "add", "add", "add", "add", "add", "contains", "add", "add", "add", "remove", "contains", "add", "contains", "add", "add", "add", "add", "add",
               "contains", "remove", "remove", "add", "remove", "contains", "add", "remove", "add", "add", "add", "add", "contains", "contains", "add", "remove", "remove", "remove", "remove", "add", "add", "contains", "add", "add", "remove", "add", "add", "add", "add", "add", "add", "add", "add", "remove", "add", "remove", "remove", "add", "remove", "add", "remove", "add", "add", "add", "remove", "remove", "remove", "add", "contains", "add"]
        ins = [[], [72], [91], [48], [41], [96], [87], [48], [49], [84], [82], [24], [7], [56], [87], [81], [55], [19], [40], [68], [23], [80], [53], [76], [93], [95], [95], [67], [31], [80], [62], [73], [97], [33], [28], [62], [81], [57], [40], [11], [89], [28], [97], [86], [20], [5], [77], [52], [57], [88], [
            20], [48], [42], [86], [49], [62], [53], [43], [98], [32], [15], [42], [50], [19], [32], [67], [84], [60], [8], [85], [43], [59], [65], [40], [81], [55], [56], [54], [59], [78], [53], [0], [24], [7], [53], [33], [69], [86], [7], [1], [16], [58], [61], [34], [53], [84], [21], [58], [25], [45], [3]]
        outs = [None, False, None, None, None, False, None, True, False, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, False, None, True, None, None, True, None, None, None, None, None, None, None, None, True, None, None, None, None, False, None, False, None, None, None, None,
                None, True, None, None, None, None, True, None, None, None, None, None, None, True, True, None, None, None, None, None, None, None, False, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, False, None]
        results, notes = self.leetcode_format(MyHashSet(), ops, ins, outs)
        # print(notes)
        self.assertEqual(results, outs)

    def test_full2(self):
        ops = ["MyHashSet", "add", "contains", "add", "contains", "remove", "add", "contains", "add", "add", "add", "add", "add", "add", "contains", "add", "add", "add", "contains", "remove", "contains", "contains", "add", "remove", "add", "remove", "add", "remove", "add", "contains", "add", "add", "contains", "add", "add", "add", "add", "remove", "contains", "add", "contains", "add", "add", "add", "remove", "remove", "add", "contains", "add",
               "add", "contains", "remove", "add", "contains", "add", "remove", "remove", "add", "contains", "add", "contains", "contains", "add", "add", "remove", "remove", "add", "remove", "add", "add", "add", "add", "add", "add", "remove", "remove", "add", "remove", "add", "add", "add", "add", "contains", "add", "remove", "remove", "remove", "remove", "add", "add", "add", "add", "contains", "add", "add", "add", "add", "add", "add", "add", "add"]
        ins = [[], [58], [0], [14], [58], [91], [6], [58], [66], [51], [16], [40], [52], [48], [40], [42], [85], [36], [16], [0], [43], [6], [3], [25], [99], [66], [60], [58], [97], [3], [35], [65], [40], [41], [10], [37], [65], [37], [40], [28], [60], [30], [63], [76], [90], [3], [43], [81], [61], [39], [
            75], [10], [55], [92], [71], [2], [20], [7], [55], [88], [39], [97], [44], [1], [51], [89], [37], [19], [3], [13], [11], [68], [18], [17], [41], [87], [48], [43], [68], [80], [35], [2], [17], [71], [90], [83], [42], [88], [16], [37], [33], [66], [59], [6], [79], [77], [14], [69], [36], [21], [40]]
        outs = [None, None, False, None, True, None, None, True, None, None, None, None, None, None, True, None, None, None, True, None, False, True, None, None, None, None, None, None, None, True, None, None, True, None, None, None, None, None, True, None, True, None, None, None, None, None, None, False, None, None,
                False, None, None, False, None, None, None, None, True, None, True, True, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, True, None, None, None, None, None, None, None, None, None, False, None, None, None, None, None, None, None, None]
        mhs = MyHashSet()
        results, notes = self.leetcode_format(mhs, ops, ins, outs)
        print(mhs.get_load())
        self.assertEqual(results, outs)

    def test_full3(self):
        ops = ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "add", "add", "remove", "add", "contains", "add", "add", "contains", "add", "add", "add", "add", "add", "remove", "add", "add", "add", "remove", "add", "add", "contains", "remove", "remove", "remove", "add", "add", "remove", "add", "add", "contains", "add", "add", "contains", "add", "add", "remove", "add", "add", "add", "remove", "add", "contains", "add", "add",
               "contains", "add", "add", "add", "add", "add", "add", "contains", "add", "remove", "add", "remove", "add", "add", "remove", "add", "contains", "add", "remove", "remove", "add", "add", "remove", "add", "remove", "contains", "add", "remove", "add", "add", "contains", "remove", "contains", "add", "contains", "contains", "add", "add", "add", "add", "remove", "add", "add", "contains", "contains", "add", "add", "add", "remove", "remove"]
        ins = [[], [95], [17], [95], [26], [70], [43], [33], [75], [86], [29], [39], [74], [56], [99], [4], [57], [81], [79], [26], [82], [13], [59], [69], [98], [45], [53], [84], [77], [89], [70], [51], [96], [6], [46], [86], [96], [87], [37], [96], [95], [58], [46], [41], [4], [80], [50], [89], [17], [4], [
            14], [69], [93], [3], [59], [63], [26], [5], [5], [44], [25], [17], [46], [69], [82], [28], [72], [6], [43], [11], [85], [61], [85], [62], [58], [98], [70], [13], [48], [91], [96], [87], [30], [91], [84], [59], [92], [97], [61], [91], [78], [16], [36], [85], [32], [93], [54], [89], [74], [79], [54]]
        outs = [None, None, None, True, False, None, False, None, None, None, None, False, None, None, False, None, None, None, None, None, None, None, None, None, None, None, None, False, None, None, None, None, None, None, None, None, True, None, None, True, None, None, None, None, None, None, None, None, True, None,
                None, True, None, None, None, None, None, None, True, None, None, None, None, None, None, None, None, False, None, None, None, None, None, None, None, None, False, None, None, None, None, True, None, True, None, True, False, None, None, None, None, None, None, None, False, True, None, None, None, None, None]
        mhs = MyHashSet()
        results, notes = self.leetcode_format(mhs, ops, ins, outs)
        print(mhs.get_load())
        self.assertEqual(results, outs)


if __name__ == "__main__":
    # unittest.main()
    mhs = MyHashSet()
    for i in range(1, 10000000):
        mhs.add(i)
    print(mhs.get_load())
