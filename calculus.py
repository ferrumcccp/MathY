from basic import *


def derivative(f,a,method='central',h=0.00001):

    '''Compute the difference formula for f'(a) with step size h.

    Parameters
    ----------
    f : function
        Vectorized function of one variable
    a : number
        Compute derivative at x = a
    method : string
        Difference formula: 'forward', 'backward' or 'central'
    h : number
        Step size in difference formula

    Returns
    -------
    float
        Difference formula:
            central: f(a+h) - f(a-h))/2h
            forward: f(a+h) - f(a))/h
            backward: f(a) - f(a-h))/h            
    '''
    if method == 'central':
        return (f(a + h) - f(a - h))/(2*h)#float("%.3f" % ((f(a + h) - f(a - h))/(2*h)))
    elif method == 'forward':
        return (f(a + h) - f(a))/h#float("%.3f" % ((f(a + h) - f(a))/h))
    elif method == 'backward':
        return (f(a) - f(a - h))/h#float("%.3f" % ((f(a) - f(a - h))/h))
    else:
        raise ValueError("Method must be 'central', 'forward' or 'backward'.")

# steps being the number of members between the interval
# conventionally, start value is smaller than end value


# warning! extremely not precise! only for recreational use
# substitutes with more powerful Simpson formula and Gauss formula
def integrate_regular(function,start,end,precision = 2500):
	sum = 0
	
	for i in linspace(start,end,precision):
		sum+=function(i)*(end-start)/precision
	return float("%.16f"%sum)



def integrate_gauss(function,start,end,n=3):
    # 高斯点及其求积系数列表
    x1=[0.0]
    A1=[2]
    x2=[-0.5773502691896250, 0.5773502691896250]
    A2=[1, 1]
    x3=[-0.7745966692414830, 0.0, 0.7745966692414830]
    A3=[0.5555555555555550, 0.8888888888888880, 0.5555555555555550]
    x4=[0.3399810435848560, -0.3399810435848560, 0.8611363115940520, -0.8611363115940520]
    A4=[0.6521451548625460, 0.6521451548625460, 0.3478548451374530, 0.3478548451374530]
    x5=[0.0, 0.5384693101056830, -0.5384693101056830, 0.9061798459386640, -0.9061798459386640]
    A5=[0.5688889, 0.4786287, 0.4786287, 0.2369269, 0.2369269]
    x6=[-0.9324695142031520,-0.6612093864662640,-0.2386191860831960,0.2386191860831960,0.6612093864662640,0.9324695142031520]
    A6=[0.1713244923791700, 0.3607615730481380, 0.4679139345726910, 0.4679139345726910,0.3607615730481380, 0.1713244923791700]
    x7=[-0.949107912,-0.741531186,-0.405845151,0,0.405845151,0.741531186,0.949107912]
    x8=[-0.960289856,-0.796666477,-0.52553241,-0.183434642,0.183434642,0.52553241,0.796666477,0.960289856]
    x9=[-0.96816024,-0.836031107,-0.613371433,-0.324253423,0,0.324253423,0.613371433,0.836031107,0.96816024]
    x10=[-0.973906529,-0.865063367,-0.679409568,-0.433395394,-0.148874339,0.148874339,0.433395394,0.679409568,0.865063367,0.973906529]
    x11=[-0.978228658,-0.8870626,-0.730152006,-0.519096129,-0.269543156,0,0.269543156,0.519096129,0.730152006,0.8870626,0.978228658]
    x12=[-0.981560634,-0.904117256,-0.769902674,-0.587317954,-0.367831499,-0.125233409,0.125233409,0.367831499,0.587317954,0.769902674,0.904117256,0.981560634]
    x13=[-0.984183055,-0.917598399,-0.801578091,-0.642349339,-0.448492751,-0.230458316,0,0.230458316,0.448492751,0.642349339,0.801578091,0.917598399,0.984183055]
    x14=[-0.986283809,-0.928434884,-0.827201315,-0.687292905,-0.515248636,-0.319112369,-0.108054949,0.108054949,0.319112369,0.515248636,0.687292905,0.827201315,0.928434884,0.986283809,]
    x15=[-0.987992518,-0.937273392,-0.848206583,-0.724417731,-0.570972173,-0.394151347,-0.201194094,0,0.201194094,0.394151347,0.570972173,0.724417731,0.848206583,0.937273392,0.987992518]
    x16=[-0.989400935,-0.944575023,-0.865631202,-0.755404408,-0.617876244,-0.458016778,-0.281603551,-0.09501251,0.09501251,0.281603551,0.458016778,0.617876244,0.755404408,0.865631202,0.944575023,0.989400935]
    x17=[-0.990575475,-0.950675522,-0.880239154,-0.781514004,-0.657671159,-0.512690537,-0.351231763,-0.178484181,0,0.178484181,0.351231763,0.512690537,0.657671159,0.781514004,0.880239154,0.950675522,0.990575475]
    x18=[-0.991565168,-0.95582395,-0.892602466,-0.803704959,-0.691687043,-0.559770831,-0.411751161,-0.251886226,-0.084775013,0.084775013,0.251886226,0.411751161,0.559770831,0.691687043,0.803704959,0.892602466,0.95582395,0.991565168]
    x19=[-0.992406844,-0.960208152,-0.903155904,-0.822714657,-0.720966177,-0.600545305,-0.464570741,-0.3165641,-0.160358646,0,0.160358646,0.3165641,0.464570741,0.600545305,0.720966177,0.822714657,0.903155904,0.960208152,0.992406844]
    x20=[-0.993128599,-0.963971927,-0.912234428,-0.839116972,-0.746331906,-0.636053681,-0.510867002,-0.373706089,-0.227785851,-0.076526521,0.076526521,0.227785851,0.373706089,0.510867002,0.636053681,0.746331906,0.839116972,0.912234428,0.963971927,0.993128599]
    A7=[0.129484966,0.279705391,0.381830051,0.417959184,0.381830051,0.279705391,0.129484966]
    A8=[0.101228536,0.222381034,0.313706646,0.362683783,0.362683783,0.313706646,0.222381034,0.101228536]
    A9=[0.081274388,0.180648161,0.260610696,0.312347077,0.330239355,0.312347077,0.260610696,0.180648161,0.081274388]
    A10=[0.066671344,0.149451349,0.219086363,0.269266719,0.295524225,0.295524225,0.269266719,0.219086363,0.149451349,0.066671344]
    A11=[0.055668567,0.125580369,0.186290211,0.233193765,0.262804545,0.272925087,0.262804545,0.233193765,0.186290211,0.125580369,0.055668567]
    A12=[0.047175336,0.106939326,0.160078329,0.203167427,0.233492537,0.249147046,0.249147046,0.233492537,0.203167427,0.160078329,0.106939326,0.047175336]
    A13=[0.040484005,0.0921215,0.13887351,0.178145981,0.207816048,0.22628318,0.232551553,0.22628318,0.207816048,0.178145981,0.13887351,0.0921215,0.040484005]
    A14=[0.03511946,0.080158087,0.121518571,0.157203167,0.185538397,0.205198464,0.215263853,0.215263853,0.205198464,0.185538397,0.157203167,0.121518571,0.080158087,0.03511946]
    A15=[0.030753242,0.070366047,0.10715922,0.139570678,0.166269206,0.186161,0.198431485,0.202578242,0.198431485,0.186161,0.166269206,0.139570678,0.10715922,0.070366047,0.030753242]
    A16=[0.027152459,0.062253524,0.095158512,0.124628971,0.149595989,0.169156519,0.182603415,0.18945061,0.18945061,0.182603415,0.169156519,0.149595989,0.124628971,0.095158512,0.062253524,0.027152459]
    A17=[0.024148303,0.055459529,0.085036148,0.111883847,0.135136368,0.154045761,0.168004102,0.176562705,0.17944647,0.176562705,0.168004102,0.154045761,0.135136368,0.111883847,0.085036148,0.055459529,0.024148303]
    A18=[0.021616014,0.049714549,0.07642573,0.100942044,0.122555207,0.140642915,0.154684675,0.164276484,0.169142383,0.169142383,0.164276484,0.154684675,0.140642915,0.122555207,0.100942044,0.07642573,0.049714549,0.021616014]
    A19=[0.019461788,0.044814227,0.069044543,0.091490022,0.111566646,0.128753963,0.142606702,0.152766042,0.158968843,0.16105445,0.158968843,0.152766042,0.142606702,0.128753963,0.111566646,0.091490022,0.069044543,0.044814227,0.019461788]
    A20=[0.017614007,0.04060143,0.062672048,0.083276742,0.10193012,0.118194532,0.131688638,0.142096109,0.149172986,0.152753387,0.152753387,0.149172986,0.142096109,0.131688638,0.118194532,0.10193012,0.083276742,0.062672048,0.04060143,0.017614007]
    summation = 0
    
    if n == 1:
        p=x1
        t=A1
    elif n == 2:
        p = x2
        t = A2
    elif n == 3:
        p = x3
        t = A3
    elif n == 4:
        p = x4
        t = A4
    elif n == 5:
        p = x5
        t = A5
    elif n ==6:
        p = x6
        t = A6
    elif n ==7:
        p = x7
        t = A7
    elif n ==8:
        p = x8
        t = A8
    elif n ==9:
        p = x9
        t = A9
    elif n ==10:
        p = x10
        t = A10
    elif n ==11:
        p = x11
        t = A11
    elif n ==12:
        p = x12
        t = A12
    elif n ==13:
        p = x13
        t = A13
    elif n ==14:
        p = x14
        t = A14
    elif n ==15:
        p = x15
        t = A15
    elif n ==16:
        p = x16
        t = A16
    elif n ==17:
        p = x17
        t = A17
    elif n ==18:
        p = x18
        t = A18
    elif n ==19:
        p = x19
        t = A19
    elif n ==20:
        p = x20
        t = A20
    for i in range(n):
        summation +=function((end-start)*p[i]/2+(start+end)/2)*t[i]
    summation*=(end-start)/2
    return summation


# # below, numpy is needed because of historical reason
# below, custom linspace is implemented
# import numpy as np
# simpson formula and trapezoid method belongs to newton cote
def linspace(a,b,n):
    if n == 1:
        return [a]
    else:
        step = (b - a) / (n - 1)
        return [a + step * i for i in range(0,n)]

def integrate_trapezoid(f,a,b,n):
    h = (b-a)/n; # 步长
    xi = linspace(a,b,n+1) # n+1 个节点
    Tn = h/2 * ((f(xi[0]))+2*sum(f(xi[1:n]))+f(xi[n]))
    print("使用复化梯形公式求得：Tn = %.7f"%Tn)
    return Tn

def integrate_simpson(f,a,b,n):
    h = (b-a)/(2*n); # 步长
    xi = linspace(a,b,2*n+1) # n+1 个节点
    #这里索引公式上有所区别
    Sn = h/3 * (f(xi[0])+4*sum(f(xi[1:2*n:2])) + 2*sum(f(xi[2:2*n-1:2]))  + f(xi[2*n]))
    print(sum(f(xi[1:2*n:2])))
    print(sum(f(xi[2:2*n-1:2])))
    print("使用复化Simpson公式求得：Sn = %.7f"%Sn)
    return Sn

def integrate(function,start,end,n=3):
    # use gauss integration as backend
    return integrate_gauss(function,start,end,n)
if __name__ == "__main__":
    print(integrate(lambda x: x, 0,1))
