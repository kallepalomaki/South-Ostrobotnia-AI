import Levenshtein

def normalized_levenshtein(s1, s2):
  dist = Levenshtein.distance(s1, s2)
  max_len = max(len(s1), len(s2))
  return dist / max_len if max_len > 0 else 0