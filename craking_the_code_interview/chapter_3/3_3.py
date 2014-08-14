#!/usr/bin/env python

class SetOfStacks:
	def __init__(self, capacity):
		self.capacity = capacity
		self.stacks = [[]]

	def pop(self):
		result = self.stacks[-1].pop()
		if len(self.stacks[-1]) == 0:
			del self.stacks[-1]
		return result

	def push(self, value):
		last_stack = self.stacks[-1]
		if len(last_stack) == self.capacity:
			self.stacks.append([value])
		else:
			last_stack.append(value)

	def pop_at(self, index):
		if index == len(self.stacks):
			return self.pop()
		elif len(self.stacks[index]) == 1:
			result = self.stacks[index]
			del self.stacks[index]
			return result
		else:
			return self.stacks[index].pop()

def main():
	a = SetOfStacks(2)

	a.push(1)
	a.push(2)
	a.push(3)
	a.push(4)
	a.push(5)
	print a.stacks

	a.pop_at(1)
	print a.stacks

	a.pop_at(1)
	print a.stacks

	a.pop_at(2)
	print a.stacks

if __name__ == "__main__":
	main()