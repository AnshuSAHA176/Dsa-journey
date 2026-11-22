class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        if len(s) < 4 or len(s) > 12: return []
    
        result = []

        def solved(index: int, current: str, dot_count):
            if dot_count > 3: return
            if index == len(s):
                parts = current.split(".")

                # Check that there are 4 parts, none are empty, and no invalid leading zeros
                if len(parts) == 4 and all(
                    p.isdigit()
                    and (p == "0" or not p.startswith("0"))
                    and 0 <= int(p) <= 255
                    for p in parts
                ):
                    result.append(current)
                return
            if dot_count < 3 and index < len(s) - 1:
                solved(
                index=index + 1,
                current=current + s[index] + ".",
                dot_count=dot_count + 1,
            )
            solved(index=index + 1, current=current + s[index], dot_count=dot_count)

        solved(index=0, current="", dot_count=0)
        return result