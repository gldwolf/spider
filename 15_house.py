class House:
	def __init__(self, area, info, addr):
		self.area = area
		self.info = info
		self.addr = addr
		self.left_area = area
		self.items = []

	def __str__(self):
		msg = '房子的户型是:%s, 总面积是:%d, 地址是:%s'%(self.info, self.area, self.addr)
		msg += '. 现在的家具有:%s, 房子的剩余面积是: %d'%(str(self.items), self.left_area)
		return msg

	def add_items(self, item):	
		self.left_area -= item.get_area()
		self.items.append(item.get_name())

class Bed:
	def __init__(self, name, area):
		self.name = name
		self.area = area

	def get_area(self):
		return self.area

	def get_name(self):
		return self.name


new_house = House(150, '三室两厅', '北京市朝阳区长安路８８８号')
print(new_house)

bed1 = Bed('席梦思', 4)
bed2 = Bed('双人床', 6)
new_house.add_items(bed1)
print(new_house)
new_house.add_items(bed2)
print(new_house)

input("Wait...")