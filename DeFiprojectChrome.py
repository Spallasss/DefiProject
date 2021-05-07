import requests
import json
import time
from selenium import webdriver
from tabulate import tabulate

defiswap_list=list()

bakery_list  = list()
julswap_list  = list()
pancake_list  = list()
uniswap_list= list()
sushiswap_list= list()
bancor_list= list()
serum_list = list()
mdex_list  = list()
linkswap_list= list()
quickswap_list= list()
wanswap_list= list()
sashimiswap_list= list()
swipeswap_list= list()
pangolin_list= list()
mov_list= list()
apeswap_list=list()
burger_list=list()
def DeFi():
    
    print("PROJE ÇALIŞIYOR")
    wanlistSwap()
    bancorlistSwap()
    julistSwap()
    linklistSwap()
    bakerylistSwap()
    mdexlistSwap()
    burgerswaplistSwap()
    sushiswaplistSwap()                            
    uniswaplistSwap()
    #serumlistSwap()
    pancakelistSwap()
    quicklistSwap()
    sashimilistSwap()
    swipelistSwap()
    pangolinlistSwap()
    movlistSwap()
    apeswaplistSwap()
 
    j=0
    while j<16:
                    datas = [swipeswap_list,burger_list,pangolin_list,wanswap_list,apeswap_list,mov_list,uniswap_list,sushiswap_list,sashimiswap_list,mdex_list,julswap_list,bakery_list,pancake_list,linkswap_list,quickswap_list,bancor_list]
                    for i in datas[j]:
                        if(float(i[5])!=0):
                            defiswap_list.append([i[0],i[1],i[2],i[3],i[4],i[5]])
                    j +=1
                    data = sorted(defiswap_list, key=lambda x:float(x[5]), reverse=True)
    print(tabulate(data))
                #print(defiswap_list)
    print("PROJE BİTTİ")
    
        
def burgerswaplistSwap():#doğru çalışıyor
    try:
        print("burgerswap başladı")
        pair = list()
        data_values = list()
        def looper():
                name = driver.find_elements_by_css_selector(".sc-jlyJG.hZRHdD")
                values = driver.find_elements_by_css_selector(".sc-fMiknA.cObOEH.css-4cffwv")
                for i in name:
                    pair.append(i.text)
                for i in values:
                    data_values.append(i.text)
        exchange= "burgerswap"
        driver = webdriver.Chrome()
        url="https://info.burgerswap.org/pairs"
        driver.get(url)
        time.sleep(15)
        try:    
            looper()
            driver.find_element_by_css_selector(".sc-Rmtcm.eeIIib").click()
            looper()
            l=0
            v=1
            f=3
            a=4
            p=0
            while (a<=len(data_values)):
                        burger_list.append([exchange,pair[p],data_values[l].replace("$", ""),data_values[v].replace("$", ""),data_values[f].replace("$", ""),(data_values[a].replace("+", "")).replace("%","")])
                        l+=5
                        v+=5
                        f+=5
                        a+=5
                        p+=1
            driver.close()
            print("burgerswap bitti")
        except:
            print("burgerswap listesi oluşturulamadı")
    except:
        print("burgerswap çalışmadı")
def movlistSwap():#doğru çalışıyor
    try:
        print("mov başladı")
        pair = list()
        data_values = list()
        def looper():
            name = driver.find_elements_by_css_selector(".ant-table-row.ant-table-row-level-0 td a")
            values = driver.find_elements_by_css_selector(".ant-table-cell.cell span")
            for i in name:
                pair.append(i.text)
            for i in values:
                data_values.append(i.text)
            time.sleep(2)
        exchange= "mov"
        driver = webdriver.Chrome()
        url="https://sup.finance/dashboard"
        driver.get(url)
        time.sleep(15)
        try:
            looper()
            l=2
            v=3
            f=4
            a=5
            p=0
            while(a<=91):
                mov_list.append([exchange,pair[p],data_values[l].replace("$", ""),data_values[v].replace("$", ""),data_values[f].replace("$", ""),(data_values[a].replace("+", "")).replace("%","")])    
                l+=7
                v+=7
                f+=5
                a+=7
                p+=1
            driver.close()
            print("mov bitti")
        except:
            print("mov listesi oluşturulamadı")
    except:
        print("mov çalışmadı")
def swipelistSwap():#doğru çalışıyor
    try:
        print("swipeswap başladı")
        pair = list()
        data_values = list()
        def looper():
            name = driver.find_elements_by_css_selector(".MuiTypography-root.MuiLink-root.MuiLink-underlineHover.MuiTypography-body2.MuiTypography-colorPrimary.MuiTypography-noWrap")
            values = driver.find_elements_by_css_selector(".MuiTableCell-root.MuiTableCell-body.MuiTableCell-alignRight")
            for i in name:
                pair.append(i.text)
            for i in values:
                data_values.append(i.text)
        exchange= "swipeswap"
        driver = webdriver.Chrome()
        url="https://info.swipe.org/"
        driver.get(url)
        time.sleep(15)
        try:
            looper()
            l=36
            v=37
            f=39
            a=41
            p=0
            while(p<10):
                swipeswap_list.append([exchange,pair[p],data_values[l].replace("$", ""),data_values[v].replace("$", ""),data_values[f].replace("$", ""),(data_values[a].replace("+", "")).replace("%","")])    
                l+=6
                v+=6
                f+=6
                a+=6
                p+=1
            driver.close()
            print("swipeswap bitti")
        except:
            print("swipeswap listesi oluşturulamadı")          
    except:
        print("swipeswap çalışmadı")
def sashimilistSwap():#doğru çalışıyor
    try:
        print("sashimiswap başladı")
        pair = list()
        data_values = list()
        def looper():
            name = driver.find_elements_by_css_selector(".sc-gPEVay.bYsHcw")
            values = driver.find_elements_by_css_selector(".sc-hzDkRC.hvyZgB.css-4cffwv")
            for i in name:
                pair.append(i.text)
            for i in values:
                data_values.append(i.text)
        exchange= "sashimiswap"
        driver = webdriver.Chrome()
        url="https://info.sashimi.cool/pairs"
        driver.get(url)
        time.sleep(15)
        try:
            looper()
            l=0
            v=1
            f=3
            a=4
            p=0
            while(p<=10):
                sashimiswap_list.append([exchange,pair[p],data_values[l].replace("$", ""),data_values[v].replace("$", ""),data_values[f].replace("$", ""),(data_values[a].replace("+", "")).replace("%","")])    
                l+=5
                v+=5
                f+=5
                a+=5
                p+=1
            driver.close()
            print("sashimiswap bitti")
        except:
            print("sashimiswap listesi oluşturulamadı")
    except:
        print("sashimiswap çalışmadı")
def wanlistSwap():#doğru çalışıyor
    try:
        print("wanswap başladı")
        pair = list()
        data_values = list()
        def looper():
            name = driver.find_elements_by_css_selector(".sc-jlyJG.hZRHdD")
            values = driver.find_elements_by_css_selector(".sc-fBuWsC.KrSIM.css-4cffwv div div:nth-child(1)")
            for i in name:
                pair.append(i.text)
            for i in values:
                data_values.append(i.text)
        exchange= "wanswap"
        driver = webdriver.Chrome()
        url="https://info.wanswap.finance/pairs"
        driver.get(url)
        time.sleep(15)
        try:
            looper()
            l=0
            v=1
            f=3
            a=4
            p=0
            while (l<=180):
                    wanswap_list.append([exchange,pair[p],data_values[l].replace("$", ""),data_values[v].replace("$", ""),data_values[f].replace("$", ""),(data_values[a].replace("+", "")).replace("%","")])    
                    l+=6
                    v+=6
                    f+=6
                    a+=6
                    p+=1
            driver.close()
            print("wanswap bitti")
        except:
            print("wanswap listesi oluşturulamadı")  
    except:
        print("wanswap çalışmadı")
def bancorlistSwap():#doğru çalışıyor
    try:
        print("bancorswap başladı")
        url = 'https://api-v2.bancor.network/pools' 
        response = requests.get(url,timeout=10,headers={
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"})
        json_data= response.json()
        exchange = "Bancor"
        try:
            for i in json_data["data"]:
                if(float((i["liquidity"]["usd"]))!=0):
                    ayp=str((float(i["fees_24h"]["usd"])/float((i["liquidity"]["usd"])))*100*365)
                    bancor_list.append([exchange,i["name"],i["liquidity"]["usd"],"no volume",i["liquidity"]["usd"],ayp])
            print("bancorswap bitti")
        except:
            print("bancorswap listesi oluşturulamadı")         
    except:
        print("bancorswap çalışmadı")
def quicklistSwap():#doğru çalışıyor
    try:
        print("quickswap başladı")
        pair = list()
        data_values = list()
        def looper():
            name = driver.find_elements_by_css_selector(".sc-gPEVay.gLawMS")
            values = driver.find_elements_by_css_selector(".sc-VigVT.dNgKCa div:nth-child(1)")
            for i in name:
                pair.append(i.text)
            for i in values:
                data_values.append(i.text)
        exchange= "quickswap"
        driver = webdriver.Chrome()
        url="https://info.quickswap.exchange/pairs"
        driver.get(url)
        time.sleep(15)
        try:
            looper()
            l=0
            v=1
            f=3
            a=4
            p=0
            while (a<=len(data_values)):
                quickswap_list.append([exchange,pair[p],data_values[l].replace("$", ""),data_values[v].replace("$", ""),data_values[f].replace("$", ""),(data_values[a].replace("+", "")).replace("%","")])    
                l+=6
                v+=6
                f+=6
                a+=6
                p+=1
            driver.close()
            print("quickswap bitti")
        except:
            print("quickswap listesi oluşturulamadı")
    except:
        print("quickswap çalışmadı")
def pangolinlistSwap():#doğru çalışıyor
    try:
        print("pangolin başladı")
        pair = list()
        data_values = list()
        def looper():
            name = driver.find_elements_by_css_selector(".sc-iRbamj.bowFDd")
            values = driver.find_elements_by_css_selector(".sc-jhAzac.ewmrIK.css-4cffwv")
            for i in name:
                pair.append(i.text)
            for i in values:
                data_values.append(i.text)
        time.sleep(2)
        exchange= "pangolin"
        driver = webdriver.Chrome()
        url="https://info.pangolin.exchange/#/pairs"
        driver.get(url)
        time.sleep(15)
        try:
            looper()
            l=0
            v=1
            f=3
            a=4
            p=0
            while(a<=len(data_values)):
                pangolin_list.append([exchange,pair[p],data_values[l].replace("$", ""),data_values[v].replace("$", ""),data_values[f].replace("$", ""),(data_values[a].replace("+", "")).replace("%","")])    
                l+=5
                v+=5
                f+=5
                a+=5
                p+=1
            driver.close()
            print("pangolin bitti")
        except:
            print("pangolin listesi oluşturulamadı")
    except:
        print("pangolin çalışmadı")
def pancakelistSwap():#doğru çalışıyor
    try:
        print("pancakeswap başladı")
        pair = list()
        data_values = list()
        def looper():
                name = driver.find_elements_by_css_selector(".sc-iRbamj.bowFDd")
                values = driver.find_elements_by_css_selector(".sc-jhAzac.iggPaB.css-4cffwv")
                for i in name:
                    pair.append(i.text)
                for i in values:
                    data_values.append(i.text)
        exchange= "pancakeswap"
        driver = webdriver.Chrome()
        url="https://pancakeswap.info/pairs"
        driver.get(url)
        time.sleep(15)
        try:  
            looper()
            driver.find_element_by_css_selector(".sc-gipzik.kLOwjF").click()
            looper()
            l=0
            v=1
            f=3
            a=4
            p=0
            while (a<=len(data_values)):
                        pancake_list.append([exchange,pair[p],data_values[l].replace("$", ""),data_values[v].replace("$", ""),data_values[f].replace("$", ""),(data_values[a].replace("+", "")).replace("%","")])
                        l+=5
                        v+=5
                        f+=5
                        a+=5
                        p+=1
            driver.close()
            print("pancakeswap bitti")
        except:
            print("pancakeswap listesi oluşturulamadı")
    except:
        print("pancakeswap çalışmadı")
def mdexlistSwap():#doğru çalışıyor
    try:
        print("mdexswap başladı")
        pair = list()
        data_values = list()
        exchange= "mdex"
        driver = webdriver.Chrome()
        url="https://bsc-info.mdex.com/#/pairs"
        driver.get(url)
        def looper():
                name = driver.find_elements_by_css_selector(".sc-gPEVay.gLawMS")
                values = driver.find_elements_by_css_selector(".sc-VigVT.dNgKCa div")
                for i in name:
                    pair.append(i.text)
                for i in values:
                    data_values.append(i.text)
        time.sleep(15)
        try:
            looper()
            driver.find_element_by_css_selector(".sc-jlyJG.fBsklp").click()
            looper()
            l=0
            v=2
            f=6
            a=8
            p=0
            while (a<=len(data_values)):
                mdex_list.append([exchange,pair[p],data_values[l].replace("$", ""),data_values[v].replace("$", ""),data_values[f].replace("$", ""),(data_values[a].replace("+", "")).replace("%","")])    
                l+=11
                v+=11
                f+=11
                a+=11
                p+=1
            driver.close() 
            print("mdexswap bitti")
        except:
            print("mdexswap listesi oluşturulamadı")
    except:
        print("mdexswap çalışmadı")  
def julistSwap():#doğru çalışıyor
    try:
        print("julswap başladı")
        pair = list()
        data_values = list()
        def looper():
            name = driver.find_elements_by_css_selector(".sc-kcbnda.dcPXpm.css-1n3zwju a div")
            values = driver.find_elements_by_css_selector(".sc-kcbnda.dcPXpm.css-4cffwv")
            for i in name:
                pair.append(i.text)
            for i in values:
                data_values.append(i.text)
            time.sleep(2)
        exchange= "julswap"
        driver = webdriver.Chrome()
        url="https://info.julswap.com/home"
        driver.get(url)
        time.sleep(15)
        try:
            looper()
            driver.find_element_by_css_selector(".sc-imABML.fKZlSM").click()
            looper()
            j=0
            while j<=5:
                driver.find_element_by_css_selector(".sc-hUfwpO.fvrRCk div:nth-child(3) div").click()
                looper()
                j+=1
            l=0
            v=1
            f=3
            a=4
            p=0
            while (a<=len(data_values)):
                julswap_list.append([exchange,pair[p],data_values[l].replace("$", ""),data_values[v].replace("$", ""),data_values[f].replace("$", ""),(data_values[a].replace("+", "")).replace("%","")])    
                l+=5
                v+=5
                f+=5
                a+=5
                p+=1
            driver.close()
            print("julyswap bitti")
        except:
            print("julswap listesi oluşturulamadı")
    except:
        print("julswap çalışmadı")
def bakerylistSwap():#doğru çalışıyor
    try:
        print("bakeryswap başladı")
        pair = list()
        data_values = list()
        def looper():
            name = driver.find_elements_by_css_selector(".sc-Rmtcm.gfMZds div a div")
            values = driver.find_elements_by_css_selector(".sc-jhAzac.ewmrIK.css-4cffwv")
            for i in name:
                pair.append(i.text)
            for i in values:
                data_values.append(i.text)
            time.sleep(2)
        exchange= "bakeryswap"
        driver = webdriver.Chrome()
        url="https://info.bakeryswap.org/#/home"
        driver.get(url)
        time.sleep(15)
        try:
            looper()
            j=0
            while j<=9:
                    driver.find_element_by_css_selector(".sc-jlyJG.fBMhOD div:nth-child(3) div").click()
                    looper()
                    j+=1
            l=0
            v=1
            f=3
            a=4
            p=0
            while (a<=len(data_values)):
                bakery_list.append([exchange,pair[p],data_values[l].replace("$", ""),data_values[v].replace("$", ""),data_values[f].replace("$", ""),(data_values[a].replace("+", "")).replace("%","")])    
                l+=5
                v+=5
                f+=5
                a+=5
                p+=1
            driver.close()
            print("bakeryswap bitti")
        except:
            print("bakeryswap listesi oluşturulamadı")
    except:
        print("bakeryswap çalışmadı")
def linklistSwap():#doğru çalışıyor
    try:
        print("linkswap başladı")
        pair = list()
        data_values = list()
        def looper():
            name = driver.find_elements_by_css_selector(".sc-iRbamj.bowFDd")
            values = driver.find_elements_by_css_selector(".sc-jhAzac.cVBsLB.css-4cffwv")
            for i in name:
                pair.append(i.text)
            for i in values:
                data_values.append(i.text)
            time.sleep(2)
        exchange= "linkswap"
        driver = webdriver.Chrome()
        url="https://info.linkswap.app/pairs"
        driver.get(url)
        time.sleep(15)
        try:
            looper()
            driver.find_element_by_css_selector(".sc-gipzik.fPxmcZ").click()
            looper()
            l=0
            v=1
            f=3
            a=4
            p=0
            while (a<=len(data_values)):
                linkswap_list.append([exchange,pair[p],data_values[l].replace("$", ""),data_values[v].replace("$", ""),data_values[f].replace("$", ""),(data_values[a].replace("+", "")).replace("%","")])    
                l+=5
                v+=5
                f+=5
                a+=5
                p+=1
            driver.close()
            print("linkswap bitti")
        except:
            print("linkswap listesi oluşturulamadı")
    except:
        print("linkswap çalışmadı")
def uniswaplistSwap():#bazı datalar yanlış
    try:
        print("uniswap başladı")
        query = """query 
            {
            pairs{
            id
            volumeUSD
            reserveUSD
            token0 {
            
            symbol
            name
      
            }
            token1 {
            
            symbol
            name
            }
            } 
      }"""
        exchange="Uniswap" 
        url = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
        r = requests.post(url, json={'query': query})
        json_data = json.loads(r.text)
        parced = json_data["data"]["pairs"]
        try:  
            for i in parced:
                    if float(i["volumeUSD"])!=0:
                        a=(float(i["volumeUSD"])*0.003)/(float(i["reserveUSD"]))*100
                        uniswap_list.append([exchange,i["token0"]["symbol"]+"/"+i["token1"]["symbol"],i["reserveUSD"],i["volumeUSD"],float(i["volumeUSD"])*0.003,a])
            print("uniswap bitti")   
        except:
            print("uniswap listesi oluşturulamadı") 
    except:
        print("uniswap çalışmadı")
def sushiswaplistSwap():#bazı datalar yanlış
    try:
            print("sushiswap başladı")
            query = """query 
                {
                pairs{
                id
                volumeUSD
                reserveUSD
                token0 {
                
                symbol
                name
        
                }
                token1 {
                
                symbol
                name
                }
                } 
        }"""
            exchange="Sushiswap" 
            url = 'https://api.thegraph.com/subgraphs/name/zippoxer/sushiswap-subgraph-fork'
            r = requests.post(url, json={'query': query})
            json_data = json.loads(r.text)
            parced = json_data["data"]["pairs"]
            try:
                for i in parced:
                
                    if float(i["volumeUSD"])!=0:
                        a=(float(i["volumeUSD"])*0.003)/float(i["reserveUSD"])*100
                        sushiswap_list.append([exchange,i["token0"]["symbol"]+"/"+i["token1"]["symbol"],i["reserveUSD"],i["volumeUSD"],float(i["volumeUSD"])*0.003,a])
                print("sushiswap bitti")   
            except:
                print("sushiswap listesi oluşturulamadı")            
    except:
        print("sushiswap çalışmadı")
def serumlistSwap():#apyler 0 olduğu için kaldırdım
    try:
        print("serumswap başladı")
        url = 'https://serum-api.bonfida.com/pools' 
        response = requests.get(url,timeout=10,headers={
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"})
        json_data= response.json()
        exchange = "Serum"
        try:
            for i in json_data["data"]:
                if float(i["volume"])!=0:
                    serum_list.append([exchange,i["name"],i["liquidity_locked"],i["volume"],i["fees"],float(i["apy"])*100])
            print("serumswap bitti")
        except:
            print("serumswap listesi oluşturulamadı")
    except:
        print("serumswap çalışmadı")
def apeswaplistSwap():#doğru çalışıyor
    try:
        print("apeswap başladı")
        pair = list()
        data_values = list()
        def looper():
                name = driver.find_elements_by_css_selector(".sc-iRbamj.bowFDd")
                values = driver.find_elements_by_css_selector(".sc-jhAzac.iggPaB.css-4cffwv")
                for i in name:
                    pair.append(i.text)
                for i in values:
                    data_values.append(i.text)
        exchange= "apeswap"
        driver = webdriver.Chrome()
        url="https://info.apeswap.finance/pairs"
        driver.get(url)
        time.sleep(15) 
        try:  
            looper()
            driver.find_element_by_css_selector(".sc-gipzik.Lgock").click()
            looper()
            l=0
            v=1
            f=3
            a=4
            p=0
            while (a<=len(data_values)):
                        apeswap_list.append([exchange,pair[p],data_values[l].replace("$", ""),data_values[v].replace("$", ""),data_values[f].replace("$", ""),(data_values[a].replace("+", "")).replace("%","")])
                        l+=5
                        v+=5
                        f+=5
                        a+=5
                        p+=1
            driver.close()
            print("apeswap bitti")
        except:
            print("apeswap listesi oluşturulamadı")
    except:
        print("apeswap çalışmadı")
DeFi()   