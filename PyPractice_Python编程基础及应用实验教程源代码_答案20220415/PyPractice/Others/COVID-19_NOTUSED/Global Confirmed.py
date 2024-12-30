from pyecharts import options as opts
from pyecharts.charts import Map, Timeline, Geo, Grid, Bar
from pyecharts.components import Image
from pyecharts.options import ComponentTitleOpts
import csv

# 读取数据
csv_reader = csv.reader(open("covid19_confirmed_global.csv"))
a = 0
data = []

# 创建名字映射字典(用于国家名称语言转换)
nameMap = {
    'Singapore':'新加坡',
    'Dominican Rep.':'多米尼加',
    'Palestine':'巴勒斯坦',
    'Bahamas':'巴哈马',
    'Timor-Leste':'东帝汶',
    'Afghanistan':'阿富汗',
    'Guinea-Bissau':'几内亚比绍',
    "Côte d'Ivoire":'科特迪瓦',
    'Siachen Glacier':'锡亚琴冰川',
    "Br. Indian Ocean Ter.":'英属印度洋领土',
    'Angola':'安哥拉',
    'Albania':'阿尔巴尼亚',
    'United Arab Emirates':'阿联酋',
    'Argentina':'阿根廷',
    'Armenia':'亚美尼亚',
    'French Southern and Antarctic Lands':'法属南半球和南极领地',
    'Australia':'澳大利亚',
    'Austria':'奥地利',
    'Azerbaijan':'阿塞拜疆',
    'Burundi':'布隆迪',
    'Belgium':'比利时',
    'Benin':'贝宁',
    'Burkina Faso':'布基纳法索',
    'Bangladesh':'孟加拉国',
    'Bulgaria':'保加利亚',
    'The Bahamas':'巴哈马',
    'Bosnia and Herz.':'波斯尼亚和黑塞哥维那',
    'Belarus':'白俄罗斯',
    'Belize':'伯利兹',
    'Bermuda':'百慕大',
    'Bolivia':'玻利维亚',
    'Brazil':'巴西',
    'Brunei':'文莱',
    'Bhutan':'不丹',
    'Botswana':'博茨瓦纳',
    'Central African Rep.':'中非',
    'Canada':'加拿大',
    'Switzerland':'瑞士',
    'Chile':'智利',
    'China':'中国',
    'Ivory Coast':'象牙海岸',
    'Cameroon':'喀麦隆',
    'Dem. Rep. Congo':'刚果民主共和国',
    'Congo':'刚果',
    'Colombia':'哥伦比亚',
    'Costa Rica':'哥斯达黎加',
    'Cuba':'古巴',
    'N. Cyprus':'北塞浦路斯',
    'Cyprus':'塞浦路斯',
    'Czech Rep.':'捷克',
    'Germany':'德国',
    'Djibouti':'吉布提',
    'Denmark':'丹麦',
    'Algeria':'阿尔及利亚',
    'Ecuador':'厄瓜多尔',
    'Egypt':'埃及',
    'Eritrea':'厄立特里亚',
    'Spain':'西班牙',
    'Estonia':'爱沙尼亚',
    'Ethiopia':'埃塞俄比亚',
    'Finland':'芬兰',
    'Fiji':'斐',
    'Falkland Islands':'福克兰群岛',
    'France':'法国',
    'Gabon':'加蓬',
    'United Kingdom':'英国',
    'Georgia':'格鲁吉亚',
    'Ghana':'加纳',
    'Guinea':'几内亚',
    'Gambia':'冈比亚',
    'Guinea Bissau':'几内亚比绍',
    'Eq. Guinea':'赤道几内亚',
    'Greece':'希腊',
    'Greenland':'格陵兰',
    'Guatemala':'危地马拉',
    'French Guiana':'法属圭亚那',
    'Guyana':'圭亚那',
    'Honduras':'洪都拉斯',
    'Croatia':'克罗地亚',
    'Haiti':'海地',
    'Hungary':'匈牙利',
    'Indonesia':'印度尼西亚',
    'India':'印度',
    'Ireland':'爱尔兰',
    'Iran':'伊朗',
    'Iraq':'伊拉克',
    'Iceland':'冰岛',
    'Israel':'以色列',
    'Italy':'意大利',
    'Jamaica':'牙买加',
    'Jordan':'约旦',
    'Japan':'日本',
    'Kazakhstan':'哈萨克斯坦',
    'Kenya':'肯尼亚',
    'Kyrgyzstan':'吉尔吉斯斯坦',
    'Cambodia':'柬埔寨',
    'Korea':'韩国',
    'Kosovo':'科索沃',
    'Kuwait':'科威特',
    'Lao PDR':'老挝',
    'Lebanon':'黎巴嫩',
    'Liberia':'利比里亚',
    'Libya':'利比亚',
    'Sri Lanka':'斯里兰卡',
    'Lesotho':'莱索托',
    'Lithuania':'立陶宛',
    'Luxembourg':'卢森堡',
    'Latvia':'拉脱维亚',
    'Morocco':'摩洛哥',
    'Moldova':'摩尔多瓦',
    'Madagascar':'马达加斯加',
    'Mexico':'墨西哥',
    'Macedonia':'马其顿',
    'Mali':'马里',
    'Myanmar':'缅甸',
    'Montenegro':'黑山',
    'Mongolia':'蒙古',
    'Mozambique':'莫桑比克',
    'Mauritania':'毛里塔尼亚',
    'Malawi':'马拉维',
    'Malaysia':'马来西亚',
    'Namibia':'纳米比亚',
    'New Caledonia':'新喀里多尼亚',
    'Niger':'尼日尔',
    'Nigeria':'尼日利亚',
    'Nicaragua':'尼加拉瓜',
    'Netherlands':'荷兰',
    'Norway':'挪威',
    'Nepal':'尼泊尔',
    'New Zealand':'新西兰',
    'Oman':'阿曼',
    'Pakistan':'巴基斯坦',
    'Panama':'巴拿马',
    'Peru':'秘鲁',
    'Philippines':'菲律宾',
    'Papua New Guinea':'巴布亚新几内亚',
    'Poland':'波兰',
    'Puerto Rico':'波多黎各',
    'Dem. Rep. Korea':'朝鲜',
    'Portugal':'葡萄牙',
    'Paraguay':'巴拉圭',
    'Qatar':'卡塔尔',
    'Romania':'罗马尼亚',
    'Russia':'俄罗斯',
    'Rwanda':'卢旺达',
    'W. Sahara':'西撒哈拉',
    'Saudi Arabia':'沙特阿拉伯',
    'Sudan':'苏丹',
    'S. Sudan':'南苏丹',
    'Senegal':'塞内加尔',
    'Solomon Is.':'所罗门群岛',
    'Sierra Leone':'塞拉利昂',
    'El Salvador':'萨尔瓦多',
    'Somaliland':'索马里兰',
    'Somalia':'索马里',
    'Serbia':'塞尔维亚',
    'Suriname':'苏里南',
    'Slovakia':'斯洛伐克',
    'Slovenia':'斯洛文尼亚',
    'Sweden':'瑞典',
    'Swaziland':'斯威士兰',
    'Syria':'叙利亚',
    'Chad':'乍得',
    'Togo':'多哥',
    'Thailand':'泰国',
    'Tajikistan':'塔吉克斯坦',
    'Turkmenistan':'土库曼斯坦',
    'East Timor':'东帝汶',
    'Trinidad and Tobago':'特里尼达和多巴哥',
    'Tunisia':'突尼斯',
    'Turkey':'土耳其',
    'Tanzania':'坦桑尼亚',
    'Uganda':'乌干达',
    'Ukraine':'乌克兰',
    'Uruguay':'乌拉圭',
    'United States':'美国',
    'Uzbekistan':'乌兹别克斯坦',
    'Venezuela':'委内瑞拉',
    'Vietnam':'越南',
    'Vanuatu':'瓦努阿图',
    'West Bank':'西岸',
    'Yemen':'也门',
    'South Africa':'南非',
    'Zambia':'赞比亚',
    'Zimbabwe':'津巴布韦'
}

# 添加时间
for row in csv_reader:
    data.append(row)
time = data[0]
for i in range(3):
    time.pop(0)

# 添加国家
countries = []
for i in range(1,len(data)):
    countries.append(nameMap.get(str(data[i][0])))

# 创建时间线轮播多图
timeLine = Timeline(init_opts=opts.InitOpts(width='100%',height="1000px"))

for i in range(len(time)):
    # 添加单日数据
    dates = []
    for j in range(1,len(data)):
        dates.append(int(data[j][i + 3]))
    
    dataSet = [list(z) for z in zip(countries, dates)]
    dataSet.sort(key = lambda x:x[1], reverse=True)

    # 添加用于坐标图的地理坐标
    coords = []
    for j in range(1,len(data)):
        coords.append([nameMap.get(str(data[j][0])), float(data[j][2]), float(data[j][1]), int(data[j][i + 3])])  # ['国家名称', '纬度', '经度', 确诊人数]
    coords.sort(key = lambda x:x[3], reverse=True)                                              # 按确诊人数从大到小排序

    # 创建坐标图
    geo = Geo()
    # 向坐标图中添加确诊人数前五国家的坐标
    for j in range(5):
        geo.add_coordinate(coords[j][0], coords[j][1], coords[j][2])
    # 坐标图数据及参数设置
    geo.add_schema(maptype='world', is_roam=False, itemstyle_opts={'normal': {'opacity': 0}})
    geo.add('', data_pair=dataSet[0:5], type_='effectScatter', color="red")
    geo.set_series_opts(label_opts=opts.LabelOpts(color='black', position='right', font_weight='bold', formatter='{@[2]}'),
                        tooltip_opts=opts.TooltipOpts(is_show=False))

    # 创建地理图
    map0 = Map()
    map0.add('累计确诊人数',
            dataSet,
            'world',
            is_map_symbol_show=False,
            is_roam=False,
            tooltip_opts=opts.TooltipOpts(is_show=True),
            name_map=nameMap)
    map0.set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                        itemstyle_opts={'normal': {'opacity': 0.8}})                                       
    map0.set_global_opts(title_opts=opts.TitleOpts(title="全球疫情累计确诊人数分布图", 
                                                    subtitle="日期：{}".format(time[i]),subtitle_textstyle_opts=opts.TextStyleOpts(color='red',font_size='14')),
                            legend_opts=opts.LegendOpts(is_show=False),
                            
                            visualmap_opts=opts.VisualMapOpts(max_=10000000,is_show=False,
                                                            range_color=['#6495ED','#00FF00','#FFFF00','#808000','#FF0000','#FF0000','#000000','#000000','#000000']))
    
    # 创建柱状图
    bar = Bar()
    # 顺序重排,使柱状图显示结果从高到低排列
    dataSet_sort = []
    for j in range(5):
        dataSet_sort.append(dataSet[4-j])
    # 柱状图数据及参数设置
    bar.add_xaxis([x for x, y in dataSet_sort])
    bar.add_yaxis("",
                [y for x, y in dataSet_sort],
                color='red',
                itemstyle_opts={'normal': {'opacity': 0.8}})
    bar.set_series_opts(label_opts=opts.LabelOpts(position="right",
                                                color='black',
                                                font_size=10,
                                                font_weight='bold',
                                                formatter='{c}',))                              
    bar.set_global_opts(xaxis_opts=opts.AxisOpts(is_show=False, max_=4e7),
                        yaxis_opts=opts.AxisOpts(is_show=True, axislabel_opts=opts.LabelOpts(font_size=14,font_weight='bold')),
                        title_opts=opts.TitleOpts(title="", pos_top='35%', pos_left='5%',
                                                title_textstyle_opts=opts.TextStyleOpts(font_size=14)),
                        visualmap_opts=opts.VisualMapOpts(is_show=False,
                                                        pos_top='12%',
                                                        pos_left='2%',
                                                        max_=1e7,
                                                        is_piecewise=False,
                                                        dimension=0,
                                                        range_color=['#6495ED','#00FF00','#FFFF00','#808000','#808000','#FF0000','#FF0000','#000000','#000000']))
    bar.reversal_axis()

    # 对单日数据进行多图合并
    grid = Grid(init_opts=opts.InitOpts(theme='chalk', width='100%', height='100%'))
    grid.add(bar, grid_opts=opts.GridOpts(pos_top="50%",pos_left="5%",pos_right="70%"))
    grid.add(map0, grid_opts=opts.GridOpts(pos_top="12%"))
    grid.add(geo, grid_opts=opts.GridOpts(pos_bottom="12%"))
   
    # 添加进时间线
    timeLine.add(grid, time[i])
    # 时间线参数设置
    timeLine.add_schema(play_interval=100, is_auto_play=False, is_loop_play=False, symbol_size=5)

# 导出html文件
timeLine.render("全球疫情累计确诊人数分布图.html")