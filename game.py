face1 = [[1,1,1],[1,1,1],[1,1,1]]
face2 = [[2,2,2],[2,2,2],[2,2,2]]
face3 = [[3,3,3],[3,3,3],[3,3,3]]
face4 = [[4,4,4],[4,4,4],[4,4,4]]
face5 = [[5,5,5],[5,5,5],[5,5,5]]
face6 = [[6,6,6],[6,6,6],[6,6,6]]
faces = [face1,face2,face3,face4,face5,face6]

print('GAME START')
print('----------')
print('key:')
print('column (1-9) - #')
print('up (u) - down (d)')
print('left (l) - right (r)')

print('Syntax: column|direction   ex)3u')
print('--------------------------------')
print('          ',face1[0][0],' ',face1[0][1],' ',face1[0][2])
print('          ',face1[1][0],' ',face1[1][1],' ',face1[1][2])
print('          ',face1[2][0],' ',face1[2][1],' ',face1[2][2])
print(face2[0][0],' ',face2[0][1],' ',face2[0][2],'',face3[0][0],' ',face3[0][1],' ',face3[0][2],'',face4[0][0],' ',face4[0][1],' ',face4[0][2])
print(face2[1][0],' ',face2[1][1],' ',face2[1][2],'',face3[1][0],' ',face3[1][1],' ',face3[1][2],'',face4[1][0],' ',face4[1][1],' ',face4[1][2])
print(face2[2][0],' ',face2[2][1],' ',face2[2][2],'',face3[2][0],' ',face3[2][1],' ',face3[2][2],'',face4[2][0],' ',face4[2][1],' ',face4[2][2])
print('          ',face5[0][0],' ',face5[0][1],' ',face5[0][2])
print('          ',face5[1][0],' ',face5[1][1],' ',face5[1][2])
print('          ',face5[2][0],' ',face5[2][1],' ',face5[2][2])
print('          ',face6[0][0],' ',face6[0][1],' ',face6[0][2])
print('          ',face6[1][0],' ',face6[1][1],' ',face6[1][2])
print('          ',face6[2][0],' ',face6[2][1],' ',face6[2][2])
print('--------------------------------')

move = input('Move: ')
#if function = '1w'
