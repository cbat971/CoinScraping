from lxml import html
import requests
import datetime
import time

page = requests.get('https://coinmarketcap.com/', 'https://coinmarketcap.com/2')
tree = html.fromstring(page.content)

# = tree.xpath('/text()')

BTC = tree.xpath('//*[@id="id-bitcoin"]/td[4]/a/text()')
TRX = tree.xpath('//*[@id="id-tron"]/td[4]/a/text()')
XRP = tree.xpath('//*[@id="id-ripple"]/td[4]/a/text()')
ETH = tree.xpath('//*[@id="id-ethereum"]/td[4]/a/text()')
BCH = tree.xpath('//*[@id="id-bitcoin-cash"]/td[4]/a/text()')
EOS = tree.xpath('//*[@id="id-eos"]/td[4]/a/text()')
LTC = tree.xpath('//*[@id="id-litecoin"]/td[4]/a/text()')
BNB = tree.xpath('//*[@id="id-binance-coin"]/td[4]/a/text()')
USDT = tree.xpath('//*[@id="id-tether"]/td[4]/a/text()')
XLM = tree.xpath('//*[@id="id-stellar"]/td[4]/a/text()')
ADA = tree.xpath('//*[@id="id-cardano"]/td[4]/a/text()')
XMR = tree.xpath('//*[@id="id-monero"]/td[4]/a/text()')
DASH = tree.xpath('//*[@id="id-dash"]/td[4]/a/text()')
BSV = tree.xpath('//*[@id="id-bitcoin-sv"]/td[4]/a/text()')
ATOM = tree.xpath('//*[@id="id-cosmos"]/td[4]/a/text()')
MIOTA = tree.xpath('//*[@id="id-iota"]/td[4]/a/text()')
XTZ = tree.xpath('//*[@id="id-tezos"]/td[4]/a/text()')
ETC = tree.xpath('//*[@id="id-ethereum-classic"]/td[4]/a/text()')
NEO = tree.xpath('//*[@id="id-neo"]/td[4]/a/text()')
MKR = tree.xpath('//*[@id="id-maker"]/td[4]/a/text()')
ONT = tree.xpath('//*[@id="id-ontology"]/td[4]/a/text()')
NEM = tree.xpath('//*[@id="id-nem"]/td[4]/a/text()')
BAT = tree.xpath('//*[@id="id-basic-attention-token"]/td[4]/a/text()')
CRO = tree.xpath('//*[@id="id-crypto-com-chain"]/td[4]/a/text()')
ZEC = tree.xpath('//*[@id="id-zcash"]/td[4]/a/text()')
VET = tree.xpath('//*[@id="id-vechain"]/td[4]/a/text()')
BTG = tree.xpath('//*[@id="id-bitcoin-gold"]/td[4]/a/text()')
DOGE = tree.xpath('//*[@id="id-dogecoin"]/td[4]/a/text()')
USDC = tree.xpath('//*[@id="id-usd-coin"]/td[4]/a/text()')
DCR = tree.xpath('//*[@id="id-decred"]/td[4]/a/text()')
QTUM = tree.xpath('//*[@id="id-qtum"]/td[4]/a/text()')
OMG = tree.xpath('//*[@id="id-omisego"]/td[4]/a/text()')
TUSD = tree.xpath('//*[@id="id-trueusd"]/td[4]/a/text()')
REP = tree.xpath('//*[@id="id-augur"]/td[4]/a/text()')
WAVES = tree.xpath('//*[@id="id-waves"]/td[4]/a/text()')
LSK = tree.xpath('//*[@id="id-lisk"]/td[4]/a/text()')
NANO = tree.xpath('//*[@id="id-nano"]/td[4]/a/text()')
LINK = tree.xpath('//*[@id="id-chainlink"]/td[4]/a/text()')
PAX = tree.xpath('//*[@id="id-paxos-standard-token"]/td[4]/a/text()')
HOT = tree.xpath('//*[@id="id-holo"]/td[4]/a/text()')
BCN = tree.xpath('//*[@id="id-bytecoin-bcn"]/td[4]/a/text()')
RVN = tree.xpath('//*[@id="id-ravencoin"]/td[4]/a/text()')
ZRX = tree.xpath('//*[@id="id-0x"]/td[4]/a/text()')
ICX = tree.xpath('//*[@id="id-icon"]/td[4]/a/text()')
ZIL = tree.xpath('//*[@id="id-zilliqa"]/td[4]/a/text()')
BTS = tree.xpath('//*[@id="id-bitshares"]/td[4]/a/text()')
NPXS = tree.xpath('//*[@id="id-pundi-x"]/td[4]/a/text()')
BTT = tree.xpath('//*[@id="id-bittorrent"]/td[4]/a/text()')
IOST = tree.xpath('//*[@id="id-iostoken"]/td[4]/a/text()')
AE = tree.xpath('//*[@id="id-aeternity"]/td[4]/a/text()')
DGB = tree.xpath('//*[@id="id-digibyte"]/td[4]/a/text()')
KMD = tree.xpath('//*[@id="id-komodo"]/td[4]/a/text()')
HT = tree.xpath('//*[@id="id-huobi-token"]/td[4]/a/text()')
XVG = tree.xpath('//*[@id="id-verge"]/td[4]/a/text()')
AOA = tree.xpath('//*[@id="id-aurora"]/td[4]/a/text()')
ENJ = tree.xpath('//*[@id="id-enjin-coin"]/td[4]/a/text()')
SC = tree.xpath('//*[@id="id-siacoin"]/td[4]/a/text()')
STEEM = tree.xpath('//*[@id="id-steem"]/td[4]/a/text()')
BTM = tree.xpath('//*[@id="id-bytom"]/td[4]/a/text()')
KCS = tree.xpath('//*[@id="id-kucoin-shares"]/td[4]/a/text()')
ABBC = tree.xpath('//*[@id="id-abbc-coin"]/td[4]/a/text()')
INB = tree.xpath('//*[@id="id-insight-chain"]/td[4]/a/text()')
WTC = tree.xpath('//*[@id="id-waltonchain"]/td[4]/a/text()')
FCT = tree.xpath('//*[@id="id-factom"]/td[4]/a/text()')
QBIT = tree.xpath('//*[@id="id-qubitica"]/td[4]/a/text()')
STRAT = tree.xpath('//*[@id="id-stratis"]/td[4]/a/text()')
DAI = tree.xpath('//*[@id="id-dai"]/td[4]/a/text()')
THETA = tree.xpath('//*[@id="id-theta"]/td[4]/a/text()')
MCO = tree.xpath('//*[@id="id-crypto-com"]/td[4]/a/text()')
XIN = tree.xpath('//*[@id="id-mixin"]/td[4]/a/text()')
SNT = tree.xpath('//*[@id="id-status"]/td[4]/a/text()')
CNX = tree.xpath('//*[@id="id-cryptonex"]/td[4]/a/text()')
THR = tree.xpath('//*[@id="id-thorecoin"]/td[4]/a/text()')
GNT = tree.xpath('//*[@id="id-golem-network-tokens"]/td[4]/a/text()')
VEST = tree.xpath('//*[@id="id-vestchain"]/td[4]/a/text()')
ARDR = tree.xpath('//*[@id="id-ardor"]/td[4]/a/text()')
MONA = tree.xpath('//*[@id="id-monacoin"]/td[4]/a/text()')
WAX = tree.xpath('//*[@id="id-wax"]/td[4]/a/text()')
GXC = tree.xpath('//*[@id="id-gxchain"]/td[4]/a/text()')
MXM = tree.xpath('//*[@id="id-maximine-coin"]/td[4]/a/text()')
DGD = tree.xpath('//*[@id="id-digixdao"]/td[4]/a/text()')
MAID = tree.xpath('//*[@id="id-maidsafecoin"]/td[4]/a/text()')
AION = tree.xpath('//*[@id="id-aion"]/td[4]/a/text()')
ZEN = tree.xpath('//*[@id="id-zencash"]/td[4]/a/text()')
MANA = tree.xpath('//*[@id="id-decentraland"]/td[4]/a/text()')
ELF = tree.xpath('//*[@id="id-aelf"]/td[4]/a/text()')
PAI = tree.xpath('//*[@id="id-project-pai"]/td[4]/a/text()')
PPT = tree.xpath('//*[@id="id-populous"]/td[4]/a/text()')
ARK = tree.xpath('//*[@id="id-ark"]/td[4]/a/text()')
NEW = tree.xpath('//*[@id="id-newton"]/td[4]/a/text()')
ORBS = tree.xpath('//*[@id="id-orbs"]/td[4]/a/text()')
TRUE = tree.xpath('//*[@id="id-truechain"]/td[4]/a/text()')
LOOM = tree.xpath('//*[@id="id-loom-network"]/td[4]/a/text()')
ETN = tree.xpath('//*[@id="id-electroneum"]/td[4]/a/text()')
NULS = tree.xpath('//*[@id="id-nuls"]/td[4]/a/text()')
LRC = tree.xpath('//*[@id="id-loopring"]/td[4]/a/text()')
NEXO = tree.xpath('//*[@id="id-nexo"]/td[4]/a/text()')
HC = tree.xpath('//*[@id="id-hypercash"]/td[4]/a/text()')
XZC = tree.xpath('//*[@id="id-zcoin"]/td[4]/a/text()')


coins = ["TRX", "BTC", "XRP", 'ETH', 'BCH', 'EOS', 'LTC', 'BNB', 'USDT', 'XLM', 'ADA', 'XMR', 
'DASH', 'BSV', 'ATOM', 'MIOTA', 'XTZ', 'ETC', 'NEO', 'KKR', 'ONT', 'MEM', 'BAT', 'CRO', 'ZEC', 
'VET', 'BTG', 'DOGE', 'USDC', 'DCR', 'QTUM', 'OMG', 'TUSD', 'REP', 'WAVES', 'LSK', 'NANO', 'LINK', 
'PAX', 'HOT', 'BCN', 'RVN', 'ZRX', 'ICX', 'ZIL', 'BTS', 'NPXS', 'BTT', 'IOST', 'AE', 'DGB', 'KMD', 'HT', 
'XVG', 'AOA', 'ENJ', 'SC', 'STEEM', 'BTM', 'KCS', 'ABBS', 'INB', 'WTC', 'FCT', 'QBIT', 'STRAT', 'DAI', 
'THETA', 'MCO', 'XIN', 'SNT', 'CNX', 'THR', 'GNT', 'VEST', 'ARDR', 'MONA', 'WAX', 'GXC', 'MXM', 'DGD', 
'MAID', 'AION', 'ZEN', 'MANA', 'ELF', 'PAI', 'PPT', 'ARK', 'NEW', 'ORBS', 'TRUE', 'LOOM', 'ETN', 'NULS', 
'LRC', 'NEXO', 'HC', 'XZC']

coin = [TRX, BTC, XRP, ETH, BCH, EOS, LTC, BNB, USDT, XLM, ADA, XMR, DASH, BSV, ATOM, MIOTA, XTZ,
        ETC, NEO, MKR, ONT, NEM, BAT, CRO, ZEC, PAX, HOT, BCN, RVN, ZRX, ICX, ZIL, BTS, NPXS, BTT, IOST,
        AE, DGB, KMD, HT, XVG, AOA, ENJ, SC, STEEM, BTM, KCS, ABBC, INB, WTC, FCT, QBIT, STRAT, DAI, THETA,
        MCO, XIN, SNT, CNX, THR, GNT, VEST, ARDR, MONA, WAX, GXC, MXM, DGD, MAID, AION, ZEN, MANA, ELF, PAI,
        PPT, ARK, NEW, ORBS, TRUE, LOOM, ETN, NULS, LRC, NEXO, HC, XZC]








print(LOOM)


Bitcoinlist = list(BTC[0])
Bitcoinlist.pop(0)
BTCcompare = ''.join(Bitcoinlist)
BTCcompare = float(BTCcompare)



def crypto_Convert(stuff):
    a = str(stuff)
    stufflist = list(a)
    stufflist.pop(0)
    stufflist.pop(0)
    stufflist.pop(0)
    stufflist.pop(-1)
    stufflist.pop(-1)
    stuff = ''.join(stufflist)
    stuff = float(stuff)
    print(stuff)







for i in coin:
  crypto_Convert(i)
  
  
coinDict = dict(zip(coins, coin))
#print(coinDict)


