
import numpy
from matplotlib import pyplot
import statistics
import plot_functions as pl


from curve_functions import Richards

def GenerateChunckCasesFromDailyCases(Data, Chunck):
    #NewData[(len(Data)//Chunck) +1]
    Maxlen = (len(Data)//Chunck) +1
    NewData     = numpy.array(range(0, Maxlen))
    aux = 0
    DataChunckSum = 0
    for i in range(0,len(Data)-1):
        DataChunckSum = DataChunckSum + Data[i]
        if (i+1)%Chunck == 0:
            NewData[aux] = DataChunckSum
            aux = aux + 1
            DataChunckSum = 0
    return(NewData)

def CopyListArray (lst_tpl) : # funcao para copiar elementos de lista/tupla gerando lista nova
  list = [];
  for item in lst_tpl : list.append(item);
  return list;

def GetBestChunckSize(Data, limit):
    BestChunckSize = 1
    BestVariance = -1
    for i in range(limit):
        ChunckedData = GenerateChunckCasesFromDailyCases(Data, i+1)
        Variance = statistics.variance(ChunckedData)
        # print(i, Variance)
        if (BestVariance == -1 or Variance < BestVariance):
            BestVariance = Variance
            BestChunckSize = i+1
    return BestChunckSize, BestVariance

def rmse(predictions, targets):
    return numpy.sqrt(((predictions - targets) ** 2).mean())

def GetRSquared(Data, Prediction):
    residuals = Data - Prediction
    ss_res = numpy.sum(residuals**2)
    ss_tot = numpy.sum((Data-numpy.mean(Data))**2)
    r_squared = 1 - (ss_res / ss_tot)
    return round(r_squared, 4)
    
def GetPearson(Data, Prediction):
    #sqrt(GetRSquared(Data, Prediction))
    print("edoke")
    
def GetRMSE(BruteData, BrutePrediction):
    scaler = StandardScaler()
    Data = BruteData.reshape(-1,1)
    Prediction = BrutePrediction.reshape(-1,1)
    Data = scaler.fit_transform(Data)
    Prediction = scaler.fit_transform(Prediction)
    MSE = mean_squared_error(Data, Prediction, squared=True)
    RMSE = mean_squared_error(Data, Prediction, squared=False)
    
    return RMSE, MSE
    

def PreparedDataToPerformGrowthFunction(v1,v2,Z):
    v1len = len(v1)#sim
    v2len = len(v2)#real

    if v1len > v2len:
        maxlen = v2len
    else:
        maxlen = v1len
    #-----------------------------------------
    
    aux=0 #subitratir os vetores que se sobrepõe
    for i in range(1,maxlen):
        value = v2[aux] - v1[aux]
        if i <= Z or value < 0:
            v2[aux] = 0
        else:
            v2[aux] = value
        aux = aux + 1
    #-----------------------------------------
    
    aux=0 #remover os zeros iniciais do vetor final
    for item in v2:
        if (item == 0):
            aux = aux + 1
        else:
            break
    #print("Firsts Zeros-->[",aux,"]")
    #print('v2 length 2 [', len(v2[aux:]),"]")
    #PlotDataCurve(v2,"green","v2  Cases")

    #-----------------------------------------
    # print("V1", len(v1), "V2", len(v2), "RESULT", len(v2[aux:]))
    return v2[aux:]


def GenerateTotalCasesDataCurveFittingRichards(Data,K, A, r, s, Fpd):
    Maxlen = len(Data)+ Fpd
    TotalCaseCurveFitted = numpy.array(range(1, Maxlen))
    alfa = 0	
    for i in range(1,len(TotalCaseCurveFitted)):
        TotalCaseCurveFitted[alfa] = Richards(i, K, A, r, s)        
        alfa = alfa +1
    return TotalCaseCurveFitted

def GenerateTotalCasesDataCurveFitting(Data, K, A, r, s, Fpd, CurveFn):
    Maxlen = len(Data)+ Fpd
    TotalCaseCurveFitted = numpy.array(range(1, Maxlen))
    alfa = 0
    last = 0	
    for i in range(1,len(TotalCaseCurveFitted)):
        TotalCaseCurveFitted[alfa] = CurveFn(i, K, A, r, s)        
        alfa = alfa +1
    return TotalCaseCurveFitted[:len(TotalCaseCurveFitted)-1]

def GenerateDailyCasesDataFromTotalCases(TC):
    Maxlen = len(TC)
    DC     = numpy.array(range(0, Maxlen))
    DC[0]  = TC[0]
    for i in range(1,(Maxlen)):
        DC[i] = TC[i] - TC[i-1]
    return DC

def GenerateTotalCasesDataFromDailyCases(DC):
    Maxlen = len(DC) 
    TC     = numpy.array(range(0, Maxlen)) # starting vector TC
    TC[0]  = DC[0]
    for i in range(1,(Maxlen)):
        TC[i] = TC[i-1] + DC[i] 
    return TC	 

def PrepareDataToPlot(data, chunck_size=1):    
    tmpDataTotalCases = numpy.sort(data, axis=None)
    tmpDataDailyCases    = GenerateDailyCasesDataFromTotalCases(tmpDataTotalCases)
    DataChunckSize_Cases =  GenerateChunckCasesFromDailyCases(tmpDataDailyCases,chunck_size)
    return tmpDataTotalCases, tmpDataDailyCases, DataChunckSize_Cases
        
#     return deaths_array

def FindPeaks(Data,WSize):
    Peak  = Data[0]
    DownBar = 0
    Count = 0 
    PeakDate=[]
    PeakValue=[]
    FlagNewPeak = 1
    Pos=0

    for i in range(1,len(Data)):
        #print("Posição do Vetor: [",i,"] \tvalor [",Data[i],"]\tPICO [",Peak,"]")
        if Data[i] > Peak:
            Peak = Data[i]
            Pos = i
            DownBar = 0
            FlagNewPeak = 1
        else:
            DownBar = DownBar + 1        
        if  i == len(Data)-1 or ((DownBar > WSize) and (FlagNewPeak == 1)):
            #print("Pico Confirmado em [",i,"] : Posição/Pico [", Pos,"/",Peak,"]")
            PeakValue.append(Peak)
            PeakDate.append(Pos)
            DownBar = 0
            FlagNewPeak = 0
            Peak = Data[i]

    return PeakDate,PeakValue



        
def BestFitWavesLimitDefination(Data, Peaks,WinSize):
    DataBar=[]
    DataAvg=[]
    for aux in range(0,len(Peaks)-1):
        for i in range((Peaks[aux]+WinSize+1),len(Data)):
            Sum = 0
            for j in range(Peaks[aux],(Peaks[aux]+WinSize)):
                Sum = Sum + Data[j] 
            Avg = Sum/WinSize
            #DataBar.append(Data[i-1])
            DataBar.append(Data[i])
            #DataBar.append(Data[i+1])
            DataAvg.append(Avg)
            if (Data[i]>Avg):
                print("Found new Wave: Date[",i,"] Value[",Data[i],"]")
                #break
            else:
                WinSize = WinSize + 1
    
#     pyplot.bar(range(0,len(DataBar[:20])),DataBar[:20],color='lightgray')
#     pyplot.plot(range(0,len(DataAvg[:20])),DataAvg[:20],'o',color='red')

def BestFitWavesLimitDefination2(Data, Peaks,WinSize):
    BestFitWaves=[]
    DataBar=[]
    DataAvg=[]
    LI = 0
    tmpWinSize = WinSize
    for aux in range(0,len(Peaks)):
        
#         print("picos",len(Peaks))
#         print("Estudando pico: ",aux)
#         print("PeakAux",Peaks[aux])
#         print("Cond 01: ",Peaks[aux]+WinSize+1)
#         print("Cond 02: ",len(Data))

        for i in range((Peaks[aux]+WinSize+1),len(Data)):
            Sum = 0
#             print("Dados: Ini[",Peaks[aux]+LI,"] - FIM[",Peaks[aux]+WinSize,"] ANALISE[",i,"]")
            for j in range(Peaks[aux]+LI,(Peaks[aux]+WinSize)):
                Sum = Sum + Data[j] 
                #print("NO JJJJJJJJJJJ")
            Avg = Sum/WinSize
            #DataBar.append(Data[i-1])
            DataBar.append(Data[i])
            #DataBar.append(Data[i+1])
            DataAvg.append(Avg)
            if (Data[i]>Avg):
#                 print("Found new Wave: Date[",i,"] Value[",Data[i],"]")
                #pyplot.bar(range(0,len(DataBar[:20])),DataBar[:20],color='lightgray')
                #pyplot.plot(range(0,len(DataAvg[:20])),DataAvg[:20],'.',color='red')
                #pyplot.show()
                WinSize = tmpWinSize 
                BestFitWaves.append(i)
                break
            else:
                WinSize = WinSize + 1
                #LI = LI + 1
    
#     pyplot.bar(range(0,len(Data)),Data,color='lightgray')
#     if (len(Peaks) > 1): 
#         pyplot.plot(range(Peaks[0]+3,len(DataAvg[:15])+Peaks[0]+3),DataAvg[:15],'-',color='red')
#         pyplot.plot(range(Peaks[1]+1,len(DataAvg[16:25])+Peaks[1]+1),DataAvg[16:25],'-',color='red')
#     pyplot.show()  
    return BestFitWaves

def GetAbsNoise(Data):
    vectorlength = len(Data)
    absdiff = 0;
    for i in range (1,vectorlength):
        absdiff= absdiff + (abs(Data[i-1] - Data[i]));
    return absdiff;

def GetBestChunckSize2(Data,MaxChunckSize=30):
    BestChunckSize=-1;
    AbsNoise = -1;
    TMP = [];
    for i in range (1,MaxChunckSize):
        ChunckedData= GenerateChunckCasesFromDailyCases(Data, i)
        str = f"Valor de Chunk[ {i} ]"
        #pl.PlotData(ChunckedData,str)
        tmpAbsNoise = GetAbsNoise(ChunckedData)
        TMP.append(tmpAbsNoise)
        if (AbsNoise == -1) or (tmpAbsNoise < AbsNoise):
            AbsNoise = tmpAbsNoise;
            BestChunckSize = i;
            
    #pl.PlotDataCurve(TMP,'blue',"GRAFICO")
    return BestChunckSize;