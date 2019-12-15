from queue import PriorityQueue as pQueue


class PriorityQueue(pQueue):
    def _init(self):
        self.data = []

    def _get(self, index):
        return self.data[index]

    def put(self, ):
        super().put(item, block, timeout)

    def empty(self) -> bool:
        return super().empty()
