import os
import re

# specify the path of the porn list file
file_path = "porn_list.txt"

# open the porn list file and read the lines using the correct encoding
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# replace any non-ascii characters with a placeholder string
non_ascii_re = re.compile(r'[^\x00-\x7F]+')
new_lines = [non_ascii_re.sub('###', line).replace("0.0.0.0", "").strip() for line in lines if line.strip()]

# write the new lines to a new file using utf-8 encoding
with open("new_porn_list.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(new_lines))

# specify the path of the hosts file
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"  # update this path to match your operating system

# open the new porn list file and add each website to the hosts file with the localhost IP address
with open("new_porn_list.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open(hosts_path, "a") as hosts_file:
    for line in lines:
        hosts_file.write("127.0.0.1 " + line.strip() + "\n")

# flush the DNS cache to ensure that the changes take effect immediately
os.system("ipconfig /flushdns")
