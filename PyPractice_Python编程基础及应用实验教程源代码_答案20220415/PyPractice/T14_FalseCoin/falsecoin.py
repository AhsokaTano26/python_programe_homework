

###############二分法查找轻的假硬币##############

def find_false_coin_recursive(coin_weight_list, start_idx, length): 
       #递归法二分查找较轻的假币
       #输入为：硬币重量序列， 待判断硬币序列的第一个硬币下标索引， 待判断硬币的总个数
    if length == 1: #如果待判断硬币为1个
        return start_idx #则该硬币为假币

    half_length = length // 2  #待判断硬币长度 的一半， 此处用整数，是待判断硬币个数有可能不能平均分成两堆
    left_half_weight = sum( coin_weight_list[start_idx : start_idx + half_length])  # 左边堆硬币的总重量,注意下标的范围
    right_half_weight = sum(coin_weight_list[start_idx + half_length : start_idx + half_length + half_length]) #右边堆硬币的总重量，注意下标的范围
    if left_half_weight < right_half_weight : #如果左边堆硬币更轻
        return find_false_coin_recursive(coin_weight_list, start_idx, half_length) #则假币在左边堆硬币，递归调用本函数找出假币
    if left_half_weight > right_half_weight: #如果右边堆硬币更轻
        return find_false_coin_recursive(coin_weight_list, start_idx + half_length , half_length) #则假币在右边堆硬币， 递归调用本函数找出假币
    if left_half_weight == right_half_weight and half_length * 2 == length: #如果左边堆和右边堆一样轻，且待判断硬币能均分
        return None #则没有假币
    else:
        return start_idx + length - 1 #否则假币为待判断硬币序列的最后一个硬币

if __name__ == '__main__':
    coins  = [100, 100, 100, 100, 100, 100, 100, 100,  0, 100]
    r = find_false_coin_recursive(coins, 0, len(coins))
    print(('False coin idx by recursive: %d, weight: %d'% (r,coins[r]) ) if r != None else "No false coin")    


##二分法非递归调用查找较轻的假币
def find_false_coin_not_recursive(coin_weight_list): 
      #非递归调用二分法查找较轻的假币，即将硬币等分成 左边堆、右边堆        
      #输入硬币的重量列表
    left_idx = 0 #初始化待查找硬币序列的第一个硬币下标索引为0
    right_idx = len(coin_weight_list) - 1 #初始化待查找硬币序列的最后一个硬币的下标索引为最后一个硬币

    while left_idx != right_idx: #如果待查找硬币序列的不止1个（待查找硬币序列的第一个硬币的索引下标 不等于 待查找硬币序列的最后一个硬币的索引下标）
        checking_coins_number = left_idx + right_idx + 1 #计算待查找硬币序列的硬币个数
        if checking_coins_number % 2 == 0 :  #若被检查硬币有偶数个
                                             #划分方案为： 左边堆（左边堆）  ||  右边堆（右边堆）
            middle_idx =  (left_idx + right_idx) // 2 #二分得到的中间硬币的索引下标
            weight_left = sum(coin_weight_list[ left_idx : (middle_idx + 1) ]) #左边堆硬币的总重量
            weight_right = sum(coin_weight_list[middle_idx + 1 : right_idx + 1]) #右边堆硬币的总重量
            if weight_left < weight_right : #如果左边堆硬币更轻
                right_idx = middle_idx  #则更新待查找硬币序列的最后一个硬币的索引下标为中间点硬币的索引下标
            elif weight_left > weight_right: #如果右边堆硬币更轻
                left_idx  = middle_idx + 1 #则更新待查找硬币序列的第一个硬币的索引下标为中间点硬币的索引下标 + 1
            else:
                return None #若左边堆硬币和右边堆硬币一样重，则没有假币
        else:   #被检查硬币有奇数个
                #划分方案为：  左边堆   中间个  右边堆
            middle_idx = int((left_idx + right_idx) / 2)  #左边堆硬币的最后一个硬币索引
            weight_left = sum(coin_weight_list [ left_idx : middle_idx]) #左边堆硬币的总重量

            weight_right = sum(coin_weight_list[ middle_idx + 1 : right_idx + 1 ]) #右边堆硬币的总重量
            if weight_left == weight_right : #若左边堆硬币和右边堆硬币一样中
                if coin_weight_list[middle_idx] == coin_weight_list[middle_idx + 1]: #若待判断硬币序列的中间硬币和它的前一个硬币一样重
                    return None #则没有假币
                else:
                    return middle_idx #则假币为中间的那个硬币
            elif weight_left > weight_right: #若右边堆硬币更轻
                left_idx  = middle_idx + 1 #则更新待检查硬币的第一个硬币的索引下标为右边堆硬币的第一硬币索引下标
            else: #若左边堆硬币更轻
                right_idx  = middle_idx - 1  # 则更新待检查硬币序列的最后一个硬币的索引下标为左边堆硬币的最后一个硬币的索引下标
        
    return left_idx #当待判断硬币序列只有一个硬币时，该硬币是假币

if __name__ == '__main__':
    # coins  = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    r = find_false_coin_not_recursive(coins)
    print(('False coin idx by not recursive: %d， weight: %d'% (r, coins[r]) ) if r != None else "No false coin")



#######################三分法递归查找更轻的假硬币#############################
def find_false_coin_recursive(coin_weight_list, start_idx, length): #三分法递归查找更轻的假硬币
    # 当数量较少时，手动指定的情形
    if length == 1: #如果待判断硬币是一个硬币
        return start_idx #则这个硬币一定是假币
    if length == 2: #如果待判断硬币是两个硬币
        if coin_weight_list[start_idx] > coin_weight_list[start_idx + 1]: #如果第一个硬币更重
            return start_idx + 1 #则假币是第二个
        else:
            return start_idx  #否则，假币是第一个
    if length == 3: #如果待判断硬币是三个硬币
        if coin_weight_list[start_idx] > coin_weight_list[start_idx + 1]: #如果前两个硬币相比较， 第一个硬币更重
            return start_idx + 1  #则假币是第二个
        elif coin_weight_list[start_idx] < coin_weight_list[start_idx + 1]: #如果前两个硬币相比较， 第二个硬币更重
            return start_idx  #则假币是第一个
        else:
            return start_idx + 2  #否则，假币是第三个

    #如果待判断假币数量是3个以上，则分情况递归调用
    if length % 3 == 0:  #如果待判断硬币数量是3的倍数
        step = length // 3 #则三分法中，每段的长度是 总长度的 三分之一
    else: #如果待判断硬币数不是3的倍数
        step = length // 3 + 1 #则三分法中，每段的长度是 总长度的 三分之一 + 1
    

    first_section_start_idx = start_idx  #第一段硬币的第一个硬币的索引数字
    first_section_end_idx = start_idx + step #第一段的结束硬币的索引数字， 不包含该数字  
    weight_first_section = sum( coin_weight_list[first_section_start_idx : first_section_end_idx]) #第一段硬币的总重量

    middle_section_start_idx = first_section_end_idx  #中间段硬币的开始硬币索引数字
    middle_section_end_idx = middle_section_start_idx + step  # 中间段硬币的结束硬币索引数字， 不包含该数字
    weight_middle_section = sum( coin_weight_list[middle_section_start_idx : middle_section_end_idx ]) #中间段硬币的总重量

    end_section_start_idx = middle_section_end_idx  #最后段硬币的开始硬币索引数字
    end_section_end_idx = start_idx + length #最后段硬币的结束硬币索引数字， 不包含该数字。 注意，最后段的硬币数量并不固定， 有可能比前两段少1个， 可能少2个，
    weight_end_section = sum(coin_weight_list[end_section_start_idx : end_section_end_idx]) #最后段硬币的总重量

    if weight_first_section < weight_middle_section: #如果第一段重量比中间段重量小，则假币在第一段
        length = first_section_end_idx - first_section_start_idx  #第一段硬币的个数
        return find_false_coin_recursive(coin_weight_list,first_section_start_idx,  length) #返回 递归调用查找函数 的查找结果，
    elif weight_first_section > weight_middle_section: #如果中间段重量比第一段重量小， 则假币在中间段
        length = middle_section_end_idx - middle_section_start_idx #中间段硬币的硬币数量
        return find_false_coin_recursive(coin_weight_list, middle_section_start_idx, length) #返回 递归调用查找函数 的查找结果，
    else: #否则，假币在第三段
        length = end_section_end_idx - end_section_start_idx #最后段硬币的硬币数量
        return find_false_coin_recursive(coin_weight_list, end_section_start_idx, length )#返回 递归调用查找函数 的查找结果，
    
if __name__ == '__main__':
    coins  = [0, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    r = find_false_coin_recursive(coins, 0, len(coins))
    print(('False coin idx by recursive: %d, weight: %d'% (r, coins[r])) if r !=None else "No false coin" )



##三分法非递归查找更轻的假硬币
def find_false_coin_not_recursive(coin_weight_list):
    length = len(coin_weight_list)
    start_idx = 0
    
    while length >= 3:  #当待判断硬币数大于3个时， 使用while循环减少待判断硬币数量
        if length % 3 == 0: #如果待判断硬币数正好是3的倍数
            step = length // 3 #则待判断硬币，正好平均分为3份
        else:
            step = length // 3 + 1 #否则，待判断硬币不能平均分为三份，前两份更多，后一份最少

        first_section_start_idx = start_idx  #第一段的初始硬币索引数字
        first_section_end_idx = start_idx + step #第一段的结束硬币索引数字， 不包含该数字  
        weight_first_section = sum( coin_weight_list[first_section_start_idx : first_section_end_idx]) #第一段硬币的总重量

        middle_section_start_idx = first_section_end_idx  #中间段硬币的开始硬币索引数字
        middle_section_end_idx = middle_section_start_idx + step  # 中间段硬币的结束硬币索引数字， 不包含该数字
        weight_middle_section = sum( coin_weight_list[middle_section_start_idx : middle_section_end_idx ]) #中间段硬币的总重量

        end_section_start_idx = middle_section_end_idx  #最后段硬币的开始硬币索引数字
        end_section_end_idx = start_idx + length #最后段硬币的结束硬币索引数字， 不包含该数字。 注意，最后段的硬币数量并不固定， 有可能比前两段个数少1个， 可能少2个，
        weight_end_section = sum(coin_weight_list[end_section_start_idx : end_section_end_idx]) #最后段硬币的总重量

        if weight_first_section < weight_middle_section: #如果第一段重量比中间段重量小，则假币在第一段
            length = first_section_end_idx - first_section_start_idx  #更新待比较硬币的数量为第一段硬币的个数
            start_idx = first_section_start_idx #更新待比较硬币的开始索引下标为第一段硬币的开始坐标
        elif weight_first_section > weight_middle_section: #如果中间段重量比第一段重量小， 则假币在中间段
            length = middle_section_end_idx - middle_section_start_idx #更新待比较硬币的数量为中间段硬币的硬币数量
            start_idx = middle_section_start_idx #更新待比较硬币的开始索引下标 为中间段硬币的开始坐标
        else: #否则，假币在第三段
            length = end_section_end_idx - end_section_start_idx #更新待比较硬币的数量为最后段硬币的硬币数量
            start_idx = end_section_start_idx #更新待比较硬币的开始索引下标 为最后段硬币的开始坐标
    
    # 当待判断数量小于3个时，手动指定假币的下标
    if length == 1: #如果待判断硬币是一个硬币
        return start_idx #则这个硬币一定是假币
    if length == 2: #如果待判断硬币是两个硬币
        if coin_weight_list[start_idx] > coin_weight_list[start_idx + 1]: #如果第一个硬币更重
            return start_idx + 1 #则假币是第二个
        else:
            return start_idx  #否则，假币是第一个


if __name__ == '__main__':
    coins  = [100, 100, 100, 100, 100, 100, 10, 100, 100, 100, 100, 100,100, 100]
    r = find_false_coin_not_recursive(coins)
    print(('False coin idx by not recursive: %d, weight: %d'% (r, coins[r])) if r !=None else "No false coin" )