def numberToWords(num):
        def helper(num):
            if num == 0:
                return ''
            if num < 20:
                return lessThan20[num] + ' '
            if num < 100:
                return tens[num//10] + ' '+ helper(num%10)
            else:
                return lessThan20[num//100] + ' Hundred ' + helper(num%100)
        lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        thousands = ["","Thousand","Million","Billion"]
        if num == 0:
            return 'Zero'
        res = ''
        for i in range(len(thousands)):
            if num % 1000 != 0:
                res = helper(num % 1000) + thousands[i] + ' '+ res
            num = num//1000
        return res.strip()
            
