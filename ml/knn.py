import heapq
import pandas as pd
from collections import Counter

class KNN:
    def __init__(self, n: int, X_train, Y_train):
        self.n = n
        self.X_train = X_train
        self.Y_train = Y_train

    def distance(self, row1, row2) -> int:
        distance = 0.0
        for val1, val2 in zip(row1, row2):
            distance += pow(val1 - val2, 2)
        return distance
    
    def getNeighbors(self, stats) -> list[str]:
        heap = []
        for idx, X in self.X_train.iterrows():
            d = self.distance(stats, X)
            heapq.heappush(heap, (d, idx))
            if len(heap) > self.n:
                _, throw = heapq.heappop(heap)
        labels = [self.Y_train[i] for _,i in heap]
        return labels

    def predict(self, stats) -> str:
        predicted_vals = self.getNeighbors(stats)
        pred_count = Counter(predicted_vals)
        most = max(pred_count.values())
        ans = ""
        for pred in pred_count:
            if pred_count[pred] == most:
                ans = pred
        return ans

def load_class(n: int, data) -> KNN:
    df = pd.read_json(data)
    X = df.iloc[:,:-1]
    Y = df.iloc[:,-1]
    return KNN(n, X, Y)
