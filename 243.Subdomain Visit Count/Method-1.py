# Method-1

def subdomainVisits(cpdomains):
    domain_count = {}

    for cpdomain in cpdomains:
        count, domain = cpdomain.split(' ')
        sub_domain = domain.split('.')

        for i in range(len(sub_domain)):
            curr = '.'.join(sub_domain[i:])
            domain_count[curr] = domain_count.get(curr, 0) + int(count)

    return [str(v) + ' ' + k for k, v in domain_count.items()]

# Time Complexity : O(n)
# Space Complexity : O(n)