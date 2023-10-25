import instaloader
import pandas as pd
import matplotlib.pyplot as plt

profile_username = "charles_leclerc" 

captions = []
likes = []
comments = []

#this creates an instance of the instaloader
L = instaloader.Instaloader()

profile = instaloader.Profile.from_username(L.context, profile_username)

for post in profile.get_posts():
    captions.append(post.caption)
    likes.append(post.likes)
    comments.append(post.comments)

df = pd.DataFrame({
    'Caption': captions,
    'Likes': likes,
    'Comments': comments,
})

df.to_csv(f'{profile_username}_instagram_data.csv', index=False)

plt.figure(figsize=(10, 6))

# Histogram of likes
plt.subplot(2, 1, 1)
plt.hist(likes, bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Likes')
plt.xlabel('Likes')
plt.ylabel('Frequency')

# Histogram of comments
plt.subplot(2, 1, 2)
plt.hist(comments, bins=20, color='lightcoral', edgecolor='black')
plt.title('Histogram of Comments')
plt.xlabel('Comments')
plt.ylabel('Frequency')

plt.tight_layout()

# Show the plots
plt.show()

print(f'Data scraped from {profile_username} and saved to {profile_username}_instagram_data.csv')
