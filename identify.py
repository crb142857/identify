"""
    编写时间 ： 2021年9月5日19:48:08
    编写人员 ： Chen RunBen
"""


class Identify:
    # 将字符串按照输入标准分割为数类型，以列表形式输出分割后的字符串（可修改）
    def identify(self, infor, standard = ''):
        i = -1
        list_last = []
        list_first = list(infor)
        string = ""
        list_middle = [""]
        list_stan = list(standard)
        for stans in list_stan:
            i += 1
            if str(stans) == "," or str(stans) == "，":
                list_front = list_stan[0: i]
                list_second = list_stan[i + 1: -1]
                list_second.append(list_stan[-1])
        for list_value in list_first:
            if str(list_value) in list_front:
                if string != "":
                    list_middle = list(string)
                if str(list_middle[-1]) not in list_front and str(list_middle[-1]) != "":
                    list_last.append(string)
                    string = ""
                string += str(list_value)
            if str(list_value) in list_second:
                if string != "":
                    list_middle = list(string)
                if str(list_middle[-1]) not in list_second and str(list_middle[-1]) != "":
                    list_last.append(string)
                    string = ""
                string += str(list_value)
        list_last.append(string)
        return list_last

    # 把一组字符串中不为某类型数据筛选出来
    def identify_two(self, infors, standard):
        infors = list(infors)
        string = ''
        list_final = []
        for infor in infors:
            if infor == standard:
                if string:
                    list_final.append(string)
                    string = ''
            else:
                string = string + str(infor)
        if string:
            list_final.append(string)
        return list_final
