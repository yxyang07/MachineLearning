# left circular shift
 
#int_value是输入的整数，k是位移的位数，bit是整数对应二进制的位数

def XOR(msg,pad,length):
    return ([msg[i] ^ pad[i] for i in range(length)])


def circular_shift_left (int_value,k,bit): 
 bit_string = '{:0%db}' % bit
 bin_value = bit_string.format(int_value) # 8 bit binary
 bin_value = bin_value[k:] + bin_value[:k]
 int_value = int(bin_value,2) 
 return int_value
 

def 
# right circular shift
 
def circular_shift_right (int_value,k,bit): 
 bit_string = '{:0%db}' % bit 
 bin_value = bit_string.format(int_value) # 8 bit binary 
 bin_value = bin_value[-k:] + bin_value[:-k] 
 int_value = int(bin_value,2) 
 return int_value
 
 
if __name__ == "__main__": 
 A=88675123 
 B=circular_shift_right(A, 12, 32)
 print(A,"右循环位移1位的结果是",B)
 A1 = bin(A).replace('0b','')
 B1 = bin(B).replace('0b','')
 msg1=[]
 msg2=[]
 msg1 = [int(n) for n in A1.split()]
 msg2 = [int(n) for n in B1.split()]
 print(msg1,msg2)
 l =len(A1)
 print(l)
 X =  XOR(msg1,msg2,l)
 X1 = int(X,2) 
 print(X1)
 
 C = 88675123
 
 D =circular_shift_left(C,12,32)
 
 print(C, "左循环位移1位的结果是", D)
