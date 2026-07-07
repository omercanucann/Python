import sys

print("=== Player Score Analytics ===")

if len(sys.argv) == 1:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    sys.exit()

scores = []

for arg in sys.argv[1:]:
    try:
        scores.append(int(arg))
    except ValueError:
        print(f"Invalid parameter: '{arg}'")
    
if len(scores) == 0:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    sys.exit()

total = sum(scores)
avarage = total / len(scores)
high = max(scores)
low = min(scores)
score_range = high - low

print(f"Scores processed: {scores}")
print(f"Total players: {len(scores)}")
print(f"Total score: {total}")
print(f"Average score: {avarage}")
print(f"High score: {high}")
print(f"Low score: {low}")
print(f"Score range: {score_range}")