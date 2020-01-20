# pyMultisig
A Swiss bank account in your pocket. Bitcoin multiple signature (multisig) addresses maximise security against loss, theft, hack and seizure due to the nature of the split responsibility and / or redundancy required for spending. By way of explanation, let's say I want to start a family fund, in Bitcoin. I make a 2 of 5 multisig wallet; 2 signatures required of 5 possible to spend from this address. Of the 5 generated keys, I send one key to my father. One to my mother (they live separately). One to my brother. I keep one and I send a backup paper key to a trusted family friend. Requiring at least 2 signatures immediately cuts almost any unintentional loss. Let that sink in. It is almost impossible for anyone to seize, steal, hack the funds away. It is almost impossible for you to lose access to the funds. Instant spending is easy enough with any 2 members present. Businesses, Trusts or Governments might require more signatures to avoid collusion. Herein I provide a detailed explanation and code of how to create and use your own multisig address. 

# Keys
Multiple signatures require multiple keys. To generate fresh keys we use the random key generator provided by bitcoin.

```python
from bitcoin import *

# private keys
k1 = random_key()
k2 = random_key()
k3 = random_key()
k4 = random_key()
k5 = random_key()

print("Private keys: these are the keys you need to disperse. Do not save copies. It would defeat the point.")
print(k1)
print(k2)
print(k3)
print(k4)
print(k5)

# public keys
p1 =  privtopub (k1) 
p2 =  privtopub (k2)
p3 =  privtopub (k3)
p4 =  privtopub (k4)
p5 =  privtopub (k5)
```

# Redeem script
We can use the above keys to generate a redeem script and multisig address.

```python
k = 2 # signitures required
n = 5 # keys generated

script =  mk_multisig_script ([p1 ,p2 ,p3 ,p4 ,p5], k, n)
address = scriptaddr(script)

print(script)
print(address)
```
        
# Spending
Now you have a multisig address with the redeem script and keys to distribute. To test the spending, you will need to send some bitcoin to your new multisig address. Once sent, you can test the funds were received with:

```python
unspentData = unspent(address)
print(unspentData)

unspentOutput = unspentData["output"]
```
          
To spend funds you will need any 2 of the 5 generated to sign the new transaction.

```python
spendSats = 10000 # satoshis to spend
addSpend = '112eMCQJUkUz7kvxDSFCGf1nnFJZ61CE4W' # address to receive new transaction
tx =  mktx (unspentOutput, addSpend+':'+str(spendSats))
print(tx)

# Now, let’s sign it with keys 1 and 3:
sig1 =  multisign (tx, 0, script, k1)
sig2 =  multisign (tx, 0, script, k3)

tx2 =  apply_multisignatures (tx, 0, script, [sig1, sig2])
print(tx2)

# And now we push:
eligius_pushtx (tx2 )
```            
                      
Financial sovereignty. It's that easy, thanks to Bitcoin.

# Starting the script
pip install bitcoin

python pyMultisig.py

# Karma Jar
BTC - 112eMCQJUkUz7kvxDSFCGf1nnFJZ61CE4W

LTC - LR3BfiS77dZcp3KrEkfbXJS7U2vBoMFS7A

ZEC - t1bQpcWAuSg3CkBs29kegBPXvSRSaHqhy2b

XLM - GAHK7EEG2WWHVKDNT4CEQFZGKF2LGDSW2IVM4S5DP42RBW3K6BTODB4A Memo: 1015040538

Nano - nano_1ca5fxd7uk3t61ghjnfd59icxg4ohmbusjthb7supxh3ufef1sykmq77awzh

XRP - rEb8TK3gBgk5auZkwc6sHnwrGVJH8DuaLh Tag: 103535357

EOS - binancecleos Memo: 103117718

# Recommended links
Getting started - [Coinbase](https://www.coinbase.com/join/bradle_6r)

Portfolio balance - [Binance](https://www.binance.com/en/register?ref=LTUMGDDC)

Futures trading - [Deribit](https://www.deribit.com/reg-8106.6912)

Cold wallet - [Atomic](https://atomicWallet.io?kid=12GR52)
