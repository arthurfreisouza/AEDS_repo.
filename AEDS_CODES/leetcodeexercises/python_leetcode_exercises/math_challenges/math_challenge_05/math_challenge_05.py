def generate_anti_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    
    num = n * n
    row_start, row_end, col_start, col_end = 0, n - 1, 0, n - 1
    
    while row_start <= row_end and col_start <= col_end:
        for i in range(row_start, row_end + 1):
            matrix[i][col_start] = num
            num -= 1
        col_start += 1
        
        for i in range(col_start, col_end + 1):
            matrix[row_end][i] = num
            num -= 1
        row_end -= 1
        
        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                matrix[i][col_end] = num
                num -= 1
            col_end -= 1
            
        if row_start <= row_end:
            for i in range(col_end, col_start - 1, -1):
                matrix[row_start][i] = num
                num -= 1
            row_start += 1
    
    return matrix

# Gerar e imprimir a matriz anti-espiral
anti_spiral_matrix = generate_anti_spiral_matrix(1001)
#for row in anti_spiral_matrix:
#    print(row)


total_sum_1 = 0
for i in range(1001):
    total_sum_1 = total_sum_1 + anti_spiral_matrix[i][i]



total_sum_2 = 0
for i in range(1001):
    #print(i)
    total_sum_2 = total_sum_2 + anti_spiral_matrix[i][1000 - i]

print(total_sum_1)
print(total_sum_2)
print(' The sum is {}'.format(total_sum_1 + total_sum_2))

