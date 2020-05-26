    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        rows_A = len(A)
        rows_B = len(B)
        cols_A = len(A[0])
        cols_B = len(B[0])
        
        product = [[0 for col in range(cols_B)] for row in range(rows_A)]
        
        for row in range(rows_A):
            for col in range(cols_B):
                sum = 0
                for num in range(cols_A):
                    sum += A[row][col] * B[col][num]
                product[row][col] = sum
        
        
        return product