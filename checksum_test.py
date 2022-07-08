
dynamixel_id = 1
length = 5
instruction = 3
P1 = 30
P2 = 32
P3 = 3

Checksum = (0x02+0x30+0x30+0x81+0x56+0x8B+0x82) & 0xff

#Checksum = hex(~(0x01+0x05+0x03+0x1E+0x32+0x03) & 0xff)

Checksum = hex(~(0x01+0x05+0x03+0x1E+0xCD+0x00) & 0xff)

Checksum_0 =   hex(~(0x01+0x05+0x03+0x1E+0x00+0x00) & 0xff)
Checksum_60 =  hex(~(0x01+0x05+0x03+0x1E+0xCC+0x00) & 0xff)
Checksum_120 = hex(~(0x01+0x05+0x03+0x1E+0x99+0x01) & 0xff)
Checksum_180 = hex(~(0x01+0x05+0x03+0x1E+0x66+0x02) & 0xff)
Checksum_240 = hex(~(0x01+0x05+0x03+0x1E+0x33+0x03) & 0xff)
Checksum_300 = hex(~(0x01+0x05+0x03+0x1E+0x00+0x04) & 0xff)


a = "0x02"

b = int(a, 16)


print(Checksum_0)
print(Checksum_60)
print(Checksum_120)
print(Checksum_180)
print(Checksum_240)
print(Checksum_300)

print(2.31//1)



def angle_to_instruction(angle):

	A = angle / 300 * 1024  # map to 10-bit number 

	B = A/256               # seperate into 2 8 bit bytes by dividing by max value of 8 bit byte 

	H = int(B // 1)         # decimal value of high byte, convert to intager
	print(H)

	L = B - H                     
	print(L)
	L = int(L * 256)        # decimal value of low byte

	
	H = hex(H)

	L = hex(L)

	return(H, L)


a = angle_to_instruction(60)
print(a)

# TODO add hex strings to instruction packet to send to motor

# TODO calculate checksum using instruction packet then send to motor  



