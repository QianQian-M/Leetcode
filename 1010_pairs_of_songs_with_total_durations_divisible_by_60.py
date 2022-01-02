class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time_mod_dict = defaultdict(int)
        ret = 0
        for time_i in time:
            time_i_mod = time_i % 60 
            rest_time_mod = (60 - time_i_mod) % 60
            if rest_time_mod in time_mod_dict:
                ret += time_mod_dict[rest_time_mod]
            time_mod_dict[time_i_mod] += 1
        return ret
'''
two conditions:

(a+b)%60 =0 ----> ((a%60)+(b%60))%60=0

1. (a%60)=0 and (b%60)=0
2. (a%60)+(b%60)=60


'''