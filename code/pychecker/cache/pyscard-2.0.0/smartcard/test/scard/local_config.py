from smartcard.util import toHexString
expectedReaders = []
expectedATRs = []
expectedATRinReader = {}
for i in range(len(expectedReaders)):
    expectedATRinReader[expectedReaders[i]] = expectedATRs[i]
expectedReaderForATR = {}
for i in range(len(expectedReaders)):
    expectedReaderForATR[toHexString(expectedATRs[i])] = expectedReaders[i]
expectedReaderGroups = ['SCard$DefaultReaders']
