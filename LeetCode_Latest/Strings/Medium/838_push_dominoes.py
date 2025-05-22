# https://leetcode.com/problems/push-dominoes/description/

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Every 'R' pushes force to the right, which decays as you go further right
        # Every 'L' pushes force to the left, which decays as you go further left
        # At each index, you compute the net force:
        # Positive = right push wins → 'R'
        # Negative = left push wins → 'L'
        # Zero = balanced → '.'

        # Time: O(n) - have to iterate through the entire string
        # Space: O(n) - force array

        n = len(dominoes)
        forces = [0] * n

        # Step 1: apply rightward force
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n  # large force
            elif dominoes[i] == 'L':
                force = 0  # left cancels right
            else:
                # Why this works
                # influence of a falling domino fades as we move away from the source.
                # In real life: farther dominoes feel less force from a pushing domino.
                # Here, we're modeling that with:
                force = max(force - 1, 0)
            forces[i] += force

        # Step 2: apply leftward force
        force = 0
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        # Step 3: build result
        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')

        return ''.join(result)