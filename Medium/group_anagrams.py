def groupAnagrams(strs):
        m = collections.defaultdict(list)
        for s in strs:
            m[''.join(sorted(s))].append(s)
        return list(m.values())
