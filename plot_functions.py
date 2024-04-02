 
from matplotlib import pyplot

def PlotData(Data,String):
    pyplot.bar(range(1,len(Data )+1), Data,label=String)
    pyplot.grid(color='0.78', linestyle='-', linewidth=1)
    pyplot.legend(title='Legend')
    pyplot.title(String)
    pyplot.show()	
    return 0

def PlotDataCurve(Data,ColorStr,LabelStr):
    pyplot.plot(range(1,len(Data )+1), Data, '-', color=ColorStr,label=LabelStr)
    pyplot.grid(color='0.78', linestyle='-', linewidth=1)
    pyplot.legend(title='Legend')
    pyplot.title(LabelStr)
    pyplot.show()	
    return 0	

def PlotPeaks(Data, DataPeaksOccurange,DataPeaksValues):
    if (len(DataPeaksValues) < 1):
        return
    pyplot.bar(range(0,len(Data)),Data,color='lightgray')
    annotate_height = 1000 + DataPeaksValues[0]
    for i in range(0,len(DataPeaksOccurange)):
        Height = 1000 + DataPeaksValues[i]
        pyplot.vlines(x=DataPeaksOccurange[i], ymin=0, ymax=Height)
        pyplot.annotate("Peak Value", 
            xy=(DataPeaksOccurange[i], DataPeaksValues[i]),
            xycoords='data',
            xytext=(30, annotate_height),
            textcoords='data',
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3"))