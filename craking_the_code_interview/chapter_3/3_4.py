#!/usr/bin/env python

class Tower:
	def __init__(self, label, tower):
		self.label = label
		self.tower = tower

	def pop(self):
		return self.tower.pop()

	def push(self, value):
		self.tower.append(value)

	def __str__(self):
		return str(self.tower)


class HanoiTower:
	def __init__(self, size, label=["a", "b", "c"]):
		self.size = size
		self.label = label
		self.source_tower = Tower(label[0], tower=range(size, 0, -1))
		self.buffer_tower = Tower(label[1], [])
		self.target_tower = Tower(label[2], [])

	def move_disks(self, n, source_tower, target_tower, buffer_tower):
		if n == 0:
			return

		self.move_disks(n-1, source_tower, buffer_tower, target_tower)
		self.move_top(source_tower, target_tower)
		self.move_disks(n-1, buffer_tower, target_tower, source_tower)

	def move_top(self, source_tower, target_tower):
		result = source_tower.pop()
		target_tower.push(result)
		print "move %d from %s to %s" % (result, source_tower.label, target_tower.label)
		print self.source_tower, self.buffer_tower, self.target_tower

	def play(self):
		print "origin status"
		print self.source_tower, self.buffer_tower, self.target_tower
		self.move_disks(self.size, self.source_tower, self.target_tower, self.buffer_tower)

	def reset(self):
		self.source_tower.tower = range(self.size)
		self.buffer_tower.tower = []
		self.target_tower.tower = []


def main():
	hanoi = HanoiTower(3)
	hanoi.play()


if __name__ == "__main__":
	main()