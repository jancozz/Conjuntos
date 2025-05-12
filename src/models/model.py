class SetOperationsModel:
    def __init__(self):
        self.sets = {}

    def create_set(self, name, elements):
        self.sets[name] = set(elements)

    def get_set(self, name):
        return self.sets.get(name, set())

    def union(self, set1_name, set2_name):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)
        return sorted(set1.union(set2))

    def intersection(self, set1_name, set2_name):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)
        return sorted(set1.intersection(set2))

    def difference(self, set1_name, set2_name):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)
        return sorted(set1.difference(set2))

    def symmetric_difference(self, set1_name, set2_name):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)
        return sorted(set1.symmetric_difference(set2))

    def is_subset(self, set1_name, set2_name):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)
        return set1.issubset(set2)

    def is_superset(self, set1_name, set2_name):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)
        return set1.issuperset(set2)