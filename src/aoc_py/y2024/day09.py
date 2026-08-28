"""
2024 day 9 - Disk Fragmenter
"""

class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__diskmap = [int(c) for c in rawstr]

    def get_p1(self) -> int:
        left_idx = 0
        right_idx = len(self.__diskmap) - 1
        if right_idx % 2 == 1:
            right_idx -= 1
        right_counter = self.__diskmap[right_idx]
        target_idx = 0
        checksum = 0
        buffer = self.__diskmap[left_idx]
        while right_idx >= left_idx:
            if buffer > 0:
                if left_idx % 2 == 0:
                    buffer -= 1
                    checksum += target_idx * left_idx // 2
                    target_idx += 1
                elif right_counter > 0:
                    buffer -= 1
                    right_counter -= 1
                    checksum += target_idx * right_idx // 2
                    target_idx += 1
                else:
                    right_idx -= 2
                    right_counter = self.__diskmap[right_idx]
            else:
                left_idx += 1
                buffer = right_counter if left_idx == right_idx else self.__diskmap[left_idx]
        return checksum

    def get_p2(self) -> int:
        emptyblocks: list[tuple[int, int]] = []
        mempos = 0
        for i, v in enumerate(self.__diskmap):
            if i % 2 == 1 and v > 0:
                emptyblocks.append((mempos, v))
            mempos += v
        checksum = 0
        for memid, memlen in reversed(list(enumerate(self.__diskmap))):
            # Note: the memory id is actually half the index, so divide memid by 2 later when used
            mempos -= memlen
            if memid % 2 == 0:
                moved = False
                for eidx, (e_start, e_len) in enumerate(emptyblocks):
                    if e_start >= mempos:
                        break
                    if e_len >= memlen:
                        checksum += sum([i * memid // 2 for i in range(e_start, e_start + memlen)])
                        if e_len - memlen > 0:
                            emptyblocks[eidx] = e_start + memlen, e_len - memlen
                        else:
                            _ = emptyblocks.pop(eidx)
                        moved = True
                        break
                if not moved:
                    checksum += sum([i * memid // 2 for i in range(mempos, mempos + memlen)])
        return checksum


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
        p1, p2 = "-1"
        p = InputData(inputdata)
        if part in (None, 1):
            p1 = str(p.get_p1())
        if part in (None, 2):
            p2 = str(p.get_p2())

        return p1, p2
