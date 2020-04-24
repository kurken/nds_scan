import ArifmeticRound as ar


from xml.dom import minidom
xmldoc = minidom.parse('NDS.xml')
itemlist = xmldoc.getElementsByTagName('КнПродСтр')
#print(len(itemlist))
#print(itemlist[0].attributes['СумНДССФ20'].value)
for s in itemlist:
    stpr = float(s.attributes['СтоимПродСФ'].value)
    nds = float(s.attributes['СумНДССФ20'].value)
    nds_r =  ar.ArifmeticRound(stpr*20/120)
    razn_nds = ar.ArifmeticRound(nds_r - nds)
    data_sf = s.attributes['ДатаСчФПрод'].value
    nomer_sf = s.attributes['НомСчФПрод'].value 
    #print(razn_nds)
    if razn_nds == 0.01 or razn_nds == -0.01 or razn_nds == 0:
        # print('Yes')
        ok = 1
    else:
        print("---")
        print("Разница: " + str(razn_nds) + " Сумма документа: " + str(stpr) + " НДС в документе: " + str(nds) + " НДС рассчитанный: " + str(nds_r))
        #print("Сумма документа: " + str(stpr))
        #print("НДС в документе: " + str(nds))
        #print("НДС рассчитанный: " + str(nds_r))
        print("Дата СФ: " + data_sf + " Номер СФ: " + nomer_sf)
        #print("Номер СФ: " + str(itemlist[0].attributes['НомСчФПрод'].value))
        
        
    
   # if nds_r != nds:
     #   print("---")
##        print(stpr)
##        print(nds)
##        print(nds_r)
##        print("---")
    #else:
        #print("________")
