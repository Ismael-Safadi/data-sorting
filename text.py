import re
import requests
class A:
    def __init__(self,fname,choice,uurl):
        
        global string 
        if choice ==1:
            fname=str(fname)
            choice=int(choice)
            read_read=open(fname,"r")
            string=read_read.readlines()
            string=str(string)
            read_read.close()
        elif choice ==2:
            uurl=str(uurl)
            choice=str(choice)
            x=requests.get(uurl)
            string=x.text
    def filemaker(self,name,hashvalue):
        hashvalue=str(hashvalue)
        open_open=open(name,"a")
        open_open.writelines(hashvalue+"\n")
        open_open.close()
    def macs(self):
        macs=re.findall(r"([\dA-F]{2}(?:[-:][\dA-F]{2}){5})", string)
        for mac in macs:
            self.filemaker("mac.txt",mac)
    def hashes(self):
        md5=re.findall(r'\b([0-9a-fA-F]{32})\b',string)
        sha1=re.findall(r'\b([0-9a-fA-F ]{40})\b',string)
        sha512=re.findall(r'\b([0-9a-fA-F ]{128})\b',string)
        sha256=re.findall(r'\b([0-9a-fA-F ]{64})\b',string)
        sha384=re.findall(r'\b([0-9a-fA-F ]{96})\b',string)
        sha224=re.findall(r'\b([0-9a-fA-F ]{56})\b',string)  
        if md5 ==[] or md5 ==['']:
            pass
        else:
            for m in md5:
                self.filemaker("md5.txt",m)
        if sha1 ==[] or sha1 ==['']:
            pass
        else:
            for s1 in sha1:
                self.filemaker("sha1.txt",s1)
        if sha512 ==[] or sha512 ==['']:
            pass
        else:
            for s5 in sha512:
                self.filemaker("sha512.txt",s5)
        if sha256 ==[] or sha256 ==['']:
            pass
        else:
            for s25 in sha256:
                self.filemaker("sha256.txt",s25)
        if sha384 ==[] or sha384 ==['']:
            pass
        else:
            for s3 in sha384:
                self.filemaker("sha384.txt",s3)
        if sha224 ==[] or sha224 ==['']:
            pass
        else:
            for s22 in sha384:
                self.filemaker("sha224.txt",s22)        
                        
                
                
       
    def extention(self):	
            extention =  re.findall(r'https?://(?:[a-z0-9\-]+\.)+[a-z0-9]{2,6}(?:/[^/#?]+)+\.(?:mp4|png|jpg|mp3)',string)
            for ext in extention:
                    if "jpg" in str(ext):
                            self.filemaker("jpg.txt",ext)
                    elif "png" in str(ext):
                             self.filemaker("png.txt",ext)
                    elif "mp4" in str(ext):
                             self.filemaker("mp4.txt",ext)
                    elif "mp3" in str(ext):
                             self.filemaker("mp3.txt",ext)
                            
    def emails(self):
            emails=re.findall(r'[\w\.-]+@[\w\.-]+',string)
            for email in emails:
                    if "gmail" in str(email):
                        self.filemaker("gmail.txt",email)
                    elif "hotmail" in str(email):
                            filemaker("hotmail.txt",email)
                    elif "protonmail" in str(email):
                            filemaker("protonmail.txt",email)
                    elif "yahoo" in str(email):
                            filemaker("yahoo.txt",email)
    def domains(self):
            domains=re.findall(r'(?P<url>www[^\s]+)',string)
            for domain in domains:
                    self.filemaker("domains.txt",domain)
                    
    def urls(self):
            urls=re.findall("(?P<url>https?://[^\s]+)",string)
            for url in urls:
                    self.filemaker("urls.txt",url)
    def ips(self):
            ips = re.findall( r'[0-9]+(?:\.[0-9]+){3}', string )
            for ip in ips:
                    self.filemaker("ips.txt",ip)
