from priority_queue import PriorityQueue


def test_priority_and_sort_order():

    p = PriorityQueue()
    p.add(1, 1)
    p.add(2, 1)
    p.add(3, 2)
    p.add(4, 1)
    assert p.pop() == 3
    assert p.pop() == 1
    assert p.pop() == 2
    assert p.pop() == 4
    assert p.peek() is None
