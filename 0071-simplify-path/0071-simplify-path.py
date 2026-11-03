class Solution:
    def simplifyPath(self, path: str) -> str:
        segmented_path = path.split("/")	
        segmented_path = [s for s in segmented_path if s and s != "."]
        folder_stack = []
        for folder in segmented_path:
            if folder == "..":
                if folder_stack:
                    folder_stack.pop()
                continue
            folder_stack.append(folder)
        cleaned_path = "/" + "/".join(folder_stack)
        return cleaned_path
