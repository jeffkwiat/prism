class KSums(object):
    def __init__(self, input_file):
        self.input_file = input_file
        self.number_of_factors = 0
        self.target_sum = 0
        self.potentials = []
        self.parse_file()

    def __str__(self):
        """ Return a string of this object. """
        return 'Factors: %s, TargetSum: %s, Potentials: %s' % \
               (self.number_of_factors,
               self.target_sum,
               ', '.join([str(p) for p in self.potentials]))

    def parse_file(self):
        """ Parse the file and populate our object. """
        line_number = 0
        for line in open(self.input_file):
            if line_number == 0:
                self.number_of_factors = int(line.strip())
            elif line_number == 1:
                self.target_sum = int(line.strip())
            else:
                self.potentials.append(int(line.strip()))

            line_number += 1

    def get_factors_brute_force(self):

        """
        Return a list of values that can be used to reach the
        target sum.

        We will return the first set of numbers.  If there are multiple sets
        of triplets that work, we will miss them.

        Time Complexity: O(n^3)
        Space Complexity: O(n)

        :return: a list of factors
        """
        factors = []

        if len(self.potentials) < 3:
            raise Exception('You must have a least 3 potential values')

        # For each first digit...
        for i in range(len(self.potentials)):
            factors = []

            # Loop through our second digits
            for j in range(len(self.potentials)):

                # Make sure we don't use the same value twice.
                if i != j:

                    # Loop through our third digits
                    for k in range(len(self.potentials)):

                        # Make sure this digit isn't either our first or second digit.
                        if k != j and k != i:
                            sum = self.potentials[i] + self.potentials[j] + self.potentials[k]
                            if sum == self.target_sum:
                                factors.append(self.potentials[i])
                                factors.append(self.potentials[j])
                                factors.append(self.potentials[k])
                                return factors

        return factors

    def print_factors(self, factors):
        """ Just print out the list of factors to the console. """
        for factor in factors:
            print(factor)

    def get_factors_optimized(self):
        """ Let's try a greedy approach. """
        current_target = 0
        already_seen = {}
        pass



if __name__ == '__main__':
    sums = KSums('inputs/k-sum.txt')
    sums.print_factors(sums.get_factors_brute_force())
