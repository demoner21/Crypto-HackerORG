class PartyAnimal:
	x = 1 
	def party(self):
		self.x = self.x + 2
		print(self.x)

an = PartyAnimal()
an.party()
an.party()
print(type(an.party()))
