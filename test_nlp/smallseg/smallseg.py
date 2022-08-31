import re
import os
import sys

class SEG(object):
    def __init__(self):
        _localDir=os.path.dirname(__file__)
        _curpath=os.path.normpath(os.path.join(os.getcwd(),_localDir))
        curpath=_curpath
        self.d = {}
        print("loading dict...",sys.stderr) 
        self.set([x.rstrip() for x in open(os.path.join(curpath,"main.dic"),encoding='utf-8') ])
        #self.specialwords= set([x.rstrip().decode('utf-8') for x in open(os.path.join(curpath,"suffix.dic"),encoding='utf-8')])
        self.specialwords= set([x.rstrip() for x in open(os.path.join(curpath,"suffix.dic"),encoding='utf-8')])
        print('dict ok.',sys.stderr)  
    #set dictionary(a list)
    def set(self,keywords):
        p = self.d  # 以单个字符为索引/存贮，保存为树结构,每个词是倒序处理.  所以分词处理也是倒序处理
        q = {}
        k = ''
        for word in keywords:
            #word = (chr(11)+word).decode('utf-8')
            word = (chr(11)+word)   # chr() 返回值是当前整数对应的 ASCII 字符,  chr(11) 为 垂直制表符， 为什么要加这个固定前缀? 用作结束符,在 cut() 分词时匹配判断使用
            if len(word)>5:
                continue
            p = self.d
            ln = len(word)
            for i in range(ln-1,-1,-1): #字符串后边开始遍历字符
                char = word[i].lower()
                if p=='':
                    q[k] = {}
                    p = q[k]
                if not (char in p):
                    p[char] = ''
                    q = p
                    k = char
                p = p[char]
        
        pass
    
    def _binary_seg(self,s):
        ln = len(s)
        if ln==1:
            return [s]
        R = []
        for i in range(ln,1,-1):
            tmp = s[i-2:i]
            R.append(tmp)
        return R
    
    def _pro_unreg(self,piece):
        #print piece
        R = []
        tmp = re.sub(u"。|，|,|！|…|!|《|》|<|>|\"|'|:|：|？|\?|、|\||“|”|‘|’|；|—|（|）|·|\(|\)|　"," ",piece).split()
        ln1 = len(tmp)
        for i in range(len(tmp)-1,-1,-1):
            mc = re.split(r"([0-9A-Za-z\-\+#@_\.]+)",tmp[i])
            for j in range(len(mc)-1,-1,-1):
                r = mc[j]
                if re.search(r"([0-9A-Za-z\-\+#@_\.]+)",r)!=None:
                    R.append(r)
                else:
                    R.extend(self._binary_seg(r))
        return R
        
        
    def cut(self,text):
        """
        """
        #text = text.decode('utf-8','ignore')
        
        p = self.d
        ln = len(text)
        i = ln 
        j = 0
        z = ln
        q = 0
        recognised = []
        mem = None
        mem2 = None
        while i-j>0:
            t = text[i-j-1].lower() #从源句后面取一字符
            #print i,j,t,mem
            if not (t in p):
                if (mem!=None) or (mem2!=None):
                    if mem!=None:
                        i,j,z = mem
                        mem = None
                    elif mem2!=None:
                        delta = mem2[0]-i
                        if delta>=1:
                            """
.	匹配任意1个字符（除了\n）
[ ]	匹配[ ]中列举的字符
\d	匹配数字，即0-9
\D	匹配非数字，即不是数字
\s	匹配空白，即 空格，tab键
\S	匹配非空白
\w	匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
\W	匹配特殊字符，即非字母、非数字、非汉字、非_

\u2E80-\u9FFF  匹配 unicode 所有中文
                            """

                            #if (delta<5) and (re.search(ur"[\w\u2E80-\u9FFF]",t)!=None):
                            if (delta<5) and (re.search(u"[\w\u2E80-\u9FFF]",t)!=None):
                                pre = text[i-j]
                                #print pre
                                if not (pre in self.specialwords):
                                    i,j,z,q = mem2
                                    del recognised[q:]
                            mem2 = None
                            
                    p = self.d
                    if((i<ln) and (i<z)):# i < z 之前有未识别的字符串
                        unreg_tmp = self._pro_unreg(text[i:z]) #按默认规则分割 
                        recognised.extend(unreg_tmp)
                    recognised.append(text[i-j:i])
                    #print text[i-j:i],mem2
                    i = i-j
                    z = i
                    j = 0
                    continue
                j = 0
                i -= 1
                p = self.d #重新开始匹配
                continue
            p = p[t] #获得当前字在字典数据里的下一层
            j+=1
            if chr(11) in p:   #判断是否有 结束符 在当前字下一层,如果有则字典里的词匹配成功
                if j<=2:
                    mem = i,j,z
                    #print text[i-1]
                    if (z-i<2) and (text[i-1] in self.specialwords) and ((mem2==None) or ((mem2!=None and mem2[0]-i>1))):
                        #print text[i-1]
                        mem = None
                        mem2 = i,j,z,len(recognised)
                        p = self.d
                        i -= 1
                        j = 0
                    continue
                    #print mem
                p = self.d
                #print i,j,z,text[i:z]
                if((i<ln) and (i<z)):
                    unreg_tmp = self._pro_unreg(text[i:z])
                    recognised.extend(unreg_tmp)
                recognised.append(text[i-j:i])
                i = i-j
                z = i
                j = 0
                mem = None
                mem2 = None
        #print mem
        if mem!=None:
            i,j,z = mem
            recognised.extend(self._pro_unreg(text[i:z]))
            recognised.append(text[i-j:i])        
        else:
            recognised.extend(self._pro_unreg(text[i-j:z]))
        return recognised