class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        common_prefix = strs[0]

        for s in strs[1:]:
            # Compare characters until they match
            while common_prefix and not s.startswith(common_prefix):
                common_prefix = common_prefix[:-1]  # Shorten the common prefix
            
            if not common_prefix:  # Early exit if there's no common prefix
                break

        return common_prefix