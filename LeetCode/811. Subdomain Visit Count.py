class Solution:
    def subdomainVisits(self, cpdomains):
        domains = {}
        for cpdomain in cpdomains:
            freq, website = cpdomain.split()
            if website not in domains:
                domains[website] = int(freq)
            else:
                domains[website] += int(freq)
            for i, char in enumerate(website):
                if char == '.':
                    if website[i+1:] not in domains:
                        domains[website[i+1:]] = int(freq)
                    else:
                        domains[website[i+1:]] += int(freq)
        def output(domain):
            return ''.join([str(domain[1]), ' ', domain[0]])
        return list(map(output, domains.items()))
