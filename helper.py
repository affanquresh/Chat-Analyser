from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji
def fetch_stats(selected_user,df):
    if selected_user != 'Overall':
        df=df[df['User'] == selected_user]
    #1. fetch the total number of messages
    num_messages=df.shape[0]
    #2. fetch the total number of words
    words=[]
    for message in df['Message']:
        words.extend(message.split())
     #3. fetch the total number of media
    media_df = df[df['Message'].str.contains("omitted", na=False)]
    num_media=media_df.shape[0]
    #4. fetch the total number of links
    extractor = URLExtract()
    links=[]
    for message in df['Message']:
        links.extend(extractor.find_urls(message))
    num_links=len(links)

    
    return num_messages,len(words),num_media,num_links

def most_busy_users(df):
    busy_users=df['User'].value_counts().head()
    x=round((busy_users/df.shape[0])*100,2)
    return x

def create_wordcloud(selected_user,df):
    f=open("stop_hinglish.txt","r")
    stop_words=f.read()
    if selected_user != 'Overall':
        df=df[df['User'] == selected_user]
    words_to_remove = ["omitted", "message", "deleted", "admin"]
    pattern = '|'.join(words_to_remove)  # Create regex pattern: "omitted|message|deleted|admin"
    temp = df[~df['Message'].str.contains(pattern, case=False, na=False)]
    temp=temp[~temp['Message'].str.contains(stop_words)]

    wc=WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df_wc=wc.generate( temp['Message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user,df):
    f=open("stop_hinglish.txt","r")
    stop_words=f.read()
    if selected_user != 'Overall':
        df=df[df['User'] == selected_user]
    words_to_remove = ["omitted", "message", "deleted", "admin"]
    pattern = '|'.join(words_to_remove)  # Create regex pattern: "omitted|message|deleted|admin"
    temp = df[~df['Message'].str.contains(pattern, case=False, na=False)]
    temp=temp[~temp['Message'].str.contains(stop_words)]

    words=[]
    for message in temp['Message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
    return_df=pd.DataFrame(Counter(words).most_common(20))
    return return_df

def emoji_helper(selected_user,df):
    if selected_user != 'Overall':
        df=df[df['User'] == selected_user]
    emojis=[]
    df["Message"] = df["Message"].fillna("")
    for message in df['Message']:
        emojis.extend([e["emoji"] for e in emoji.emoji_list(message)])
    emoji_counts=Counter(emojis)
    top_10_emojis=emoji_counts.most_common(10)

    return pd.DataFrame(top_10_emojis, columns=["Emoji", "Count"])



def monthly_timeline(selected_user,df):
    if selected_user != 'Overall':
        df=df[df['User'] == selected_user]
    timeline=df.groupby(['Year','Month_num','Month_Name']).count()['Message'].reset_index()
    time=[]
    for i in range(timeline.shape[0]):
        time.append(timeline['Month_Name'][i]+"-"+str(timeline['Year'][i]))
    timeline['Time']=time
    return timeline
def weekly_activity_map(selected_user,df):
    if selected_user != 'Overall':
        df=df[df['User'] == selected_user] 
    return df['Day_Name'].value_counts()

def monthly_activity_map(selected_user,df):
    if selected_user != 'Overall':
        df=df[df['User'] == selected_user] 

    return df['Month_Name'].value_counts()
                   
def activity_heatmap(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['User'] == selected_user]

    user_heatmap = df.pivot_table(index='Day_Name', columns='period', values='Message', aggfunc='count').fillna(0)

    return user_heatmap
