from collections import OrderedDict

codedic=OrderedDict()

codedic['python']='dsdkfjlakdfj'
codedic['c']='abc'
codedic['php']='used for website'
codedic['ruby']='used for sdjfoijs'
codedic['go']='developed by google'

for name,describe in codedic.items():
    print(name.title()+":"+describe)