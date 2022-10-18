
import math

import numpy as np



def probposicion(n,v):
    a = len(v)
    b = 0 
    for i in range(a):
        b = b + (modulocmplx(v[i]))**2
    b = math.sqrt(b)

    probabilidad =  (modulocmplx(v[n]**2))/b**2
    return probabilidad

def probtrans(v1,v2):
    a = len (v1)
    b = [(0,0)] * a 

    for i in range(a):
        b[i] = conjugadocmplx(v2[i])
    
    c =  (0,0)
    for j in range(a):  
        c = sumacmplx (c, multiplicarcmplx(v1[j],b[j]))

    return c 

#segunda parte

def varianza(m1,v):

    tam = len(v)
    
    matrizM = [[(0,0) for _ in range (tam)]for _ in range (tam)]
    vari = (0,0)
    a = [[(0,0) for _ in range (tam)]for _ in range (tam)] 
    b = [(0,0)]*tam 
    c = [(0,0)]*tam
    d = [(0,0)]*tam

    for i in range (tam):
        d[i] =v[i]
    m = (0,0)
    if matriz_hermitania == True:  
        b = accion_M_V(m1,v)

        for i in range (tam):
            c[i] = conjugadocmplx(b[i])
        for j in range(tam):  
            m = sumacmplx(m,multiplicarcmplx(c[j],v[j]))
        mame = multi_escalar_m(dia(tam),m)

        a = restacmplx (m1,mame)
        a = producto_matrices(a,a)

        for k in range (tam):
            v[k]=conjugadocmplx(v[k])
        v = accion_M_V(traspuesta_mv(a),v)
        for n in range(tam):
            vari = sumacmplx(vari,multiplicarcmplx(v[n],d[n]))
    return vari 

def vaLPropio (m1,x):
    tam = len (m1)
    a = [(0,0)]*tam
    b = [[(0,0) for _ in range (tam)]for _ in range (tam)]
    c = [[(0,0) for _ in range (tam)]for _ in range (tam)]
    
    for i in range(tam):
        a[i] = conjugadocmplx(a[i])
    for j in range (tam):
        for k in range (tam):
            for n in range (tam):
                b [j][k] = m1[j][k]
    mat  = np.array(m)
    valp, vecp = np.linalg.eig(mat)

    for i in range(tam): 
        for j in range(tam):
            c [j][i] = (a[i]*vecp[i])
    return valp

def probeig(m1,s):

    val,vec = vaLPropio(m1)
    prob = [0 for _ in range(len(vec))]

    for i in range(len(vec)): 
        a = abs(np.dot(s,vec[i]))
        prob [i] = a  
    return a

# tercera parte

def cuaun(m1,m2):
    tam = len(m1)
    z = [[(0,0) for _ in range (tam)]for _ in range (tam)]

    if  matriz_unitaria(m1)and matriz_unitaria(m2) == True:

        z = producto_matrices(traspuesta_mv(m1),m2)
        if matriz_unitaria(z):
            print("el producto es unitario")

        else:
            print("el producto no es unitario")

    else: 
        print("no son unitariaas")

def cuado(m1,c,m2):

    tam = len (m1)
    mat = [[(0,0) for _ in range (tam)]for _ in range (tam)]
    mat = m1  
    for i in range(c-1):
        mat = producto_matrices(mat,m1)
    vecp = accion_M_V(mat,m2)
    print(vecp)

def cindo (m1,m2):
    tamx = len(m1)
    tamy = len(m2)
    a = 0 
    tamcomp = tamx*tamy
    b =[(0,0)]*tamcomp
    for i in range(tamx):
        for j in range(tamy):
            b[a] = producto_matrices(m1[i],m2[j])
            a+=1
    print(b)

def cintre (v):
    a = 1
    b = 1 
    c = 1
    d = 1
    if v[0] == 0:
        a =0
        b=0

    if v[1] == 0:
        a = 0
        d =0 

    if v[2]== 0:
        c = 0 
        b = 0
    if v[3]==0:
        c = 0
        d = 0

    if a ==1 or b ==1 or c ==1 or d == 1 : 

        print("es separab")

    else : 
        print("no es separable")

if __name__ == '__main__':
        #punto 4.4.1
    x = [[(0,0),(1,0)],
         [(1,0),(0,0)]]
    z = [[((2**(1/2)/2),0),((2**(1/2)/2),0)],
         [((2**(1/2)/2),0),(-(2**(1/2)/2),0)]]
    #cuatroUno(x,z)

        #punto 4.4.2
    x = [[(0,0),(1/(2**(1/2)),0),(1/(2**(1/2)),0),(0,0)],
         [(1/(2**(1/2)),0),(0,0),(0,0),(1/(2**(1/2)),0)],
         [(1/(2**(1/2)),0),(0,0),(0,0),(1/(2**(1/2)),0)],
         [(0,0),(1/(2**(1/2)),0),(-1/(2**(1/2)),0),(0,0)]]
    v = [(1,0),(0,0),(0,0),(0,0)]
    #cuatroDos(x,3,v)

#--------------------------------------------------------------------------------------------------DE AQUI PARA ABAJO SOLO SON LAS FUNCIONES NECESARIAAS PARA QUE FUNCIONE EL PROGRAMA (no lograba llamar la libreria :´c)

def sumacmplx(c1, c2):
    real = c1[0] + c2[0]
    img = c1[1] + c2[1]
    return [real, img]


def restacmplx(c1, c2):
    real = c1[0] - c2[0]
    img = c1[1] - c2[1]
    return [real, img]

def multiplicarcmplx(c1, c2):
    real = c1[0] * c2[0] + (-1 * c1[1] * c2[1])
    img = c1[0] * c2[1] + c1[1] * c2[0]
    return [real, img]



def modulocmplx(c1):
    mod = ((c1[0] ** 2) + (c1[1] ** 2)) ** 0.5
    return mod

def conjugadocmplx(c1):
    conjugado = (c1[0], -1 * c1[1])
    return (conjugado)

def norma_V(v1):
    a = len(v1)
    b = (0,0)
    for i in range (a):
        b = sumacmplx(multiplicarcmplx(v1[i],v1[i]),b)
    b = modulocmplx(b)
    return b 

def accion_M_V(m1,v1):
    a = len (m1)
    b = [(0,0)] * a
    for i in range (a):
        for j in range (a):
            a[i] = LC.sumacmplx(a[i],LC.multiplicarcmplx(m1[i][j],v1[j]))
    
    return a 


def producto_matrices(m1,m2):
    a = len(m1)
    b = len(m2)
    c = [[(0,0)for i in range (b)] for i in range(a) ]
    for i in range (a):
        for j in range (b):
            for k in range(a):
                a[i][j] = sumacmplx(c[i][j],multiplicarcmplx(m1[i][k],m2[k][j]))

    return a 

def resta_mc(m1, m2):
    a = len(m1)
    b = len(m1[0])
    filas = [(0,0)]*b
    suma = [filas]*a
    for i in range(a):
        filas =  [(0,0)]*b
        suma[i] = filas
        for j in range(b):
            suma[i][j] = restacmplx(m1[i][j],m2[i][j])
    return suma 

def multi_escalar_m(m1):
    escalar = int (input("escalar ="))
    e = escalar
    a = len(m1)
    b = len(m1[0])
    filas = [(0,0)] * b
    multiE = [filas] * a
    for i in range(a):
        filas = [(0,0)] * a
        multiE[i] = filas

        for j in range(b):
            multiE[i][j] = multiplicarcmplx((e,0),m1[i][j])
    return multiE

def traspuesta_mv(mv):
    a = len(mv)
    b = len(mv[0])
    filas = [(0,0)] * b
    traspuesta = [filas] * a 
    for i in range (a):
        filas = [(0,0)] * b
        traspuesta[i] = filas
        for j in range (b):
            traspuesta[i][j] = mv[j][i]
    return traspuesta


def conjugada_mv (mv):
    a = len(mv)
    b = len(mv[0])
    filas = [(0,0)] * b
    conjugada = [filas] * a
    for i in range(a):
        filas = [(0,0)] * a
        conjugada[i] = filas 
        for j in range(b):
            conjugada[i][j] = conjugadocmplx(mv[i][j])
    return conjugada

def adjunta_mv(mv):
    a = len (mv)
    b = len(mv[0])
    filas = [(0,0)] * b
    adjunta = [filas] * a
    c= conjugada_mv(traspuesta_mv(mv))
    for i in range(a):
        filas = [(0,0)] * b
        adjunta[i] = filas
        for j in range(b):
            adjunta[i][j] = mv[i][j]
    return adjunta

def accion_M_V(m1,v1):
    a = len (m1)
    b = [(0,0)] * a
    for i in range (a):
        for j in range (a):
            a[i] = sumacmplx(a[i],multiplicarcmplx(m1[i][j],v1[j]))
    
    return a 

def matriz_hermitania(m1):
    a = len(m1)
    b = [[(0,0)for i in range (a)]for i in range (a)]
    b = adjunta_mv(m1)
    c = a == m1
    return c

        
def matriz_unitaria(m1):
    a = len(m1)
    b = [[(0,0)for i in range (a)]for i in range (a)]
    c = [[(0,0)for i in range (a)]for i in range (a)]
    for i in range (a):
        b = producto_matrices(adjunta_mv(m1),m1)
    for i in range (a):
        c [i][i] =(1,0)
    d = a ==c
    return d


