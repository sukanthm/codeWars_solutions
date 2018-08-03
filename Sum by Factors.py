def primeFactors(n):
  a=[]
  while n % 2 == 0:
      a.append(2)
      n = n / 2
  for i in range(3,int(abs(n)**0.5)+1,2):
      while n % i== 0:
          a.append(i)
          n = n / i
  if abs(n) > 2:
      a.append(abs(n))
  return list(set(sorted(a)))
def sum_for_list(lst):
  a=[[x,primeFactors(x)] for x in lst]
  b={}
  for x,y in a:
    for z in y:
      if z in b:
        b[z]+=x
      else:
        b[z]=x
  return [[x,b[x]] for x in sorted(b.keys())]
