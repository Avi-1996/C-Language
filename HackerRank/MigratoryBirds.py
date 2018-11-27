# Complete the migratoryBirds function below.
def migratoryBirds(arr):
     a={}
     for x in range(len(arr)):
          if arr[x] not in a:
               a[arr[x]] = 1
          else:
               a[arr[x]]+=1
     count,m,k=0,0,0
     
     for x,v in a.items():
          if v >m:
               m=v
               k=x
     return k
