from math import sin, pi
import matplotlib.pyplot as plt
'''
    We will decompose our signal into a Fourier series.
    The Fourier series of a square wave is:
    f(x) = (4/pi)*sum_{n=1,3,5,...}^{infinity}{(1/n)*sin(n*pi*x/L)}
    where L 1/2 the domain over [0,2L]

    We will use the first 3 components to make a note of given frequency (C4).

    C4 frequency: 261.636Hz
    C4 period = 1/261.636Hz ~= .00382225008 secs

    There are 44100 samples/sec in a wav file, so samples/sec is:
    44100*(1/261.636) ~= 168.5612286 ~= 168

    If we want to play our C4 note for one second, we need ~168 samples.

    Our Fourier series for the 1st component is: (4/pi)*(1/1)*sin(2*1*pi*x/168)
    2nd Component: (4/pi)*(1/3)*sin(2*3*pi*i/168)
    3rd Component: (4/pi)*(1/5)*sin(2*5*pi*i/168)

    The square wave approximation comes from adding these components together

    The program below plots the sin wave of the approximation of square wave.
'''


'''
N=168 #samples/sec
x=range(N) #[0,1,2,3,...,N-1] -- N elements
y=N*[0] #[0,0,0,0,...,0] -> empty list with N elements

for i in x:
    y1 = 4/pi*(1/1)*sin(2*1*pi*i/N) #Fourier series 1,2,3
    y2 = 4/pi*(1/3)*sin(2*3*pi*i/N)   
    y3 = 4/pi*(1/5)*sin(2*5*pi*i/N)

    y[i]=y1+y2+y3 #Three Fourier series conefficents

y=1313*y        #The lists is duplicated 1313 times, making 1313 periods
x=range(1313*N)
plt.plot(x,y)   #The plot is calculated
plt.show()      #The plot is displayed
'''

N=168 #samples/second
x=range(N) #[0,1,2,...,N-1]
y=N*[0] #[0,0,0...0]
for i in x:
    if i<N/2: y[i]=1.0
    else: y[i]=-1.0

y=1313*y

'''
    3 periods gives us 3*168/44100 ~= .011428 secs of audio.
    If we want to have 5 seconds, we need: (44100*5)/168 ~= 1313 periods.

    The program below makes the 5-second wav file:
'''

import wave
import struct
fout=wave.open("sin1313.wav","w")
fout.setnchannels(1) # Mono
fout.setsampwidth(2) # Sample is 2 Bytes
fout.setframerate(44100) # Sampling Frequency
fout.setcomptype('NONE','Not Compressed')
BinStr=b'' # Create a binary string of data
for i in range(len(y)):
    BinStr = BinStr + struct.pack('h',round(y[i]*20000))
fout.writeframesraw(BinStr)
fout.close()
