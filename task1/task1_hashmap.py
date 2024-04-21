from typing import Any, List


class HashmapStructure:
    size: int
    threshold: float
    num_elements: int
    buckets: List

    def __init__(self, size: int = 100):
        self.size = size
        self.threshold = 0.75
        self.num_elements = 0
        self.buckets = [[] for _ in range(size)]

    def __hash(self, key: Any) -> int:
        return hash(key) % self.size

    def put(self, key: Any, val: Any) -> None:
        if self.num_elements / self.size >= self.threshold:
            self._resize()
        hashed_key = self.__hash(key)
        bucket = self.buckets[hashed_key]

        for index, (record_key, _) in enumerate(bucket):
            if record_key == key:
                bucket[index] = (key, val)
                return

        bucket.append((key, val))
        self.num_elements += 1

    def _resize(self) -> None:
        self.size *= 2
        new_buckets = [[] for _ in range(self.size)]
        for bucket in self.buckets:
            for key, val in bucket:
                hashed_key = self.__hash(key)
                new_buckets[hashed_key].append((key, val))
        self.buckets = new_buckets

    def get(self, key: Any, custom_value: Any = None) -> Any:
        hashed_key = self.__hash(key)
        bucket = self.buckets[hashed_key]

        for index, (existing_key, value) in enumerate(bucket):
            if existing_key == key:
                return value

        return custom_value

    def remove(self, key: Any) -> Any:
        hashed_key = self.__hash(key)
        bucket = self.buckets[hashed_key]

        for index, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                self.num_elements -= 1
                return bucket.pop(index)

    def keys(self) -> List[Any]:
        all_keys = []
        for bucket in self.buckets:
            for key, _ in bucket:
                all_keys.append(key)
        return all_keys

    def values(self) -> List[Any]:
        all_values = []
        for bucket in self.buckets:
            for _, value in bucket:
                all_values.append(value)
        return all_values

    def count(self) -> int:
        return self.num_elements

    def __str__(self) -> str:
        return "".join(str(bucket) for bucket in self.buckets)


if __name__ == "__main__":
    hash_table = HashmapStructure(1)

    hash_table.put("VM001", {'Total Sales': 100, 'Items Sold': 50, 'Revenue Generated': 500})
    val = hash_table.get("VM001")
    print(val)
    hash_table.remove("VM001")
    val = hash_table.get("VM001")
    print(val)