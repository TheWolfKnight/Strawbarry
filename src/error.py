if __name__ == "__main__":
	exit(1)


class UnreachableCodeError(Exception):
	"""
	An exception made to report and unreachable part of the code.\n
	Should only be placed for my own debuging, and will never be run into during code.\n
	The entire thing will likely be removed, once i think the game is done.\n
	@param file: str\n
	@param line: int\n
	@param char: int\n
	"""
	def __init__(self, file: str, line: int, char: int):
		f: int = file[::-1].index('\\')
		self.file = file[-f:]
		self.line = line
		self.char = char

	def __str__(self) -> str:
		return f"\n{self.file}:{self.line}:{self.char}: Unreachable code reached"
