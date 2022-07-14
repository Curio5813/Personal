def gerarPrimos():
  lim = 700_000 + 1
  p = []
  n_p = set()
  for i in range(2, lim):
    if i in n_p:
      continue
    for k in range(i * 2, lim, i):
      n_p.add(k)
    p.append(i)
  return p

