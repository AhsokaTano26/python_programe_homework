import folium,os,pandas as pd
from folium.plugins import HeatMap

sanMap = folium.Map(location=[37.76,-122.42], zoom_start=14)  #按经纬度创建旧金山地图
cdata = pd.read_csv('d:/PyPractice/T18_Lib/CrimeData2016.csv')  #读入csv格式的犯罪数据
heatData = cdata[['Y','X']].values.tolist()                   #数据投影-->经纬图热力图数据
HeatMap(heatData).add_to(sanMap)                              #热力图加入地图
sanMap.save("san_map.html")                                   #地图保存为html
os.system("explorer san_map.html")                            #调用浏览器打开html