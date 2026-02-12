class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []        # final output list
        in_block = False   #  flag to check are we inside a block comment
        current_line = ""  # storing current line being in rsult and later appended and reset to impty for next line code 
    
        for line in source:
            i = 0
            while i < len(line):
                # CASE 1: NOT inside block comment - true 
                if not in_block:
                    # Check for start of line comment '//'
                    if i + 1 < len(line) and line[i] == '/' and line[i+1] == '/':
                        break  # ignore rest of this line
                    
                    # Check for start of block comment '/*'
                    elif i + 1 < len(line) and line[i] == '/' and line[i+1] == '*':
                        in_block = True
                        i += 1  # skip the '*'
                    
                    # Normal code character
                    else:
                        current_line += line[i]
                
                # CASE 2: INSIDE block comment
                else:
                    # Check for end of block comment '*/'
                    if i + 1 < len(line) and line[i] == '*' and line[i+1] == '/':
                        in_block = False
                        i += 1  # skip the '/'
                    # Otherwise, ignore everything inside block comment
                
                i += 1  # move to next character
            
            # After processing a line:
            # If we have accumulated code AND we're NOT inside a block comment
            if current_line and not in_block:
                result.append(current_line)
                current_line = ""  # reset for next line
            
            # If we ARE inside a block comment:
            # current_line continues accumulating across lines
        
        return result