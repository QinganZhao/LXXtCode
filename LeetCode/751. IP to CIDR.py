class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        res = []
        binip = self.ip2bin(ip)
        while n:
            possibleNum = self.possibleNum(binip)
            while possibleNum > n:
                possibleNum >>= 1
            n -= possibleNum
            res.append(self.bin2ip(binip) + '/' + str(32-self.lastOneInd(possibleNum)))
            binip += possibleNum 
        return res
        
    def ip2bin(self, ip):
        domains = list(map(int, ip.split('.')))
        return (domains[0] << 24) + (domains[1] << 16) + (domains[2] << 8) + domains[3]
    
    def bin2ip(self, binip):
        return '.'.join([str(binip >> 24 & 255), str(binip >> 16 & 255), str(binip >> 8 & 255), str(binip & 255)])
    
    def lastOneInd(self, binip):
        i = 0
        while binip:
            if binip & 1:
                return i
            binip >>= 1 
            i += 1
            
    def possibleNum(self, binip):
        index = self.lastOneInd(binip)
        return 1 << index
