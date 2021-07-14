import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
array = [[120,3,2,2,3,4,6], 
        [2,122,7,1,3,2,3], 
        [4,2,119,3,5,3,4], 
        [2,1,1,124,2,1,9], 
        [5,3,4,3,121,2,2], 
        [2,6,3,1,3,123,2], 
        [6,4,3,5,0,1,121]]
df_cm = pd.DataFrame(array, index = ['Afraid','Angry','Disgusted','Happy','Neutral','Sad','Surprised'],
                  columns = ['AFRAID','ANGRY','DISGUSTED','HAPPY','NEUTRAL','SAD','SURPRISED'])
plt.figure(figsize = (10,5))
ax=sn.heatmap(df_cm, annot=True, annot_kws={"size":18}, cmap="GnBu",fmt='g', vmax=14, cbar=0)
ax.set(xlabel='PREDICTED EMOTIONS', ylabel='TRUE EMOTIONS',title='CONFUSION MATRIX FOR VENTURI ARCHITECTURE',fontsize=20,font='sans-serif')
plt.show()
#sn.set(font_scale=1.4)#for label size
#sn.heatmap(df_cm, annot=True,annot_kws={"size": 16})# font size
#'Afraid','Angry','Disgusted','Happy','Neutral','Sad','Surprised'
#'AFRAID','ANGRY','DISGUSTED','HAPPY','NEUTRAL','SAD','SURPRISED'