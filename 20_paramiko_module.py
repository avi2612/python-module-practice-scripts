import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='139.59.46.196' ,username='root',password='aVinash123singh',port=22)
# ssh.connect(hostname='139.59.46.196' ,username='root',key_file_name='/home/avi/temp',port=22)


stdin,stdout,stderr=ssh.exec_command('cat /etc/os-release')
print("output is ",stdout.readlines())
# print("error is ",stderr.readlines())


sftp_client=ssh.open_sftp()
print(sftp_client.getcwd())
sftp_client.chdir("/root/")
print(sftp_client.getcwd())
# sftp_client.get("/root/jjt","/home/avi/kky")
sftp_client.put("/home/avi/kky","/tmp/ppp")
sftp_client.close()

ssh.close()