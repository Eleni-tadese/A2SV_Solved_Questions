class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        mapp={")":"(", 
        "}":"{",
        "]":"["
        }

        for brances in s:
            if braces in mapp :
                top = stack.pop() 
                

            
