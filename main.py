import emoji
import pandas as pd

print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.demojize("🪥"))
print("🪥" in emoji.EMOJI_DATA.keys())
# df = pd.read_csv('data.csv')

# res = pd.DataFrame(columns=['Text', 'Emoji'])

# # loop through df an print the emoji
# for i in df['Text']:
#     s = emoji.emojize(f":{i}:")
#     if emoji.is_emoji(s) and s not in res['Emoji'].values:
#         res = pd.concat([res, pd.DataFrame([[i, s]], columns=['Text', 'Emoji'])])
    
# print(res)
# res.to_csv('result.csv', index=False)