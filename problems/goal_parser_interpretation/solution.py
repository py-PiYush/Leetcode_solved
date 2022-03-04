class Solution:
    def interpret(self, command: str) -> str:
        ans, i = [], 0
        while i < len(command):
            c = command[i]
            if c == 'G':
                ans += [c]
                i += 1
            elif c == '(' and command[i + 1] == ')':
                ans += ['o']
                i += 2
            else:
                ans += ['al']
                i += 4
        return ''.join(ans)
    
        ''' 1-liner'''
        return command.replace('()', 'o').replace('(al)', 'al')