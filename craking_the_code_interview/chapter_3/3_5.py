class MyQueue:
	def __init__(self):
		self.new = []
		self.old = []

	def dequeue(self):
		if self.size() == 0:
			return None

		self.shift()
		return self.old.pop()

	def enqueue(self, value):
		self.new.append(value)

	def shift(self):
		if len(self.old) == 0:
			for i in range(len(self.new)):
				self.old.append(self.new.pop())

	def size(self):
		return len(self.new) + len(self.old)

	def __str__(self):
		return str(self.old) + str(self.new)


def main():
	queue = MyQueue()
	queue.enqueue(1)
	queue.enqueue(2)
	queue.enqueue(3)

	print queue.dequeue()
	print queue.dequeue()


if __name__ == "__main__":
	main()