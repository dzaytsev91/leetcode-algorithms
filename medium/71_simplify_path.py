class Solution:
    def simplifyPath(self, path: str) -> str:
        path = [x for x in path.split("/") if x]
        new_path = []
        for w in path:
            if w == '.':
                continue
            if w == "..":
                if new_path:
                    new_path.pop()
                continue

            new_path.append(w)

        return "/" + "/".join(new_path)
