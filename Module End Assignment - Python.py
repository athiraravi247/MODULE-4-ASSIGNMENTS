# Survey Feedback Analyzer

# Step 1: Preloaded feedbacks
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

# Step 2: Add more feedbacks
more = int(input("How many more feedbacks do you want to add? "))

for i in range(more):
    print("\nFeedback", i + 1)
    name = input("Enter name: ")
    text = input("Enter feedback: ")
    rating = int(input("Enter rating (1-5): "))
    while rating < 1 or rating > 5:
        print("Rating must be between 1 and 5.")
        rating = int(input("Enter rating (1-5): "))

    feedback_data['S_No'].append(len(feedback_data['S_No']) + 1)   # starts from 11
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(text)
    feedback_data['Rating'].append(rating)

# Step 3: Text cleaning
cleaned = []
for text in feedback_data['Feedback']:
    for p in ['.', ',', '!', '?']:
        text = text.replace(p, '')
    text = ' '.join(text.split())    # removes extra/leading/trailing spaces
    text = text.lower()
    cleaned.append(text)

feedback_data['Feedback'] = cleaned


# Step 4: Word count insights
def count_word_in_feedbacks(word):
    count = 0
    for text in feedback_data['Feedback']:
        if word.lower() in text.lower().split():
            count += 1
    return count


print("\nFeedbacks containing 'good':", count_word_in_feedbacks("good"))
print("Feedbacks containing 'poor':", count_word_in_feedbacks("poor"))
print("Feedbacks containing 'excellent':", count_word_in_feedbacks("excellent"))

# Step 5: Final summary
print("\nCleaned feedback data:")
print(feedback_data)

average = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print("\nAverage rating:", round(average, 2))

longest = ''
longest_index = 0
for i in range(len(feedback_data['Feedback'])):
    if len(feedback_data['Feedback'][i].split()) > len(longest.split()):
        longest = feedback_data['Feedback'][i]
        longest_index = i

print("\nLongest feedback:", longest)
print("By:", feedback_data['Name'][longest_index])
print("Word count:", len(longest.split()))

unique_words = set()
for text in feedback_data['Feedback']:
    for w in text.split():
        unique_words.add(w)

print("\nUnique words:")
print(sorted(unique_words))

# Optional: sort by rating (highest to lowest)
combined = zip(feedback_data['Rating'], feedback_data['Name'], feedback_data['Feedback'])
sorted_entries = sorted(combined, key=lambda x: x[0], reverse=True)

print("\nFeedbacks sorted by rating:")
for rating, name, text in sorted_entries:
    print(rating, "|", name, "|", text)