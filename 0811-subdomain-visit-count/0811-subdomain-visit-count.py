class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        all_sub_domains =[]
        sub_domains=[]
        count={}
        for i in range(len(cpdomains)):
            number_index_count = 0  
            for ch in cpdomains[i]:
                if ch.isdigit():
                    number_index_count += 1
                else:
                    break   # stop when digit ends


            number=int(cpdomains[i][:number_index_count])
            domain=cpdomains[i][number_index_count+1:]

    
            sub_domains_collection=domain.split('.')
    
            for j in range(len(sub_domains_collection)):
            
                sub =".".join(sub_domains_collection[j:])

                if sub in count:
                        count[sub] += number
                else:
                    count[sub] = number
        result = []
        for k, v in count.items():
            result.append(str(v) + " " + k)
        return result

       


       
