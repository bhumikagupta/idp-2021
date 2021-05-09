class solution(object):
    def generate_subset(self,nums):
        def dfs(nums,index,res,path):
            res.append(path)
            for i in range(index,len(nums)):
                dfs(nums,i+1,res,path+[nums[i]])
        res=[]
        dfs(nums,0,res,[])
                
        return res
