import pyshark
import pandas as pd
from bokeh.plotting import figure,curdoc,show,ColumnDataSource,output_file,save
from bokeh.driving import linear

def pktCap ():
    cap = pyshark.LiveCapture(interface='Wi-Fi', only_summaries=True) 
    cap.sniff(packet_count=20)

    file = open('pcap2.csv','w')

    with file:

        file.write('pkTime')
        file.write(',')
        file.write('ipLen')
        file.write('\n')

        for pkt in cap:
            pkTime = pkt.time
            ipLen = pkt.length 
            #print(pkTime + ',',ipLen)
            file.write(pkTime)
            file.write(',')
            file.write(ipLen)
            file.write('\n')


    p = figure(title='RT Packet Length',x_axis_label = 'Time',y_axis_label = 'Packet Length',plot_width=1080, plot_height=600)

    df = pd.read_csv('pcap2.csv')

    ds1 = ColumnDataSource(df)

    line1 = p.line(x="pkTime",y="ipLen", color="firebrick", line_width=2, source=ds1)

    #output_file('line.html')

    show(p)

    return ds1

def update():

    ds1=pktCap()

    f = open('pcap2.csv', 'r')
    cv = pd.read_csv(f)
    df = pd.DataFrame(cv)
    ds1.data['pkTime'] = df.x
    ds1.data['ipLen'] = df.y
    f.close()



pktCap()
curdoc().add_periodic_callback(update, 100)