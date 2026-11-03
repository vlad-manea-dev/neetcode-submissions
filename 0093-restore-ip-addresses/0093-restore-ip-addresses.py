class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        valid_address = []
	
        def backtrack(i, parts):
            if i >= len(s) and len(parts) == 4:
                valid_address.append(".".join(parts.copy()))
                return
            if len(parts) == 4:
                return
            for L in range(1, 4):
                if i + L > len(s):
                    break
                part = s[i:i+L]
                if part[0] == "0" and L > 1:
                    break
                if int(part) > 255:
                    break
                parts.append(part)
                backtrack(i + L, parts)	
                parts.pop()
                    

        backtrack(0,[])
        return valid_address
