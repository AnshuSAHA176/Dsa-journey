class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        frequency={}
        for tile in tiles:
            if tile in frequency:
                frequency[tile]+=1
                continue
            frequency[tile]=1
        print(frequency)
        def solved():
           
            count = 0
            for ch in frequency:
                if frequency[ch] == 0:
                    continue
                count+=1
                frequency[ch]-=1
                count+=solved()
                frequency[ch]+=1
            return count
                
        return solved()