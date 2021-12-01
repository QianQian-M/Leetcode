class Solution:
    def reformatDate(self, date: str) -> str:
        
        s = date.split()
        
        month ={"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
        res = s[-1]
        
        res = res+"-"+month[s[1]]+"-"
        
        day=""
        for ele in s[0]:
            if ele.isdigit():
                day+=ele
            else:
                break
        
        if len(day)==1:
            res+="0"+day
        else:
            res+=day
        return res
        

## Concise Solution
class Solution:
    def reformatDate(self, date: str) -> str:
        parts = date.split()
        
        day = int(parts[0][:-2])
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"].index(parts[1]) + 1
        year = int(parts[2])
        
        return '{:04d}-{:02d}-{:02d}'.format(year, month, day)