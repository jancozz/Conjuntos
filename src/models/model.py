class SetOperationsModel:
    def __init__(self):
        self.sets = {}

    def create_set(self, name, elements):
        self.sets[name] = set(elements)

    def get_set(self, name):
        return self.sets.get(name, set())

    def get_all_sets(self):
        return self.sets

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

    def is_equal(self, set1_name, set2_name):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)
        return set1 == set2

    def is_disjoint(self, set1_name, set2_name):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)
        return set1.isdisjoint(set2)

    def check_elements_in_sets(self, relation_set, set1, set2):
        """ Verifica que los elementos en relation_set estén en al menos uno de los dos conjuntos """
        for (a, b) in relation_set:
            a, b = str(a), str(b)
            if a not in set1 and a not in set2:
                raise ValueError(f"Elemento {a} no pertenece a ninguno de los conjuntos dados.")
            if b not in set1 and b not in set2:
                raise ValueError(f"Elemento {b} no pertenece a ninguno de los conjuntos dados.")

    def is_reflexive(self, set1_name, set2_name, relation_set):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)

        self.check_elements_in_sets(relation_set, set1, set2)

        relation_set = [(str(a), str(b)) for (a, b) in relation_set]

        combined_set = set1.union(set2)

        for a in combined_set:
            if (str(a), str(a)) not in relation_set:
                return False
        return True

        for (a, a) in relation_set:
            if (a, a) not in set1.union(set2):
                return False
        return True

    def is_symmetric(self, set1_name, set2_name, relation_set):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)

        self.check_elements_in_sets(relation_set, set1, set2)

        for (a, b) in relation_set:
            if (b, a) not in relation_set:
                return False
        return True

    def is_antisymmetric(self, set1_name, set2_name, relation_set):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)

        self.check_elements_in_sets(relation_set, set1, set2)

        for (a, b) in relation_set:
            if (b, a) in relation_set and a != b:
                return False
        return True

    def is_transitive(self, set1_name, set2_name, relation_set):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)

        self.check_elements_in_sets(relation_set, set1, set2)

        for (a, b) in relation_set:
            for (b2, c) in relation_set:
                if b == b2:
                    if (a, c) not in relation_set:
                        return False
        return True
