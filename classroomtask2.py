class ipaddr()
	def __init__(self,ip=[0,0,0,0],nm=[0,0,0,0]):
		self.ip=ip
		self.nm=nm
	def __str__(self):
		ipformat=""
		for ips in self.ip:
		ipformat=ipformat+str(ips)+"."
		return(ipformat)








myip=ipaddr[192,168,1,1],[255,255,255,0])
addip=ipaddr(2,1,1,0)


