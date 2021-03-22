"""
Estudiante: Josue Peña Atencio
Código:     8935601
Fecha:      06/11/2019

Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica.
"""

from sys import stdin

def solve(K, state, A):
  """
  Return uppercase hexadecimal representation of final 
  configuration of bitmask 'state' of length K by applying corresponding switches
  and checks for every query pair (ai, bi) in list A of length M.
  """
  for ai, bi in A:
    li, ri = ai, bi
    _ai, _bi = K-ai, K-bi
    if ((1 << _ai) & state) == 0:
      # Extraer segmento L[1..ai-1]
      lseg = (state >> (_ai))
      if lseg != 0:
        # Calcular distancia desde el lsb de L[1..ai-1] hasta ai
        lsb = (lseg & -lseg).bit_length()-1
        li = ai-lsb
    if ((1 << _bi) & state) == 0:
      # Extraer segmento L[bi+1..K]
      rm = (1 << _bi)-1
      rseg = (state & rm)
      if rseg != 0:
        msb = rseg.bit_length()-1
        # Prender L[bi] y diferenciar L[bi..K] con el msb de L[bi+1..K]
        bi_on = (rseg | (1 << _bi))
        d = (bi_on.bit_length()-1) - msb
        ri = bi+d
    # Hacer flip del segmento L[li..ri]
    s = (ri-li)+1
    m = (1 << s)-1
    m = (m << (K-ri))
    state = state^m
  return state

def main():
  """
  Read input and print final state of initial 
  configuration of bitmask 'init' for each testcase.
  """
  T = int(stdin.readline())
  while T!=0:
    K, M = map(int, stdin.readline().split())
    init, A = int(stdin.readline().strip(), 16), list()
    for i in range(M):
      ai, bi = map(int, stdin.readline().split())
      A.append((ai,bi))
    print(format(solve(K, init, A),'X'))
    T-=1
  
main()
