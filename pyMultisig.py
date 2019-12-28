# pip install bitcoin

from bitcoin import *

# generate the three private keys

k1 = random_key()
k2 = random_key()
k3 = random_key()
 
p1 = privtopub (k1) 
p2 =  privtopub (k2)
p3 =  privtopub (k3)

print(k1,p1)
print(k2,p2)
print(k3,p3)

# make the multisig script and address

k = 2 # signitures requires
n = 3 # keys generated

script =  mk_multisig_script ([p1 ,p2 ,p3], k, n)
address = scriptaddr(script)

print(script)
print(address)

# send some BTC to your address, and run the following to make sure you actually received the funds.

# unspentData = unspent(address)
# unspentOutput = unspentData["output"]

# sending the funds

# spendSats = 10000 # satoshis to spend
# addSpend = '1GRF5cmvAqQPNVPRHe1TpMZGS1mYFHFQHu'
# tx =  mktx (unspentOutput, addSpend+':'+str(spendSats))
# print(tx)

# Now, let’s sign it with keys 1 and 3:

# sig1 =  multisign (tx, 0, script, k1)
# sig2 =  multisign (tx, 0, script, k3)

# tx2 =  apply_multisignatures (tx, 0, script, [sig1, sig2])
# print(tx2)

# And now we push:

# eligius_pushtx (tx2 )
