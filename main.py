class Okus(object):

	_who = "str"
	_nickname = "str"
	_age = 0

	def __init__(self, who, nick, age):
		self._who = who
		self._nickname = nick
		self._age = age
	
	def set_who(self, w):
		self._who = w		

	def set_nickname(self, n):
		self._nickname = n
		
	def set_age(self, a):
		self._age = a

	def who(self):
		return self._who
	
	def nickname(self):
		return self._nickname
	
	def age(self):
		return self._age
		
	def status_printf(self):
		print("\n     ВЫВОД:     ")
		print("Who = ", self._who)
		print("Nickname = ", self._nickname)
		print("Age = ", self._age, "\n")
	
	def getters(self):
		while True:		
			try:
				print("Запрос данный начат")
				self._who = input("Введите ваше имя: \n")
				self._nickname = input("Введите ваш никнейм: \n")
				self._age = int(input("Введите ваш возраст: \n"))
				print("Запрас данный закончен")
				break
			except:
				print("\nОшибка, попробуйте ещё\n")		
				
pi_obj = Okus("Vlad", "Infix", 15)
pi_obj.status_printf()

py_obj = Okus("n", "n", 1)
py_obj.getters()
py_obj.status_printf()