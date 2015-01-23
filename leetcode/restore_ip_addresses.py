class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        record, result = [], set()
        self.parse_ip(s, 0, 4, record, result)
        
        real_result = []
        for ip in result:
            ip_address = ".".join([str(c) for c in list(ip)])
            real_result.append(ip_address)
        return real_result

    def parse_ip(self, ip, index, left, record, result):
        if left == 0:
            if index >= len(ip):
                result.add(tuple(record))
            else:
                return
        if index >= len(ip):
            return
     
        ip_value = int(ip[index:index+1])
        record.append(ip_value)
        self.parse_ip(ip, index+1, left-1, record, result)
        record.pop()

        if ip[index] != "0":
            ip_value = int(ip[index:index+2])
            record.append(ip_value)
            self.parse_ip(ip, index+2, left-1, record, result)
            record.pop()

            ip_value = int(ip[index:index+3])
            if ip_value <= 255:
                record.append(ip_value)
                self.parse_ip(ip, index+3, left-1, record, result)
                record.pop()


s = Solution()
ip = "25525511135"
ip = "010010"
print s.restoreIpAddresses(ip)