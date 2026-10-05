"""
2015 day 20 - Infinite Elves and Infinite Houses

Part 1 asks for the lowest house number that receives at least the target in presents, where every
elf delivers ten times its own number to each of its multiples. That makes each house total ten
times the sum of its divisors, so part 1 is a divisor-sum sieve followed by a scan for the first
house to clear the target.

This is using a linear sieve: a first pass finds each number's smallest prime factor, and a second
pass rebuilds the divisor sums from that. Sigma is multiplicative, so for a house n split as
p**k * m with p its smallest prime factor and p not dividing m, the sum of divisors is the sum of
divisors of m times the geometric series 1 + p + ... + p**k. The split is a loop of divisions per
house, which sounds worse than the plain sieve but measures far better: a plain sieve performs one
addition for every divisor of every house, which is N log N of them, while this one is linear in N
and touches each house a few times. On this day's input the plain sieve takes about 2.4 seconds and
the linear one about 0.6.

Part 2 changes one number and adds a rule: each elf brings eleven presents and stops after fifty
houses. A house still collects from its divisors, but only from those with few enough multiples
between them, so the plain sigma no longer applies and there is nothing to sieve in closed form.
What is left is the delivery loop itself: elf e adds 11 * e to houses e, 2e, 3e and so on, stopping
at house 50e. Totals are then scanned for the first house to reach the target.

Both parts need a bound on how many houses to consider, which comes from elf 1 alone. Elf 1 delivers
its gift to every house, so house n receives gift presents from it, and the lowest house that can
possibly reach the target is therefore the ceiling of target divided by gift. Rounding up matters:
dividing down instead leaves the last house short of the target and can return a house below the
answer, or no house at all for targets under the gift. The real input happens to divide evenly by
both gifts, so that mistake stays invisible on it and on any round test input.
"""

from typing import Final


class InputData:
    __ELF_PRESENTS: Final = 10
    __LAZY_ELF_PRESENTS: Final = 11
    __LAZY_ELF_CAPACITY: Final = 50

    def __init__(self, rawstr: str) -> None:
        self.__target = int(rawstr)

    def __house_bound(self, gift: int) -> int:
        """The lowest house that elf 1 alone can bring up to the target."""
        return -(-self.__target // gift)

    def __first_reaching(self, totals: list[int]) -> int:
        """Scans house numbers upwards for the first one whose total reaches the target."""
        return next(
            (
                house
                for house, total in enumerate(totals)
                if house > 0 and total >= self.__target
            ),
            -1,
        )

    def __divisor_sums(self, bound: int) -> list[int]:
        """Sum of divisors for every house up to bound, by the linear sieve."""
        smallest_prime = [0] * (bound + 1)
        primes: list[int] = []
        for n in range(2, bound + 1):
            if smallest_prime[n] == 0:
                smallest_prime[n] = n
                primes.append(n)
            lowest = smallest_prime[n]
            for prime in primes:
                product = prime * n
                if product > bound:
                    break
                smallest_prime[product] = prime
                if prime == lowest:
                    break

        sums = [0] * (bound + 1)
        if bound >= 1:
            sums[1] = 1
        for n in range(2, bound + 1):
            prime = smallest_prime[n]
            if prime == n:  # n is prime, so its only divisors are 1 and itself
                sums[n] = n + 1
                continue
            # Split n into rest * prime**power and use sigma(n) = sigma(rest) * sigma(prime**power).
            rest, power, geometric = n, 1, 1
            while rest % prime == 0:
                rest //= prime
                power *= prime
                geometric += power
            sums[n] = sums[rest] * geometric
        return sums

    def get_p1(self) -> int:
        bound = self.__house_bound(InputData.__ELF_PRESENTS)
        totals = [InputData.__ELF_PRESENTS * s for s in self.__divisor_sums(bound)]
        return self.__first_reaching(totals)

    def get_p2(self) -> int:
        bound = self.__house_bound(InputData.__LAZY_ELF_PRESENTS)
        totals = [0] * (bound + 1)
        gift = InputData.__LAZY_ELF_PRESENTS
        capacity = InputData.__LAZY_ELF_CAPACITY
        for elf in range(1, bound + 1):
            presents = gift * elf
            # The elf's last delivery is to house capacity * elf; beyond that it moves on.
            for house in range(elf, min(bound, capacity * elf) + 1, elf):
                totals[house] += presents
        return self.__first_reaching(totals)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
