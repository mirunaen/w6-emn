def range(start,stop=None,step=1):
  if stop is None:
    stop = start 
    start = 0
  rn = []
  while start < stop:
    rn +=start
    start += step 
  return rn