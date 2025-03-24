import streamlit as st
import matplotlib.pyplot as plt
import preprocess,helper
import seaborn as sns

st.sidebar.title("Whatsapp Chat Analyser")
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["txt"])

if uploaded_file is not None:
  bytes_data = uploaded_file.read()
  data = bytes_data.decode("utf-8")
  df = preprocess.preprocess(data)
  st.dataframe(df)

  # fetch unique users
  user_list=df['User'].unique().tolist()
  user_list.sort()
  user_list.insert(0,'Overall')
  selected_user=st.sidebar.selectbox("show analysis wrt:",user_list)



  if st.sidebar.button("Show Analysis"):
    st.title("Analysis of the chat")
    st.subheader("Top statistics")

    #1. fetch the total number of messages, words, media, links
    num_messages,num_words,num_media,num_links=helper.fetch_stats(selected_user,df)
    col1,col2,col3,col4=st.columns(4)
    with col1:
     st.subheader("Total Messages")
     st.title(num_messages)
    with col2:
      st.subheader("Total Words")
      st.title(num_words)
    with col3:
      st.subheader("Total Media")
      st.title(num_media)
    with col4:
      st.subheader("Total Links")
      st.title(num_links)

    #2. monthly timeline
    st.title("Yearly Timeline")
    timeline=helper.monthly_timeline(selected_user,df)
    fig,ax=plt.subplots()
    ax.plot(timeline['Time'],timeline['Message'],color='green')
    plt.xticks(rotation=75)
    ax.set_xlabel("Time")
    ax.set_ylabel("Messages")
    ax.set_title("Monthly Timeline")
    for index,value in enumerate(timeline["Message"]):
      ax.text(index,value,str(value),fontsize=8)
    st.pyplot(fig)

    #3. weekly timeline
    col1,col2=st.columns(2)
    with col1:
      st.title("Weekly activity map")
      timeline=helper.weekly_activity_map(selected_user,df)
      fig,ax=plt.subplots()
      ax.bar(timeline.index,timeline.values,color='green')
      plt.xticks(rotation=75)
      ax.set_xlabel("Time")
      ax.set_ylabel("Messages")
      ax.set_title("Weekly activity map")
      st.pyplot(fig)
    with col2:
      st.title("Monthly activity map")
      timeline=helper.monthly_activity_map(selected_user,df)
      fig,ax=plt.subplots()
      ax.bar(timeline.index,timeline.values,color='green')
      plt.xticks(rotation=75)
      ax.set_xlabel("Time")
      ax.set_ylabel("Messages")
      ax.set_title("Monthly activity map")
      st.pyplot(fig)
    
    st.title("Weekly Activity Map")
    user_heatmap = helper.activity_heatmap(selected_user,df)
    fig,ax = plt.subplots()
    ax = sns.heatmap(user_heatmap)
    st.pyplot(fig)


      #2. fetch the busiest users
    if selected_user == 'Overall':
      st.title("Most Busy Users")
      x=helper.most_busy_users(df)
      fig,ax=plt.subplots()
      #  col=st.columns(1)
      #  with col:
      ax.bar(x.index,x.values)
      ax.set_xlabel("Users")
      ax.set_ylabel("Chat Percentage (%)", fontsize=19)
      ax.set_title("User chat contribution in (%)")
      for index, value in enumerate(x.values):
       ax.text(index, value + 1, f"{value:.2f}%", ha='center', fontsize=10)  # Adjust positioning
      ax.tick_params(axis='x', rotation=90) 
      st.pyplot(fig)

     #3. word cloud
    st.title("Word Cloud")
    df_wc=helper.create_wordcloud(selected_user,df)
    fig,ax=plt.subplots()
    ax.imshow(df_wc)
    st.pyplot(fig)

    #4. most common words
    st.title("Most Common Words")
    most_common_df=helper.most_common_words(selected_user,df)
    fig,ax=plt.subplots()
    ax.bar(most_common_df[0],most_common_df[1])
    ax.set_xlabel("Count")
    ax.set_ylabel("Words")
    ax.set_title("Most Common Words")
    plt.xticks(rotation='vertical')
    st.dataframe(most_common_df)
    st.pyplot(fig)

    #5. emoji analysis
    st.title("Emoji Analysis")
    emoji_df=helper.emoji_helper(selected_user,df)
    st.dataframe(emoji_df)
    fig,ax=plt.subplots()
    ax.bar(emoji_df["Emoji"],emoji_df["Count"])
    ax.set_xlabel("Emojis")
    ax.set_ylabel("Count")
    ax.set_title("Emoji Count")  
    st.pyplot(fig)

      









