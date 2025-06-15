import os
from pathlib import Path

def find_partially_matching_files(dir1, dir2):
    """
    Finds matching files where the first 10 characters of a file in dir1
    are contained within a filename in dir2.

    Args:
        dir1 (str): The path to the first directory.
        dir2 (str): The path to the second directory.

    Returns:
        list: A list of tuples, where each tuple contains the matching
              pair of filenames (file_from_dir1, file_from_dir2).
    """
    try:
        files1 = os.listdir(dir1)
        files2 = os.listdir(dir2)
        matching_pairs = []

        for file1 in files1:
            if len(file1) >= 10:
                search_key = file1[:10]
                for file2 in files2:
                    if search_key in file2:
                        matching_pairs.append((file1, file2))
        
        return matching_pairs

    except FileNotFoundError as e:
        return f"Error: {e}"

def add_media(filepath, matching_tuple):
    for media, post in matching_tuple:
        with open(filepath+post, "r") as file:
            contents = file.read()
            if media not in contents:
                file.close()
                with open(filepath+post, "a") as file:
                    if "img" in media:
                        file.write("\n" + "<img src=\"{{site.base_url}}{% link /assets/images/" +media+ " %}\" style=\"width:330px\"><br> \n")                
                    elif "mov" in media:
                        if "-p" in media:
                            file.write("\n" + "<video autoplay muted playsinline width=\"270\" height=\"480\ preload=\"metadata\" controls=\"controls\">" + "\n" +
                                "<source src=\"{{site.base_url}}{% link /assets/videos/" +media+ " %}\" type=\"video/mp4\">" + "\n" +
                                "Your browser does not support video tag." + "\n" + 
                                "</video> \n")
                        if "-l" in media:
                            file.write("\n" + "<video autoplay muted playsinline width=\"660\" height=\"371\" preload=\"metadata\" controls=\"controls\">" + "\n" +
                                "<source src=\"{{site.base_url}}{% link /assets/videos/" +media+ " %}\" type=\"video/mp4\">" + "\n" +
                                "Your browser does not support video tag." + "\n" + 
                                "</video> \n")
                                
                file.close()
            
""" Run Script """
cwd = str(Path.cwd())
img_pairs = find_partially_matching_files(cwd + "/assets/images", cwd + "/_posts")
#print(img_pairs)
mov_pairs = find_partially_matching_files(cwd + "/assets/videos", cwd + "/_posts")
#print(mov_pairs)
add_media(cwd + "/_posts/", img_pairs)
add_media(cwd + "/_posts/", mov_pairs) 
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

