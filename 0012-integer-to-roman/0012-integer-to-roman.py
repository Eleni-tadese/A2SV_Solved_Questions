class Solution:
    def intToRoman(self, num: int) -> str:
        symoly_list=[
            
            ["I",1], ["IV",4],["V",5],
            ["IX",9], ["X",10],["XL",40],
            ["L",50],["XC",90], ["C",100],
            ["CD",400], ["D",500],["CM",900], 
            ["M",1000]
          
        ]
        result=''
        for symbol,value in reversed(symoly_list):
            if num//value:#2400//1000=2 , integer is true except 0 true
                count= num//value #2
                result += count * symbol  # 2* symbol , so 2*M=MM
                num= num%value
        return result

        

        