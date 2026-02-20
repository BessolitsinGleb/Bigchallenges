#python3 cont_terminal_prototype.py
import numpy as np
import copy

data= [     
    [[1, 2, 3],         #1                   
     [4, 5, 6],         #2
     [7, 8, 9],         #3
     [208, 29, 30],
     [31, 32, 33],
     [34, 35, 36],
     [37, 38, 39],
     [40, 41, 42],
     [43, 44, 45],
     [46, 47, 48],
     [49, 50, 51],
     [52, 53, 54],
     [55, 56, 57],
     [58, 59, 60],
     [61, 62, 63],
     [64, 65, 66],
     [67, 68, 69],
     [70, 71, 72],
     [73, 74, 75],
     [76, 77, 78],
     [79, 80, 81],
     [82, 83, 84],
     [85, 86, 87],
     [88, 89, 90],
     [91, 92, 93],
     [94, 95, 96],
     [97, 98, 99],
     [100, 101, 102],
     [103, 104, 105],
     [106, 107, 108]],   #30  слой A 
#     X    Y    Z
     [[11, 12, 13],      #1
     [14, 15, 16],       #2
     [17, 18, 19],
     [128, 129, 130],
     [0, 132, 133],
     [134, 135, 136],
     [137, 138, 139],
     [140, 0, 142],
     [143, 144, 145],
     [0, 147, 148],
     [149, 150, 151],
     [152, 153, 154],
     [155, 0, 157],
     [158, 159, 160],
     [161, 162, 163],
     [164, 165, 166],
     [167, 168, 169],
     [170, 171, 172],
     [0, 174, 175],
     [176, 177, 178],
     [179, 180, 181],
     [182, 183, 0],
     [185, 186, 187],
     [188, 189, 190],
     [191, 0, 193],
     [194, 195, 196],
     [197, 198, 199],
     [0, 1101, 1102],
     [1103, 1104, 1105],
     [1106, 0, 1108]],   #30 слой B
#     X    Y    Z
     [[21, 22, 23],      #1
     [24, 25, 26],       #2
     [27, 28, 29],
     [228, 229, 230],
     [0, 232, 233],
     [0, 235, 236],
     [237, 238, 239],
     [240, 0, 242],
     [243, 244, 245],
     [0, 247, 248],
     [249, 250, 251],
     [252, 253, 254],
     [255, 0, 257],
     [258, 259, 260],
     [261, 262, 263],
     [264, 265, 266],
     [267, 268, 269],
     [0, 271, 272],
     [0, 274, 275],
     [276, 277, 278],
     [279, 280, 281],
     [282, 283, 0],
     [285, 286, 287],
     [288, 289, 290],
     [291, 0, 293],
     [294, 295, 296],
     [297, 298, 299],
     [0, 2101, 2102],
     [2103, 2104, 2105],
     [2106, 0, 2108]]    #30 слой C           
]    # X    Y   Z                                                                        
                                                                 

project_1= np.array(data)

A= project_1[0]                                               #СЛОИ
B= project_1[1]
C= project_1[2]

n1= [A[0], B[0], C[0]]                                      #РЯДЫ          
n1= np.array(n1)
n1= n1.astype(int)
n1= n1.tolist()
n1= np.array(n1)

n2= [A[1], B[1], C[1]]
n2= np.array(n2)
n2= n2.astype(int)
n2= n2.tolist()
n2= np.array(n2)

n3= [A[2], B[2], C[2]]
n3= np.array(n3)
n3= n3.astype(int)
n3= n3.tolist()
n3= np.array(n3)
#print(n1)
#print(n2)
#print(n3)

n4= [A[3], B[3], C[3]]
n4= np.array(n4)
n4= n4.astype(int)
n4= n4.tolist()
n4= np.array(n4)

n5= [A[4], B[4], C[4]]
n5= np.array(n5)
n5= n5.astype(int)
n5= n5.tolist()
n5= np.array(n5)

n6= [A[5], B[5], C[5]]
n6= np.array(n6)
n6= n6.astype(int)
n6= n6.tolist()
n6= np.array(n6)

n7= [A[6], B[6], C[6]]
n7= np.array(n7)
n7= n7.astype(int)
n7= n7.tolist()
n7= np.array(n7)

n8= [A[7], B[7], C[7]]
n8= np.array(n8)
n8= n8.astype(int)
n8= n8.tolist()
n8= np.array(n8)

n9= [A[8], B[8], C[8]]
n9= np.array(n9)
n9= n9.astype(int)
n9= n9.tolist()
n9= np.array(n9)

n10= [A[9], B[9], C[9]]
n10= np.array(n10)
n10= n10.astype(int)
n10= n10.tolist()
n10= np.array(n10)

n11= [A[10], B[10], C[10]]
n11= np.array(n11)
n11= n11.astype(int)
n11= n11.tolist()
n11= np.array(n11)

n12= [A[11], B[11], C[11]]
n12= np.array(n12)
n12= n12.astype(int)
n12= n12.tolist()
n12= np.array(n12)

n13= [A[12], B[12], C[12]]
n13= np.array(n13)
n13= n13.astype(int)
n13= n13.tolist()
n13= np.array(n13)

n14= [A[13], B[13], C[13]]
n14= np.array(n14)
n14= n14.astype(int)
n14= n14.tolist()
n14= np.array(n14)

n15= [A[14], B[14], C[14]]
n15= np.array(n15)
n15= n15.astype(int)
n15= n15.tolist()
n15= np.array(n15)

n16= [A[15], B[15], C[15]]
n16= np.array(n16)
n16= n16.astype(int)
n16= n16.tolist()
n16= np.array(n16)

n17= [A[16], B[16], C[16]]
n17= np.array(n17)
n17= n17.astype(int)
n17= n17.tolist()
n17= np.array(n17)

n18= [A[17], B[17], C[17]]
n18= np.array(n18)
n18= n18.astype(int)
n18= n18.tolist()
n18= np.array(n18)

n19= [A[18], B[18], C[18]]
n19= np.array(n19)
n19= n19.astype(int)
n19= n19.tolist()
n19= np.array(n19)

n20= [A[19], B[19], C[19]]
n20= np.array(n20)
n20= n20.astype(int)
n20= n20.tolist()
n20= np.array(n20)

n21= [A[20], B[20], C[20]]
n21= np.array(n21)
n21= n21.astype(int)
n21= n21.tolist()
n21= np.array(n21)

n22= [A[21], B[21], C[21]]
n22= np.array(n22)
n22= n22.astype(int)
n22= n22.tolist()
n22= np.array(n22)

n23= [A[22], B[22], C[22]]
n23= np.array(n23)
n23= n23.astype(int)
n23= n23.tolist()
n23= np.array(n23)

n24= [A[23], B[23], C[23]]
n24= np.array(n24)
n24= n24.astype(int)
n24= n24.tolist()
n24= np.array(n24)

n25= [A[24], B[24], C[24]]
n25= np.array(n25)
n25= n25.astype(int)
n25= n25.tolist()
n25= np.array(n25)

n26= [A[25], B[25], C[25]]
n26= np.array(n26)
n26= n26.astype(int)
n26= n26.tolist()
n26= np.array(n26)

n27= [A[26], B[26], C[26]]
n27= np.array(n27)
n27= n27.astype(int)
n27= n27.tolist()
n27= np.array(n27)

n28= [A[27], B[27], C[27]]
n28= np.array(n28)
n28= n28.astype(int)
n28= n28.tolist()
n28= np.array(n28)

n29= [A[28], B[28], C[28]]
n29= np.array(n29)
n29= n29.astype(int)
n29= n29.tolist()
n29= np.array(n29)

n30= [A[29], B[29], C[29]]
n30= np.array(n30)
n30= n30.astype(int)
n30= n30.tolist()
n30= np.array(n30)

def xabc(project_1):             
    x= []
    for n in n1:
        x.append(n[0])
    for j in n2:
        x.append(j[0])
    for i in n3:
        x.append(i[0])
    for nn in n4:
        x.append(nn[0])
    for jj in n5:
        x.append(jj[0])
    for ii in n6:
        x.append(ii[0])
    for nq in n7:
        x.append(nq[0])
    for jq in n8:
        x.append(jq[0])
    for iq in n9:
        x.append(iq[0])
    for nw in n10:
        x.append(nw[0])
    for jw in n11:
        x.append(jw[0])
    for iw in n12:
        x.append(iw[0])
    for ne in n13:
        x.append(ne[0])
    for je in n14:
        x.append(je[0])
    for ie in n15:
        x.append(ie[0])
    for nne in n16:
        x.append(nne[0])
    for jje in n17:
        x.append(jje[0])
    for iie in n18:
        x.append(iie[0])
    for nqe in n19:
        x.append(nqe[0])
    for jqe in n20:
        x.append(jqe[0])
    for iqe in n21:
        x.append(iqe[0])
    for nwe in n22:
        x.append(nwe[0])
    for jwe in n23:
        x.append(jwe[0])
    for iwe in n24:
        x.append(iwe[0])
    for nqea in n25:
        x.append(nqea[0])
    for jqea in n26:
        x.append(jqea[0])
    for iqea in n27:
        x.append(iqea[0])
    for nwea in n28:
        x.append(nwea[0])
    for jwea in n29:
        x.append(jwea[0])
    for iwea in n30:
        x.append(iwea[0])
    return x

X= xabc(project_1)
X= np.array(X)
X= X.astype(int)
X= X.tolist()
X= np.array(X)
#print(X)

def yabc(project_1):
    y= []
    for n in n1:
        y.append(n[1])
    for j in n2:
        y.append(j[1])
    for i in n3:
        y.append(i[1])
    for nn in n4:
        y.append(nn[1])
    for jj in n5:
        y.append(jj[1])
    for ii in n6:
        y.append(ii[1])
    for nq in n7:
        y.append(nq[1])
    for jq in n8:
        y.append(jq[1])
    for iq in n9:
        y.append(iq[1])
    for nw in n10:
        y.append(nw[1])
    for jw in n11:
        y.append(jw[1])
    for iw in n12:
        y.append(iw[1])
    for ne in n13:
        y.append(ne[1])
    for je in n14:
        y.append(je[1])
    for ie in n15:
        y.append(ie[1])
    for nne in n16:
        y.append(nne[1])
    for jje in n17:
        y.append(jje[1])
    for iie in n18:
        y.append(iie[1])
    for nqe in n19:
        y.append(nqe[1])
    for jqe in n20:
        y.append(jqe[1])
    for iqe in n21:
        y.append(iqe[1])
    for nwe in n22:
        y.append(nwe[1])
    for jwe in n23:
        y.append(jwe[1])
    for iwe in n24:
        y.append(iwe[1])
    for nqea in n25:
        y.append(nqea[1])
    for jqea in n26:
        y.append(jqea[1])
    for iqea in n27:
        y.append(iqea[1])
    for nwea in n28:
        y.append(nwea[1])
    for jwea in n29:
        y.append(jwea[1])
    for iwea in n30:
        y.append(iwea[1])
    return y

Y= yabc(project_1)
Y= np.array(Y)
Y= Y.astype(int)
Y= Y.tolist()
Y= np.array(Y)
#print(Y)

def zabc(project_1):
    z= []
    for n in n1:
        z.append(n[2])
    for j in n2:
        z.append(j[2])
    for i in n3:
        z.append(i[2])
    for nn in n4:
        z.append(nn[2])
    for jj in n5:
        z.append(jj[2])
    for ii in n6:
        z.append(ii[2])
    for nq in n7:
        z.append(nq[2])
    for jq in n8:
        z.append(jq[2])
    for iq in n9:
        z.append(iq[2])
    for nw in n10:
        z.append(nw[2])
    for jw in n11:
        z.append(jw[2])
    for iw in n12:
        z.append(iw[2])
    for ne in n13:
        z.append(ne[2])
    for je in n14:
        z.append(je[2])
    for ie in n15:
        z.append(ie[2])
    for nne in n16:
        z.append(nne[2])
    for jje in n17:
        z.append(jje[2])
    for iie in n18:
        z.append(iie[2])
    for nqe in n19:
        z.append(nqe[2])
    for jqe in n20:
        z.append(jqe[2])
    for iqe in n21:
        z.append(iqe[2])
    for nwe in n22:
        z.append(nwe[2])
    for jwe in n23:
        z.append(jwe[2])
    for iwe in n24:
        z.append(iwe[2])
    for nqea in n25:
        z.append(nqea[2])
    for jqea in n26:
        z.append(jqea[2])
    for iqea in n27:
        z.append(iqea[2])
    for nwea in n28:
        z.append(nwea[2])
    for jwea in n29:
        z.append(jwea[2])
    for iwea in n30:
        z.append(iwea[2])
    return z

Z= zabc(project_1)
Z= np.array(Z)
Z= Z.astype(int)
Z= Z.tolist()
Z= np.array(Z)
#print(Z)

AX1= A[np.isin(A, X)]                           # упрощенный пример поиска ячеек в перменных А данные о контейнерах в этом слое, в перменной Х 
AX1= AX1[np.isin(AX1, n1)]                      # все данные о контейнерах в этой колонне, а в н1 все контейнера из первого ряда. Методами пересечений множеств находится ячейка 

def abc(cont_num):                              #слой
        correct_layer= None
        cell_a= A[np.isin(cont_num, A)]
        cell_b= B[np.isin(cont_num, B)]
        cell_c= C[np.isin(cont_num, C)]
        
        if len(cell_a)>(len(cell_b)+len(cell_c)):
            correct_layer= 'A'
        elif len(cell_b)>(len(cell_a)+len(cell_c)):
            correct_layer= 'B'
        elif len(cell_c)>(len(cell_b)+len(cell_a)):
            correct_layer= 'C'
        else:
            correct_layer= '0'
        
        return correct_layer

def xyz(cont_num):                              #столбец
        correct_layer= None
        cell_x= X[np.isin(cont_num, X)]
        cell_y= Y[np.isin(cont_num, Y)]
        cell_z= Z[np.isin(cont_num, Z)]
        
        if len(cell_x)>(len(cell_y)+len(cell_z)):
            correct_layer= 'X'
        elif len(cell_y)>(len(cell_x)+len(cell_z)):
            correct_layer= 'Y'
        elif len(cell_z)>(len(cell_y)+len(cell_x)):
            correct_layer= 'Z'
        else:
            correct_layer= '0'
        
        return correct_layer

def n123(cont_num):                              #ряды     
        correct_layer= None
        cell_1= n1[np.isin(cont_num, n1)]
        cell_2= n2[np.isin(cont_num, n2)]
        cell_3= n3[np.isin(cont_num, n3)]
        cell_4= n4[np.isin(cont_num, n4)]
        cell_5= n5[np.isin(cont_num, n5)]
        cell_6= n6[np.isin(cont_num, n6)]
        cell_7= n7[np.isin(cont_num, n7)]
        cell_8= n8[np.isin(cont_num, n8)]
        cell_9= n9[np.isin(cont_num, n9)]
        cell_10= n10[np.isin(cont_num, n10)]
        cell_11= n11[np.isin(cont_num, n11)]
        cell_12= n12[np.isin(cont_num, n12)]
        cell_13= n13[np.isin(cont_num, n13)]
        cell_14= n14[np.isin(cont_num, n14)]
        cell_15= n15[np.isin(cont_num, n15)]
        cell_16= n16[np.isin(cont_num, n16)]
        cell_17= n17[np.isin(cont_num, n17)]
        cell_18= n18[np.isin(cont_num, n18)]
        cell_19= n19[np.isin(cont_num, n19)]
        cell_20= n20[np.isin(cont_num, n20)]
        cell_21= n21[np.isin(cont_num, n21)]
        cell_22= n22[np.isin(cont_num, n22)]
        cell_23= n23[np.isin(cont_num, n23)]
        cell_24= n24[np.isin(cont_num, n24)]
        cell_25= n25[np.isin(cont_num, n25)]
        cell_26= n26[np.isin(cont_num, n26)]
        cell_27= n27[np.isin(cont_num, n27)]
        cell_28= n28[np.isin(cont_num, n28)]
        cell_29= n29[np.isin(cont_num, n29)]
        cell_30= n30[np.isin(cont_num, n30)]

        if len(cell_1)>(len(cell_2)+len(cell_3)):
            correct_layer= '1'
        elif len(cell_2)>(len(cell_1)+len(cell_3)):
            correct_layer= '2'
        elif len(cell_3)>(len(cell_2)+len(cell_1)):
            correct_layer= '3'
        elif len(cell_4)>(len(cell_2)+len(cell_1)):
            correct_layer= '4'
        elif len(cell_5)>(len(cell_2)+len(cell_1)):
            correct_layer= '5'
        elif len(cell_6)>(len(cell_2)+len(cell_1)):
            correct_layer= '6'
        elif len(cell_7)>(len(cell_2)+len(cell_1)):
            correct_layer= '7'
        elif len(cell_8)>(len(cell_2)+len(cell_1)):
            correct_layer= '8'
        elif len(cell_9)>(len(cell_2)+len(cell_1)):
            correct_layer= '9'
        elif len(cell_10)>(len(cell_2)+len(cell_1)):
            correct_layer= '10'
        elif len(cell_11)>(len(cell_2)+len(cell_1)):
            correct_layer= '11'
        elif len(cell_12)>(len(cell_2)+len(cell_1)):
            correct_layer= '12'
        elif len(cell_13)>(len(cell_2)+len(cell_1)):
            correct_layer= '13'
        elif len(cell_14)>(len(cell_2)+len(cell_1)):
            correct_layer= '14'
        elif len(cell_15)>(len(cell_2)+len(cell_1)):
            correct_layer= '15'
        elif len(cell_16)>(len(cell_2)+len(cell_1)):
            correct_layer= '16'
        elif len(cell_17)>(len(cell_2)+len(cell_1)):
            correct_layer= '17'
        elif len(cell_18)>(len(cell_2)+len(cell_1)):
            correct_layer= '18'
        elif len(cell_19)>(len(cell_2)+len(cell_1)):
            correct_layer= '19'
        elif len(cell_20)>(len(cell_2)+len(cell_1)):
            correct_layer= '20'
        elif len(cell_21)>(len(cell_2)+len(cell_1)):
            correct_layer= '21'
        elif len(cell_22)>(len(cell_2)+len(cell_1)):
            correct_layer= '22'
        elif len(cell_23)>(len(cell_2)+len(cell_1)):
            correct_layer= '23'
        elif len(cell_24)>(len(cell_2)+len(cell_1)):
            correct_layer= '24'
        elif len(cell_25)>(len(cell_2)+len(cell_1)):
            correct_layer= '25'
        elif len(cell_26)>(len(cell_2)+len(cell_1)):
            correct_layer= '26'
        elif len(cell_27)>(len(cell_2)+len(cell_1)):
            correct_layer= '27'
        elif len(cell_28)>(len(cell_2)+len(cell_1)):
            correct_layer= '28'
        elif len(cell_29)>(len(cell_2)+len(cell_1)):
            correct_layer= '29'
        elif len(cell_30)>(len(cell_2)+len(cell_1)):
            correct_layer= '30'
        else:
            correct_layer= '0'
        
        return correct_layer
    
def fhlfc(bot_cell): 
        empty= None
        b_cell= copy.deepcopy(bot_cell)               #B
        c_cell= copy.deepcopy(bot_cell)               #C
        for i in bot_cell:
            if bot_cell[0]=='A':
                b_cell[0]='B'
                c_cell[0]='C'
                return (f'{''.join(b_cell)}, {''.join(c_cell)}')
            elif bot_cell[0]=='B':
                c_cell[0]='C'
                return ''.join(c_cell)
            elif bot_cell[0]=='C':
                empty= 'No containers were found above'
                return empty
            else:
                return 'There is no container in the database'

def empty_cell_hc(bot_cell, list_h_cell):   
        hb= None
        hc= None
        if bot_cell== '000':
            return 'container not found'
        
        if len(list_h_cell)>3:                     
            cell_b= list_h_cell[:3]                 
            cell_b[0]=B

            if cell_b[1]=='X':          #XYZ                
                cell_b[1]=X                                 
            elif cell_b[1]=='Y':
                cell_b[1]=Y
            elif cell_b[1]=='Z':
                cell_b[1]=Z
            if cell_b[2]=='1':          #n1n2n3
                cell_b[2]=n1
            elif cell_b[2]=='2':
                cell_b[2]=n2
            elif cell_b[2]=='3':
                cell_b[2]=n3
            elif cell_b[2]=='4':
                cell_b[2]=n4
            elif cell_b[2]=='5':
                cell_b[2]=n5
            elif cell_b[2]=='6':
                cell_b[2]=n6
            elif cell_b[2]=='7':
                cell_b[2]=n7
            elif cell_b[2]=='8':
                cell_b[2]=n8    
            elif cell_b[2]=='9':
                cell_b[2]=n9
            elif cell_b[2]=='10':
                cell_b[2]=n10
            elif cell_b[2]=='11':
                cell_b[2]=n11
            elif cell_b[2]=='12':
                cell_b[2]=n12
            elif cell_b[2]=='13':
                cell_b[2]=n13
            elif cell_b[2]=='14':
                cell_b[2]=n14
            elif cell_b[2]=='15':
                cell_b[2]=n15
            elif cell_b[2]=='16':
                cell_b[2]=n16
            elif cell_b[2]=='17':
                cell_b[2]=n17
            elif cell_b[2]=='18':
                cell_b[2]=n18
            elif cell_b[2]=='19':
                cell_b[2]=n19
            elif cell_b[2]=='20':
                cell_b[2]=n20
            elif cell_b[2]=='21':
                cell_b[2]=n21
            elif cell_b[2]=='22':
                cell_b[2]=n22
            elif cell_b[2]=='23':
                cell_b[2]=n23
            elif cell_b[2]=='24':
                cell_b[2]=n24
            elif cell_b[2]=='25':
                cell_b[2]=n25
            elif cell_b[2]=='26':
                cell_b[2]=n26
            elif cell_b[2]=='27':
                cell_b[2]=n27
            elif cell_b[2]=='28':
                cell_b[2]=n28
            elif cell_b[2]=='29':
                cell_b[2]=n29
            elif cell_b[2]=='30':
                cell_b[2]=n30

            hb= cell_b[0][np.isin(cell_b[0], cell_b[1])]
            hb= hb[np.isin(hb, cell_b[2])]

            cell_c= list_h_cell[-3:]               
            cell_c[0]=C
            
            if cell_c[1]=='X':          #XYZ                
                cell_c[1]=X                                 
            elif cell_c[1]=='Y':
                cell_c[1]=Y
            elif cell_c[1]=='Z':
                cell_c[1]=Z
            if cell_c[2]=='1':          #n1n2n3
                cell_c[2]=n1
            elif cell_c[2]=='2':
                cell_c[2]=n2
            elif cell_c[2]=='3':
                cell_c[2]=n3
            elif cell_c[2]=='4':
                cell_c[2]=n4
            elif cell_c[2]=='5':
                cell_c[2]=n5
            elif cell_c[2]=='6':
                cell_c[2]=n6
            elif cell_c[2]=='7':
                cell_c[2]=n7
            elif cell_c[2]=='8':
                cell_c[2]=n8    
            elif cell_c[2]=='9':
                cell_c[2]=n9
            elif cell_c[2]=='10':
                cell_c[2]=n10
            elif cell_c[2]=='11':
                cell_c[2]=n11
            elif cell_c[2]=='12':
                cell_c[2]=n12
            elif cell_c[2]=='13':
                cell_c[2]=n13
            elif cell_c[2]=='14':
                cell_c[2]=n14
            elif cell_c[2]=='15':
                cell_c[2]=n15
            elif cell_c[2]=='16':
                cell_c[2]=n16
            elif cell_c[2]=='17':
                cell_c[2]=n17
            elif cell_c[2]=='18':
                cell_c[2]=n18
            elif cell_c[2]=='19':
                cell_c[2]=n19
            elif cell_c[2]=='20':
                cell_c[2]=n20
            elif cell_c[2]=='21':
                cell_c[2]=n21
            elif cell_c[2]=='22':
                cell_c[2]=n22
            elif cell_c[2]=='23':
                cell_c[2]=n23
            elif cell_c[2]=='24':
                cell_c[2]=n24
            elif cell_c[2]=='25':
                cell_c[2]=n25
            elif cell_c[2]=='26':
                cell_c[2]=n26
            elif cell_c[2]=='27':
                cell_c[2]=n27
            elif cell_c[2]=='28':
                cell_c[2]=n28
            elif cell_c[2]=='29':
                cell_c[2]=n29
            elif cell_c[2]=='30':
                cell_c[2]=n30

            hc= cell_c[0][np.isin(cell_c[0], cell_c[1])]
            hc= hc[np.isin(hc, cell_c[2])]

            return (f'{hb}, {hc}')

        elif len(list_h_cell)>=3:
            cell_c= list_h_cell
            cell_c[0]=C

            if cell_c[1]=='X':          #XYZ                
                cell_c[1]=X                                 
            elif cell_c[1]=='Y':
                cell_c[1]=Y
            elif cell_c[1]=='Z':
                cell_c[1]=Z
            if cell_c[2]=='1':          #n1n2n3
                cell_c[2]=n1
            elif cell_c[2]=='2':
                cell_c[2]=n2
            elif cell_c[2]=='3':
                cell_c[2]=n3
            elif cell_c[2]=='4':
                cell_c[2]=n4
            elif cell_c[2]=='5':
                cell_c[2]=n5
            elif cell_c[2]=='6':
                cell_c[2]=n6
            elif cell_c[2]=='7':
                cell_c[2]=n7
            elif cell_c[2]=='8':
                cell_c[2]=n8    
            elif cell_c[2]=='9':
                cell_c[2]=n9
            elif cell_c[2]=='10':
                cell_c[2]=n10
            elif cell_c[2]=='11':
                cell_c[2]=n11
            elif cell_c[2]=='12':
                cell_c[2]=n12
            elif cell_c[2]=='13':
                cell_c[2]=n13
            elif cell_c[2]=='14':
                cell_c[2]=n14
            elif cell_c[2]=='15':
                cell_c[2]=n15
            elif cell_c[2]=='16':
                cell_c[2]=n16
            elif cell_c[2]=='17':
                cell_c[2]=n17
            elif cell_c[2]=='18':
                cell_c[2]=n18
            elif cell_c[2]=='19':
                cell_c[2]=n19
            elif cell_c[2]=='20':
                cell_c[2]=n20
            elif cell_c[2]=='21':
                cell_c[2]=n21
            elif cell_c[2]=='22':
                cell_c[2]=n22
            elif cell_c[2]=='23':
                cell_c[2]=n23
            elif cell_c[2]=='24':
                cell_c[2]=n24
            elif cell_c[2]=='25':
                cell_c[2]=n25
            elif cell_c[2]=='26':
                cell_c[2]=n26
            elif cell_c[2]=='27':
                cell_c[2]=n27
            elif cell_c[2]=='28':
                cell_c[2]=n28
            elif cell_c[2]=='29':
                cell_c[2]=n29
            elif cell_c[2]=='30':
                cell_c[2]=n30

            hc= cell_c[0][np.isin(cell_c[0], cell_c[1])]
            hc= hc[np.isin(hc, cell_c[2])]

            return (f'{hc}')

def cor_empty_cell_hc(h_cell):
        if len(h_cell)>5:
            h_cell= h_cell.replace('[', '')
            h_cell= h_cell.replace(']', '')
            h_cell= h_cell.replace(' 0', '')
            h_cell= h_cell.replace(' ', '')
            
            if len(h_cell)==0:
                h_cell= 'There are no containers above'
            return h_cell
        else:
            h_cell= h_cell.replace('[', '')
            h_cell= h_cell.replace(']', '')
            h_cell= h_cell.replace(' 0', '')
            h_cell= h_cell.replace(' ', '')
            
            if len(h_cell)==0:
                h_cell= 'There are no containers above'
            print(h_cell)
            return h_cell

def find_empty_cells(project_1):            
            a= A
            b= B
            c= C
            res_list= []

            for i in a:
                dubl_a_1= a[0]
                dubl_a_2= a[1]
                dubl_a_3= a[2]
                dubl_a_4= a[3]
                dubl_a_5= a[4]
                dubl_a_6= a[5]
                dubl_a_7= a[6]
                dubl_a_8= a[7]
                dubl_a_9= a[8]
                dubl_a_10= a[9]
                dubl_a_11= a[10]
                dubl_a_12= a[11]
                dubl_a_13= a[12]
                dubl_a_14= a[13]
                dubl_a_15= a[14]
                dubl_a_16= a[15]
                dubl_a_17= a[16]
                dubl_a_18= a[17]
                dubl_a_19= a[18]
                dubl_a_20= a[19]
                dubl_a_21= a[20]
                dubl_a_22= a[21]
                dubl_a_23= a[22]
                dubl_a_24= a[23]
                dubl_a_25= a[24]
                dubl_a_26= a[25]
                dubl_a_27= a[26]
                dubl_a_28= a[27]
                dubl_a_29= a[28]
                dubl_a_30= a[29]
                zero= 0
                dubl_a_1= [i for i, x in enumerate(dubl_a_1) if x == zero]    
                dubl_a_1= np.array(dubl_a_1)
                for a_1 in dubl_a_1:
                    ax1= dubl_a_1[np.isin(0, dubl_a_1)]
                    ay1= dubl_a_1[np.isin(1, dubl_a_1)]
                    az1= dubl_a_1[np.isin(2, dubl_a_1)]
                    if len(ax1)>=1:
                        res_list.append('AX1')
                    if len(ay1)>=1:
                        res_list.append('AY1')
                    if len(az1)>=1:
                        res_list.append('AZ1')

                dubl_a_2= [i for i, x in enumerate(dubl_a_2) if x == zero]   
                dubl_a_2= np.array(dubl_a_2)
                for a_2 in dubl_a_2:
                    ax2= dubl_a_2[np.isin(0, dubl_a_2)]
                    ay2= dubl_a_2[np.isin(1, dubl_a_2)]
                    az2= dubl_a_2[np.isin(2, dubl_a_3)]
                    if len(ax2)>=1:
                        res_list.append('AX2')
                    if len(ay2)>=1:
                        res_list.append('AY2')
                    if len(az2)>=1:
                        res_list.append('AZ2')

                dubl_a_3= [i for i, x in enumerate(dubl_a_3) if x == zero]    
                dubl_a_3= np.array(dubl_a_3)
                for a_3 in dubl_a_3:
                    ax3= dubl_a_3[np.isin(0, dubl_a_3)]
                    ay3= dubl_a_3[np.isin(1, dubl_a_3)]
                    az3= dubl_a_3[np.isin(2, dubl_a_3)]
                    if len(ax3)>=1:
                        res_list.append('AX3')
                    if len(ay3)>=1:
                        res_list.append('AY3')
                    if len(az3)>=1:
                        res_list.append('AZ3')

                dubl_a_4= [i for i, x in enumerate(dubl_a_4) if x == zero]   
                dubl_a_4= np.array(dubl_a_4)
                for a_4 in dubl_a_4:
                    ax4= dubl_a_4[np.isin(0, dubl_a_4)]
                    ay4= dubl_a_4[np.isin(1, dubl_a_4)]
                    az4= dubl_a_4[np.isin(2, dubl_a_4)]
                    if len(ax4)>=1:
                        res_list.append('AX4')
                    if len(ay4)>=1:
                        res_list.append('AY4')
                    if len(az4)>=1:
                        res_list.append('AZ4')

                dubl_a_5= [i for i, x in enumerate(dubl_a_5) if x == zero]    
                dubl_a_5= np.array(dubl_a_5)
                for a_5 in dubl_a_5:
                    ax5= dubl_a_5[np.isin(0, dubl_a_5)]
                    ay5= dubl_a_5[np.isin(1, dubl_a_5)]
                    az5= dubl_a_5[np.isin(2, dubl_a_5)]
                    if len(ax5)>=1:
                        res_list.append('AX5')
                    if len(ay5)>=1:
                        res_list.append('AY5')
                    if len(az5)>=1:
                        res_list.append('AZ5')   
                          
                dubl_a_6= [i for i, x in enumerate(dubl_a_6) if x == zero]  
                dubl_a_6= np.array(dubl_a_6)
                for a_6 in dubl_a_6:
                    ax6= dubl_a_6[np.isin(0, dubl_a_6)]
                    ay6= dubl_a_6[np.isin(1, dubl_a_6)]
                    az6= dubl_a_6[np.isin(2, dubl_a_6)]
                    if len(ax6)>=1:
                        res_list.append('AX6')
                    if len(ay6)>=1:
                        res_list.append('AY6')
                    if len(az6)>=1:
                        res_list.append('AZ6')     

                dubl_a_7= [i for i, x in enumerate(dubl_a_7) if x == zero]   
                dubl_a_7= np.array(dubl_a_7)
                for a_7 in dubl_a_7:
                    ax7= dubl_a_7[np.isin(0, dubl_a_7)]
                    ay7= dubl_a_7[np.isin(1, dubl_a_7)]
                    az7= dubl_a_7[np.isin(2, dubl_a_7)]
                    if len(ax7)>=1:
                        res_list.append('AX7')
                    if len(ay7)>=1:
                        res_list.append('AY7')
                    if len(az7)>=1:
                        res_list.append('AZ7')   

                dubl_a_8= [i for i, x in enumerate(dubl_a_8) if x == zero]    
                dubl_a_8= np.array(dubl_a_8)
                for a_8 in dubl_a_8:
                    ax8= dubl_a_8[np.isin(0, dubl_a_8)]
                    ay8= dubl_a_8[np.isin(1, dubl_a_8)]
                    az8= dubl_a_8[np.isin(2, dubl_a_8)]
                    if len(ax8)>=1:
                        res_list.append('AX8')
                    if len(ay8)>=1:
                        res_list.append('AY8')
                    if len(az8)>=1:
                        res_list.append('AZ8') 

                dubl_a_9= [i for i, x in enumerate(dubl_a_9) if x == zero]    
                dubl_a_9= np.array(dubl_a_9)
                for a_9 in dubl_a_9:
                    ax9= dubl_a_9[np.isin(0, dubl_a_9)]
                    ay9= dubl_a_9[np.isin(1, dubl_a_9)]
                    az9= dubl_a_9[np.isin(2, dubl_a_9)]
                    if len(ax9)>=1:
                        res_list.append('AX9')
                    if len(ay9)>=1:
                        res_list.append('AY9')
                    if len(az9)>=1:
                        res_list.append('AZ9')

                dubl_a_10= [i for i, x in enumerate(dubl_a_10) if x == zero]   
                dubl_a_10= np.array(dubl_a_10)
                for a_10 in dubl_a_10:
                    ax10= dubl_a_10[np.isin(0, dubl_a_10)]
                    ay10= dubl_a_10[np.isin(1, dubl_a_10)]
                    az10= dubl_a_10[np.isin(2, dubl_a_10)]
                    if len(ax10)>=1:
                        res_list.append('AX10')
                    if len(ay10)>=1:
                        res_list.append('AY10')
                    if len(az10)>=1:
                        res_list.append('AZ10')  

                dubl_a_11= [i for i, x in enumerate(dubl_a_11) if x == zero]    
                dubl_a_11= np.array(dubl_a_11)
                for a_11 in dubl_a_11:
                    ax11= dubl_a_11[np.isin(0, dubl_a_11)]
                    ay11= dubl_a_11[np.isin(1, dubl_a_11)]
                    az11= dubl_a_11[np.isin(2, dubl_a_11)]
                    if len(ax11)>=1:
                        res_list.append('AX11')
                    if len(ay11)>=1:
                        res_list.append('AY11')
                    if len(az11)>=1:
                        res_list.append('AZ11')    

                dubl_a_12= [i for i, x in enumerate(dubl_a_12) if x == zero]  
                dubl_a_12= np.array(dubl_a_12)
                for a_12 in dubl_a_12:
                    ax12= dubl_a_12[np.isin(0, dubl_a_12)]
                    ay12= dubl_a_12[np.isin(1, dubl_a_12)]
                    az12= dubl_a_12[np.isin(2, dubl_a_12)]
                    if len(ax12)>=1:
                        res_list.append('AX12')
                    if len(ay12)>=1:
                        res_list.append('AY12')
                    if len(az12)>=1:
                        res_list.append('AZ12')     

                dubl_a_13= [i for i, x in enumerate(dubl_a_13) if x == zero]  
                dubl_a_13= np.array(dubl_a_13)
                for a_13 in dubl_a_13:
                    ax13= dubl_a_13[np.isin(0, dubl_a_13)]
                    ay13= dubl_a_13[np.isin(1, dubl_a_13)]
                    az13= dubl_a_13[np.isin(2, dubl_a_13)]
                    if len(ax13)>=1:
                        res_list.append('AX13')
                    if len(ay13)>=1:
                        res_list.append('AY13')
                    if len(az13)>=1:
                        res_list.append('AZ13')        

                dubl_a_14= [i for i, x in enumerate(dubl_a_14) if x == zero]   
                dubl_a_14= np.array(dubl_a_14)
                for a_14 in dubl_a_14:
                    ax14= dubl_a_14[np.isin(0, dubl_a_14)]
                    ay14= dubl_a_14[np.isin(1, dubl_a_14)]
                    az14= dubl_a_14[np.isin(2, dubl_a_14)]
                    if len(ax14)>=1:
                        res_list.append('AX14')
                    if len(ay14)>=1:
                        res_list.append('AY14')
                    if len(az14)>=1:
                        res_list.append('AZ14')     

                dubl_a_15= [i for i, x in enumerate(dubl_a_15) if x == zero]    
                dubl_a_15= np.array(dubl_a_15)
                for a_15 in dubl_a_15:
                    ax15= dubl_a_15[np.isin(0, dubl_a_15)]
                    ay15= dubl_a_15[np.isin(1, dubl_a_15)]
                    az15= dubl_a_15[np.isin(2, dubl_a_15)]
                    if len(ax15)>=1:
                        res_list.append('AX15')
                    if len(ay15)>=1:
                        res_list.append('AY15')
                    if len(az15)>=1:
                        res_list.append('AZ15')               

                dubl_a_16= [i for i, x in enumerate(dubl_a_16) if x == zero]   
                dubl_a_16= np.array(dubl_a_16)
                for a_16 in dubl_a_16:
                    ax16= dubl_a_16[np.isin(0, dubl_a_16)]
                    ay16= dubl_a_16[np.isin(1, dubl_a_16)]
                    az16= dubl_a_16[np.isin(2, dubl_a_16)]
                    if len(ax16)>=1:
                        res_list.append('AX16')
                    if len(ay16)>=1:
                        res_list.append('AY16')
                    if len(az16)>=1:
                        res_list.append('AZ16')    

                dubl_a_17= [i for i, x in enumerate(dubl_a_17) if x == zero]   
                dubl_a_17= np.array(dubl_a_17)
                for a_17 in dubl_a_17:
                    ax17= dubl_a_17[np.isin(0, dubl_a_17)]
                    ay17= dubl_a_17[np.isin(1, dubl_a_17)]
                    az17= dubl_a_17[np.isin(2, dubl_a_17)]
                    if len(ax17)>=1:
                        res_list.append('AX17')
                    if len(ay17)>=1:
                        res_list.append('AY17')
                    if len(az17)>=1:
                        res_list.append('AZ17')        
                
                dubl_a_18= [i for i, x in enumerate(dubl_a_18) if x == zero]   
                dubl_a_18= np.array(dubl_a_18)
                for a_18 in dubl_a_18:
                    ax18= dubl_a_18[np.isin(0, dubl_a_18)]
                    ay18= dubl_a_18[np.isin(1, dubl_a_18)]
                    az18= dubl_a_18[np.isin(2, dubl_a_18)]
                    if len(ax18)>=1:
                        res_list.append('AX18')
                    if len(ay18)>=1:
                        res_list.append('AY18')
                    if len(az18)>=1:
                        res_list.append('AZ18')
                
                dubl_a_19= [i for i, x in enumerate(dubl_a_19) if x == zero]    #   A n
                dubl_a_19= np.array(dubl_a_19)
                for a_19 in dubl_a_19:
                    ax19= dubl_a_19[np.isin(0, dubl_a_19)]
                    ay19= dubl_a_19[np.isin(1, dubl_a_19)]
                    az19= dubl_a_19[np.isin(2, dubl_a_19)]
                    if len(ax19)>=1:
                        res_list.append('AX19')
                    if len(ay19)>=1:
                        res_list.append('AY19')
                    if len(az19)>=1:
                        res_list.append('AZ19')
                
                dubl_a_20= [i for i, x in enumerate(dubl_a_20) if x == zero]    #   A n
                dubl_a_20= np.array(dubl_a_20)
                for a_20 in dubl_a_20:
                    ax20= dubl_a_20[np.isin(0, dubl_a_20)]
                    ay20= dubl_a_20[np.isin(1, dubl_a_20)]
                    az20= dubl_a_20[np.isin(2, dubl_a_20)]
                    if len(ax20)>=1:
                        res_list.append('AX20')
                    if len(ay20)>=1:
                        res_list.append('AY20')
                    if len(az20)>=1:
                        res_list.append('AZ20')
                
                dubl_a_21= [i for i, x in enumerate(dubl_a_21) if x == zero]    #   A n
                dubl_a_21= np.array(dubl_a_21)
                for a_21 in dubl_a_21:
                    ax21= dubl_a_21[np.isin(0, dubl_a_21)]
                    ay21= dubl_a_21[np.isin(1, dubl_a_21)]
                    az21= dubl_a_21[np.isin(2, dubl_a_21)]
                    if len(ax21)>=1:
                        res_list.append('AX21')
                    if len(ay21)>=1:
                        res_list.append('AY21')
                    if len(az21)>=1:
                        res_list.append('AZ21')
                
                dubl_a_22= [i for i, x in enumerate(dubl_a_22) if x == zero]    #   A n
                dubl_a_22= np.array(dubl_a_22)
                for a_22 in dubl_a_22:
                    ax22= dubl_a_22[np.isin(0, dubl_a_22)]
                    ay22= dubl_a_22[np.isin(1, dubl_a_22)]
                    az22= dubl_a_22[np.isin(2, dubl_a_22)]
                    if len(ax22)>=1:
                        res_list.append('AX22')
                    if len(ay22)>=1:
                        res_list.append('AY22')
                    if len(az22)>=1:
                        res_list.append('AZ22')
                
                dubl_a_23= [i for i, x in enumerate(dubl_a_23) if x == zero]    #   A n
                dubl_a_23= np.array(dubl_a_23)
                for a_23 in dubl_a_23:
                    ax23= dubl_a_23[np.isin(0, dubl_a_23)]
                    ay23= dubl_a_23[np.isin(1, dubl_a_23)]
                    az23= dubl_a_23[np.isin(2, dubl_a_23)]
                    if len(ax23)>=1:
                        res_list.append('AX23')
                    if len(ay23)>=1:
                        res_list.append('AY23')
                    if len(az23)>=1:
                        res_list.append('AZ23')
                
                dubl_a_24= [i for i, x in enumerate(dubl_a_24) if x == zero]    #   A n
                dubl_a_24= np.array(dubl_a_24)
                for a_24 in dubl_a_24:
                    ax24= dubl_a_24[np.isin(0, dubl_a_24)]
                    ay24= dubl_a_24[np.isin(1, dubl_a_24)]
                    az24= dubl_a_24[np.isin(2, dubl_a_24)]
                    if len(ax24)>=1:
                        res_list.append('AX24')
                    if len(ay24)>=1:
                        res_list.append('AY24')
                    if len(az24)>=1:
                        res_list.append('AZ24')
                
                dubl_a_25= [i for i, x in enumerate(dubl_a_25) if x == zero]    #   A n
                dubl_a_25= np.array(dubl_a_25)
                for a_25 in dubl_a_25:
                    ax25= dubl_a_25[np.isin(0, dubl_a_25)]
                    ay25= dubl_a_25[np.isin(1, dubl_a_25)]
                    az25= dubl_a_25[np.isin(2, dubl_a_25)]
                    if len(ax25)>=1:
                        res_list.append('AX25')
                    if len(ay25)>=1:
                        res_list.append('AY25')
                    if len(az25)>=1:
                        res_list.append('AZ25')
                
                dubl_a_26= [i for i, x in enumerate(dubl_a_26) if x == zero]    #   A n
                dubl_a_26= np.array(dubl_a_26)
                for a_26 in dubl_a_26:
                    ax26= dubl_a_26[np.isin(0, dubl_a_26)]
                    ay26= dubl_a_26[np.isin(1, dubl_a_26)]
                    az26= dubl_a_26[np.isin(2, dubl_a_26)]
                    if len(ax26)>=1:
                        res_list.append('AX26')
                    if len(ay26)>=1:
                        res_list.append('AY26')
                    if len(az26)>=1:
                        res_list.append('AZ26')
                
                dubl_a_27= [i for i, x in enumerate(dubl_a_27) if x == zero]    #   A n
                dubl_a_27= np.array(dubl_a_27)
                for a_27 in dubl_a_27:
                    ax27= dubl_a_27[np.isin(0, dubl_a_27)]
                    ay27= dubl_a_27[np.isin(1, dubl_a_27)]
                    az27= dubl_a_27[np.isin(2, dubl_a_27)]
                    if len(ax27)>=1:
                        res_list.append('AX27')
                    if len(ay27)>=1:
                        res_list.append('AY27')
                    if len(az27)>=1:
                        res_list.append('AZ27')
                
                dubl_a_28= [i for i, x in enumerate(dubl_a_28) if x == zero]    #   A n
                dubl_a_28= np.array(dubl_a_28)
                for a_28 in dubl_a_28:
                    ax28= dubl_a_28[np.isin(0, dubl_a_28)]
                    ay28= dubl_a_28[np.isin(1, dubl_a_28)]
                    az28= dubl_a_28[np.isin(2, dubl_a_28)]
                    if len(ax28)>=1:
                        res_list.append('AX28')
                    if len(ay28)>=1:
                        res_list.append('AY28')
                    if len(az28)>=1:
                        res_list.append('AZ28')
                
                dubl_a_29= [i for i, x in enumerate(dubl_a_29) if x == zero]    #   A n
                dubl_a_29= np.array(dubl_a_29)
                for a_29 in dubl_a_29:
                    ax29= dubl_a_29[np.isin(0, dubl_a_29)]
                    ay29= dubl_a_29[np.isin(1, dubl_a_29)]
                    az29= dubl_a_29[np.isin(2, dubl_a_29)]
                    if len(ax29)>=1:
                        res_list.append('AX29')
                    if len(ay29)>=1:
                        res_list.append('AY29')
                    if len(az29)>=1:
                        res_list.append('AZ29')

                dubl_a_30= [i for i, x in enumerate(dubl_a_30) if x == zero]    #   A n
                dubl_a_30= np.array(dubl_a_30)
                for a_30 in dubl_a_30:
                    ax30= dubl_a_30[np.isin(0, dubl_a_30)]
                    ay30= dubl_a_30[np.isin(1, dubl_a_30)]
                    az30= dubl_a_30[np.isin(2, dubl_a_30)]
                    if len(ax30)>=1:
                        res_list.append('AX30')
                    if len(ay30)>=1:
                        res_list.append('AY30')
                    if len(az30)>=1:
                        res_list.append('AZ30')


            for j in b:
                dubl_b_1= b[0]
                dubl_b_2= b[1]
                dubl_b_3= b[2]
                dubl_b_4= b[3]
                dubl_b_5= b[4]
                dubl_b_6= b[5]
                dubl_b_7= b[6]
                dubl_b_8= b[7]
                dubl_b_9= b[8]
                dubl_b_10= b[9]
                dubl_b_11= b[10]
                dubl_b_12= b[11]
                dubl_b_13= b[12]
                dubl_b_14= b[13]
                dubl_b_15= b[14]
                dubl_b_16= b[15]
                dubl_b_17= b[16]
                dubl_b_18= b[17]
                dubl_b_19= b[18]
                dubl_b_20= b[19]
                dubl_b_21= b[20]
                dubl_b_22= b[21]
                dubl_b_23= b[22]
                dubl_b_24= b[23]
                dubl_b_25= b[24]
                dubl_b_26= b[25]
                dubl_b_27= b[26]
                dubl_b_28= b[27]
                dubl_b_29= b[28]
                dubl_b_30= b[29]
                zero= 0
                dubl_b_1= [i for i, x in enumerate(dubl_b_1) if x == zero]    #   A n1                      
                dubl_b_1= np.array(dubl_b_1)
                for b_1 in dubl_b_1:
                    bx1= dubl_b_1[np.isin(0, dubl_b_1)]
                    by1= dubl_b_1[np.isin(1, dubl_b_1)]
                    bz1= dubl_b_1[np.isin(2, dubl_b_1)]
                    if len(bx1)>=1:
                        res_list.append('BX1')
                    if len(by1)>=1:
                        res_list.append('BY1')
                    if len(bz1)>=1:
                        res_list.append('BZ1')

                dubl_b_2= [i for i, x in enumerate(dubl_b_2) if x == zero]    #   A n2
                dubl_b_2= np.array(dubl_b_2)
                for b_2 in dubl_b_2:
                    bx2= dubl_b_2[np.isin(0, dubl_b_2)]
                    by2= dubl_b_2[np.isin(1, dubl_b_2)]
                    bz2= dubl_b_2[np.isin(2, dubl_b_3)]
                    if len(bx2)>=1:
                        res_list.append('BX2')
                    if len(by2)>=1:
                        res_list.append('BY2')
                    if len(bz2)>=1:
                        res_list.append('BZ2')

                dubl_b_3= [i for i, x in enumerate(dubl_b_3) if x == zero]    #   A n
                dubl_b_3= np.array(dubl_b_3)
                for b_3 in dubl_b_3:
                    bx3= dubl_b_3[np.isin(0, dubl_b_3)]
                    by3= dubl_b_3[np.isin(1, dubl_b_3)]
                    bz3= dubl_b_3[np.isin(2, dubl_b_3)]
                    if len(bx3)>=1:
                        res_list.append('BX3')
                    if len(by3)>=1:
                        res_list.append('BY3')
                    if len(bz3)>=1:
                        res_list.append('BZ3')

                dubl_b_4= [i for i, x in enumerate(dubl_b_4) if x == zero]    #   A n
                dubl_b_4= np.array(dubl_b_4)
                for b_4 in dubl_b_4:
                    bx4= dubl_b_4[np.isin(0, dubl_b_4)]
                    by4= dubl_b_4[np.isin(1, dubl_b_4)]
                    bz4= dubl_b_4[np.isin(2, dubl_b_4)]
                    if len(bx4)>=1:
                        res_list.append('BX4')
                    if len(by4)>=1:
                        res_list.append('BY4')
                    if len(bz4)>=1:
                        res_list.append('BZ4')

                dubl_b_5= [i for i, x in enumerate(dubl_b_5) if x == zero]    #   A n
                dubl_b_5= np.array(dubl_b_5)
                for a_5 in dubl_b_5:
                    bx5= dubl_b_5[np.isin(0, dubl_b_5)]
                    by5= dubl_b_5[np.isin(1, dubl_b_5)]
                    bz5= dubl_b_5[np.isin(2, dubl_b_5)]
                    if len(bx5)>=1:
                        res_list.append('BX5')
                    if len(by5)>=1:
                        res_list.append('BY5')
                    if len(bz5)>=1:
                        res_list.append('BZ5')   
                          
                dubl_b_6= [i for i, x in enumerate(dubl_b_6) if x == zero]    #   A n
                dubl_b_6= np.array(dubl_b_6)
                for b_6 in dubl_b_6:
                    bx6= dubl_b_6[np.isin(0, dubl_b_6)]
                    by6= dubl_b_6[np.isin(1, dubl_b_6)]
                    bz6= dubl_b_6[np.isin(2, dubl_b_6)]
                    if len(bx6)>=1:
                        res_list.append('BX6')
                    if len(by6)>=1:
                        res_list.append('BY6')
                    if len(bz6)>=1:
                        res_list.append('BZ6')     

                dubl_b_7= [i for i, x in enumerate(dubl_b_7) if x == zero]    #   A n
                dubl_b_7= np.array(dubl_b_7)
                for b_7 in dubl_b_7:
                    bx7= dubl_b_7[np.isin(0, dubl_b_7)]
                    by7= dubl_b_7[np.isin(1, dubl_b_7)]
                    bz7= dubl_b_7[np.isin(2, dubl_b_7)]
                    if len(bx7)>=1:
                        res_list.append('BX7')
                    if len(by7)>=1:
                        res_list.append('BY7')
                    if len(bz7)>=1:
                        res_list.append('BZ7')   

                dubl_b_8= [i for i, x in enumerate(dubl_b_8) if x == zero]    #   A n
                dubl_b_8= np.array(dubl_b_8)
                for b_8 in dubl_b_8:
                    bx8= dubl_b_8[np.isin(0, dubl_b_8)]
                    by8= dubl_b_8[np.isin(1, dubl_b_8)]
                    bz8= dubl_b_8[np.isin(2, dubl_b_8)]
                    if len(bx8)>=1:
                        res_list.append('BX8')
                    if len(by8)>=1:
                        res_list.append('BY8')
                    if len(bz8)>=1:
                        res_list.append('BZ8') 

                dubl_b_9= [i for i, x in enumerate(dubl_b_9) if x == zero]    #   A n
                dubl_b_9= np.array(dubl_b_9)
                for b_9 in dubl_b_9:
                    bx9= dubl_b_9[np.isin(0, dubl_b_9)]
                    by9= dubl_b_9[np.isin(1, dubl_b_9)]
                    bz9= dubl_b_9[np.isin(2, dubl_b_9)]
                    if len(bx9)>=1:
                        res_list.append('BX9')
                    if len(by9)>=1:
                        res_list.append('BY9')
                    if len(bz9)>=1:
                        res_list.append('BZ9')

                dubl_b_10= [i for i, x in enumerate(dubl_b_10) if x == zero]    #   A n
                dubl_b_10= np.array(dubl_b_10)
                for a_10 in dubl_b_10:
                    bx10= dubl_b_10[np.isin(0, dubl_b_10)]
                    by10= dubl_b_10[np.isin(1, dubl_b_10)]
                    bz10= dubl_b_10[np.isin(2, dubl_b_10)]
                    if len(bx10)>=1:
                        res_list.append('BX10')
                    if len(by10)>=1:
                        res_list.append('BY10')
                    if len(bz10)>=1:
                        res_list.append('BZ10')  

                dubl_b_11= [i for i, x in enumerate(dubl_b_11) if x == zero]    #   A n
                dubl_b_11= np.array(dubl_b_11)
                for b_11 in dubl_b_11:
                    bx11= dubl_b_11[np.isin(0, dubl_b_11)]
                    by11= dubl_b_11[np.isin(1, dubl_b_11)]
                    bz11= dubl_b_11[np.isin(2, dubl_b_11)]
                    if len(bx11)>=1:
                        res_list.append('BX11')
                    if len(by11)>=1:
                        res_list.append('BY11')
                    if len(bz11)>=1:
                        res_list.append('BZ11')    

                dubl_b_12= [i for i, x in enumerate(dubl_b_12) if x == zero]    #   A n
                dubl_b_12= np.array(dubl_b_12)
                for b_12 in dubl_b_12:
                    bx12= dubl_b_12[np.isin(0, dubl_b_12)]
                    by12= dubl_b_12[np.isin(1, dubl_b_12)]
                    bz12= dubl_b_12[np.isin(2, dubl_b_12)]
                    if len(bx12)>=1:
                        res_list.append('BX12')
                    if len(by12)>=1:
                        res_list.append('BY12')
                    if len(bz12)>=1:
                        res_list.append('BZ12')     

                dubl_b_13= [i for i, x in enumerate(dubl_b_13) if x == zero]    #   A n
                dubl_b_13= np.array(dubl_b_13)
                for b_13 in dubl_b_13:
                    bx13= dubl_b_13[np.isin(0, dubl_b_13)]
                    by13= dubl_b_13[np.isin(1, dubl_b_13)]
                    bz13= dubl_b_13[np.isin(2, dubl_b_13)]
                    if len(bx13)>=1:
                        res_list.append('BX13')
                    if len(by13)>=1:
                        res_list.append('BY13')
                    if len(bz13)>=1:
                        res_list.append('BZ13')        

                dubl_b_14= [i for i, x in enumerate(dubl_b_14) if x == zero]    #   A n
                dubl_b_14= np.array(dubl_b_14)
                for b_14 in dubl_b_14:
                    bx14= dubl_b_14[np.isin(0, dubl_b_14)]
                    by14= dubl_b_14[np.isin(1, dubl_b_14)]
                    bz14= dubl_b_14[np.isin(2, dubl_b_14)]
                    if len(bx14)>=1:
                        res_list.append('BX14')
                    if len(by14)>=1:
                        res_list.append('BY14')
                    if len(bz14)>=1:
                        res_list.append('BZ14')     

                dubl_b_15= [i for i, x in enumerate(dubl_b_15) if x == zero]    #   A n
                dubl_b_15= np.array(dubl_b_15)
                for b_15 in dubl_b_15:
                    bx15= dubl_b_15[np.isin(0, dubl_b_15)]
                    by15= dubl_b_15[np.isin(1, dubl_b_15)]
                    bz15= dubl_b_15[np.isin(2, dubl_b_15)]
                    if len(bx15)>=1:
                        res_list.append('BX15')
                    if len(by15)>=1:
                        res_list.append('BY15')
                    if len(bz15)>=1:
                        res_list.append('BZ15')               

                dubl_b_16= [i for i, x in enumerate(dubl_b_16) if x == zero]    #   A n
                dubl_b_16= np.array(dubl_b_16)
                for b_16 in dubl_b_16:
                    bx16= dubl_b_16[np.isin(0, dubl_b_16)]
                    by16= dubl_b_16[np.isin(1, dubl_b_16)]
                    bz16= dubl_b_16[np.isin(2, dubl_b_16)]
                    if len(bx16)>=1:
                        res_list.append('BX16')
                    if len(by16)>=1:
                        res_list.append('BY16')
                    if len(bz16)>=1:
                        res_list.append('BZ16')    

                dubl_b_17= [i for i, x in enumerate(dubl_b_17) if x == zero]    #   A n
                dubl_b_17= np.array(dubl_b_17)
                for b_17 in dubl_b_17:
                    bx17= dubl_b_17[np.isin(0, dubl_b_17)]
                    by17= dubl_b_17[np.isin(1, dubl_b_17)]
                    bz17= dubl_b_17[np.isin(2, dubl_b_17)]
                    if len(bx17)>=1:
                        res_list.append('BX17')
                    if len(by17)>=1:
                        res_list.append('BY17')
                    if len(bz17)>=1:
                        res_list.append('BZ17')        
                
                dubl_b_18= [i for i, x in enumerate(dubl_b_18) if x == zero]    #   A n
                dubl_b_18= np.array(dubl_b_18)
                for b_18 in dubl_b_18:
                    bx18= dubl_b_18[np.isin(0, dubl_b_18)]
                    by18= dubl_b_18[np.isin(1, dubl_b_18)]
                    bz18= dubl_b_18[np.isin(2, dubl_b_18)]
                    if len(bx18)>=1:
                        res_list.append('BX18')
                    if len(by18)>=1:
                        res_list.append('BY18')
                    if len(bz18)>=1:
                        res_list.append('BZ18')
                
                dubl_b_19= [i for i, x in enumerate(dubl_b_19) if x == zero]    #   A n
                dubl_b_19= np.array(dubl_b_19)
                for b_19 in dubl_b_19:
                    bx19= dubl_b_19[np.isin(0, dubl_b_19)]
                    by19= dubl_b_19[np.isin(1, dubl_b_19)]
                    bz19= dubl_b_19[np.isin(2, dubl_b_19)]
                    if len(bx19)>=1:
                        res_list.append('BX19')
                    if len(by19)>=1:
                        res_list.append('BY19')
                    if len(bz19)>=1:
                        res_list.append('BZ19')
                
                dubl_b_20= [i for i, x in enumerate(dubl_b_20) if x == zero]    #   A n
                dubl_b_20= np.array(dubl_b_20)
                for b_20 in dubl_b_20:
                    bx20= dubl_b_20[np.isin(0, dubl_b_20)]
                    by20= dubl_b_20[np.isin(1, dubl_b_20)]
                    bz20= dubl_b_20[np.isin(2, dubl_b_20)]
                    if len(bx20)>=1:
                        res_list.append('BX20')
                    if len(by20)>=1:
                        res_list.append('BY20')
                    if len(bz20)>=1:
                        res_list.append('BZ20')
                
                dubl_b_21= [i for i, x in enumerate(dubl_b_21) if x == zero]    #   A n
                dubl_b_21= np.array(dubl_b_21)
                for b_21 in dubl_b_21:
                    bx21= dubl_b_21[np.isin(0, dubl_b_21)]
                    by21= dubl_b_21[np.isin(1, dubl_b_21)]
                    bz21= dubl_b_21[np.isin(2, dubl_b_21)]
                    if len(bx21)>=1:
                        res_list.append('BX21')
                    if len(by21)>=1:
                        res_list.append('BY21')
                    if len(bz21)>=1:
                        res_list.append('BZ21')
                
                dubl_b_22= [i for i, x in enumerate(dubl_b_22) if x == zero]    #   A n
                dubl_b_22= np.array(dubl_b_22)
                for b_22 in dubl_b_22:
                    bx22= dubl_b_22[np.isin(0, dubl_b_22)]
                    by22= dubl_b_22[np.isin(1, dubl_b_22)]
                    bz22= dubl_b_22[np.isin(2, dubl_b_22)]
                    if len(bx22)>=1:
                        res_list.append('BX22')
                    if len(by22)>=1:
                        res_list.append('BY22')
                    if len(bz22)>=1:
                        res_list.append('BZ22')
                
                dubl_b_23= [i for i, x in enumerate(dubl_b_23) if x == zero]    #   A n
                dubl_b_23= np.array(dubl_b_23)
                for b_23 in dubl_b_23:
                    bx23= dubl_b_23[np.isin(0, dubl_b_23)]
                    by23= dubl_b_23[np.isin(1, dubl_b_23)]
                    bz23= dubl_b_23[np.isin(2, dubl_b_23)]
                    if len(bx23)>=1:
                        res_list.append('BX23')
                    if len(by23)>=1:
                        res_list.append('BY23')
                    if len(bz23)>=1:
                        res_list.append('BZ23')
                
                dubl_b_24= [i for i, x in enumerate(dubl_b_24) if x == zero]    #   A n
                dubl_b_24= np.array(dubl_b_24)
                for b_24 in dubl_b_24:
                    bx24= dubl_b_24[np.isin(0, dubl_b_24)]
                    by24= dubl_b_24[np.isin(1, dubl_b_24)]
                    bz24= dubl_b_24[np.isin(2, dubl_b_24)]
                    if len(bx24)>=1:
                        res_list.append('BX24')
                    if len(by24)>=1:
                        res_list.append('BY24')
                    if len(bz24)>=1:
                        res_list.append('BZ24')
                
                dubl_b_25= [i for i, x in enumerate(dubl_b_25) if x == zero]    #   A n
                dubl_b_25= np.array(dubl_b_25)
                for b_25 in dubl_b_25:
                    bx25= dubl_b_25[np.isin(0, dubl_b_25)]
                    by25= dubl_b_25[np.isin(1, dubl_b_25)]
                    bz25= dubl_b_25[np.isin(2, dubl_b_25)]
                    if len(bx25)>=1:
                        res_list.append('BX25')
                    if len(by25)>=1:
                        res_list.append('BY25')
                    if len(bz25)>=1:
                        res_list.append('BZ25')
                
                dubl_b_26= [i for i, x in enumerate(dubl_b_26) if x == zero]    #   A n
                dubl_b_26= np.array(dubl_b_26)
                for b_26 in dubl_b_26:
                    bx26= dubl_b_26[np.isin(0, dubl_b_26)]
                    by26= dubl_b_26[np.isin(1, dubl_b_26)]
                    bz26= dubl_b_26[np.isin(2, dubl_b_26)]
                    if len(bx26)>=1:
                        res_list.append('BX26')
                    if len(by26)>=1:
                        res_list.append('BY26')
                    if len(bz26)>=1:
                        res_list.append('BZ26')
                
                dubl_b_27= [i for i, x in enumerate(dubl_b_27) if x == zero]    #   A n
                dubl_b_27= np.array(dubl_b_27)
                for b_27 in dubl_b_27:
                    bx27= dubl_b_27[np.isin(0, dubl_b_27)]
                    by27= dubl_b_27[np.isin(1, dubl_b_27)]
                    bz27= dubl_b_27[np.isin(2, dubl_b_27)]
                    if len(bx27)>=1:
                        res_list.append('BX27')
                    if len(by27)>=1:
                        res_list.append('BY27')
                    if len(bz27)>=1:
                        res_list.append('BZ27')
                
                dubl_b_28= [i for i, x in enumerate(dubl_b_28) if x == zero]    #   A n
                dubl_b_28= np.array(dubl_b_28)
                for b_28 in dubl_b_28:
                    bx28= dubl_b_28[np.isin(0, dubl_b_28)]
                    by28= dubl_b_28[np.isin(1, dubl_b_28)]
                    bz28= dubl_b_28[np.isin(2, dubl_b_28)]
                    if len(bx28)>=1:
                        res_list.append('BX28')
                    if len(by28)>=1:
                        res_list.append('BY28')
                    if len(bz28)>=1:
                        res_list.append('BZ28')
                
                dubl_b_29= [i for i, x in enumerate(dubl_b_29) if x == zero]    #   A n
                dubl_b_29= np.array(dubl_b_29)
                for b_29 in dubl_b_29:
                    bx29= dubl_b_29[np.isin(0, dubl_b_29)]
                    by29= dubl_b_29[np.isin(1, dubl_b_29)]
                    bz29= dubl_b_29[np.isin(2, dubl_b_29)]
                    if len(bx29)>=1:
                        res_list.append('BX29')
                    if len(by29)>=1:
                        res_list.append('BY29')
                    if len(bz29)>=1:
                        res_list.append('BZ29')

                dubl_b_30= [i for i, x in enumerate(dubl_b_30) if x == zero]    #   A n
                dubl_b_30= np.array(dubl_b_30)
                for b_30 in dubl_b_30:
                    bx30= dubl_b_30[np.isin(0, dubl_b_30)]
                    by30= dubl_b_30[np.isin(1, dubl_b_30)]
                    bz30= dubl_b_30[np.isin(2, dubl_b_30)]
                    if len(bx30)>=1:
                        res_list.append('BX30')
                    if len(by30)>=1:
                        res_list.append('BY30')
                    if len(bz30)>=1:
                        res_list.append('BZ30')


            for q in c:
                dubl_c_1= c[0]
                dubl_c_2= c[1]
                dubl_c_3= c[2]
                dubl_c_4= c[3]
                dubl_c_5= c[4]
                dubl_c_6= c[5]
                dubl_c_7= c[6]
                dubl_c_8= c[7]
                dubl_c_9= c[8]
                dubl_c_10= c[9]
                dubl_c_11= c[10]
                dubl_c_12= c[11]
                dubl_c_13= c[12]
                dubl_c_14= c[13]
                dubl_c_15= c[14]
                dubl_c_16= c[15]
                dubl_c_17= c[16]
                dubl_c_18= c[17]
                dubl_c_19= c[18]
                dubl_c_20= c[19]
                dubl_c_21= c[20]
                dubl_c_22= c[21]
                dubl_c_23= c[22]
                dubl_c_24= c[23]
                dubl_c_25= c[24]
                dubl_c_26= c[25]
                dubl_c_27= c[26]
                dubl_c_28= c[27]
                dubl_c_29= c[28]
                dubl_c_30= c[29]
                zero= 0
                dubl_c_1= [i for i, x in enumerate(dubl_c_1) if x == zero]                 
                dubl_c_1= np.array(dubl_c_1)
                for c_1 in dubl_c_1:
                    cx1= dubl_c_1[np.isin(0, dubl_c_1)]
                    cy1= dubl_c_1[np.isin(1, dubl_c_1)]
                    cz1= dubl_c_1[np.isin(2, dubl_c_1)]
                    if len(cx1)>=1:
                        res_list.append('CX1')
                    if len(cy1)>=1:
                        res_list.append('CY1')
                    if len(cz1)>=1:
                        res_list.append('CZ1')

                dubl_c_2= [i for i, x in enumerate(dubl_c_2) if x == zero]
                dubl_c_2= np.array(dubl_c_2)
                for c_2 in dubl_c_2:
                    cx2= dubl_c_2[np.isin(0, dubl_c_2)]
                    cy2= dubl_c_2[np.isin(1, dubl_c_2)]
                    cz2= dubl_c_2[np.isin(2, dubl_c_2)]
                    if len(cx2)>=1:
                        res_list.append('CX2')
                    if len(cy2)>=1:
                        res_list.append('CY2')
                    if len(cz2)>=1:
                        res_list.append('CZ2')

                dubl_c_3= [i for i, x in enumerate(dubl_c_3) if x == zero]
                dubl_c_3= np.array(dubl_c_3)
                for c_3 in dubl_c_3:
                    cx3= dubl_c_3[np.isin(0, dubl_c_3)]
                    cy3= dubl_c_3[np.isin(1, dubl_c_3)]
                    cz3= dubl_c_3[np.isin(2, dubl_c_3)]
                    if len(cx3)>=1:
                        res_list.append('CX3')
                    if len(cy3)>=1:
                        res_list.append('CY3')
                    if len(cz3)>=1:
                        res_list.append('CZ3')
                
                dubl_c_4= [i for i, x in enumerate(dubl_c_4) if x == zero]    #   A n
                dubl_c_4= np.array(dubl_c_4)
                for c_4 in dubl_c_4:
                    cx4= dubl_c_4[np.isin(0, dubl_c_4)]
                    cy4= dubl_c_4[np.isin(1, dubl_c_4)]
                    cz4= dubl_c_4[np.isin(2, dubl_c_4)]
                    if len(cx4)>=1:
                        res_list.append('CX4')
                    if len(cy4)>=1:
                        res_list.append('CY4')
                    if len(cz4)>=1:
                        res_list.append('CZ4')

                dubl_c_5= [i for i, x in enumerate(dubl_c_5) if x == zero]    #   A n
                dubl_c_5= np.array(dubl_c_5)
                for c_5 in dubl_c_5:
                    cx5= dubl_c_5[np.isin(0, dubl_c_5)]
                    cy5= dubl_c_5[np.isin(1, dubl_c_5)]
                    cz5= dubl_c_5[np.isin(2, dubl_c_5)]
                    if len(cx5)>=1:
                        res_list.append('CX5')
                    if len(cy5)>=1:
                        res_list.append('CY5')
                    if len(cz5)>=1:
                        res_list.append('CZ5')   
                          
                dubl_c_6= [i for i, x in enumerate(dubl_c_6) if x == zero]    #   A n
                dubl_c_6= np.array(dubl_c_6)
                for c_6 in dubl_c_6:
                    cx6= dubl_c_6[np.isin(0, dubl_c_6)]
                    cy6= dubl_c_6[np.isin(1, dubl_c_6)]
                    cz6= dubl_c_6[np.isin(2, dubl_c_6)]
                    if len(cx6)>=1:
                        res_list.append('CX6')
                    if len(cy6)>=1:
                        res_list.append('CY6')
                    if len(cz6)>=1:
                        res_list.append('CZ6')     

                dubl_c_7= [i for i, x in enumerate(dubl_c_7) if x == zero]    #   A n
                dubl_c_7= np.array(dubl_c_7)
                for c_7 in dubl_c_7:
                    cx7= dubl_c_7[np.isin(0, dubl_c_7)]
                    cy7= dubl_c_7[np.isin(1, dubl_c_7)]
                    cz7= dubl_c_7[np.isin(2, dubl_c_7)]
                    if len(cx7)>=1:
                        res_list.append('CX7')
                    if len(cy7)>=1:
                        res_list.append('CY7')
                    if len(cz7)>=1:
                        res_list.append('CZ7')   

                dubl_c_8= [i for i, x in enumerate(dubl_c_8) if x == zero]    #   A n
                dubl_c_8= np.array(dubl_c_8)
                for c_8 in dubl_c_8:
                    cx8= dubl_c_8[np.isin(0, dubl_c_8)]
                    cy8= dubl_c_8[np.isin(1, dubl_c_8)]
                    cz8= dubl_c_8[np.isin(2, dubl_c_8)]
                    if len(cx8)>=1:
                        res_list.append('CX8')
                    if len(cy8)>=1:
                        res_list.append('CY8')
                    if len(cz8)>=1:
                        res_list.append('CZ8') 

                dubl_c_9= [i for i, x in enumerate(dubl_c_9) if x == zero]    #   A n
                dubl_c_9= np.array(dubl_c_9)
                for c_9 in dubl_c_9:
                    cx9= dubl_c_9[np.isin(0, dubl_c_9)]
                    cy9= dubl_c_9[np.isin(1, dubl_c_9)]
                    cz9= dubl_c_9[np.isin(2, dubl_c_9)]
                    if len(cx9)>=1:
                        res_list.append('CX9')
                    if len(cy9)>=1:
                        res_list.append('CY9')
                    if len(cz9)>=1:
                        res_list.append('CZ9')

                dubl_c_10= [i for i, x in enumerate(dubl_c_10) if x == zero]    #   A n
                dubl_c_10= np.array(dubl_c_10)
                for c_10 in dubl_c_10:
                    cx10= dubl_c_10[np.isin(0, dubl_c_10)]
                    cy10= dubl_c_10[np.isin(1, dubl_c_10)]
                    cz10= dubl_c_10[np.isin(2, dubl_c_10)]
                    if len(cx10)>=1:
                        res_list.append('CX10')
                    if len(cy10)>=1:
                        res_list.append('CY10')
                    if len(cz10)>=1:
                        res_list.append('CZ10')  

                dubl_c_11= [i for i, x in enumerate(dubl_c_11) if x == zero]    #   A n
                dubl_c_11= np.array(dubl_c_11)
                for c_11 in dubl_c_11:
                    cx11= dubl_c_11[np.isin(0, dubl_c_11)]
                    cy11= dubl_c_11[np.isin(1, dubl_c_11)]
                    cz11= dubl_c_11[np.isin(2, dubl_c_11)]
                    if len(cx11)>=1:
                        res_list.append('CX11')
                    if len(cy11)>=1:
                        res_list.append('CY11')
                    if len(cz11)>=1:
                        res_list.append('CZ11')    

                dubl_c_12= [i for i, x in enumerate(dubl_c_12) if x == zero]    #   A n
                dubl_c_12= np.array(dubl_c_12)
                for c_12 in dubl_c_12:
                    cx12= dubl_c_12[np.isin(0, dubl_c_12)]
                    cy12= dubl_c_12[np.isin(1, dubl_c_12)]
                    cz12= dubl_c_12[np.isin(2, dubl_c_12)]
                    if len(cx12)>=1:
                        res_list.append('CX12')
                    if len(cy12)>=1:
                        res_list.append('CY12')
                    if len(cz12)>=1:
                        res_list.append('CZ12')     

                dubl_c_13= [i for i, x in enumerate(dubl_c_13) if x == zero]    #   A n
                dubl_c_13= np.array(dubl_c_13)
                for c_13 in dubl_c_13:
                    cx13= dubl_c_13[np.isin(0, dubl_c_13)]
                    cy13= dubl_c_13[np.isin(1, dubl_c_13)]
                    cz13= dubl_c_13[np.isin(2, dubl_c_13)]
                    if len(cx13)>=1:
                        res_list.append('CX13')
                    if len(cy13)>=1:
                        res_list.append('CY13')
                    if len(cz13)>=1:
                        res_list.append('CZ13')        

                dubl_c_14= [i for i, x in enumerate(dubl_c_14) if x == zero]    #   A n
                dubl_c_14= np.array(dubl_c_14)
                for c_14 in dubl_c_14:
                    cx14= dubl_c_14[np.isin(0, dubl_c_14)]
                    cy14= dubl_c_14[np.isin(1, dubl_c_14)]
                    cz14= dubl_c_14[np.isin(2, dubl_c_14)]
                    if len(cx14)>=1:
                        res_list.append('CX14')
                    if len(cy14)>=1:
                        res_list.append('CY14')
                    if len(cz14)>=1:
                        res_list.append('CZ14')     

                dubl_c_15= [i for i, x in enumerate(dubl_c_15) if x == zero]    #   A n
                dubl_c_15= np.array(dubl_c_15)
                for c_15 in dubl_c_15:
                    cx15= dubl_c_15[np.isin(0, dubl_c_15)]
                    cy15= dubl_c_15[np.isin(1, dubl_c_15)]
                    cz15= dubl_c_15[np.isin(2, dubl_c_15)]
                    if len(cx15)>=1:
                        res_list.append('CX15')
                    if len(cy15)>=1:
                        res_list.append('CY15')
                    if len(cz15)>=1:
                        res_list.append('CZ15')               

                dubl_c_16= [i for i, x in enumerate(dubl_c_16) if x == zero]    #   A n
                dubl_c_16= np.array(dubl_c_16)
                for c_16 in dubl_c_16:
                    cx16= dubl_c_16[np.isin(0, dubl_c_16)]
                    cy16= dubl_c_16[np.isin(1, dubl_c_16)]
                    cz16= dubl_c_16[np.isin(2, dubl_c_16)]
                    if len(cx16)>=1:
                        res_list.append('CX16')
                    if len(cy16)>=1:
                        res_list.append('CY16')
                    if len(cz16)>=1:
                        res_list.append('CZ16')    

                dubl_c_17= [i for i, x in enumerate(dubl_c_17) if x == zero]    #   A n
                dubl_c_17= np.array(dubl_c_17)
                for c_17 in dubl_c_17:
                    cx17= dubl_c_17[np.isin(0, dubl_c_17)]
                    cy17= dubl_c_17[np.isin(1, dubl_c_17)]
                    cz17= dubl_c_17[np.isin(2, dubl_c_17)]
                    if len(cx17)>=1:
                        res_list.append('CX17')
                    if len(cy17)>=1:
                        res_list.append('CY17')
                    if len(cz17)>=1:
                        res_list.append('CZ17')        
                
                dubl_c_18= [i for i, x in enumerate(dubl_c_18) if x == zero]    #   A n
                dubl_c_18= np.array(dubl_c_18)
                for c_18 in dubl_c_18:
                    cx18= dubl_c_18[np.isin(0, dubl_c_18)]
                    cy18= dubl_c_18[np.isin(1, dubl_c_18)]
                    cz18= dubl_c_18[np.isin(2, dubl_c_18)]
                    if len(cx18)>=1:
                        res_list.append('CX18')
                    if len(cy18)>=1:
                        res_list.append('CY18')
                    if len(cz18)>=1:
                        res_list.append('CZ18')
                
                dubl_c_19= [i for i, x in enumerate(dubl_c_19) if x == zero]    #   A n
                dubl_c_19= np.array(dubl_c_19)
                for c_19 in dubl_c_19:
                    cx19= dubl_c_19[np.isin(0, dubl_c_19)]
                    cy19= dubl_c_19[np.isin(1, dubl_c_19)]
                    cz19= dubl_c_19[np.isin(2, dubl_c_19)]
                    if len(cx19)>=1:
                        res_list.append('CX19')
                    if len(cy19)>=1:
                        res_list.append('CY19')
                    if len(cz19)>=1:
                        res_list.append('CZ19')
                
                dubl_c_20= [i for i, x in enumerate(dubl_c_20) if x == zero]    #   A n
                dubl_c_20= np.array(dubl_c_20)
                for c_20 in dubl_c_20:
                    cx20= dubl_c_20[np.isin(0, dubl_c_20)]
                    cy20= dubl_c_20[np.isin(1, dubl_c_20)]
                    cz20= dubl_c_20[np.isin(2, dubl_c_20)]
                    if len(cx20)>=1:
                        res_list.append('CX20')
                    if len(cy20)>=1:
                        res_list.append('CY20')
                    if len(cz20)>=1:
                        res_list.append('CZ20')
                
                dubl_c_21= [i for i, x in enumerate(dubl_c_21) if x == zero]    #   A n
                dubl_c_21= np.array(dubl_c_21)
                for c_21 in dubl_c_21:
                    cx21= dubl_c_21[np.isin(0, dubl_c_21)]
                    cy21= dubl_c_21[np.isin(1, dubl_c_21)]
                    cz21= dubl_c_21[np.isin(2, dubl_c_21)]
                    if len(cx21)>=1:
                        res_list.append('CX21')
                    if len(cy21)>=1:
                        res_list.append('CY21')
                    if len(cz21)>=1:
                        res_list.append('CZ21')
                
                dubl_c_22= [i for i, x in enumerate(dubl_c_22) if x == zero]    #   A n
                dubl_c_22= np.array(dubl_c_22)
                for c_22 in dubl_c_22:
                    cx22= dubl_c_22[np.isin(0, dubl_c_22)]
                    cy22= dubl_c_22[np.isin(1, dubl_c_22)]
                    cz22= dubl_c_22[np.isin(2, dubl_c_22)]
                    if len(cx22)>=1:
                        res_list.append('CX22')
                    if len(cy22)>=1:
                        res_list.append('CY22')
                    if len(cz22)>=1:
                        res_list.append('CZ22')
                
                dubl_c_23= [i for i, x in enumerate(dubl_c_23) if x == zero]    #   A n
                dubl_c_23= np.array(dubl_c_23)
                for c_23 in dubl_c_23:
                    cx23= dubl_c_23[np.isin(0, dubl_c_23)]
                    cy23= dubl_c_23[np.isin(1, dubl_c_23)]
                    cz23= dubl_c_23[np.isin(2, dubl_c_23)]
                    if len(cx23)>=1:
                        res_list.append('CX23')
                    if len(cy23)>=1:
                        res_list.append('CY23')
                    if len(cz23)>=1:
                        res_list.append('CZ23')
                
                dubl_c_24= [i for i, x in enumerate(dubl_c_24) if x == zero]    #   A n
                dubl_c_24= np.array(dubl_c_24)
                for c_24 in dubl_c_24:
                    cx24= dubl_c_24[np.isin(0, dubl_c_24)]
                    cy24= dubl_c_24[np.isin(1, dubl_c_24)]
                    cz24= dubl_c_24[np.isin(2, dubl_c_24)]
                    if len(cx24)>=1:
                        res_list.append('CX24')
                    if len(cy24)>=1:
                        res_list.append('CY24')
                    if len(cz24)>=1:
                        res_list.append('CZ24')
                
                dubl_c_25= [i for i, x in enumerate(dubl_c_25) if x == zero]    #   A n
                dubl_c_25= np.array(dubl_c_25)
                for c_25 in dubl_c_25:
                    cx25= dubl_c_25[np.isin(0, dubl_c_25)]
                    cy25= dubl_c_25[np.isin(1, dubl_c_25)]
                    cz25= dubl_c_25[np.isin(2, dubl_c_25)]
                    if len(cx25)>=1:
                        res_list.append('CX25')
                    if len(cy25)>=1:
                        res_list.append('CY25')
                    if len(cz25)>=1:
                        res_list.append('CZ25')
                
                dubl_c_26= [i for i, x in enumerate(dubl_c_26) if x == zero]    #   A n
                dubl_c_26= np.array(dubl_c_26)
                for c_26 in dubl_c_26:
                    cx26= dubl_c_26[np.isin(0, dubl_c_26)]
                    cy26= dubl_c_26[np.isin(1, dubl_c_26)]
                    cz26= dubl_c_26[np.isin(2, dubl_c_26)]
                    if len(cx26)>=1:
                        res_list.append('CX26')
                    if len(cy26)>=1:
                        res_list.append('CY26')
                    if len(cz26)>=1:
                        res_list.append('CZ26')
                
                dubl_c_27= [i for i, x in enumerate(dubl_c_27) if x == zero]    #   A n
                dubl_c_27= np.array(dubl_c_27)
                for c_27 in dubl_c_27:
                    cx27= dubl_c_27[np.isin(0, dubl_c_27)]
                    cy27= dubl_c_27[np.isin(1, dubl_c_27)]
                    cz27= dubl_c_27[np.isin(2, dubl_c_27)]
                    if len(cx27)>=1:
                        res_list.append('CX27')
                    if len(cy27)>=1:
                        res_list.append('CY27')
                    if len(cz27)>=1:
                        res_list.append('CZ27')
                
                dubl_c_28= [i for i, x in enumerate(dubl_c_28) if x == zero]    #   A n
                dubl_c_28= np.array(dubl_c_28)
                for c_28 in dubl_c_28:
                    cx28= dubl_c_28[np.isin(0, dubl_c_28)]
                    cy28= dubl_c_28[np.isin(1, dubl_c_28)]
                    cz28= dubl_c_28[np.isin(2, dubl_c_28)]
                    if len(cx28)>=1:
                        res_list.append('CX28')
                    if len(cy28)>=1:
                        res_list.append('CY28')
                    if len(cz28)>=1:
                        res_list.append('CZ28')
                
                dubl_c_29= [i for i, x in enumerate(dubl_c_29) if x == zero]    #   A n
                dubl_c_29= np.array(dubl_c_29)
                for c_29 in dubl_c_29:
                    cx29= dubl_c_29[np.isin(0, dubl_c_29)]
                    cy29= dubl_c_29[np.isin(1, dubl_c_29)]
                    cz29= dubl_c_29[np.isin(2, dubl_c_29)]
                    if len(cx29)>=1:
                        res_list.append('CX29')
                    if len(cy29)>=1:
                        res_list.append('CY29')
                    if len(cz29)>=1:
                        res_list.append('CZ29')

                dubl_c_30= [i for i, x in enumerate(dubl_c_30) if x == zero]    #   A n
                dubl_c_30= np.array(dubl_c_30)
                for c_30 in dubl_c_30:
                    cx30= dubl_c_30[np.isin(0, dubl_c_30)]
                    cy30= dubl_c_30[np.isin(1, dubl_c_30)]
                    cz30= dubl_c_30[np.isin(2, dubl_c_30)]
                    if len(cx30)>=1:
                        res_list.append('CX30')
                    if len(cy30)>=1:
                        res_list.append('CY30')
                    if len(cz30)>=1:
                        res_list.append('CZ30')

            res_list= set(res_list)
            res_list= list(res_list)
            return res_list

def flower(cell_selection):
    
            a_cell= copy.deepcopy(cell_selection)               #A
            b_cell= copy.deepcopy(cell_selection)               #B
            for i in cell_selection:
                if cell_selection[0]=='C':
                    a_cell[0]='A'
                    b_cell[0]='B'
                    return (f'{''.join(a_cell)}, {''.join(b_cell)}')
                elif cell_selection[0]=='B':
                    a_cell[0]='A'
                    return ''.join(a_cell)
                elif bot_cell[0]=='A':
                    return 'No containers were found below'
                else:
                    return 'There is no container in the database'
                
def correct_empty_cells(cell_selection_lits):           
            q= empty_cells[np.isin(cell_selectionn, empty_cells)]       
            
            if len(q)>=1:
            # hc= None
                hc= flower(cell_selection)
                hll= list(hc)
                if len(hll)==4:
                    cells= hll[2]+hll[3]
                    hll.pop(3)
                    hll.pop(2)
                    hll.insert(2, cells)
                h_1= hll[:3]
                h_1= ''.join(h_1)
                h_2= hll[-3:]
                h_2= ''.join(h_2)
            # hc= np.array(hll)
                ha= empty_cells[np.isin(h_1, empty_cells)]
                hb= empty_cells[np.isin(h_2, empty_cells)]
                if len(ha)>0:
                    return 'There is no container under the selected cell'
                elif len(hb)>0:
                    return 'There is no container under the selected cell'
                else:
                    return 'The cell has been found'
            else:
                return 'Empty cell not found'

def perp1(h2, hcell2): 
            cont_per= higher_cel2[-1]
            cont_per= list(cont_per)
            if len(cont_per)==4:
                qwer= cont_per[2]+cont_per[3]
                cont_per.pop(3)
                cont_per.pop(2)
                cont_per.insert(2, qwer)
            count_cont= h2_cell[-1]
            h2_cell.pop(-1)
            index_1= None              
            index_2= None               
            n= None
            j= None
            i= None
            q= None
            w= None
            e= None

            if cell_selection[0]=='A':
                n= 0
            elif cell_selection[0]=='B':
                n= 1
            elif cell_selection[0]=='C':
                n= 2
            
            if cell_selection[1]=='X':
                j= 0
            elif cell_selection[1]=='Y':
                j= 1
            elif cell_selection[1]=='Z':
                j= 2

            if cell_selection[2]=='1':                     
                i= 0
            elif cell_selection[2]=='2':
                i= 1
            elif cell_selection[2]=='3':
                i= 2                             
            elif cell_selection[2]=='4':                      
                i= 3
            elif cell_selection[2]=='5':
                i= 4
            elif cell_selection[2]=='6':
                i= 5
            elif cell_selection[2]=='7':
                i= 6
            elif cell_selection[2]=='8':
                i= 7                             
            elif cell_selection[2]=='9':                      
                i= 8
            elif cell_selection[2]=='10':
                i= 9
            elif cell_selection[2]=='11':
                i= 10
            elif cell_selection[2]=='12':
                i= 11
            elif cell_selection[2]=='13':
                i= 12                             
            elif cell_selection[2]=='14':                      
                i= 13
            elif cell_selection[2]=='15':
                i= 14
            elif cell_selection[2]=='16':
                i= 15
            elif cell_selection[2]=='17':
                i= 16
            elif cell_selection[2]=='18':
                i= 17
            elif cell_selection[2]=='19':
                i= 18
            elif cell_selection[2]=='20':
                i= 19                             
            elif cell_selection[2]=='21':                      
                i= 20
            elif cell_selection[2]=='22':
                i= 21
            elif cell_selection[2]=='23':
                i= 22
            elif cell_selection[2]=='24':
                i= 23
            elif cell_selection[2]=='25':
                i= 24
            elif cell_selection[2]=='26':
                i= 25
            elif cell_selection[2]=='27':
                i= 26                             
            elif cell_selection[2]=='28':                      
                i= 27
            elif cell_selection[2]=='29':
                i= 28
            elif cell_selection[2]=='30':
                i= 29
            
                                        


            if cont_per[0]=='A':
                q= 0
            elif cont_per[0]=='B':
                q= 1
            elif cont_per[0]=='C':
                q= 2
            
            if cont_per[1]=='X':
                w= 0
            elif cont_per[1]=='Y':
                w= 1
            elif cont_per[1]=='Z':
                w= 2
            
            if cont_per[2]=='1':                     
                e= 0
            elif cont_per[2]=='2':
                e= 1
            elif cont_per[2]=='3':
                e= 2                             
            elif cont_per[2]=='4':                      
                e= 3
            elif cont_per[2]=='5':
                e= 4
            elif cont_per[2]=='6':
                e= 5
            elif cont_per[2]=='7':
                e= 6
            elif cont_per[2]=='8':
                e= 7                             
            elif cont_per[2]=='9':                      
                e= 8
            elif cont_per[2]=='10':
                e= 9
            elif cont_per[2]=='11':
                e= 10
            elif cont_per[2]=='12':
                e= 11
            elif cont_per[2]=='13':
                e= 12                             
            elif cont_per[2]=='14':                      
                e= 13
            elif cont_per[2]=='15':
                e= 14
            elif cont_per[2]=='16':
                e= 15
            elif cont_per[2]=='17':
                e= 16
            elif cont_per[2]=='18':
                e= 17
            elif cont_per[2]=='19':
                e= 18
            elif cont_per[2]=='20':
                e= 19                             
            elif cont_per[2]=='21':                      
                e= 20
            elif cont_per[2]=='22':
                e= 21
            elif cont_per[2]=='23':
                e= 22
            elif cont_per[2]=='24':
                e= 23
            elif cont_per[2]=='25':
                e= 24
            elif cont_per[2]=='26':
                e= 25
            elif cont_per[2]=='27':
                e= 26                             
            elif cont_per[2]=='28':                      
                e= 27
            elif cont_per[2]=='29':
                e= 28
            elif cont_per[2]=='30':
                e= 29
            
            project_1[n][i][j], project_1[q][e][w] = project_1[q][e][w], project_1[n][i][j]
            return project_1    

def perp2(h2, hcell2): 
            cont_per= higher_cel2[0]
            cont_per= list(cont_per)
            if len(cont_per)==4:
                qq= cont_per[2]+cont_per[3]
                cont_per.pop(3)
                cont_per.pop(2)
                cont_per.insert(2, qq)
            count_cont= h2_cell[0]
            h2_cell.pop(0)
            index_1= None              
            index_2= None              
            n= None
            j= None
            i= None
            q= None
            w= None
            e= None

            if cell_selection[0]=='A':
                n= 0
            elif cell_selection[0]=='B':
                n= 1
            elif cell_selection[0]=='C':
                n= 2
            
            if cell_selection[1]=='X':
                j= 0
            elif cell_selection[1]=='Y':
                j= 1
            elif cell_selection[1]=='Z':
                j= 2

            if cell_selection[2]=='1':                     
                i= 0
            elif cell_selection[2]=='2':
                i= 1
            elif cell_selection[2]=='3':
                i= 2                             
            elif cell_selection[2]=='4':                      
                i= 3
            elif cell_selection[2]=='5':
                i= 4
            elif cell_selection[2]=='6':
                i= 5
            elif cell_selection[2]=='7':
                i= 6
            elif cell_selection[2]=='8':
                i= 7                             
            elif cell_selection[2]=='9':                      
                i= 8
            elif cell_selection[2]=='10':
                i= 9
            elif cell_selection[2]=='11':
                i= 10
            elif cell_selection[2]=='12':
                i= 11
            elif cell_selection[2]=='13':
                i= 12                             
            elif cell_selection[2]=='14':                      
                i= 13
            elif cell_selection[2]=='15':
                i= 14
            elif cell_selection[2]=='16':
                i= 15
            elif cell_selection[2]=='17':
                i= 16
            elif cell_selection[2]=='18':
                i= 17
            elif cell_selection[2]=='19':
                i= 18
            elif cell_selection[2]=='20':
                i= 19                             
            elif cell_selection[2]=='21':                      
                i= 20
            elif cell_selection[2]=='22':
                i= 21
            elif cell_selection[2]=='23':
                i= 22
            elif cell_selection[2]=='24':
                i= 23
            elif cell_selection[2]=='25':
                i= 24
            elif cell_selection[2]=='26':
                i= 25
            elif cell_selection[2]=='27':
                i= 26                             
            elif cell_selection[2]=='28':                      
                i= 27
            elif cell_selection[2]=='29':
                i= 28
            elif cell_selection[2]=='30':
                i= 29
            
                                        


            if cont_per[0]=='A':
                q= 0
            elif cont_per[0]=='B':
                q= 1
            elif cont_per[0]=='C':
                q= 2
            
            if cont_per[1]=='X':
                w= 0
            elif cont_per[1]=='Y':
                w= 1
            elif cont_per[1]=='Z':
                w= 2
            
            if cont_per[2]=='1':                     
                e= 0
            elif cont_per[2]=='2':
                e= 1
            elif cont_per[2]=='3':
                e= 2                             
            elif cont_per[2]=='4':                      
                e= 3
            elif cont_per[2]=='5':
                e= 4
            elif cont_per[2]=='6':
                e= 5
            elif cont_per[2]=='7':
                e= 6
            elif cont_per[2]=='8':
                e= 7                             
            elif cont_per[2]=='9':                      
                e= 8
            elif cont_per[2]=='10':
                e= 9
            elif cont_per[2]=='11':
                e= 10
            elif cont_per[2]=='12':
                e= 11
            elif cont_per[2]=='13':
                e= 12                             
            elif cont_per[2]=='14':                      
                e= 13
            elif cont_per[2]=='15':
                e= 14
            elif cont_per[2]=='16':
                e= 15
            elif cont_per[2]=='17':
                e= 16
            elif cont_per[2]=='18':
                e= 17
            elif cont_per[2]=='19':
                e= 18
            elif cont_per[2]=='20':
                e= 19                             
            elif cont_per[2]=='21':                      
                e= 20
            elif cont_per[2]=='22':
                e= 21
            elif cont_per[2]=='23':
                e= 22
            elif cont_per[2]=='24':
                e= 23
            elif cont_per[2]=='25':
                e= 24
            elif cont_per[2]=='26':
                e= 25
            elif cont_per[2]=='27':
                e= 26                             
            elif cont_per[2]=='28':                      
                e= 27
            elif cont_per[2]=='29':
                e= 28
            elif cont_per[2]=='30':
                e= 29
            
            project_1[n][i][j], project_1[q][e][w] = project_1[q][e][w], project_1[n][i][j]
            return project_1    

def del_cont_car(bot_cell):
                n= None
                j= None
                i= None
                bot_cell= list(bot_cell)
                if len(bot_cell)==4:
                    bye= bot_cell[2]+bot_cell[3]
                    bot_cell.pop(3)
                    bot_cell.pop(2)
                    bot_cell.insert(2, bye)
                if bot_cell[0]=='A':
                    n= 0
                elif bot_cell[0]=='B':
                    n= 1
                elif bot_cell[0]=='C':
                    n= 2
                
                if bot_cell[1]=='X':
                    j= 0
                elif bot_cell[1]=='Y':
                    j= 1
                elif bot_cell[1]=='Z':
                    j= 2

                if bot_cell[2]=='1':                        
                    i= 0
                elif bot_cell[2]=='2':
                    i= 1
                elif bot_cell[2]=='3':
                    i= 2  
                elif bot_cell[2]=='4':
                    i= 3
                elif bot_cell[2]=='5':
                    i= 4  
                elif bot_cell[2]=='6':
                    i= 5
                elif bot_cell[2]=='7':
                    i= 6  
                elif bot_cell[2]=='8':
                    i= 7
                elif bot_cell[2]=='9':
                    i= 8
                elif bot_cell[2]=='10':
                    i= 9
                elif bot_cell[2]=='11':
                    i= 10  
                elif bot_cell[2]=='12':
                    i= 11
                elif bot_cell[2]=='13':
                    i= 12   
                elif bot_cell[2]=='14':
                    i= 13
                elif bot_cell[2]=='15':
                    i= 14  
                elif bot_cell[2]=='16':
                    i= 15
                elif bot_cell[2]=='17':
                    i= 16
                elif bot_cell[2]=='18':
                    i= 17
                elif bot_cell[2]=='19':
                    i= 18  
                elif bot_cell[2]=='20':
                    i= 19
                elif bot_cell[2]=='21':
                    i= 20      
                elif bot_cell[2]=='22':
                    i= 21
                elif bot_cell[2]=='23':
                    i= 22   
                elif bot_cell[2]=='24':
                    i= 23
                elif bot_cell[2]=='25':
                    i= 24      
                elif bot_cell[2]=='26':
                    i= 25
                elif bot_cell[2]=='27':
                    i= 26
                elif bot_cell[2]=='28':
                    i= 27      
                elif bot_cell[2]=='29':
                    i= 28
                elif bot_cell[2]=='30':
                    i= 29
                   

                car[0]= project_1[n][i][j]
                project_1[n][i][j]= 0

                return car, project_1

def del_cont_carr(bot_cell):
                n= None
                j= None
                i= None

                if bot_cell[0]=='A':
                    n= 0
                elif bot_cell[0]=='B':
                    n= 1
                elif bot_cell[0]=='C':
                    n= 2
                
                if bot_cell[1]=='X':
                    j= 0
                elif bot_cell[1]=='Y':
                    j= 1
                elif bot_cell[1]=='Z':
                    j= 2

                if bot_cell[2]=='1':                        
                    i= 0
                elif bot_cell[2]=='2':
                    i= 1
                elif bot_cell[2]=='3':
                    i= 2  
                elif bot_cell[2]=='4':
                    i= 3
                elif bot_cell[2]=='5':
                    i= 4  
                elif bot_cell[2]=='6':
                    i= 5
                elif bot_cell[2]=='7':
                    i= 6  
                elif bot_cell[2]=='8':
                    i= 7
                elif bot_cell[2]=='9':
                    i= 8
                elif bot_cell[2]=='10':
                    i= 9
                elif bot_cell[2]=='11':
                    i= 10  
                elif bot_cell[2]=='12':
                    i= 11
                elif bot_cell[2]=='13':
                    i= 12   
                elif bot_cell[2]=='14':
                    i= 13
                elif bot_cell[2]=='15':
                    i= 14  
                elif bot_cell[2]=='16':
                    i= 15
                elif bot_cell[2]=='17':
                    i= 16
                elif bot_cell[2]=='18':
                    i= 17
                elif bot_cell[2]=='19':
                    i= 18  
                elif bot_cell[2]=='20':
                    i= 19
                elif bot_cell[2]=='21':
                    i= 20      
                elif bot_cell[2]=='22':
                    i= 21
                elif bot_cell[2]=='23':
                    i= 22   
                elif bot_cell[2]=='24':
                    i= 23
                elif bot_cell[2]=='25':
                    i= 24      
                elif bot_cell[2]=='26':
                    i= 25
                elif bot_cell[2]=='27':
                    i= 26
                elif bot_cell[2]=='28':
                    i= 27      
                elif bot_cell[2]=='29':
                    i= 28
                elif bot_cell[2]=='30':
                    i= 29
                   

                project_1[n][i][j]= carr[0]
                carr[0]= 0

                return carr, project_1

def del_cont_train(bot_cell):
                bot_cell= list(bot_cell)
                if len(bot_cell)==4:
                    by= bot_cell[2]+bot_cell[3]
                    bot_cell.pop(3)
                    bot_cell.pop(2)
                    bot_cell.insert(2, by)
                n= None
                j= None
                i= None

                if bot_cell[0]=='A':
                    n= 0
                elif bot_cell[0]=='B':
                    n= 1
                elif bot_cell[0]=='C':
                    n= 2
                
                if bot_cell[1]=='X':
                    j= 0
                elif bot_cell[1]=='Y':
                    j= 1
                elif bot_cell[1]=='Z':
                    j= 2

                if bot_cell[2]=='1':                        
                    i= 0
                elif bot_cell[2]=='2':
                    i= 1
                elif bot_cell[2]=='3':
                    i= 2  
                elif bot_cell[2]=='4':
                    i= 3
                elif bot_cell[2]=='5':
                    i= 4  
                elif bot_cell[2]=='6':
                    i= 5
                elif bot_cell[2]=='7':
                    i= 6  
                elif bot_cell[2]=='8':
                    i= 7
                elif bot_cell[2]=='9':
                    i= 8
                elif bot_cell[2]=='10':
                    i= 9
                elif bot_cell[2]=='11':
                    i= 10  
                elif bot_cell[2]=='12':
                    i= 11
                elif bot_cell[2]=='13':
                    i= 12   
                elif bot_cell[2]=='14':
                    i= 13
                elif bot_cell[2]=='15':
                    i= 14  
                elif bot_cell[2]=='16':
                    i= 15
                elif bot_cell[2]=='17':
                    i= 16
                elif bot_cell[2]=='18':
                    i= 17
                elif bot_cell[2]=='19':
                    i= 18  
                elif bot_cell[2]=='20':
                    i= 19
                elif bot_cell[2]=='21':
                    i= 20      
                elif bot_cell[2]=='22':
                    i= 21
                elif bot_cell[2]=='23':
                    i= 22   
                elif bot_cell[2]=='24':
                    i= 23
                elif bot_cell[2]=='25':
                    i= 24      
                elif bot_cell[2]=='26':
                    i= 25
                elif bot_cell[2]=='27':
                    i= 26
                elif bot_cell[2]=='28':
                    i= 27      
                elif bot_cell[2]=='29':
                    i= 28
                elif bot_cell[2]=='30':
                    i= 29

                train[0]= project_1[n][i][j]
                project_1[n][i][j]= 0

                return train, project_1

def del_cont_trainn(bot_cell):
                n= None
                j= None
                i= None

                if bot_cell[0]=='A':
                    n= 0
                elif bot_cell[0]=='B':
                    n= 1
                elif bot_cell[0]=='C':
                    n= 2
                
                if bot_cell[1]=='X':
                    j= 0
                elif bot_cell[1]=='Y':
                    j= 1
                elif bot_cell[1]=='Z':
                    j= 2

                if bot_cell[2]=='1':                        
                    i= 0
                elif bot_cell[2]=='2':
                    i= 1
                elif bot_cell[2]=='3':
                    i= 2  
                elif bot_cell[2]=='4':
                    i= 3
                elif bot_cell[2]=='5':
                    i= 4  
                elif bot_cell[2]=='6':
                    i= 5
                elif bot_cell[2]=='7':
                    i= 6  
                elif bot_cell[2]=='8':
                    i= 7
                elif bot_cell[2]=='9':
                    i= 8
                elif bot_cell[2]=='10':
                    i= 9
                elif bot_cell[2]=='11':
                    i= 10  
                elif bot_cell[2]=='12':
                    i= 11
                elif bot_cell[2]=='13':
                    i= 12   
                elif bot_cell[2]=='14':
                    i= 13
                elif bot_cell[2]=='15':
                    i= 14  
                elif bot_cell[2]=='16':
                    i= 15
                elif bot_cell[2]=='17':
                    i= 16
                elif bot_cell[2]=='18':
                    i= 17
                elif bot_cell[2]=='19':
                    i= 18  
                elif bot_cell[2]=='20':
                    i= 19
                elif bot_cell[2]=='21':
                    i= 20      
                elif bot_cell[2]=='22':
                    i= 21
                elif bot_cell[2]=='23':
                    i= 22   
                elif bot_cell[2]=='24':
                    i= 23
                elif bot_cell[2]=='25':
                    i= 24      
                elif bot_cell[2]=='26':
                    i= 25
                elif bot_cell[2]=='27':
                    i= 26
                elif bot_cell[2]=='28':
                    i= 27      
                elif bot_cell[2]=='29':
                    i= 28
                elif bot_cell[2]=='30':
                    i= 29

                project_1[n][i][j]= trainn[0]
                trainn[0]= 0

                return trainn, project_1

operation= input("Choose an operation: Take or Add => ")

if operation== "Take":         #Full correct
    cont_num= int(input('Enter a container number: '))

    cell_abc= abc(cont_num)
    cell_xyz= xyz(cont_num)
    cell_123= n123(cont_num)
    cell= cell_abc+cell_xyz+cell_123
    print(cell)

    bot_cell= list(cell)
    # print(bot_cell)
    higher_cell= fhlfc(bot_cell)
    # print(higher_cell)
    higher_cel= higher_cell.replace(' ', '')
    higher_cel= higher_cel.replace(' ', '')
    higher_cel2=higher_cel.split(',')
    print(higher_cel)
    list_h_cell= list(higher_cell)

    if len(list_h_cell)==10:        
        list_23= list_h_cell[2]+list_h_cell[3]
        list_89= list_h_cell[8]+list_h_cell[9]
        list_h_cell.pop(3)
        list_h_cell.pop(2)
        list_h_cell.pop(7)
        list_h_cell.pop(6)
        list_h_cell.insert(2, list_23)
        list_h_cell.insert(7, list_89)
        # print(list_h_cell)
    
    if len(list_h_cell)==4:
                cel2= list_h_cell[2]+list_h_cell[3]
                list_h_cell.pop(3)
                list_h_cell.pop(2)
                list_h_cell.insert(2, cel2)
    h_cell= empty_cell_hc(bot_cell, list_h_cell)
    h_cell= cor_empty_cell_hc(h_cell)
    print(h_cell)

    h2_cell= h_cell.split(',')
    if len(h2_cell)>=2:
        if h2_cell[1]=='':
            h2_cell.remove('')
    # print(h2_cell)            #['14', '23']

    if higher_cell=='No containers were found above':
        a_= 2+2
    elif len(h2_cell)==2:   #full correct                   
            empty_cells= find_empty_cells(project_1) #correct ['CX1', 'CX2', 'BX1', 'CZ1']
            print(empty_cells)

            empty_cells= np.array(empty_cells)

            cell_selectionn= input('Select a cell to rearrange: ')               #'BX1' =bot_cell
            cell_selection= list(cell_selectionn)
            # print(cell_selection)
            if len(cell_selection)==4:
                cel2= cell_selection[2]+cell_selection[3]
                cell_selection.pop(3)
                cell_selection.pop(2)
                cell_selection.insert(2, cel2)
                # print(len(cell_selection))
            
            lower_cell= flower(cell_selection)
            cell_selection_list= list(lower_cell)
            if len(cell_selection_list)==4:
                cells= cell_selection_list[2]+cell_selection_list[3]
                cell_selection_list.pop(3)
                cell_selection_list.pop(2)
                cell_selection_list.insert(2, cells)
            if len(cell_selection_list)==10:      
                list_23= cell_selection_list[2]+cell_selection_list[3]
                list_89= cell_selection_list[8]+cell_selection_list[9]
                cell_selection_list.pop(3)
                cell_selection_list.pop(2)
                cell_selection_list.pop(7)
                cell_selection_list.pop(6)
                cell_selection_list.insert(2, list_23)
                cell_selection_list.insert(7, list_89)
            
            correct_e= correct_empty_cells(cell_selection_list)
            print(correct_e)                                        #correct
            if correct_e=='Empty cell not found':
                raise ValueError(f'{correct_e}')
            elif correct_e=='There is no container under the selected cell':
                raise ValueError(f'{correct_e}')
            # print(higher_cel2)
            if len(cell_selection)==10:        
                list_23= cell_selection[2]+cell_selection[3]
                list_89= cell_selection[8]+cell_selection[9]
                cell_selection.pop(3)
                cell_selection.pop(2)
                cell_selection.pop(7)
                cell_selection.pop(6)
                cell_selection.insert(2, list_23)
                cell_selection.insert(7, list_89)
            perrr= perp1(h2_cell, higher_cel2)
            print(perrr)         

            empty_cells= find_empty_cells(project_1) #correct ['CX1', 'CX2', 'BX1', 'CZ1']
            print(empty_cells)

            empty_cells= np.array(empty_cells)

            cell_selectionn= input('Select a cell to rearrange: ')               #'BX1' =bot_cell
            cell_selection= list(cell_selectionn)
            # print(cell_selection)
            if len(cell_selection)==4:
                cel2= cell_selection[2]+cell_selection[3]
                cell_selection.pop(3)
                cell_selection.pop(2)
                cell_selection.insert(2, cel2)
                # print(len(cell_selection))

            lower_cell= flower(cell_selection)
            cell_selection_list= list(lower_cell)
            if len(cell_selection_list)==4:
                cells= cell_selection_list[2]+cell_selection_list[3]
                cell_selection_list.pop(3)
                cell_selection_list.pop(2)
                cell_selection_list.insert(2, cells)
            if len(cell_selection_list)==10:       
                list_23= cell_selection_list[2]+cell_selection_list[3]
                list_89= cell_selection_list[8]+cell_selection_list[9]
                cell_selection_list.pop(3)
                cell_selection_list.pop(2)
                cell_selection_list.pop(7)
                cell_selection_list.pop(6)
                cell_selection_list.insert(2, list_23)
                cell_selection_list.insert(7, list_89)
            
            correct_e= correct_empty_cells(cell_selection_list)
            print(correct_e)                                        #correct
            if correct_e=='Empty cell not found':
                raise ValueError(f'{correct_e}')
            elif correct_e=='There is no container under the selected cell':
                raise ValueError(f'{correct_e}')
            
            if len(cell_selection)==10:        
                list_23= cell_selection[2]+cell_selection[3]
                list_89= cell_selection[8]+cell_selection[9]
                cell_selection.pop(3)
                cell_selection.pop(2)
                cell_selection.pop(7)
                cell_selection.pop(6)
                cell_selection.insert(2, list_23)
                cell_selection.insert(7, list_89)
            perrr= perp2(h2_cell, higher_cel2)
            print(perrr)  
    elif len(h2_cell)==1:   #full correct
            empty_cells= find_empty_cells(project_1) #correct ['CX1', 'CX2', 'BX1', 'CZ1']
            print(empty_cells)

            empty_cells= np.array(empty_cells)

            cell_selectionn= input('Select a cell to rearrange: ')               #'BX1' =bot_cell
            cell_selection= list(cell_selectionn)
            # print(cell_selection)
            if len(cell_selection)==4:
                cel2= cell_selection[2]+cell_selection[3]
                cell_selection.pop(3)
                cell_selection.pop(2)
                cell_selection.insert(2, cel2)
                # print(len(cell_selection))

            lower_cell= flower(cell_selection)
            cell_selection_list= list(lower_cell)
            if len(cell_selection_list)==4:
                cells= cell_selection_list[2]+cell_selection_list[3]
                cell_selection_list.pop(3)
                cell_selection_list.pop(2)
                cell_selection_list.insert(2, cells)
            if len(cell_selection_list)==10:       
                list_23= cell_selection_list[2]+cell_selection_list[3]
                list_89= cell_selection_list[8]+cell_selection_list[9]
                cell_selection_list.pop(3)
                cell_selection_list.pop(2)
                cell_selection_list.pop(7)
                cell_selection_list.pop(6)
                cell_selection_list.insert(2, list_23)
                cell_selection_list.insert(7, list_89)
            
            correct_e= correct_empty_cells(cell_selection_list)
            print(correct_e)                                        #correct
            if correct_e=='Empty cell not found':
                raise ValueError(f'{correct_e}')
            elif correct_e=='There is no container under the selected cell':
                raise ValueError(f'{correct_e}')
            
            if len(cell_selection)==10:      
                list_23= cell_selection[2]+cell_selection[3]
                list_89= cell_selection[8]+cell_selection[9]
                cell_selection.pop(3)
                cell_selection.pop(2)
                cell_selection.pop(7)
                cell_selection.pop(6)
                cell_selection.insert(2, list_23)
                cell_selection.insert(7, list_89)
            perrr= perp1(h2_cell, higher_cel2)
            print(perrr)
    car= np.array([0])
    train= np.array([0])
    transpor= input('Transport for loading(Train or Car):  ')
    if transpor=='Car' or 'car':
        to_car= del_cont_car(bot_cell)
        print(to_car)
    elif transpor=='Train' or 'train':
        to_train= del_cont_train(bot_cell)
        print(to_train)
elif operation=="Add":          #Full correct
    trasport= input('Select transport: Train or Car => ')
    carr=[0]
    carr= np.array(carr)
    trainn= [0]
    trainn= np.array(trainn)

    empty_cells= find_empty_cells(project_1) #correct ['CX1', 'CX2', 'BX1', 'CZ1']
    print(empty_cells)
    empty_cells= np.array(empty_cells)

    cell_selectionn= input('Select a cell to add: ')               #'BX1' =bot_cell
    cell_selection= list(cell_selectionn)
    cel2= cell_selection[-2:]
    if len(cell_selection)==4:
        cell_selection.pop(-2)
        cell_selection.pop(-1)
        cel2= ''.join(cel2)
        cell_selection.append(cel2)

    lower_cell= flower(cell_selection)
    #print(lower_cell)           #correct            return   AX1, BX1
    cell_selection_list= list(lower_cell)
    correct_e= correct_empty_cells(cell_selection_list)
    print(correct_e)

    if correct_e=='Empty cell not found':
        raise ValueError(f'{correct_e}')
    elif correct_e=='There is no container under the selected cell':
        raise ValueError(f'{correct_e}')
    
    if trasport== 'Car' or 'car':
        carr[0]= int(input('Container number: '))
        to_car= del_cont_carr(cell_selection)
        print(to_car)
    elif trasport== 'Train' or 'train':
        trainn[0]= int(input('Container number: '))
        to_train= del_cont_trainn(cell_selection)
        print(to_train)