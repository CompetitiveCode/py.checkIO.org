#Answer to Friends - https://py.checkio.org/en/mission/friends/

class Friends:
    def __init__(self, connections):
        self.connections = list(connections)

    def add(self, connection):
        if connection not in self.connections:
            self.connections.append(connection)
            return True
        return False

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        return False

    def names(self):
        return set().union(*self.connections)

    def connected(self, name):
        return {n for n in self.names() if {n, name} in self.connections}

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"