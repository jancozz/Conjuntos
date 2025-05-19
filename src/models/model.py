import random


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

        union_set = set()

        for a in set1:
            union_set.add(a)
            for b in set2:
                union_set.add(b)

        return sorted(union_set)

    def intersection(self, set1_name, set2_name):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)

        intersection_set = set()

        for a in set1:
            if a in set2:
                intersection_set.add(a)

        for b in set2:
            if b in set1:
                intersection_set.add(b)

        return sorted(intersection_set)

    def difference(self, set1_name, set2_name):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)

        difference_set = set()

        for a in set1:
            if a not in set2:
                difference_set.add(a)

        return sorted(difference_set)

    def symmetric_difference(self, set1_name, set2_name):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)

        s_difference_set = set()

        for a in set1:
            if a not in set2:
                s_difference_set.add(a)

        for b in set2:
            if b not in set1:
                s_difference_set.add(b)

        return sorted(s_difference_set)

    def is_subset(self, set1_name, set2_name):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)

        for a in set1:
            if a not in set2:
                return False

        return True

    def is_superset(self, set1_name, set2_name):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)

        for b in set2:
            if b not in set1:
                return False

        return True

    def is_equal(self, set1_name, set2_name):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)

        if len(set1) != len(set2):
            return False

        for x in set1:
            if x not in set2:
                return False

        return True

    def is_disjoint(self, set1_name, set2_name):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)

        for x in set1:
            if x in set2:
                return False
        return True

    def check_elements_in_sets(self, relation_set, set1, set2):
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

    def generate_reflexive_set(self, set1_name, set2_name):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)

        combined_set = set1.union(set2)

        reflexive_set = set()

        for a in combined_set:
            reflexive_set.add((a, a))
        return sorted(reflexive_set)

    def generate_random_symmetric_set(self, set1_name, set2_name):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)

        possible_pairs = set(
            [(a, b) for a in set1 for b in set2] + [(b, a) for a in set1 for b in set2] + [(a, a) for a in set1] + [
                (b, b) for b in set2]
        )

        symmetric_set = set()

        selected_pairs = random.sample(list(possible_pairs), 2)

        for (a, b) in selected_pairs:
            symmetric_set.add((a, b))
            symmetric_set.add((b, a))
        return symmetric_set

    def generate_random_antisymmetric_set(self, set1_name, set2_name):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)

        possible_pairs = set(
            [(a, b) for a in set1 for b in set2] + [(b, a) for a in set1 for b in set2] + [(a, a) for a in set1] + [
                (b, b) for b in set2]
        )

        antisymmetric_set = set()

        selected_pairs = random.sample(list(possible_pairs), 4)

        for (a, b) in selected_pairs:
            if (b, a) not in antisymmetric_set:
                antisymmetric_set.add((a, b))
        return antisymmetric_set

    def generate_random_transitive_set(self, set1_name, set2_name):
        set1 = self.get_set(set1_name)
        set2 = self.get_set(set2_name)

        possible_pairs = set(
            [(a, b) for a in set1 for b in set2] + [(b, a) for b in set2 for a in set1]
        )

        transitive_set = set()

        first_pair = random.choice(list(possible_pairs))
        transitive_set.add(first_pair)

        a, b = first_pair

        second_pair = random.choice([pair for pair in possible_pairs if pair[0] == b])
        transitive_set.add(second_pair)

        b, c = second_pair

        third_pair = (a, c)
        transitive_set.add(third_pair)

        return transitive_set
