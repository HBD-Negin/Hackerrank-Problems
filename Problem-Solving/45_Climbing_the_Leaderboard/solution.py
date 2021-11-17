def climbingLeaderboard(ranked, player):
  ranked = sorted(list(set(ranked)), reverse=True)
  player = sorted(player, reverse=True)
  
  l=len(ranked)
  j=0
  
  ans=[]
  for i in range(len(player)):
    while j<l and player[i]<ranked[j]:
      j+=1
    
    ans.append(j+1)
      
  return ans[::-1]

n = int(input())
ranked = list(map(int, input().split()))
m = int(input())
player = list(map(int, input().split()))

res = climbingLeaderboard(ranked, player)
print('\n'.join(map(str, res)))


