from progress.bar import ChargingBar

N=10000
bar = ChargingBar('Processing',max=N )
x=1 
for i in range(0,N):
    x+=1
    bar.next()
bar.finish()



from tqdm import tqdm
for i in tqdm(range(0,N)):
    x+=1
   