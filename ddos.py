# DDOS ATTACK BY FUCKHIM SIR EAR BIG FAN
import os, sys, time
P = '\x1b[0m'
H = '\x1b[91m'
G = '\x1b[92m'
K = '\x1b[93m'

def Loads():
    for i in range(101):
        time.sleep(0.3)
        sys.stdout.write(G + '\r[+] ' + P + 'Loads Akun : %d%%' % i)
        sys.stdout.flush()


def Report():
    for d in range(101):
        time.sleep(0.2)
        sys.stdout.write(G + '\r[*] ' + P + 'DDOS POSSESSING ... [%d%%] ' % d)
        sys.stdout.flush()


print '-' * 49 + H
os.system('figlet " D D O S "')
print P + '=' * 49
B = raw_input(G + '[+]' + P + 'FB-ID  : ')
print '=' * 49
if not B.startswith('1000'):
    print '[!] WAIT... WE ARE READY TO FUCK'

    print '=' * 49
Loads()
time.sleep(2)
print ''
print '=' * 49
a = 1
while True:
    print ('{}[-] {} DDOS ATTACK [{}] => {}{}').format(G, P, a, H, B)
    print ('{} | {}[+]{} SUCCESS ').format(Report(), K, G)
    print '=' * 49
    a += 1
