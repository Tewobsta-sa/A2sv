class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        i = 0
        ch = []
        while i < len(command):
            if command[i] == "G":
                ch.append("G")
                i += 1
            elif command[i:i+2] == "()":
                    ch.append("o")
                    i += 2
            else:
                ch.append("al")
                i += 4
        return ''.join(ch)
