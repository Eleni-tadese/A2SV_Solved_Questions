class Solution:
    def findDuplicate(self, path: List[str]) -> List[List[str]]:
        fd_with_path=defaultdict(list)
        for file_dir in path :
            # ex - root/a 1.txt(abcd) 2.txt(efgh) = file_dir
            parts_of_file_dir = file_dir.split()
            # split it by space and make it this ['root/a', '1.txt(abcd)', '2.txt(efgh)']
            # parts[0] → directory path - root/a
            # parts[1:] → files with content '1.txt(abcd)', '2.txt(efgh)'
            root = parts_of_file_dir[0]
        
            for files in parts_of_file_dir[1:]:
                file_name = files[:files.index("(")]
                file_data = files[files.index("(")+1: files.index(")")]
                full_file_path = root + "/" + file_name
            
                fd_with_path[file_data].append(full_file_path)

   

        d = []
        for file_paths in fd_with_path.values():
            if len(file_paths) > 1:
                d.append(file_paths)
        return d
