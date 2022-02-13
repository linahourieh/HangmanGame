class HashTable:

    def __init__(self, bucket_count):
        self.buckets = []
        for _ in range(bucket_count):
            self.buckets.append([])

    def __str__(self):
        return str(self.buckets)

    def _bucket_index(self, key):
        # use the hash function to convert the key into bucket index
        key_hash = hash(key)
        idx = key_hash % len(self.buckets)
        return idx

    def _index_of_key_in_bucket(self, bucket, key):
        for idx, pair in enumerate(bucket):
            pair_key, pair_value = pair
            if pair_key == key:
                return idx
        return None

    def add(self, key, val):
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        bucket_key_index = self._index_of_key_in_bucket(bucket, key)

        new_pair = (key, val)
        if bucket_key_index is not None:
            bucket[bucket_key_index] = new_pair
        else:
            bucket.append(new_pair)

    def get(self, key):
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        bucket_key_index = self._index_of_key_in_bucket(bucket, key)

        if bucket_key_index is None:
            return None
        _, value = bucket[bucket_key_index]
        return value


