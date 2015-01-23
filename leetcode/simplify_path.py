class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        directories = path.split("/")[1:]
        stack = []

        for d in directories:
            if d == "" or d == ".":
                continue
            
            if d == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(d)
        
        if len(stack) == 0:
            return "/"

        result = ""
        while len(stack) != 0:
            result = "/" + stack.pop() + result
        return result


s = Solution()
path = "/Ey///tGTOpEYLanDPMbi///GSQ///FrpmBGYNWwzzmjht///../////././//lecgkBRZAVAxZ///Zd/./mk/ATwoPIhGxCJ/kKhSWFvnxu/./././..///AGXWOJ/./fGnxupDYzlLSj///////././//////./..///.././aXQnUdOa/ghFWgHbsbtwC///dqnUEkXWT/Szhywanfeq/.///wkuyecUs///./././kcQBpYsmVK/LJlKKjVoMSd/./agJXrBN/CvWrzYKPfu/../vEqiwsQIGQDZVqGdRj/../Dg/XOkpesihfmM/mwAQwacSdqPhZt/./MQXrcLcaqFX///./RydpRMPOVQcbCkREn/./itNLpEYOwBGxKL///.///////././../VHXkg///////////YQGUoQyKqyNyU/../JqGXusfFTTrYzhrPdSSF/./mtFa/.///MpKfOKMrtRBiZAaPhlM/./../bpDtnlOa/cIXfRgPdpVinySWVwZL/IixIezvPlipikiEGFhBV/yNdUYAPdkmXjeygkmrJ/.///Xx/CouwagZdaOBRa/ks/uUdMVLMECAmfyZpEMfb///.///uaLqqFutkvTrhmSiNql///LNNgsXCVp/EcQd///IdMOhJOtHXkqAi/././GoTWQSOzwIzfeYv/bVFpaNE/./bSnAMjnpMtj///twdbrXhwmRpKVrFluUA///U///oZxnyCK/gadpSFEKEwlxexkCrNN/DfOnawleHNLkvDFaRsM///aj/UPCOEDUHCTM/guDKoQLUxK///W/WzzymEguXHWA/.///./cgdqMgS/../esaYBlSUDizBHj/./../GktkmPrBltEjhDtbCrGH/fyrjyNIsVeopA/.././//.///MCDIBEsyoOEe/b///PrtMJuYAQ/qjxcVyDgudaET///nFvXtHDrUDohAYwkeAZ/DZLneYpMfaigp/TjLysoIqQuvyGyzXYi///GnNTTias/eKvBRtp/vPAJqAveyDwlBUfy/.././aeqpSIyC/./qSgNfCEy///"
#path = "/a/./b/../../c/"
#path = "/home//foo/"
path = "/.../"
print s.simplifyPath(path)