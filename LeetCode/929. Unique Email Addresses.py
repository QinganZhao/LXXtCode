class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            for i, char in enumerate(local):
                if char == '+':
                    local = local[:i]
            res.add(local + '@' + domain)
        return len(res)
