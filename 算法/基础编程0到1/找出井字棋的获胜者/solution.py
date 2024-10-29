class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        matrix=[[6,1,8],[7,5,3],[2,9,4]]
        A,B=[],[]
        
        action=0
        while action<len(moves):
            if action%2==0:
                A.append(matrix[moves[action][0]][moves[action][1]])
                #print(A)
                if self.judgement(A):
                    return 'A'
            else:
                B.append(matrix[moves[action][0]][moves[action][1]])
                #print(B)
                if self.judgement(B):
                    return 'B'
            action+=1
        
        if len(moves)<9:
            return 'Pending'
        else:
            return "Draw"

    def judgement(self,n):
        if len(n)<3:
            return False
        for i in range(len(n)-2):
            for j in range(i+1,len(n)-1):
                for k in range(j+1,len(n)):
                    if n[i]+n[j]+n[k]==15:
                        #print(n[i],n[j],n[k])
                        return True
        return False