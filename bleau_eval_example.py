import nltk
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

# Reference and candidate sentences
reference = [["miten menee sitte?"]]  # Human translation (reference)
candidate = "miten menee sulla sitte?"  # Model output

# Ensure consistent tokenization by splitting by space (manual tokenization)
reference_tokens = [["miten", "menee", "sitte", "sulla?"]]  # Tokenized reference
candidate_tokens = candidate.split()  # Tokenize candidate output

# Apply smoothing to avoid a zero score for very short sentences
smoothing = SmoothingFunction().method4

# Calculate BLEU score
bleu_score = sentence_bleu(reference_tokens, candidate_tokens, smoothing_function=smoothing)

print(f"BLEU score: {bleu_score}")