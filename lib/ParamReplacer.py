from urllib.parse import urlparse
from re import findall
class ParamReplace:
    def __init__(self):
        pass
    
    def replacement(self, parameter: str, value: str, replace_str: str):
        c_counter  = []
        par_var = []
        counter = 0
        while counter != len(parameter):
            temp = value[counter]
            for i in range(len(parameter)):
                value[counter] = replace_str
                c_counter.append(parameter[i] + '=' + value[i])
            par_var.append(c_counter)
            value[counter] = temp
            counter += 1
            c_counter = []
        return par_var

    def gen_url(self, half_url: str, xdata: str):
        url_var = []
        for each in xdata:
            if half_url[-1] != "?":
                url_var.append(half_url + '?' + str("&".join(each)))
            else:
                url_var.append(half_url + str("&".join(each)))
        return url_var

    def expand_parameter(self, query_data: str) -> tuple:
        p,q = [],[]
        for parameters,values in findall(r'([^&]+)=([^&]+)', query_data):
            p.append(parameters)
            q.append(values)
        if len(p) != len(q):
            return False,False
        else:
            return p,q

    def auto(self, upto_path_url, ppath, payload):
        apath, bpath = self.expand_parameter(ppath)
        xpath = self.replacement(apath, bpath, payload)
        ypath = self.gen_url(upto_path_url, xpath)
        return ypath

