import itertools

def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

class Ulomek:
    def __init__(self, st, im):
                
        while st % 1 != 0 or im % 1 != 0:
            st *= 10
            im *= 10

        st = int(st)
        im = int(im)

        delitelj = gcd(st, im)
        self.st = int(st / delitelj)
        self.im = int(im / delitelj)

    def __repr__(self):
        return 'Ulomek({0}, {1})'.format(self.st, self.im)

    def __str__(self):
        if self.im != 1:
            return str(self.st) + '/' + str(self.im)
        else:
            return str(self.st)

    def __eq__(self, other):
        return self.st *other.im == self.im * other.st

    def __add__(self, other):
        return Ulomek(self.st * other.im + self.im * other.st, self.im * other.im)

    def __sub__(self, other):
        return Ulomek(self.st * other.im - self.im * other.st, other.im * self.im)

    def __mul__(self, other):
        return Ulomek(self.st * other.st, self.im * other.im)
    
    def __truediv__(self, other):
        return Ulomek(self.st * other.im, self.im * other.st)

    def decimalka(self):
        return self.st / self.im

    def obrni(self):
        self.st, self.im = self.im, self.st
        return self

def enotska_matrika(velikost):
    matrika = []
    for i in range(velikost):
        vrstica = []
        for j in range(velikost):
            if i == j:
                vrstica.append(1)
            else:
                vrstica.append(0)
        matrika.append(vrstica)
    return matrika

def mnozenje_s_skalarjem(matrika, k):
    nova_matrika = []
    if isinstance(k, Ulomek):
        faktor = k
    else:
        faktor = Ulomek(k, 1)
    for vrstica in matrika:
        nova_vrstica = []
        for clen in vrstica:
            novi_clen = clen * faktor
            nova_vrstica.append(novi_clen)
        nova_matrika.append(nova_vrstica)
    return nova_matrika

def sestevanje(prva, druga):
    if len(prva) != len(druga):  
        return 'Matriki nimata enakega števila vrstic.'
    else:
        velikost = len(prva)
        napaka = False
        for vrstica in range(velikost):
            if len(prva[vrstica]) != len(druga[vrstica]):
                napaka = True
        if napaka:
            return 'Matriki nimata enako dolgih stolpcev.'
        else:
            vsota = []
            for i in range(velikost):
                nova_vrstica = []
                for j in range(len(prva[i])):
                     nova_vrstica.append(prva[i][j] +
                                         druga[i][j])
                vsota.append(nova_vrstica)
            return vsota

def vsota_produkti(sez1, sez2):
    '''Vrne vsoto, ki jo dobimo, če soležna člena dveh
    seznamov zmnožimo in jih nato vse seštejemo.'''
    if len(sez1)!= len(sez2):
        return 'Seznama nista enakih dolžin'
    else:
        vsota = Ulomek(0, 1)
        for clen in range(len(sez1)):
            vsota += sez1[clen] * sez2[clen]
        return vsota

def mnozenje(prva, druga):
    if len(prva[0]) != len(druga):
        return 'Množenje ni mogoče.'
    else:
        produkt = []
        druga_trans = transponiranka(druga)
        for i in range(len(prva)):
            nova_vrstica = []
            for j in range(len(druga_trans)):
                nova_vrstica.append(vsota_produkti(prva[i], druga_trans[j]))
            produkt.append(nova_vrstica)
        return produkt

def potenca(matrika, eksponent):
    osnova = matrika
    if eksponent == 0:
        return enotska_matrika(len(matrika))
    elif eksponent > 0:
        for korak in range(eksponent - 1):
            matrika = mnozenje(matrika, osnova)
        return matrika
    elif determinanta(matrika) != Ulomek(0, 1):
        return potenca(inverz(matrika), -eksponent)

def permutacije(n):
    sez = []
    for i in range(n):
        sez.append(i)
    return list(itertools.permutations(sez))

def predznak(perm):
    predznak = 0
    for i, a in enumerate(perm):
        for j, b in enumerate(perm):
            if i < j and a > b:
                predznak += 1
    return (-1) ** predznak

def determinanta(matrika):
    velikost = len(matrika)
    cleni = []
    for p in permutacije(velikost):
        clen = Ulomek(1, 1)
        for i in range(velikost):
            clen *=  matrika[i][p[i]]
        cleni.append(Ulomek(predznak(p), 1) * clen)
    vsota = Ulomek(0, 1)
    for i in cleni:
        vsota += i
    return vsota
        
def prirejenka(matrika):
    velikost = len(matrika)
    nova_matrika = []
    for i in range(velikost):
        nova_vrstica = []
        for j in range(velikost):
            podmat = matrika[:i] + matrika[i+1:]
            for k in range(velikost - 1):
                podmat[k] = podmat[k][:j] + podmat[k][j+1:]
            poddet = Ulomek((-1) ** (i + j), 1) * determinanta(podmat)
            nova_vrstica.append(poddet)
        nova_matrika.append(nova_vrstica)
    return nova_matrika

def transponiranka(matrika):
    st_vrstic = len(matrika)
    st_stolpcev = len(matrika[0])
    nova_matrika = []
    for j in range(st_stolpcev):
        nova_vrstica = []
        for i in range(st_vrstic):
            nova_vrstica.append(matrika[i][j])
        nova_matrika.append(nova_vrstica)
    return nova_matrika

def inverz(matrika):
    if determinanta(matrika) == Ulomek(0, 1):
        return 'Matrika ni obrnljiva.'
    else:
        k = determinanta(matrika).obrni()
        return mnozenje_s_skalarjem(
            transponiranka(prirejenka(matrika)),k
            )

def preberi(shranjena_matrika):
    try:
        with open(shranjena_matrika) as vhod:
            if vhod == '':
                return ''
            else:
                matrika = []
                for vrstica in vhod:
                    matrika.append(vrstica.split('|')[:-1])
                return matrika
    except:
        return ''
                
