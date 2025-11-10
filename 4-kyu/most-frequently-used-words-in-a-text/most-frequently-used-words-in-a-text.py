import re
from collections import Counter
​
def top_3_words(text):
    words = re.findall(r"[a-z']+", text.lower())
    words = [w for w in words if re.search(r"[a-z]", w)]
    counts = Counter(words)
    return [word for word, _ in counts.most_common(3)]
​