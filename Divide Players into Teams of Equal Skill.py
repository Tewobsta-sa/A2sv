class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        total = 0
        i = 0
        j = n - 1
        
        target = skill[i] + skill[j]

        while i < j:

            if skill[i] + skill[j] == target:
                total += skill[i] * skill[j]
                j -= 1
                i += 1
            else:
                return -1

        return total
