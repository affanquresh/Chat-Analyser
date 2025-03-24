# WhatsApp Chat Analyzer

A Streamlit-based web application for analyzing WhatsApp chat exports. This tool provides various insights and visualizations from your WhatsApp chat data.

## Features

- Message statistics (total messages, words, media, links)
- User activity analysis
- Monthly and weekly timelines
- Activity heatmap
- Word cloud visualization
- Most common words analysis
- Emoji usage analysis

## Setup

1. Clone the repository:
```bash
git clone <your-repository-url>
cd chat-analyser
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run main.py
```

## Usage

1. Export your WhatsApp chat:
   - Open WhatsApp
   - Go to the chat you want to analyze
   - Click on the three dots menu
   - Select "More" > "Export chat"
   - Choose "Without media"
   - Save the .txt file

2. Upload the exported chat file in the application
3. Select a user or "Overall" for analysis
4. Click "Show Analysis" to view the insights

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- urlextract 