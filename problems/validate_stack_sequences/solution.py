class Solution:

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        my_res = []

        for i in pushed:

            my_res.append(i)

            while my_res and my_res[-1] == popped[0]:

                popped = popped[1:]

                my_res.pop()

        return (my_res) == []
        